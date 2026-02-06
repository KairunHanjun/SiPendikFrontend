<template>
  <div class="min-h-screen flex items-center justify-center bg-gradient-to-br from-blue-50 to-indigo-100 p-4">
    
    <div class="bg-white w-full max-w-5xl rounded-2xl shadow-2xl overflow-hidden flex flex-col md:flex-row h-auto md:h-[600px]">
      
      <div class="w-full md:w-1/2 p-8 md:p-12 flex flex-col justify-center relative">
        
        <div class="absolute top-8 left-8 flex space-x-4">
           <img :src="JakartaIcon" alt="Logo Jakarta" class="h-16 w-auto object-contain">
           
           <img :src="KedoyaIcon" alt="Logo Kedoya" class="h-16 w-auto object-contain">
        </div>

        <div class="mt-16 mb-8">
          <h1 class="text-3xl font-extrabold text-gray-800 mb-2">Selamat Datang</h1>
          <p class="text-gray-500">Silahkan masuk untuk mengakses Sistem Arsip Digital.</p>
        </div>

        <form @submit.prevent="handleLogin" class="space-y-6">
          
          <div>
            <label class="block text-sm font-bold text-gray-700 mb-2">Email Address</label>
            <div class="relative">
              <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-gray-400">
                <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207" /></svg>
              </span>
              <input 
                v-model="email" 
                type="email" 
                placeholder="nama@kedoyaselatan.go.id" 
                class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition outline-none"
                required
              >
            </div>
          </div>

          <div>
             <label class="block text-sm font-bold text-gray-700 mb-2">Password</label>
             <div class="relative">
              <span class="absolute inset-y-0 left-0 pl-3 flex items-center text-gray-400">
                <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" /></svg>
              </span>
              <input 
                v-model="password" 
                type="password" 
                placeholder="••••••••" 
                class="w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition outline-none"
                required
              >
            </div>
          </div>

          <div v-if="errorMsg" class="bg-red-50 text-red-600 text-sm p-3 rounded-lg border border-red-100 flex items-center">
            <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20"><path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7 4a1 1 0 11-2 0 1 1 0 012 0zm-1-9a1 1 0 00-1 1v4a1 1 0 102 0V6a1 1 0 00-1-1z" clip-rule="evenodd"/></svg>
            {{ errorMsg }}
          </div>

          <button 
            type="submit" 
            :disabled="loading"
            class="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg shadow-lg hover:shadow-xl transition duration-200 transform hover:-translate-y-0.5 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ loading ? 'Memproses...' : 'Masuk ke Dashboard' }}
          </button>

        </form>

        <div class="mt-8 text-center text-xs text-gray-400">
          &copy; 2026 Kelurahan Kedoya Selatan. All rights reserved.
        </div>
      </div>

      <div class="hidden md:flex w-1/2 bg-blue-600 items-center justify-center p-12 relative overflow-hidden">
        <div class="absolute inset-0 bg-blue-600 opacity-90 z-10"></div>
        <img :src="Placeholder" alt="Background Office" class="absolute inset-0 w-full h-full object-cover mix-blend-overlay opacity-50">
        
        <div class="relative z-20 text-center text-white">
            <h2 class="text-4xl font-bold mb-4">Efisiensi Arsip</h2>
            <p class="text-blue-100 text-lg mb-8">Kelola surat masuk, keluar, dan dokumen penting dalam satu pintu digital.</p>
            
            </div>
        
        <div class="absolute -bottom-24 -right-24 w-64 h-64 bg-white opacity-10 rounded-full z-0"></div>
        <div class="absolute -top-24 -left-24 w-64 h-64 bg-white opacity-10 rounded-full z-0"></div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { supabase } from '../supabase'
import { logActivity } from '../utils/logger' // Ensure you import the logger
import JakartaIcon from '../assets/Jakarta.jpeg'
import KedoyaIcon from '../assets/Kedoya.jpeg'
import Placeholder from '../assets/placeholder.jpeg'
const router = useRouter()
const email = ref('')
const password = ref('')
const loading = ref(false)
const errorMsg = ref('')

const handleLogin = async () => {
  loading.value = true
  errorMsg.value = ''

  try {
    const { data, error } = await supabase.auth.signInWithPassword({
      email: email.value,
      password: password.value,
    })

    if (error) throw error
    
    // Log the successful login
    // Note: data.user exists if login is successful
    if (data?.user) {
        // We log slightly differently here because we might not have the user session 
        // fully set in the global state yet, but data.user has the info we need.
        // However, our logger uses getUser(), which should work immediately after signIn.
        await logActivity('LOGIN', 'User successfully logged in')
    }

    router.push('/')

  } catch (error) {
    errorMsg.value = 'Login Gagal: ' + error.message
  } finally {
    loading.value = false
  }
}
</script>