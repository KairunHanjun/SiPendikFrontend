<script setup>
  import { RouterView, useRoute } from 'vue-router'

  const route = useRoute()
</script>

<template>
  <div class="min-h-screen bg-gray-100 p-8 flex justify-center">
    
    <div class="w-full max-w-5xl bg-white border border-gray-200 rounded-lg shadow-xl overflow-hidden">
      
      <div class="px-6 py-4 border-b border-gray-200 flex justify-between items-center bg-white">
        <h2 class="text-xl font-bold text-gray-700">Unggah Dokumen / Upload File</h2>
      </div>

      <div class="p-6">
        <div class="bg-white border border-gray-200 rounded-lg p-4 mb-6 flex items-center shadow-sm">
          <div class="bg-green-500 rounded-md p-1 mr-3 flex-shrink-0">
            <svg class="w-6 h-6 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <div class="flex-grow">
            <h3 class="font-bold text-gray-800 text-lg">Upload File Arsip</h3>
          </div>
          <a href="#" class="text-blue-600 text-sm hover:underline font-medium">Show details</a>
        </div>

        <div class="bg-white border border-gray-200 rounded-lg shadow-sm overflow-hidden">
          
          <div class="p-4 border-b border-gray-200 flex items-center bg-gray-50">
            <div class="w-8 h-8 bg-blue-600 text-white rounded-md flex items-center justify-center font-bold mr-3 shadow-md">2</div>
            <h3 class="font-bold text-gray-800 text-lg">Detail Isi Dokumen</h3>
          </div>

          <div class="p-6 grid grid-cols-1 lg:grid-cols-12 gap-8">
            
            <div class="lg:col-span-7 space-y-5">
              
              <div>
                 <div class="flex justify-between mb-1">
                    <label class="block text-sm font-bold text-gray-700">Nama</label>
                    <span class="text-xs text-gray-400">0/4 mapped*</span>
                 </div>
                 <input type="text" placeholder="Seret bidang atribut ke sini untuk memetakan" 
                        class="w-full px-4 py-2.5 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 focus:border-blue-500 outline-none transition shadow-sm">
              </div>

              <div class="grid grid-cols-1 gap-5">
                <div>
                   <label class="block text-sm font-bold text-gray-700 mb-1">Jenis Naskah</label>
                   <select class="w-full px-4 py-2.5 border border-gray-300 rounded-lg text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none shadow-sm">
                     <option>Pilih Jenis Naskah</option>
                     <option>Surat Keputusan</option>
                     <option>Surat Edaran</option>
                   </select>
                </div>
                <div>
                   <label class="block text-sm font-bold text-gray-700 mb-1">Sifat Naskah</label>
                   <select class="w-full px-4 py-2.5 border border-gray-300 rounded-lg text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none shadow-sm">
                     <option>Pilih Sifat Naskah</option>
                     <option>Biasa</option>
                     <option>Rahasia</option>
                   </select>
                </div>
                <div>
                   <label class="block text-sm font-bold text-gray-700 mb-1">Klasifikasi</label>
                   <select class="w-full px-4 py-2.5 border border-gray-300 rounded-lg text-sm bg-white focus:ring-2 focus:ring-blue-500 outline-none shadow-sm">
                     <option>Pilih Unit Kerja</option>
                     <option>Keuangan</option>
                     <option>Umum</option>
                   </select>
                </div>
              </div>

              <div>
                 <label class="block text-sm font-bold text-gray-700 mb-1">Nomor Naskah</label>
                 <div class="flex space-x-2">
                   <input type="text" placeholder="Masukkan Nomor Naskah" class="flex-grow px-4 py-2.5 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none shadow-sm">
                   <button class="bg-blue-50 text-blue-600 px-4 py-2 rounded-lg text-sm font-bold border border-blue-200 hover:bg-blue-100 transition">Ambil Nomor</button>
                 </div>
              </div>

              <div>
                 <label class="block text-sm font-bold text-gray-700 mb-1">Nomor Referensi</label>
                 <input type="text" placeholder="Pilih Nomor Naskah" class="w-full px-4 py-2.5 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none shadow-sm">
              </div>
            </div>

            <div class="lg:col-span-5">
              <div class="flex justify-between items-center mb-4">
                <h4 class="font-bold text-gray-800">Atribut Kontak</h4>
                <button class="text-blue-600 text-sm font-bold hover:underline">+ Tambahkan bidang</button>
              </div>
              
              <div class="relative mb-6">
                 <span class="absolute left-3 top-2.5 text-gray-400">
                   <svg class="w-5 h-5" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z" /></svg>
                 </span>
                 <input type="text" placeholder="Search" class="w-full pl-10 pr-4 py-2.5 border border-gray-300 rounded-lg text-sm focus:ring-2 focus:ring-blue-500 outline-none shadow-sm">
              </div>

              <div>
                 <label class="block text-sm font-bold text-gray-700 mb-2">Upload File</label>
                 <div class="border-2 border-dashed border-gray-300 rounded-lg h-72 flex flex-col items-center justify-center text-center p-4 bg-gray-50 hover:bg-gray-100 hover:border-blue-400 transition-all cursor-pointer group">
                    <div class="p-4 bg-white rounded-full mb-3 shadow-sm group-hover:scale-110 transition-transform">
                      <svg class="w-8 h-8 text-blue-500" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 6L16 6a5 5 0 011 9.9M15 13l-3-3m0 0l-3 3m3-3v12" />
                      </svg>
                    </div>
                    <p class="text-gray-700 font-bold mb-1">Format File</p>
                    <p class="text-gray-500 text-sm">yang Didukung .pdf dan .doc | Maks 5mb</p>
                 </div>
              </div>
            </div>
          </div>

          <div class="bg-blue-50/50 p-6 border-t border-gray-200">
             
             <div class="flex items-center mb-6">
                <div class="w-5 h-5 border-2 border-gray-400 rounded mr-2 flex items-center justify-center bg-white"></div>
                <span class="text-gray-700 font-bold text-sm">Verifikator dan penandatangan naskah</span>
             </div>

             <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                <div>
                  <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Verifikator</label>
                  <select class="w-full px-4 py-2 border border-gray-300 rounded-lg text-sm bg-white focus:ring-blue-500 shadow-sm"><option>Pilih Unit Kerja</option></select>
                </div>
                 <div>
                  <label class="block text-xs font-bold text-gray-500 uppercase mb-1">Penanda Tangan</label>
                  <select class="w-full px-4 py-2 border border-gray-300 rounded-lg text-sm bg-white focus:ring-blue-500 shadow-sm"><option>Pilih Unit Kerja</option></select>
                </div>
             </div>

             <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div>
                   <label class="block text-xs font-bold text-gray-500 uppercase mb-3">Tipe Tanda Tangan</label>
                   <div class="flex space-x-6">
                      <label class="flex items-center space-x-2 cursor-pointer select-none">
                        <input type="checkbox" checked class="w-5 h-5 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
                        <span class="text-sm font-medium text-gray-700">TTE</span>
                      </label>
                       <label class="flex items-center space-x-2 cursor-pointer select-none">
                        <input type="checkbox" class="w-5 h-5 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
                        <span class="text-sm font-medium text-gray-700">TTD</span>
                      </label>
                   </div>
                </div>
                <div>
                   <label class="block text-xs font-bold text-gray-500 uppercase mb-3">Visual TTE</label>
                   <div class="flex space-x-6">
                      <label class="flex items-center space-x-2 cursor-pointer select-none">
                        <input type="checkbox" checked class="w-5 h-5 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
                        <span class="text-sm font-medium text-gray-700">QR</span>
                      </label>
                       <label class="flex items-center space-x-2 cursor-pointer select-none">
                        <input type="checkbox" checked class="w-5 h-5 text-blue-600 rounded border-gray-300 focus:ring-blue-500">
                        <span class="text-sm font-medium text-gray-700">Spedman Gambar</span>
                      </label>
                   </div>
                </div>
             </div>

             <div class="flex justify-end space-x-3 border-t border-gray-200 pt-6">
               <button class="px-6 py-2.5 bg-red-600 text-white font-bold rounded-lg hover:bg-red-700 transition shadow-md">Reset</button>
               <button class="px-6 py-2.5 bg-blue-600 text-white font-bold rounded-lg hover:bg-blue-700 transition shadow-md">Simpan</button>
             </div>
          </div>

        </div>
      </div>

    </div>
  </div>
</template>
