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
            <button @click="switchPage('Kependudukan')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Kependudukan' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> Adm. Kependudukan
            </button>
            <button @click="switchPage('Pemerintah')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === 'Pemerintah' }">
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
            </button>
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
            <button @click="switchPage('???')" class="text-start ps-3 sub-nav-item w-full" :class="{ 'text-blue-300 font-bold': currentPage === '???' }">
              <span class="w-1.5 h-1.5 bg-gray-400 rounded-full mr-3"></span> ????
            </button>
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
        <button v-on:click="logout" class="flex items-center p-3 rounded-lg text-red-300 hover:bg-red-500/20 hover:text-red-100 transition-colors duration-200 group">
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
          <div class="flex rounded-full bg-gray-100 p-1 shadow-inner">
            <select class="bg-transparent text-sm text-gray-600 py-2 pl-4 pr-2 rounded-l-full focus:outline-none">
              <option>All Files</option>
            </select>
            <input type="text" placeholder="Search..." class="bg-white text-sm w-48 lg:w-64 py-2 px-4 rounded-full focus:outline-none focus:ring-2 focus:ring-blue-400 shadow-sm">
          </div>
          <button class="relative text-gray-500 hover:text-blue-600 p-2 rounded-full hover:bg-gray-100 transition-colors">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
            </svg>
            <!-- TODO: When we have notification this red thing turn on -->
            <span class="absolute top-1 right-1 h-3 w-3 bg-red-500 rounded-full ring-2 ring-white"></span>
          </button>
          
          <div class="relative inline-block text-left" ref="dropdownContainer">
    
    <button 
      @click="toggleDropdown"
      type="button"
    >
      <div class="h-10 w-10 bg-blue-200 rounded-full flex items-center justify-center text-blue-600 font-bold text-lg cursor-pointer hover:bg-blue-300 transition-colors">
        <span>A</span>
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
        class="absolute right-0 mt-2 w-56 origin-top-right rounded-md bg-gray-800 shadow-lg ring-1 ring-white/10 focus:outline-none py-1"
        role="menu"
        aria-orientation="vertical"
        tabindex="-1"
      >
        <a 
          href="#" 
          class="block px-4 py-2 text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors" 
          role="menuitem"
        >
          Account settings
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

        <form method="POST" action="#">
          <button 
            type="submit" 
            class="block w-full px-4 py-2 text-left text-sm text-gray-300 hover:bg-white/5 hover:text-white transition-colors" 
            role="menuitem"
          >
            Sign out
          </button>
        </form>
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
          <Dokumen></Dokumen>
        </div>
        <div v-if="currentPage === 'Unggah' && isDropdownOpen">
          
        </div>
      </main>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue';
import { useRouter } from 'vue-router'
import Beranda from '../components/Beranda.vue';
import Dokumen from '../components/Dokumen.vue';

const router = useRouter()
const logout = () => {
  console.log("Logged out!")
  router.push('/')
}
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

// --- EVENTS ---
onMounted(() => {
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