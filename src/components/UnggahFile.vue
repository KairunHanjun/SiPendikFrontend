<template>
  <div class="max-w-6xl mx-auto p-6">
    <div class="flex items-center justify-between mb-8">
      <h2 class="text-2xl font-bold text-gray-700">Unggah Dokumen / Upload File</h2>
    </div>

    <div 
      class="bg-white border rounded-lg shadow-sm mb-6 transition-all duration-300 overflow-hidden"
      :class="currentStep === 1 ? 'border-blue-500 ring-1 ring-blue-500' : 'border-gray-200'"
    >
      <div v-if="currentStep === 2" @click="currentStep = 1" class="p-4 flex items-center justify-between bg-white cursor-pointer hover:bg-gray-50 transition border-b border-transparent">
        <div class="flex items-center">
          <div v-if="filePreviewUrl" class="w-10 h-10 mr-3 rounded overflow-hidden border border-gray-300">
             <img :src="filePreviewUrl" class="w-full h-full object-cover">
          </div>
          <div>
             <h3 class="font-bold text-gray-800 text-lg">Upload File Arsip</h3>
             <p class="text-xs text-green-600 font-bold mt-0.5">✓ Scanned & Ready: {{ uploadedFileName }}</p>
          </div>
        </div>
        <span class="text-sm text-blue-600 font-bold hover:underline">Change File</span>
      </div>

      <div v-else class="p-6">
         <div class="flex items-center mb-4">
            <div class="w-8 h-8 bg-blue-600 text-white rounded-md flex items-center justify-center font-bold mr-3">1</div>
            <h3 class="font-bold text-gray-800 text-lg">Upload File Arsip</h3>
         </div>

         <div 
            v-if="!uploadedFileName"
            class="border-2 border-dashed border-gray-300 rounded-lg h-64 flex flex-col items-center justify-center text-center p-8 bg-gray-50 hover:bg-blue-50 hover:border-blue-400 transition-all cursor-pointer group"
            @click="triggerFileInput"
         >
            <div v-if="!isUploading">
              <div class="p-4 bg-white rounded-full mb-3 shadow-sm inline-block group-hover:scale-110 transition-transform">
                <svg class="w-10 h-10 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" /></svg>
              </div>
              <p class="text-gray-700 font-bold text-lg mb-1">Click to Scan Image</p>
              <p class="text-gray-500 text-sm">Takes an image -> Converts to Searchable PDF</p>
            </div>
            
            <div v-else class="flex flex-col items-center animate-pulse">
               <svg class="w-10 h-10 text-blue-600 mb-3 animate-spin" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
               <p class="text-blue-600 font-bold">Scanning & OCR Processing...</p>
               <p class="text-xs text-gray-500 mt-1">Calling Python API...</p>
            </div>
         </div>

         <div v-else class="bg-blue-50 border border-blue-200 rounded-xl p-6 flex flex-col items-center text-center">
            <div class="grid grid-cols-2 gap-4 mb-4 w-full max-w-lg">
                <div class="bg-white p-2 rounded shadow-sm">
                    <p class="text-xs font-bold text-gray-500 mb-2">Original Image</p>
                    <img :src="filePreviewUrl" class="h-40 w-full object-contain mx-auto">
                </div>
                <div class="bg-white p-2 rounded shadow-sm">
                    <p class="text-xs font-bold text-blue-500 mb-2">Result: OCR PDF</p>
                    <iframe v-if="ocrPdfUrl" :src="ocrPdfUrl" class="w-full h-40 border-0"></iframe>
                    <div v-else class="h-40 flex items-center justify-center text-xs text-red-500">Loading OCR</div>
                </div>
            </div>
            
            <h3 class="text-xl font-bold text-gray-800 mb-1">{{ ocrPdfUrl ? "Scan Complete" : "Loading OCR" }}</h3>
            
            <div class="flex space-x-4">
               <button @click="triggerFileInput" class="px-6 py-2 bg-white border border-gray-300 text-gray-700 font-bold rounded-lg hover:bg-gray-50">Retry</button>
               <button @click="currentStep = 2" class="px-6 py-2 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 shadow-md">Continue &rarr;</button>
            </div>
         </div>
         <input type="file" ref="fileInput" class="hidden" @change="handleFileUpload" accept="image/*">
      </div>
    </div>

    <div 
      class="bg-white border rounded-lg shadow-sm overflow-hidden transition-all duration-300"
      :class="[
        currentStep === 2 ? 'opacity-100 ring-1 ring-blue-500 border-blue-500' : 'border-gray-200',
        !uploadedFileName ? 'opacity-50 grayscale cursor-not-allowed' : 'opacity-100'
      ]"
    >
      <div 
        class="p-4 border-b border-gray-200 flex items-center bg-gray-50 transition"
        :class="{ 'cursor-pointer hover:bg-blue-50': uploadedFileName && currentStep === 1 }"
        @click="uploadedFileName && currentStep === 1 ? currentStep = 2 : null"
      >
        <div 
          class="w-8 h-8 rounded-md flex items-center justify-center font-bold mr-3 shadow-md transition-colors"
          :class="currentStep === 2 ? 'bg-blue-600 text-white' : 'bg-gray-300 text-gray-500'"
        >
          2
        </div>
        <h3 class="font-bold text-gray-800 text-lg">Detail Isi Dokumen</h3>
        <svg v-if="!uploadedFileName" class="w-5 h-5 ml-auto text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
      </div>

      <div v-if="currentStep === 2" class="p-6 grid grid-cols-1 lg:grid-cols-2 gap-8 animate-fade-in">
        
        <div class="space-y-4">
          <div>
             <div class="flex justify-between mb-1">
                <label class="block text-sm font-bold text-gray-700">Nama</label>
                <span class="text-xs text-gray-400">0/4 mapped*</span>
             </div>
             <input type="text" v-model="form.nama" placeholder="Seret bidang atribut ke sini..." class="w-full px-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none">
          </div>

          <div>
             <label class="block text-sm font-bold text-gray-700 mb-1">Jenis Naskah</label>
             <select v-model="form.jenisNaskah" class="w-full px-4 py-2 border border-gray-300 rounded-lg text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none">
               <option value="">Pilih Jenis Naskah</option>
               <option>Surat Keputusan</option>
               <option>Surat Edaran</option>
               <option>Nota Dinas</option>
             </select>
          </div>

          <div>
             <label class="block text-sm font-bold text-gray-700 mb-1">Sifat Naskah</label>
             <select v-model="form.sifatNaskah" class="w-full px-4 py-2 border border-gray-300 rounded-lg text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none">
               <option value="">Pilih Sifat Naskah</option>
               <option>Biasa</option>
               <option>Rahasia</option>
               <option>Sangat Rahasia</option>
             </select>
          </div>

          <div>
             <label class="block text-sm font-bold text-gray-700 mb-1">Klasifikasi</label>
             <select v-model="form.klasifikasi" class="w-full px-4 py-2 border border-gray-300 rounded-lg text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none">
               <option value="">Pilih Unit Kerja</option>
               <option>Keuangan</option>
               <option>Umum & Kepegawaian</option>
             </select>
          </div>

          <div>
             <label class="block text-sm font-bold text-gray-700 mb-1">Nomor Naskah</label>
             <div class="flex space-x-2">
               <input type="text" v-model="form.nomorNaskah" placeholder="Masukkan Nomor Naskah" class="flex-grow px-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none">
               <button class="bg-blue-100 text-blue-700 px-4 py-2 rounded-lg text-sm font-bold hover:bg-blue-200 transition">Ambil Nomor</button>
             </div>
          </div>

          <div>
             <label class="block text-sm font-bold text-gray-700 mb-1">Nomor Referensi</label>
             <input type="text" v-model="form.nomorReferensi" placeholder="Pilih Nomor Naskah" class="w-full px-4 py-2 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none">
          </div>
        </div>

        <div>
           <div class="border w-full h-full border-gray-200 rounded-lg p-4 bg-gray-50 flex items-center justify-between">
              <div v-if="ocrPdfUrl" class="bg-white w-full h-full p-2 rounded shadow-sm">
                  <p class="text-xs font-bold text-blue-500 mb-2">Result: OCR PDF</p>
                  <iframe v-if="ocrPdfUrl" :src="ocrPdfUrl" class="w-full h-full border-0"></iframe>
                  <div v-else class="h-40 flex items-center justify-center text-xs text-red-500">Loading OCR</div>
              </div>
              <div v-else class="bg-green-500 rounded-md p-1 mr-3">
                <svg class="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" /></svg>
              </div>
           </div>
           
        </div>
        <div v-if="currentStep === 2" class="bg-blue-50/50 p-6 border-t border-gray-200 flex justify-end space-x-3">
          <button class="px-6 py-2 bg-red-600 text-white font-bold rounded-lg">Reset</button>
          <button 
              @click="saveToSupabase" 
              :disabled="isSaving"
              class="px-6 py-2 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 disabled:bg-blue-300"
          >
              {{ isSaving ? 'Uploading...' : 'Simpan' }}
          </button>
        </div>
      </div>
      
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import { supabase } from '../supabase' // Ensure this is imported!

const currentStep = ref(1)
const isUploading = ref(false)
const isSaving = ref(false)
const uploadedFileName = ref('')
const fileInput = ref(null)

// Files to hold in memory
const originalFile = ref(null)
const ocrPdfBlob = ref(null)

// Preview URLs
const filePreviewUrl = ref(null)
const ocrPdfUrl = ref(null)

const form = reactive({
  nama: '',
  jenisNaskah: '',
  sifatNaskah: '',
  klasifikasi: '',
  nomorNaskah: '',
  nomorReferensi: ''
})

const triggerFileInput = () => fileInput.value.click()

// 1. UPLOAD AND SCAN (Talks to Python)
const handleFileUpload = async (event) => {
  const file = event.target.files[0]
  if (!file) return

  isUploading.value = true
  originalFile.value = file
  
  // A. Preview Original Image
  filePreviewUrl.value = URL.createObjectURL(file)
  uploadedFileName.value = file.name
  form.nama = file.name.split('.')[0]

  try {
    // B. Send to Python API
    const formData = new FormData()
    formData.append('file', file)

    // Ensure your Python API is running on this port
    const response = await fetch('http://localhost:5000/scan-to-pdf', {
      method: 'POST',
      body: formData
    })

    if (!response.ok) throw new Error("OCR Failed")

    // C. Get the PDF Blob back
    const blob = await response.blob()
    ocrPdfBlob.value = blob
    
    // Create a local URL so we can show it in the iframe
    ocrPdfUrl.value = URL.createObjectURL(blob)

  } catch (err) {
    alert("Error scanning document: " + err.message)
  } finally {
    isUploading.value = false
  }
}

// Helper to format folder names (Space -> Underscore)
const sanitize = (text) => {
  if (!text) return 'Uncategorized'
  // Handle specific mappings based on your bucket structure
  if (text === 'Biasa') return 'Umum' 
  if (text === 'Umum & Kepegawaian') return 'Umum'
  
  // Default: Replace spaces with underscores
  return text.replace(/\s+/g, '_')
}

// 2. SAVE TO SUPABASE (Uploads Both to specific folders)
const saveToSupabase = async () => {
  try {
    // Validation: Ensure dropdowns are selected
    if (!form.jenisNaskah || !form.sifatNaskah || !form.klasifikasi) {
      throw new Error("Mohon lengkapi Jenis, Sifat, dan Klasifikasi naskah.")
    }

    isSaving.value = true
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) throw new Error("Please login first")

    const timestamp = Date.now()
    
    // Construct Path: Jenis / Sifat / Klasifikasi / Filename
    // Example: Surat_Keputusan/Rahasia/Keuangan/12345_original.jpg
    const folderPath = `${sanitize(form.jenisNaskah)}/${sanitize(form.sifatNaskah)}/${sanitize(form.klasifikasi)}`
    
    // A. Upload Original Image
    const imagePath = `${folderPath}/${timestamp}_original_${originalFile.value.name}`
    //console.log(imagePath);
    const { error: err1 } = await supabase.storage
      .from('document') 
      .upload(imagePath, originalFile.value)
    if (err1) throw err1

    // B. Upload OCR PDF
    const pdfPath = `${folderPath}/${timestamp}_ocr.pdf`
    const { error: err2 } = await supabase.storage
      .from('document')
      .upload(pdfPath, ocrPdfBlob.value)
    if (err2) throw err2

    // C. Get Public URLs
    const { data: imgUrlData } = supabase.storage.from('document').createSignedUrl(imagePath, 60)
    const { data: pdfUrlData } = supabase.storage.from('document').createSignedUrl(pdfPath, 60)

    // D. Insert into Database Table
    const { error: dbError } = await supabase
      .from('documents_table') 
      .insert({
        nama_naskah: form.nama,
        jenis_naskah: form.jenisNaskah,
        sifat_naskah: form.sifatNaskah,
        klasifikasi: form.klasifikasi,
        nomor_naskah: form.nomorNaskah,
        nomor_referensi: form.nomorReferensi,
        original_image_url: imagePath,
        ocr_pdf_url: pdfPath,
        user_id: user.id
      })
    
    if (dbError) throw dbError

    alert("Document & PDF Saved Successfully to " + folderPath)
    
    // Reset form
    currentStep.value = 1
    uploadedFileName.value = ''
    filePreviewUrl.value = null
    ocrPdfUrl.value = null
    Object.assign(form, { nama: '', jenisNaskah: '', sifatNaskah: '', klasifikasi: '', nomorNaskah: '' })

  } catch (error) {
    alert("Save failed: " + error.message)
  } finally {
    isSaving.value = false
  }
}
</script>