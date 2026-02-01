<template>
  <div class="max-w-4xl mx-auto p-6">
    <div class="flex items-center justify-between mb-8">
      <h2 class="text-2xl font-bold text-gray-800">Edit Dokumen</h2>
      <button @click="$router.back()" class="text-gray-500 hover:text-gray-700">
        &larr; Back
      </button>
    </div>

    <div v-if="loading" class="text-center py-12">
      <p class="text-gray-500">Loading document details...</p>
    </div>

    <div v-else class="bg-white border border-gray-200 rounded-lg shadow-sm p-8">
      
      <div class="grid grid-cols-1 gap-6">
        <div>
           <label class="block text-sm font-bold text-gray-700 mb-1">Nama / Perihal</label>
           <input type="text" v-model="form.nama_naskah" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none">
        </div>

        <div class="grid grid-cols-2 gap-6">
            <div>
               <label class="block text-sm font-bold text-gray-700 mb-1">Jenis Naskah</label>
               <select v-model="form.jenis_naskah" class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-white outline-none">
                 <option>Surat Keputusan</option>
                 <option>Surat Edaran</option>
                 <option>Nota Dinas</option>
               </select>
            </div>
            <div>
               <label class="block text-sm font-bold text-gray-700 mb-1">Sifat Naskah</label>
               <select v-model="form.sifat_naskah" class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-white outline-none">
                 <option>Biasa</option>
                 <option>Rahasia</option>
                 <option>Sangat Rahasia</option>
               </select>
            </div>
        </div>

        <div class="grid grid-cols-2 gap-6">
             <div>
               <label class="block text-sm font-bold text-gray-700 mb-1">Nomor Naskah</label>
               <input type="text" v-model="form.nomor_naskah" class="w-full px-4 py-2 border border-gray-300 rounded-lg outline-none">
            </div>
            <div>
               <label class="block text-sm font-bold text-gray-700 mb-1">Klasifikasi</label>
               <select v-model="form.klasifikasi" class="w-full px-4 py-2 border border-gray-300 rounded-lg bg-white outline-none">
                 <option>Keuangan</option>
                 <option>Umum & Kepegawaian</option>
                 <option>Umum</option>
               </select>
            </div>
        </div>
      </div>

      <div class="mt-8 flex justify-end space-x-3 border-t pt-6">
         <button @click="$emit('cancel')" class="text-gray-500 hover:text-gray-700">
            &larr; Back
        </button>
         <button 
            @click="updateDocument" 
            :disabled="saving"
            class="px-6 py-2 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 disabled:opacity-50"
         >
            {{ saving ? 'Saving...' : 'Update Changes' }}
         </button>
      </div>

    </div>
  </div>
</template>

<script setup>
// UbahDokumen.vue
import { ref, onMounted, reactive, watch } from 'vue' // Add 'watch'
import { supabase } from '../supabase'
// Remove 'useRoute', 'useRouter' imports if you don't need them elsewhere

// 1. Accept the ID from Dashboard
const props = defineProps(['id']) 
const emit = defineEmits(['cancel', 'saved'])

const loading = ref(true)
const saving = ref(false)

const form = reactive({
  nama_naskah: '',
  jenis_naskah: '',
  sifat_naskah: '',
  nomor_naskah: '',
  klasifikasi: ''
})

// 2. Fetch Data Function
const fetchDocument = async (idToFetch) => {
  if (!idToFetch) return
  
  loading.value = true
  try {
    const { data, error } = await supabase
      .from('documents_table')
      .select('*')
      .eq('id', idToFetch) // Use the argument, not route param
      .single()

    if (error) throw error
    Object.assign(form, data)
  } catch (err) {
    alert("Error fetching document: " + err.message)
    emit('cancel') // Go back if error
  } finally {
    loading.value = false
  }
}

// 3. Watch for changes (In case user clicks Edit on different docs rapidly)
watch(() => props.id, (newId) => {
  fetchDocument(newId)
}, { immediate: true }) // immediate: true runs it once on mount automatically

// 4. Update Save Function to use props.id
const updateDocument = async () => {
  try {
    saving.value = true
    const { error } = await supabase
      .from('documents_table')
      .update({ ...form }) // Spread form data
      .eq('id', props.id) // Use Prop ID

    if (error) throw error

    alert("Document updated successfully!")
    emit('saved') // Tell Dashboard to switch back

  } catch (err) {
    alert("Update failed: " + err.message)
  } finally {
    saving.value = false
  }
}
</script>