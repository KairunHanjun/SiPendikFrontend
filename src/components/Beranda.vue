<template>
  <div class="animate-fade-in space-y-8">
    
    <div class="bg-gradient-to-r from-blue-800 to-blue-600 rounded-2xl p-8 text-white shadow-lg relative overflow-hidden">
      <div class="absolute top-0 right-0 -mr-16 -mt-16 w-64 h-64 bg-white opacity-10 rounded-full"></div>
      <div class="absolute bottom-0 right-20 -mb-20 w-40 h-40 bg-white opacity-10 rounded-full"></div>
      
      <div class="relative z-10">
        <h1 class="text-3xl font-bold mb-2">Selamat Datang, {{ userEmail }}</h1>
        <p class="text-blue-100 opacity-90">Sistem Arsip Digital Kelurahan Kedoya Selatan</p>
        
        <div class="mt-8 flex gap-4">
           <div class="bg-white/20 backdrop-blur-sm px-4 py-2 rounded-lg text-sm font-semibold border border-white/30">
              📅 {{ currentDate }}
           </div>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
      
      <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center">
        <div class="p-4 bg-blue-50 text-blue-600 rounded-full mr-4">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
        </div>
        <div>
          <p class="text-sm text-gray-500 font-bold uppercase">Total Dokumen</p>
          <h3 class="text-3xl font-bold text-gray-800">{{ stats.total }}</h3>
        </div>
      </div>

      <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center">
        <div class="p-4 bg-green-50 text-green-600 rounded-full mr-4">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" /></svg>
        </div>
        <div>
          <p class="text-sm text-gray-500 font-bold uppercase">Bulan Ini</p>
          <h3 class="text-3xl font-bold text-gray-800">{{ stats.thisMonth }}</h3>
        </div>
      </div>

      <div class="bg-white p-6 rounded-xl shadow-sm border border-gray-100 flex items-center">
        <div class="p-4 bg-purple-50 text-purple-600 rounded-full mr-4">
          <svg class="w-8 h-8" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 7h.01M7 3h5c.512 0 1.024.195 1.414.586l7 7a2 2 0 010 2.828l-7 7a2 2 0 01-2.828 0l-7-7A1.994 1.994 0 013 12V7a4 4 0 014-4z" /></svg>
        </div>
        <div>
          <p class="text-sm text-gray-500 font-bold uppercase">Kategori</p>
          <h3 class="text-3xl font-bold text-gray-800">{{ stats.categories }}</h3>
        </div>
      </div>
    </div>

    <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
      
      <div class="lg:col-span-2 bg-white rounded-xl shadow-sm border border-gray-100 overflow-hidden">
        <div class="p-6 border-b border-gray-100 flex justify-between items-center">
          <h3 class="font-bold text-gray-800">Baru Saja Diupload</h3>
        </div>
        
        <div v-if="loading" class="p-8 text-center text-gray-400">Loading activity...</div>
        
        <div v-else class="divide-y divide-gray-50">
          <div v-for="doc in recentDocs" :key="doc.id" class="p-4 hover:bg-gray-50 transition flex items-center">
            <div class="w-10 h-10 rounded-lg bg-blue-50 text-blue-600 flex items-center justify-center mr-4 shrink-0">
               <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" /></svg>
            </div>
            
            <div class="flex-1 min-w-0">
              <p class="text-sm font-bold text-gray-900 truncate">{{ doc.nama_naskah }}</p>
              <p class="text-xs text-gray-500 truncate">{{ doc.nomor_naskah || 'No Number' }} &bull; {{ doc.jenis_naskah }}</p>
            </div>
            
            <div class="text-right pl-4">
              <span class="text-xs font-semibold text-gray-400 block">{{ timeAgo(doc.created_at) }}</span>
            </div>
          </div>

          <div v-if="recentDocs.length === 0" class="p-6 text-center text-gray-500 text-sm">
            Belum ada dokumen yang diupload.
          </div>
        </div>
      </div>

      <div class="bg-white rounded-xl shadow-sm border border-gray-100 p-6">
        <h3 class="font-bold text-gray-800 mb-6">Distribusi Dokumen</h3>
        
        <div class="space-y-4">
          <div v-for="(count, category) in categoryBreakdown" :key="category">
            <div class="flex justify-between text-xs font-bold text-gray-600 mb-1">
              <span>{{ category }}</span>
              <span>{{ count }} File</span>
            </div>
            <div class="w-full bg-gray-100 rounded-full h-2">
              <div 
                class="bg-blue-600 h-2 rounded-full" 
                :style="{ width: calculatePercent(count) + '%' }"
              ></div>
            </div>
          </div>
        </div>

        <div class="mt-8 p-4 bg-yellow-50 rounded-lg border border-yellow-100">
           <h4 class="text-yellow-800 font-bold text-sm mb-1">💡 Tips Admin</h4>
           <p class="text-yellow-700 text-xs leading-relaxed">
             Pastikan untuk selalu mengisi "Nomor Naskah" dengan benar agar fitur pencarian dapat bekerja maksimal.
           </p>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted, reactive } from 'vue'
import { supabase } from '../supabase'

const userEmail = ref('Admin')
const currentDate = new Date().toLocaleDateString('id-ID', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' })
const loading = ref(true)

const recentDocs = ref([])
const stats = reactive({
  total: 0,
  thisMonth: 0,
  categories: 0
})
const categoryBreakdown = ref({}) // Object like { 'Surat Keputusan': 5, 'Nota': 2 }

onMounted(async () => {
  // 1. Get User Info
  const { data: { user } } = await supabase.auth.getUser()
  if (user) userEmail.value = user.email.split('@')[0] // Just show name part

  await fetchDashboardData()
})

async function fetchDashboardData() {
  try {
    loading.value = true
    
    // 1. Fetch ALL docs (needed for stats calculation)
    // Note: If you have 10,000+ docs, you should use .count() queries instead of fetching all data.
    // For a prototype/small archive, fetching metadata is fine.
    const { data: allDocs, error } = await supabase
      .from('documents_table')
      .select('id, nama_naskah, nomor_naskah, jenis_naskah, created_at')
      .order('created_at', { ascending: false })

    if (error) throw error

    if (allDocs) {
      // A. Recent Docs (Take top 5)
      recentDocs.value = allDocs.slice(0, 5)

      // B. Calculate Stats
      stats.total = allDocs.length
      
      const now = new Date()
      const thisMonth = allDocs.filter(d => {
        const dDate = new Date(d.created_at)
        return dDate.getMonth() === now.getMonth() && dDate.getFullYear() === now.getFullYear()
      })
      stats.thisMonth = thisMonth.length

      // C. Category Breakdown
      const cats = {}
      allDocs.forEach(d => {
        const c = d.jenis_naskah || 'Uncategorized'
        cats[c] = (cats[c] || 0) + 1
      })
      categoryBreakdown.value = cats
      stats.categories = Object.keys(cats).length
    }

  } catch (err) {
    console.error("Dashboard error:", err)
  } finally {
    loading.value = false
  }
}

// Helper: Calculate percentage for progress bars
function calculatePercent(count) {
  if (stats.total === 0) return 0
  return Math.round((count / stats.total) * 100)
}

// Helper: "2 hours ago", "5 mins ago"
function timeAgo(dateString) {
  if (!dateString) return ''
  const date = new Date(dateString)
  const now = new Date()
  const seconds = Math.floor((now - date) / 1000)
  
  let interval = seconds / 31536000
  if (interval > 1) return Math.floor(interval) + " tahun lalu"
  interval = seconds / 2592000
  if (interval > 1) return Math.floor(interval) + " bulan lalu"
  interval = seconds / 86400
  if (interval > 1) return Math.floor(interval) + " hari lalu"
  interval = seconds / 3600
  if (interval > 1) return Math.floor(interval) + " jam lalu"
  interval = seconds / 60
  if (interval > 1) return Math.floor(interval) + " menit lalu"
  return "Baru saja"
}
</script>

<style scoped>
@reference "tailwindcss";
.animate-fade-in { animation: fadeIn 0.5s ease-in-out; }
@keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
</style>