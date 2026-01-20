<template>
  <div class="min-h-screen w-full flex flex-col md:flex-row overflow-x-hidden overflow-y-hidden m-0 p-0">
    
    <div class="w-full md:w-7/12 bg-[#B4CDEB] flex flex-col items-center relative p-6 md:p-12 justify-center">
      
      <div class="flex items-start justify-center space-x-4 w-full max-w-2xl mb-8 md:mb-16">
        <div class="w-12 h-12 md:w-16 md:h-16 bg-gray-300 rounded-full shrink-0 flex items-center justify-center text-[10px] text-gray-500">Logo 1</div>
        
        <div class="text-center">
          <h1 class="text-xl md:text-3xl font-bold text-[#1E3A5F]">Kelurahan Kedoya Selatan</h1>
          <p class="text-xs md:text-sm text-[#3E5A7F] mt-1">Kecamatan Kebon Jeruk, Kota Administrasi Jakarta Barat</p>
        </div>
        
        <div class="w-12 h-12 md:w-16 md:h-16 bg-gray-300 rounded-full shrink-0 flex items-center justify-center text-[10px] text-gray-500">Logo 2</div>
      </div>

      <h2 class="text-3xl md:text-5xl font-extrabold text-[#1E3A5F] mb-8 md:mb-16 text-center">SI PENDIK</h2>

      <div class="w-full max-w-sm aspect-video bg-white/30 rounded-xl border-2 border-white/50 flex items-center justify-center">
        <span class="text-[#3E5A7F] font-medium">Illustration Placeholder</span>
      </div>
    </div>

    <div class="w-full md:w-5/12 bg-[#5578AC] flex flex-col justify-center items-center p-8 md:p-12 text-white shadow-2xl z-10">
      
      <div class="w-full max-w-sm">
        <h2 class="text-4xl font-bold text-center mb-10">Login</h2>

        <form @submit.prevent="handleLogin">
          <div class="mb-5 relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <svg class="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z" />
              </svg>
            </div>
            <input 
              type="text" 
              placeholder="Username" 
              class="w-full py-4 pl-12 pr-4 bg-white rounded-2xl text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#8AA6CF] shadow-md"
            />
          </div>

          <div class="mb-5 relative">
            <div class="absolute inset-y-0 left-0 pl-4 flex items-center pointer-events-none">
              <svg class="h-6 w-6 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z" />
              </svg>
            </div>
            <input 
              type="password" 
              placeholder="Password" 
              class="w-full py-4 pl-12 pr-4 bg-white rounded-2xl text-gray-800 placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-[#8AA6CF] shadow-md"
            />
          </div>

          <div class="flex items-center justify-between mb-8 text-sm">
            <label class="flex items-center cursor-pointer select-none">
              <div class="relative">
                <input type="checkbox" class="sr-only" v-model="rememberMe" />
                <div class="block w-10 h-6 rounded-full transition-colors duration-300" :class="{ 'bg-blue-300': rememberMe, 'bg-gray-300' : !rememberMe }"></div>
                <div class="dot absolute left-1 top-1 bg-white w-4 h-4 rounded-full transition-transform duration-300" :class="{ 'translate-x-4': rememberMe }"></div>
              </div>
              <span class="ml-3 font-medium">Remember me</span>
            </label>
            <a href="#" class="hover:text-blue-200 transition-colors">Forget Password</a>
          </div>

          <button type="submit" class="w-full py-3.5 bg-[#96B5DE] rounded-full text-xl font-bold text-[#1E3A5F] shadow-lg hover:bg-[#A6C3E9] transform active:scale-95 transition-all duration-200">
            Sign In
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const rememberMe = ref(false)
const router = useRouter()
const handleLogin = () => {
  console.log("Logged in!")
  router.push('/dashboard')
}
</script>

<style>
/* CRITICAL: This Global Reset removes the "Black/Gray Box" 
   caused by default browser margins.
*/
body, html {
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  box-sizing: border-box;
}

#app {
  width: 100%;
  height: 100%;
}
</style>