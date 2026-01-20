<template>
  <main class="flex-1 overflow-y-auto bg-[#F8FAFC] p-8">
        
    <div class="animate-fade-in">
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-gray-800">Daftar Dokumen</h2>
        <div class="flex space-x-2">
            <button class="px-4 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition">
              + Upload Baru
            </button>
        </div>
      </div>
      
      <div class="bg-white rounded-lg shadow overflow-hidden">
        <table class="w-full text-sm text-left">
          <thead class="bg-gray-50 text-gray-900 font-bold border-b">
            <tr>
              <th class="p-4 w-4"><input type="checkbox" class="rounded"></th>
              <th class="p-4">Perihal</th>
              <th class="p-4">Kode Naskah</th>
              <th class="p-4">Tanggal</th>
              <th class="p-4">Kategori</th>
              <th class="p-4">Run Status</th>
              <th class="p-4 w-10"></th>
            </tr>
          </thead>
          <tbody class="divide-y divide-gray-100">
            <tr v-for="(doc, idx) in documentsData" :key="idx" class="hover:bg-blue-50/50 transition-colors">
              <td class="p-4"><input type="checkbox" class="rounded text-blue-600"></td>
              <td class="p-4 font-medium text-gray-800">{{ doc.perihal }}</td>
              <td class="p-4 text-gray-600">{{ doc.kode }}</td>
              <td class="p-4 text-gray-600">{{ doc.tanggal }}</td>
              <td class="p-4 text-gray-600">{{ doc.kategori }}</td>
              <td class="p-4 text-green-600 font-semibold">{{ doc.status }}</td>
              <td class="p-4 text-gray-400 cursor-pointer hover:text-blue-600">
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M2 6a2 2 0 012-2h5l2 2h5a2 2 0 012 2v6a2 2 0 01-2 2H4a2 2 0 01-2-2V6z"/></svg>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <!-- <div class="animate-fade-in">
        <div class="bg-white p-8 rounded-2xl shadow text-center py-20">
          <div class="inline-block p-4 bg-blue-100 rounded-full mb-4">
            <svg class="w-12 h-12 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" /></svg>
          </div>
          <h2 class="text-2xl font-bold text-gray-800">Add New User</h2>
          <p class="text-gray-500 mt-2">Form to add a new admin or staff member goes here.</p>
        </div>
    </div> -->

  </main>  
</template>

<script setup>
import { ref } from 'vue'

// --- STATE VARIABLES ---
// This acts as your "Booleans". 
// 'beranda' = true means Beranda shows.
// 'daftarDokumen' = true means Document List shows.


// --- DATA ---
const documentsData = [
  { perihal: 'Surat Pengantar Domisili', kode: 'KDS-001/2024', tanggal: '05-01-2024', kategori: 'Adm. Kependudukan', status: 'Successful' },
  { perihal: 'Surat Keterangan SKTM', kode: 'KDS-002/2024', tanggal: '05-01-2024', kategori: 'Pelayanan Sosial', status: 'Successful' },
  { perihal: 'Musrenbang Kelurahan', kode: 'KDS-003/2024', tanggal: '08-08-2024', kategori: 'Perencanaan', status: 'Successful' },
  { perihal: 'Surat Pengantar SKCK', kode: 'KDS-051/2024', tanggal: '04-04-2024', kategori: 'Pelayanan Umum', status: 'Successful' },
  { perihal: 'Data RW/RT Aktif', kode: 'KDS-041/2024', tanggal: '05-06-2024', kategori: 'Perencanaan', status: 'Successful' },
]
 
</script>

<style scoped>
@reference "tailwindcss";
/* Utility for Sidebar Links */
.nav-item {
  @apply flex items-center px-4 py-3 text-gray-300 hover:bg-blue-700/50 hover:text-white transition-all cursor-pointer border-l-4 border-transparent text-left;
}
/* Active State Styling */
.active-link {
  @apply bg-blue-600 text-white border-blue-400 shadow-lg;
}
.sub-nav-item {
  @apply flex items-center px-4 py-2 text-sm text-gray-400 hover:text-white transition-colors cursor-pointer pl-8 text-left;
}

/* Simple Animation for switching pages */
.animate-fade-in {
  animation: fadeIn 0.3s ease-in-out;
}
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(5px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Scrollbar Hiding */
.no-scrollbar::-webkit-scrollbar { display: none; }
.no-scrollbar { -ms-overflow-style: none; scrollbar-width: none; }
</style>