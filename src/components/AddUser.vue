<template>
  <div class="p-8 max-w-7xl mx-auto">
    
    <div class="flex justify-between items-center mb-8">
      <div>
        <h2 class="text-2xl font-bold text-gray-800">User Management</h2>
        <p class="text-gray-500 text-sm">Create and remove system access.</p>
      </div>
      <button 
        @click="showModal = true"
        class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 shadow flex items-center"
      >
        <svg class="w-5 h-5 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4" /></svg>
        Add New User
      </button>
    </div>

    <div v-if="loading" class="text-center py-12">
      <p class="text-gray-400 mt-2">Loading users...</p>
    </div>

    <div v-else class="bg-white rounded-xl shadow overflow-hidden">
      <table class="w-full text-left">
        <thead class="bg-gray-50 border-b border-gray-100">
          <tr>
            <th class="p-4 font-bold text-gray-600 text-sm">User Profile</th>
            <th class="p-4 font-bold text-gray-600 text-sm">NIP & Contact</th>
            <th class="p-4 font-bold text-gray-600 text-sm">Role</th>
            <th class="p-4 font-bold text-gray-600 text-sm text-right">Action</th>
          </tr>
        </thead>
        <tbody class="divide-y divide-gray-100">
          <tr v-for="user in users" :key="user.uid" class="hover:bg-gray-50 transition">
            
            <td class="p-4">
              <div class="flex items-center">
                <div class="w-10 h-10 rounded-full bg-blue-100 text-blue-600 flex items-center justify-center font-bold mr-3 shrink-0">
                  {{ user.name ? user.name.charAt(0).toUpperCase() : '?' }}
                </div>
                <div>
                  <p class="font-bold text-gray-800">{{ user.name || 'No Name' }}</p>
                  <p class="text-xs text-gray-500">{{ user.user_uid }}</p> </div>
              </div>
            </td>

            <td class="p-4">
               <p class="text-sm font-bold text-gray-700">NIP: <span class="font-normal">{{ user.nip || '-' }}</span></p>
               <p class="text-xs text-gray-500">{{ user.phone || '-' }}</p>
            </td>

            <td class="p-4">
              <span 
                class="px-3 py-1 rounded-full text-xs font-bold"
                :class="user.role ? 'bg-purple-100 text-purple-700' : 'bg-green-100 text-green-700'"
              >
                {{ user.role ? 'ADMIN' : 'USER' }}
              </span>
            </td>

            <td class="p-4 text-right">
              <button 
                @click="deleteUser(user)"
                class="text-red-400 hover:text-red-600 p-2 rounded hover:bg-red-50 transition"
                title="Delete User"
              >
                <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" /></svg>
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div v-if="showModal" class="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 overflow-y-auto p-4">
      <div class="bg-white rounded-xl shadow-2xl w-full max-w-2xl p-6">
        <h3 class="text-xl font-bold text-gray-800 mb-6">Add New User</h3>
        
        <form @submit.prevent="createUser" class="space-y-4">
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="col-span-1 md:col-span-2">
                <label class="block text-sm font-bold text-gray-700 mb-1">Full Name</label>
                <input v-model="form.name" type="text" required class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none">
            </div>

            <div>
                <label class="block text-sm font-bold text-gray-700 mb-1">Email</label>
                <input v-model="form.email" type="email" required class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none">
            </div>

            <div>
                <label class="block text-sm font-bold text-gray-700 mb-1">Password</label>
                <input v-model="form.password" type="password" required minlength="6" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none">
            </div>

            <div>
                <label class="block text-sm font-bold text-gray-700 mb-1">NIP</label>
                <input v-model="form.nip" type="text" required class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none">
            </div>

            <div>
                <label class="block text-sm font-bold text-gray-700 mb-1">Phone Number</label>
                <input v-model="form.phone" type="text" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none">
            </div>

            <div>
                <label class="block text-sm font-bold text-gray-700 mb-1">Date of Birth</label>
                <input v-model="form.date_birth" type="date" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none">
            </div>

             <div class="col-span-1 md:col-span-2">
                <label class="block text-sm font-bold text-gray-700 mb-1">Address</label>
                <textarea v-model="form.address" rows="2" class="w-full border border-gray-300 rounded-lg px-4 py-2 focus:ring-2 focus:ring-blue-500 outline-none"></textarea>
            </div>
          </div>

          <div class="flex items-center justify-between bg-gray-50 p-4 rounded-lg border border-gray-200 mt-4">
            <div>
                <span class="font-bold text-gray-700 block">Admin Privileges</span>
                <span class="text-xs text-gray-500">Enable to give full access</span>
            </div>
            <label class="relative inline-flex items-center cursor-pointer">
              <input type="checkbox" v-model="form.role" class="sr-only peer">
              <div class="w-11 h-6 bg-gray-300 peer-focus:outline-none rounded-full peer peer-checked:after:translate-x-full peer-checked:after:border-white after:content-[''] after:absolute after:top-[2px] after:left-[2px] after:bg-white after:border-gray-300 after:border after:rounded-full after:h-5 after:w-5 after:transition-all peer-checked:bg-purple-600"></div>
            </label>
          </div>

          <div v-if="errorMsg" class="text-red-600 text-sm bg-red-50 p-2 rounded border border-red-200 mt-2">
            {{ errorMsg }}
          </div>

          <div class="flex justify-end space-x-3 pt-6 border-t mt-4">
            <button type="button" @click="closeModal" class="px-4 py-2 text-gray-600 font-bold hover:bg-gray-100 rounded-lg">Cancel</button>
            <button 
              type="submit" 
              :disabled="submitting"
              class="px-6 py-2 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 disabled:opacity-50"
            >
              {{ submitting ? 'Creating...' : 'Create Account' }}
            </button>
          </div>

        </form>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, reactive, onMounted } from 'vue'
import { supabase } from '../supabase'

const loading = ref(true)
const users = ref([])
const showModal = ref(false)
const submitting = ref(false)
const errorMsg = ref('')

// Form now matches your CSV structure
const form = reactive({
  name: '',
  email: '',
  password: '',
  role: false,
  nip: '',
  phone: '',
  date_birth: '',
  address: ''
})

// 1. Fetch Users
onMounted(fetchUsers)

async function fetchUsers() {
  loading.value = true
  const { data, error } = await supabase
    .from('profiles')
    .select('*')
    .order('created_at', { ascending: false })
  
  if (data) users.value = data
  loading.value = false
}

// 2. Create User
async function createUser() {
  submitting.value = true
  errorMsg.value = ''

  try {
    const response = await fetch('http://localhost:5000/admin/create-user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(form)
    })

    const result = await response.json()
    if (!response.ok) throw new Error(result.error || 'Failed to create user')

    alert('User created successfully!')
    closeModal()
    fetchUsers() 

  } catch (err) {
    errorMsg.value = err.message
  } finally {
    submitting.value = false
  }
}

// 3. Delete User
async function deleteUser(user) {
  if (!confirm(`Are you sure you want to delete ${user.name}?`)) return

  try {
    const response = await fetch('http://localhost:5000/admin/delete-user', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ user_uid: user.user_uid }) // NOTE: CSV uses 'user_uid'
    })

    if (!response.ok) throw new Error('Failed to delete user')

    users.value = users.value.filter(u => u.uid !== user.uid)
    alert('User deleted.')

  } catch (err) {
    alert(err.message)
  }
}

function closeModal() {
  showModal.value = false
  Object.assign(form, {
    name: '', email: '', password: '', role: false, 
    nip: '', phone: '', date_birth: '', address: ''
  })
  errorMsg.value = ''
}
</script>