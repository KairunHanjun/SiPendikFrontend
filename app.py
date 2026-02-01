from flask import Flask, request, send_file
from flask_cors import CORS
import pytesseract
from PIL import Image, ImageEnhance
import io
from supabase import create_client, Client

app = Flask(__name__)
CORS(app)

# OPTIONAL: Set Tesseract path for Windows
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# CONFIGURATION
SUPABASE_URL = "https://vtlusodnxzwanjjjboct.supabase.co"
# CRITICAL: Use the SERVICE_ROLE key here (starts with ey...), NOT the Anon key!
SUPABASE_KEY = "sb_secret_kRFEbEQUTacaRUj0wzMV2A_inJo0mbg" 

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

@app.route('/admin/create-user', methods=['POST'])
def create_user():
    data = request.json
    
    # 1. Get Auth Data
    email = data.get('email')
    password = data.get('password')
    
    # 2. Get Profile Data (Matching your CSV columns)
    name = data.get('name')
    role = data.get('role', False) # Boolean: True = Admin
    nip = data.get('nip')
    phone = data.get('phone')
    date_birth = data.get('date_birth')
    address = data.get('address')

    try:
        # A. Create User in Auth System (Supabase Auth)
        res = supabase.auth.admin.create_user({
            "email": email,
            "password": password,
            "email_confirm": True
        })
        user = res.user

        if not user:
            raise Exception("Failed to create auth user")

        # B. Insert into 'profiles' table
        # We use 'user_uid' to link it to the auth user, as shown in your CSV
        profile_data = {
            "user_uid": user.id,  # Link to Auth
            "name": name,
            "role": role,
            "nip": nip,
            "phone": phone,
            "date_birth": date_birth,
            "address": address
        }
        
        # Using upsert to be safe, assuming 'user_uid' is unique/PK-ish
        supabase.table('profiles').upsert(profile_data).execute()

        return jsonify({"message": "User created successfully", "user": {"id": user.id}}), 200

    except Exception as e:
        print(f"Error creating user: {e}")
        return jsonify({"error": str(e)}), 400

@app.route('/admin/delete-user', methods=['POST'])
def delete_user():
    data = request.json
    user_uid = data.get('user_uid') # Changed to match your schema if needed

    try:
        # Delete from Auth (Cascade usually deletes profile too)
        supabase.auth.admin.delete_user(user_uid)
        return jsonify({"message": "User deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/scan-to-pdf', methods=['POST'])
def scan_to_pdf():
    # 1. Validation
    if 'file' not in request.files:
        return {"error": "No file part"}, 400
    
    file = request.files['file']
    if file.filename == '':
        return {"error": "No file selected"}, 400

    try:
        # 2. Open Image from Memory
        image = Image.open(io.BytesIO(file.read()))

        # 3. Pre-process (Make it look like a scan)
        # Convert to grayscale and increase contrast for better OCR accuracy
        
        enhancer = ImageEnhance.Color(image)
        clean_image = enhancer.enhance(2.0)

        # 4. Convert to Searchable PDF using Tesseract
        # Tesseract returns raw bytes of the PDF
        pdf_bytes = pytesseract.image_to_pdf_or_hocr(clean_image, extension='pdf')

        # 5. Prepare the PDF for sending
        # We wrap the bytes in a BytesIO object so Flask can treat it like a file
        pdf_file = io.BytesIO(pdf_bytes)
        pdf_file.seek(0)  # Reset pointer to the start of the file

        # 6. Return the file to the client
        return send_file(
            pdf_file,
            mimetype='application/pdf',
            as_attachment=True,
            download_name='scanned_document.pdf'
        )

    except Exception as e:
        print({"error": str(e)}, 500)
        return {"error": str(e)}, 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)