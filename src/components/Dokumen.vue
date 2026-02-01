<template>
  <main class="flex-1 overflow-y-auto bg-[#F8FAFC] p-8">
    <div class="animate-fade-in">
      
      <div class="flex flex-col md:flex-row justify-between items-center mb-6 gap-4">
        <h2 class="text-2xl font-bold text-gray-800">Daftar Dokumen</h2>
        <div class="flex space-x-2 w-full md:w-auto">
          <div class="relative flex-grow md:flex-grow-0">
             <input 
               v-model="searchQuery" 
               @keyup.enter="handleSearch"
               type="text" 
               placeholder="Cari Nama / Nomor Naskah..." 
               class="w-full md:w-64 pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 text-sm shadow-sm"
             >
             <span class="absolute left-3 top-2.5 text-gray-400">
                <svg class="w-4 h-4" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
             </span>
          </div>
        </div>
      </div>
      
      <div class="bg-white rounded-lg shadow overflow-hidden flex flex-col min-h-[400px]">
        
        <div v-if="loading" class="flex-1 flex flex-col items-center justify-center p-8 text-gray-500">
            <svg class="w-8 h-8 animate-spin text-blue-500 mb-2" fill="none" viewBox="0 0 24 24"><circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle><path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path></svg>
            Loading documents...
        </div>
        <div v-else-if="documentsData.length === 0" class="flex-1 flex flex-col items-center justify-center p-12">
            <h3 class="text-lg font-bold text-gray-700">No Documents Found</h3>
        </div>

        <div v-else class="flex-1">
          <table class="w-full text-sm text-left">
            <thead class="bg-gray-50 text-gray-900 font-bold border-b">
              <tr>
                <th class="p-4 w-4"><input type="checkbox" class="rounded"></th>
                
                <th @click="toggleSort('nama_naskah')" class="p-4 cursor-pointer hover:bg-gray-100 select-none group transition-colors">
                  <div class="flex items-center">
                    Perihal / Nama
                    <span class="ml-1 text-gray-400">
                      <svg v-if="sortColumn === 'nama_naskah' && sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" /></svg>
                      <svg v-else-if="sortColumn === 'nama_naskah' && !sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                      <svg v-else class="w-4 h-4 opacity-0 group-hover:opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4" /></svg>
                    </span>
                  </div>
                </th>

                <th @click="toggleSort('nomor_naskah')" class="p-4 cursor-pointer hover:bg-gray-100 select-none group transition-colors">
                  <div class="flex items-center">
                    Nomor Naskah
                    <span class="ml-1 text-gray-400">
                      <svg v-if="sortColumn === 'nomor_naskah' && sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" /></svg>
                      <svg v-else-if="sortColumn === 'nomor_naskah' && !sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                      <svg v-else class="w-4 h-4 opacity-0 group-hover:opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4" /></svg>
                    </span>
                  </div>
                </th>

                <th @click="toggleSort('created_at')" class="p-4 cursor-pointer hover:bg-gray-100 select-none group transition-colors">
                  <div class="flex items-center">
                    Tanggal
                    <span class="ml-1 text-gray-400">
                      <svg v-if="sortColumn === 'created_at' && sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" /></svg>
                      <svg v-else-if="sortColumn === 'created_at' && !sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                      <svg v-else class="w-4 h-4 opacity-0 group-hover:opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4" /></svg>
                    </span>
                  </div>
                </th>

                <th @click="toggleSort('jenis_naskah')" class="p-4 cursor-pointer hover:bg-gray-100 select-none group transition-colors">
                   <div class="flex items-center">
                    Kategori
                    <span class="ml-1 text-gray-400">
                      <svg v-if="sortColumn === 'jenis_naskah' && sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" /></svg>
                      <svg v-else-if="sortColumn === 'jenis_naskah' && !sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                      <svg v-else class="w-4 h-4 opacity-0 group-hover:opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4" /></svg>
                    </span>
                  </div>
                </th>

                <th @click="toggleSort('klasifikasi')" class="p-4 cursor-pointer hover:bg-gray-100 select-none group transition-colors">
                  <div class="flex items-center">
                    Klasifikasi
                    <span class="ml-1 text-gray-400">
                      <svg v-if="sortColumn === 'klasifikasi' && sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 15l7-7 7 7" /></svg>
                      <svg v-else-if="sortColumn === 'klasifikasi' && !sortAscending" class="w-4 h-4 text-blue-600" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7" /></svg>
                      <svg v-else class="w-4 h-4 opacity-0 group-hover:opacity-50" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16V4m0 0L3 8m4-4l4 4m6 0v12m0 0l4-4m-4 4l-4-4" /></svg>
                    </span>
                  </div>
                </th>
                
                <th class="p-4 w-10">Actions</th>
              </tr>
            </thead>
            <tbody class="divide-y divide-gray-100">
               <tr v-for="doc in documentsData" :key="doc.id" class="hover:bg-blue-50/50 transition-colors">
                  <td class="p-4"><input type="checkbox" class="rounded text-blue-600"></td>
                  <td class="p-4 font-medium text-gray-800">
                      {{ doc.nama_naskah }}
                      <span class="block text-xs text-gray-400 font-normal mt-0.5">{{ doc.sifat_naskah }}</span>
                  </td>
                  <td class="p-4 text-gray-600 font-mono text-xs">{{ doc.nomor_naskah || '-' }}</td>
                  <td class="p-4 text-gray-600">{{ formatDate(doc.created_at) }}</td>
                  <td class="p-4 text-gray-600"><span class="bg-blue-100 text-blue-800 text-xs px-2 py-1 rounded-full">{{ doc.jenis_naskah }}</span></td>
                  <td class="p-4 text-gray-600">{{ doc.klasifikasi }}</td>
                  <td class="p-4 text-right">
                    <details class="relative group">
                      <summary class="list-none cursor-pointer text-gray-400 hover:text-blue-600 p-1 rounded hover:bg-blue-50">
                          <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20"><path d="M10 6a2 2 0 110-4 2 2 0 010 4zM10 12a2 2 0 110-4 2 2 0 010 4zM10 18a2 2 0 110-4 2 2 0 010 4z"/></svg>
                      </summary>
                      <div class="absolute right-0 top-full mt-2 w-48 bg-white rounded-lg shadow-xl border border-gray-100 z-50 overflow-hidden text-left animate-fade-in hidden group-open:block">
                          <a href="#" @click.prevent="$emit('edit', doc.id)" class="block px-4 py-2 text-gray-700 hover:bg-blue-50 hover:text-blue-600 text-xs flex items-center border-b border-gray-100">
                              <svg class="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" /></svg> Edit Metadata
                          </a>
                          <a v-if="doc.original_image_url" href="#" @click.prevent="downloadFile(doc.original_image_url)" class="block px-4 py-2 text-gray-700 hover:bg-blue-50 hover:text-blue-600 text-xs flex items-center"><svg class="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg> Original Image</a>
                          <a v-if="doc.ocr_pdf_url" href="#" @click.prevent="downloadFile(doc.ocr_pdf_url)" class="block px-4 py-2 text-gray-700 hover:bg-blue-50 hover:text-blue-600 text-xs flex items-center"><svg class="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg> OCR PDF</a>
                          <a href="#" @click.prevent="deleteDokumen(doc)" class="block px-4 py-2 text-red-600 hover:bg-red-50 hover:text-red-800 text-xs flex items-center border-t border-gray-100"><svg class="w-4 h-4 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg> Delete</a>
                      </div>
                    </details>
                  </td>
               </tr>
            </tbody>
          </table>
        </div>
        
        <div class="p-4 border-t border-gray-200 bg-gray-50 flex justify-between items-center">
             <span class="text-xs text-gray-500">
                Showing <span class="font-bold">{{ totalItems === 0 ? 0 : rangeStart + 1 }}</span> to <span class="font-bold">{{ Math.min(rangeEnd + 1, totalItems) }}</span> of <span class="font-bold">{{ totalItems }}</span> results
            </span>
            <div class="flex space-x-2">
                <button @click="changePage(currentPage - 1)" :disabled="currentPage === 1 || loading" class="px-3 py-1 bg-white border border-gray-300 rounded text-sm text-gray-600 hover:bg-gray-100 disabled:opacity-50">Previous</button>
                <button @click="changePage(currentPage + 1)" :disabled="currentPage >= totalPages || loading" class="px-3 py-1 bg-white border border-gray-300 rounded text-sm text-gray-600 hover:bg-gray-100 disabled:opacity-50">Next</button>
            </div>
        </div>
      </div>
    </div>
  </main>  
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { supabase } from '../supabase'

const emit = defineEmits(['edit'])

// --- SEARCH & SORT STATE ---
const searchQuery = ref('')
const sortColumn = ref('created_at') // Default sort by date
const sortAscending = ref(false)     // Default descending (Newest first)

const documentsData = ref([])
const loading = ref(true)

// Pagination logic
const currentPage = ref(1)
const itemsPerPage = 5 
const totalItems = ref(0)
const totalPages = computed(() => Math.ceil(totalItems.value / itemsPerPage))
const rangeStart = computed(() => (currentPage.value - 1) * itemsPerPage)
const rangeEnd = computed(() => rangeStart.value + itemsPerPage - 1)

onMounted(async () => {
  await fetchDocuments()
})

// --- SORTING LOGIC ---
const toggleSort = (column) => {
  // If clicking the same column, flip direction
  if (sortColumn.value === column) {
    sortAscending.value = !sortAscending.value
  } else {
    // New column? Default to Ascending (A-Z)
    sortColumn.value = column
    sortAscending.value = true
  }
  // Reset to page 1 to see the new order from the start
  currentPage.value = 1 
  fetchDocuments()
}

// --- FETCH DATA ---
async function fetchDocuments() {
  try {
    loading.value = true
    const from = rangeStart.value
    const to = rangeEnd.value

    let query = supabase
      .from('documents_table')
      .select('*', { count: 'exact' })
    
    // 1. Search Filter
    if (searchQuery.value.trim() !== '') {
       query = query.or(`nama_naskah.ilike.%${searchQuery.value}%,nomor_naskah.ilike.%${searchQuery.value}%`)
    }

    // 2. Sorting & Pagination
    query = query
      .order(sortColumn.value, { ascending: sortAscending.value }) // <--- DYNAMIC SORTING HERE
      .range(from, to)

    const { data, error, count } = await query

    if (error) throw error
    
    documentsData.value = data
    totalItems.value = count || 0

  } catch (error) {
    console.error("Error loading documents:", error.message)
  } finally {
    loading.value = false
  }
}

const handleSearch = () => {
  currentPage.value = 1 
  fetchDocuments()
}

const changePage = (newPage) => {
    if (newPage >= 1 && newPage <= totalPages.value) {
        currentPage.value = newPage
        fetchDocuments()
    }
}

// --- DELETE / DOWNLOAD / DATE HELPERS (Same as before) ---
const getPathFromUrl = (url) => {
  if (!url) return null
  const bucketName = 'document'
  const parts = url.split(`/${bucketName}/`)
  return parts.length > 1 ? decodeURIComponent(parts[1]) : null
}
const deleteDokumen = async (doc) => {
  if (!confirm(`Are you sure you want to delete "${doc.nama_naskah}"?`)) return
  try {
    const filesToRemove = []
    const originalPath = getPathFromUrl(doc.original_image_url)
    if (originalPath) filesToRemove.push(originalPath)
    const pdfPath = getPathFromUrl(doc.ocr_pdf_url)
    if (pdfPath) filesToRemove.push(pdfPath)

    if (filesToRemove.length > 0) {
      await supabase.storage.from('document').remove(filesToRemove)
    }
    const { error } = await supabase.from('documents_table').delete().eq('id', doc.id)
    if (error) throw error
    
    // Refresh to update pagination counts correctly
    fetchDocuments()
    alert('Deleted successfully')
  } catch (error) {
    alert('Error deleting: ' + error.message)
  }
}
async function downloadFile(filePath) {
  if (!filePath) return
  try {
    const { data, error } = await supabase.storage.from('document').createSignedUrl(filePath, 60)
    if (error) throw error
    if (data.signedUrl) window.open(data.signedUrl, '_blank')
  } catch (error) {
    alert("Download failed: " + error.message)
  }
}
function formatDate(dateString) {
  if (!dateString) return '-'
  const date = new Date(dateString)
  if (isNaN(date.getTime())) return '-' 
  return new Intl.DateTimeFormat('id-ID', {
    day: '2-digit', month: 'short', year: 'numeric', timeZone: 'UTC' 
  }).format(date)
}
</script>

<style scoped>
@reference "tailwindcss";
.animate-fade-in { animation: fadeIn 0.3s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(5px); } to { opacity: 1; transform: translateY(0); } }
details > summary { list-style: none; }
details > summary::-webkit-details-marker { display: none; }
</style>