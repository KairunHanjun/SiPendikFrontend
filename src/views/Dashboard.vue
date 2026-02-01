<template>
  <div class="flex h-screen bg-[#F1F5F9] font-sans">

    <aside 
      class="bg-[#1E293B] text-white transition-all duration-300 ease-in-out flex flex-col shadow-xl z-20"
      :class="isSidebarOpen ? 'w-64' : 'w-20'"
    >
      <div class="h-20 flex items-center justify-center border-b border-gray-700 px-4 truncate relative">
        <div class="w-10 h-10 bg-blue-500 rounded-lg shrink-0 flex items-center justify-center mr-3">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
          </svg>
        </div>
        <div v-if="isSidebarOpen" class="overflow-hidden transition-opacity duration-300">
          <h1 class="font-bold text-sm leading-tight">Kelurahan Kedoya Selatan</h1>
          <p class="text-xs text-blue-300">SI PENDIK</p>
        </div>
      </div>

      <nav class="flex-grow py-6 space-y-1 px-2">
        
        <button 
          @click="switchPage('Beranda')" 
          class="nav-item w-full" 
          :class="{ 'active-link': currentPage === 'Beranda' }"
        >
          <svg class="w-6 h-6 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 001-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" /></svg>
          <span v-if="isSidebarOpen" class="ml-3 font-medium">Beranda</span>
        </button>

        <div>
          <button 
            @click="toggleDocDropdown" 
            class="nav-item w-full justify-between group"
            :class="{ 'bg-blue-800/50': isDocDropdownOpen }"
          >
            <div class="flex items-center">
              <svg class="w-6 h-6 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 7v10a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-6l-2-2H5a2 2 0 00-2 2z" /></svg>
              <span v-if="isSidebarOpen" class="ml-3 font-medium">Dokumen</span>
            </div>
            <svg v-if="isSidebarOpen" class="w-4 h-4 transition-transform duration-200" :class="isDocDropdownOpen ? 'rotate-180' : ''" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
          </button>

          <div v-if="isSidebarOpen && isDocDropdownOpen" class=" bg-blue-900/30 mt-1 space-y-1 py-2 rounded-lg mx-2 border-l-2 w-full border-blue-500/30 transition transition-discrete [--anchor-gap:--spacing(2)] data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in">
            <button @click="switchPage('Dokumen')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Dokumen' }">
              <span class="w-1.5 h-1.5 bg-current rounded-full mr-3"></span> Daftar Dokumen
            </button>
            <button @click="switchPage('Ubah Dokumen')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Ubah Dokumen' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Ubah Dokumen
            </button>
            <!-- <button @click="switchPage('Pemerintah')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Pemerintah' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Adm. Pemerintahan
            </button>
            <button @click="switchPage('Keuangan')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Keuangan' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Keuangan dan Aset
            </button>
            <button @click="switchPage('Pertahanan')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Pertahanan' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Pertahanan dan Tata Wilayah
            </button>
            <button @click="switchPage('Sosial')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Sosial' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Social dan Kemasyarakatan
            </button>
            <button @click="switchPage('Kepegawaian')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Kepegawaian' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Kepegawaian
            </button>
            <button @click="switchPage('Perizinan')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Perizinan' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Perizinan dan Rekomendasi
            </button>
            <button @click="switchPage('Aduan')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Aduan' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Pengaduan dan Pelayanan Publik
            </button> -->
          </div>
        </div>

        <div>
          <button 
            @click="toggleUnggahDropdown" 
            class="nav-item w-full justify-between group"
            :class="{ 'bg-blue-800/50': isUnggahDropdownOpen }"
          >
            <div class="flex items-center">
              <svg class="w-6 h-6 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-8l-4-4m0 0L8 8m4-4v12" /></svg>
              <span v-if="isSidebarOpen" class="ml-3 font-medium">Unggah Document</span>
            </div>
            <svg v-if="isSidebarOpen" class="w-4 h-4 transition-transform duration-200" :class="isUnggahDropdownOpen ? 'rotate-180' : ''" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
          </button>

          <div v-if="isSidebarOpen && isUnggahDropdownOpen" class=" bg-blue-900/30 mt-1 space-y-1 py-2 rounded-lg mx-2 border-l-2 w-full border-blue-500/30 transition transition-discrete [--anchor-gap:--spacing(2)] data-closed:scale-95 data-closed:transform data-closed:opacity-0 data-enter:duration-100 data-enter:ease-out data-leave:duration-75 data-leave:ease-in">
            <button @click="switchPage('Unggah')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Unggah' }">
              <span class="w-1.5 h-1.5 bg-current rounded-full mr-3"></span> Unggah File
            </button>
            <!-- <button @click="switchPage('???')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === '???' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> ????
            </button> -->
          </div>
        </div>

        <button 
          @click="switchPage('Daftar')" 
          class="nav-item w-full"
          :class="{ 'active-link': currentPage === 'Daftar' }"
        >
          <svg class="w-6 h-6 flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" /></svg>
          <span v-if="isSidebarOpen" class="ml-3 font-medium">Add User</span>
        </button>

      </nav>

      <div class="p-3 border-t border-gray-700">
        <button v-on:click="handleLogout" class="flex items-center p-3 rounded-lg text-red-300 hover:bg-red-500/20 hover:text-red-100 transition-colors duration-200 group">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 group-hover:translate-x-1 transition-transform" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
          </svg>
          <span v-if="isSidebarOpen" class="ml-4 font-medium">Logout</span>
        </button>
      </div>
    </aside>

    <div class="flex-1 flex flex-col overflow-hidden">
      <header class="h-20 bg-white shadow-sm px-8 flex items-center justify-between z-10">
        <div class="flex items-center">
          <button @click="toggleSidebar" class="text-gray-500 hover:text-blue-600 focus:outline-none mr-6 p-2 rounded-full hover:bg-gray-100 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h7" />
            </svg>
          </button>
          <h2 class="text-2xl font-bold text-gray-800">Halaman Dashboard: {{ currentPage }}</h2>
        </div>

        <div class="flex items-center space-x-6">

          
          
          <div class="relative inline-block text-left" ref="dropdownContainer">
    
          <button 
            @click="toggleDropdown"
            type="button"
          >
            <div class="h-10 w-10 bg-blue-200 rounded-full flex items-center justify-center text-blue-600 font-bold text-lg cursor-pointer hover:bg-blue-300 transition-colors">
              <span v-if="!userPP && !userPPLink">{{ userEmail.charAt(0) }}</span>
              <img class="h-full w-full rounded-full object-contain" v-if="userPP && userPPLink" v-bind:src="userPPLink"></img>
            </div>
          </button>
          

          <Transition
            enter-active-class="transition ease-out duration-100"
            enter-from-class="transform opacity-0 scale-95"
            enter-to-class="transform opacity-100 scale-100"
            leave-active-class="transition ease-in duration-75"
            leave-from-class="transform opacity-100 scale-100"
            leave-to-class="transform opacity-0 scale-95"
          >
            <div 
              v-if="isOpen"
              class="absolute right-0 mt-2 w-fill origin-top-right rounded-md bg-gray-800 shadow-lg ring-1 ring-white/10 focus:outline-none py-1"
              role="menu"
              aria-orientation="vertical"
              tabindex="-1"
            >
              <a 
                href="#" 
                class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors" 
                role="menuitem"
                @click="switchPage('Profile')"
              >
                {{ userEmail }}
              </a>

              <a 
                href="#" 
                class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors" 
                role="menuitem"
              >
                Support
              </a>

              <a 
                href="#" 
                class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors" 
                role="menuitem"
              >
                License
              </a>

              
              <button 
                type="submit" 
                class="block w-full px-4 py-2 text-left text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors" 
                role="menuitem"
                @click="handleLogout"
              >
                Sign out
              </button>
              
            </div>
          </Transition>
        </div>

        </div>
      </header>

      <main class="flex-1 overflow-y-auto p-8">
        <div v-if="currentPage === 'Beranda'">
          <Beranda></Beranda>
        </div>
        <div v-if="currentPage === 'Dokumen' && isDropdownOpen">
          <Dokumen @edit="handleEditRequest"></Dokumen>
        </div>
        <div v-if="currentPage === 'Unggah' && isDropdownOpen">
          <UnggahFile></UnggahFile>
        </div>
        <div v-if="currentPage === 'Profile'">
          <div class="max-w-4xl mx-auto bg-white rounded-xl shadow-md overflow-hidden p-8">
            <div class="flex flex-col md:flex-row gap-8">
              
              <div class="flex flex-col items-center space-y-4 md:w-1/3 border-r border-gray-100 pr-4">
                <div class="relative group">
                  <img 
                    :src="profile.avatar_url || 'https://via.placeholder.com/150'" 
                    class="w-40 h-40 rounded-full object-cover border-4 border-white shadow-lg"
                    :class="{ 'opacity-50': uploading }"
                  />
                  
                  <div v-if="uploading" class="absolute inset-0 flex items-center justify-center">
                    <span class="text-blue-600 font-bold text-sm">Uploading...</span>
                  </div>
                </div>

                <label class="cursor-pointer bg-blue-50 text-blue-600 px-4 py-2 rounded-lg text-sm font-bold hover:bg-blue-100 transition">
                  Change Photo
                  <input 
                    type="file" 
                    accept="image/*" 
                    class="hidden" 
                    @change="handleAvatarUpload"
                    :disabled="uploading"
                  />
                </label>
                <p class="text-xs text-gray-400">Allowed *.jpeg, *.jpg, *.png, *.gif</p>
              </div>


              <div class="flex-1">
                

                <div v-if="!isEditing" class="space-y-6">
                  <div>
                    <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Full Name</label>
                    <p class="text-lg font-medium text-gray-800">{{ profile.full_name || 'Not set' }}</p>
                  </div>

                  <div>
                    <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Email Address</label>
                    <p class="text-lg font-medium text-gray-800">{{ profile.email }}</p>
                  </div>

                  <div>
                    <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Phone Number</label>
                    <p class="text-lg font-medium text-gray-800">{{ profile.phone }}</p>
                  </div>

                  <div>
                    <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Date of Birth</label>
                    <p class="text-lg font-medium text-gray-800">{{ profile.date_birth }}</p>
                  </div>

                  <div>
                    <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">NIP</label>
                    <p class="text-lg font-medium text-gray-800">{{ profile.nip }}</p>
                  </div>

                  <div>
                    <label class="block text-xs font-bold text-gray-400 uppercase tracking-wider mb-1">Role</label>
                    <span class="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                      {{ profile.role }}
                    </span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div v-if="currentPage === 'Ubah Dokumen'">
          <UbahDokumen 
            :id="selectedDocId" 
            @cancel="switchPage('Dokumen')"
            @saved="switchPage('Dokumen')"
          ></UbahDokumen>
        </div>
        <div v-if="currentPage === 'Daftar'">
          <AddUser></AddUser>
        </div>
      </main>
    </div>
  </div>
</template>



<script setup>
import { ref, onMounted, reactive, onUnmounted } from 'vue';
import { supabase } from '../supabase';
import { useRouter } from 'vue-router'
import Beranda from '../components/Beranda.vue';
import Dokumen from '../components/Dokumen.vue';
import UnggahFile from '../components/UnggahFile.vue';
import UbahDokumen from '../components/UbahDokumen.vue';
import AddUser from '../components/AddUser.vue';

const router = useRouter()

// --- STATE VARIABLES ---
// This acts as your "Booleans". 
// 'beranda' = true means Beranda shows.
// 'Dokumen' = true means Document List shows.
const currentPage = ref('Beranda') 

const isOpen = ref(false)
const dropdownContainer = ref(null)
const isSidebarOpen = ref(true)
const isDocDropdownOpen = ref(false)
const isUnggahDropdownOpen = ref(false)
const isDropdownOpen = ref(false)
const userEmail = ref('')
const userPP = ref(false)
const userUID = ref('')
const userPPLink = ref('');
const selectedDocId = ref(null)

const uploading = ref(false)
const saving = ref(false)
const isEditing = ref(false)

const profile = reactive({
  id: '',
  email: '',
  full_name: '',
  role: '',
  avatar_url: '',
  phone: '',
  date_birth: '',
  nip: ''
})

const form = reactive({ full_name: '' })

// --- DATA ---
const documentsData = [
  { perihal: 'Surat Pengantar Domisili', kode: 'KDS-001/2024', tanggal: '05-01-2024', kategori: 'Adm. Kependudukan', status: 'Successful' },
  { perihal: 'Surat Keterangan SKTM', kode: 'KDS-002/2024', tanggal: '05-01-2024', kategori: 'Pelayanan Sosial', status: 'Successful' },
  { perihal: 'Musrenbang Kelurahan', kode: 'KDS-003/2024', tanggal: '08-08-2024', kategori: 'Perencanaan', status: 'Successful' },
  { perihal: 'Surat Pengantar SKCK', kode: 'KDS-051/2024', tanggal: '04-04-2024', kategori: 'Pelayanan Umum', status: 'Successful' },
  { perihal: 'Data RW/RT Aktif', kode: 'KDS-041/2024', tanggal: '05-06-2024', kategori: 'Perencanaan', status: 'Successful' },
]

// --- FUNCTIONS ---
const toggleSidebar = () => {
  isSidebarOpen.value = !isSidebarOpen.value
}

const toggleDropdown = () => {
  isOpen.value = !isOpen.value
}

const handleLogout = async () => {
  // 1. Sign out from Supabase
  await supabase.auth.signOut()
  
  // 2. Push user back to the login screen
  router.push('/auth')
}

const handleEditRequest = (id) => {
  selectedDocId.value = id     // 1. Hold the ticket
  switchPage('Ubah Dokumen')   // 2. Switch the room
}

const toggleDocDropdown = () => {
  switchPage('Dokumen')
  if (!isSidebarOpen.value) isSidebarOpen.value = true // Auto open sidebar if closed
  isDocDropdownOpen.value = !isDocDropdownOpen.value
  if (isUnggahDropdownOpen.value) isUnggahDropdownOpen.value = !isUnggahDropdownOpen.value
  isDropdownOpen.value = isDocDropdownOpen.value;
}

const toggleUnggahDropdown = () => {
  switchPage('Unggah')
  if (!isSidebarOpen.value) isSidebarOpen.value = true // Auto open sidebar if closed
  if (isDocDropdownOpen.value) isDocDropdownOpen.value = !isDocDropdownOpen.value
  isUnggahDropdownOpen.value = !isUnggahDropdownOpen.value
  isDropdownOpen.value = isUnggahDropdownOpen.value;
}

// This function handles the "Boolean" logic you asked for
const switchPage = (pageName) => {
  currentPage.value = pageName
  // Optional: Auto-close dropdown if moving away from docs? 
  // For now, let's keep it open if they are working there.
}

const formatPageName = (name) => {
  if(name === 'Dokumen') return 'Daftar Dokumen'
  if(name === 'Daftar') return 'Add User'
  return name
}

const closeOnClickOutside = (event) => {
  if (dropdownContainer.value && !dropdownContainer.value.contains(event.target)) {
    isOpen.value = false
  }
}

// 2. Toggle Edit Mode
const toggleEdit = () => {
  if (!isEditing.value) {
    // Copy current data to form buffer when opening edit
    form.full_name = profile.full_name
  }
  isEditing.value = !isEditing.value
}

// 3. Update Text Info
const updateProfile = async () => {
  try {
    saving.value = true
    
    const { error } = await supabase
      .from('profiles')
      .update({ full_name: form.full_name })
      .eq('id', profile.id)

    if (error) throw error

    // Update local view
    profile.full_name = form.full_name
    isEditing.value = false // Close form
    alert('Profile updated successfully!')

  } catch (error) {
    alert('Error updating profile: ' + error.message)
  } finally {
    saving.value = false
  }
}


// --- EVENTS ---
onMounted(async () => {
  const { data: { user } } = await supabase.auth.getUser()
  
  // 2. Assign the email to your variable
  if (user) {
    userEmail.value = user.email
    userUID.value = user.id

    try{
      const path_to_image = "/pp_" + userUID.value + ".jpeg"
      const {data:image_url} = supabase.storage.from("profile_picture").getPublicUrl(path_to_image)
      userPPLink.value = image_url.publicUrl;
      console.log(image_url);
      userPP.value = true;

      const { data, error } = await supabase
        .from('profiles')
        .select('*')
        .eq('user_uid', user.id)
        .single()

      if (error) throw error

      if (data) {
        profile.full_name = data.name
        profile.role = data.role ? 'Admin' : 'User'
        profile.avatar_url = userPPLink
        profile.email = userEmail
        profile.id = userUID
        profile.phone = data.phone
        profile.date_birth = data.date_birth
        profile.nip = data.nip
      }
    }catch(error){
      userPP.value = false;
    }
  }
  window.addEventListener('click', closeOnClickOutside)
})

onUnmounted(() => {
  window.removeEventListener('click', closeOnClickOutside)
})

</script>

<style scoped>
/* Utility class for menu items.
  Creates a consistent look, hover effects, and active state styling.
*/
@reference "tailwindcss";

.nav-item {
  @apply flex items-center p-3 mx-2 rounded-lg text-blue-100 hover:bg-blue-600/30 hover:text-white transition-all duration-200 cursor-pointer;
}

/* Style for the currently active menu item */
.nav-item.active {
  @apply bg-blue-600 text-white shadow-md;
}

/* Hides scrollbar for a cleaner look in navigation */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}
.no-scrollbar {
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
}
</style>