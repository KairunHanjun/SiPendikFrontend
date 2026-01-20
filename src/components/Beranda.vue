<template>
    <main class="flex-1 overflow-y-auto p-8">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8 mb-10">
          <div class="bg-linear-to-br from-blue-500 to-blue-600 rounded-2xl p-6 shadow-lg text-white flex items-center relative overflow-hidden">
            <div class="flex-1 z-10">
              <h3 class="text-lg font-medium text-blue-100 mb-2">Arsip Masuk Hari Ini</h3>
              <p class="text-4xl font-bold">28</p>
            </div>
            <div class="p-4 bg-white/20 rounded-full z-11">
               <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <div class="absolute -bottom-6 -right-6 w-32 h-32 bg-white/10 rounded-full"></div>
          </div>
          <div class="bg-linear-to-br from-indigo-600 to-indigo-700 rounded-2xl p-6 shadow-lg text-white flex items-center relative overflow-hidden">
            <div class="flex-1 z-10">
              <h3 class="text-lg font-medium text-indigo-100 mb-2">Belum Dibaca</h3>
              <p class="text-4xl font-bold">21</p>
            </div>
            <div class="p-4 bg-white/20 rounded-full z-10">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
             <div class="absolute -bottom-6 -right-6 w-32 h-32 bg-white/10 rounded-full"></div>
          </div>
          <div class="bg-linear-to-br from-gray-700 to-gray-800 rounded-2xl p-6 shadow-lg text-white flex items-center relative overflow-hidden">
            <div class="flex-1 z-1">
              <h3 class="text-lg font-medium text-gray-300 mb-2">Total Arsip Masuk</h3>
              <p class="text-4xl font-bold">49</p>
            </div>
            <div class="p-4 bg-white/20 rounded-full z-1">
              <svg xmlns="http://www.w3.org/2000/svg" class="h-10 w-10" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4" />
              </svg>
            </div>
             <div class="absolute -bottom-6 -right-6 w-32 h-32 bg-white/10 rounded-full"></div>
          </div>
        </div>

        <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
          <div class="p-6 border-b border-gray-100 flex justify-between items-center bg-gray-50">
            <h3 class="text-xl font-bold text-gray-800">Surat Terbaru</h3>
            <button class="text-sm text-blue-600 hover:underline font-medium">Lihat Semua</button>
          </div>
          <div class="overflow-x-auto">
            <table class="w-full text-left whitespace-nowrap">
              <thead>
                <tr class="text-gray-500 border-b border-gray-200 bg-gray-50/50 text-sm uppercase font-semibold">
                  <th class="px-6 py-4">No</th>
                  <th class="px-6 py-4">Nomor Surat</th>
                  <th class="px-6 py-4">Pengirim</th>
                  <th class="px-6 py-4">Tanggal</th>
                  <th class="px-6 py-4 text-center">Status</th>
                  <th class="px-6 py-4 text-center">Aksi</th>
                </tr>
              </thead>
              <tbody class="divide-y divide-gray-100">
                <tr class="hover:bg-blue-50/50 transition-colors">
                  <td class="px-6 py-5 font-medium text-gray-700">1</td>
                  <td class="px-6 py-5 font-semibold text-blue-600">421/123/DPK</td>
                  <td class="px-6 py-5 text-gray-600">Sekretariat</td>
                  <td class="px-6 py-5 text-gray-600">20 Agustus 2025</td>
                  <td class="px-6 py-5 text-center">
                    <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-yellow-100 text-yellow-800 border border-yellow-200">
                      Belum Diperiksa
                    </span>
                  </td>
                  <td class="px-6 py-5 text-center">
                    <div class="flex items-center justify-center space-x-3">
                      <button class="p-2 bg-blue-100 text-blue-600 rounded-lg hover:bg-blue-200 transition-colors" title="Lihat Detail">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                        </svg>
                      </button>
                      <button class="p-2 bg-red-100 text-red-600 rounded-lg hover:bg-red-200 transition-colors" title="Hapus">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                      </button>
                    </div>
                  </td>
                </tr>
                <tr class="hover:bg-blue-50/50 transition-colors">
                  <td class="px-6 py-5 font-medium text-gray-700">2</td>
                  <td class="px-6 py-5 font-semibold text-blue-600">421/124/DPK</td>
                  <td class="px-6 py-5 text-gray-600">Sekretariat</td>
                  <td class="px-6 py-5 text-gray-600">20 Agustus 2025</td>
                  <td class="px-6 py-5 text-center">
                    <span class="inline-block px-3 py-1 rounded-full text-xs font-semibold bg-green-100 text-green-800 border border-green-200">
                      Diterima
                    </span>
                  </td>
                  <td class="px-6 py-5 text-center">
                    <div class="flex items-center justify-center space-x-3">
                       <button class="p-2 bg-blue-100 text-blue-600 rounded-lg hover:bg-blue-200 transition-colors" title="Lihat Detail">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
                        </svg>
                      </button>
                      <button class="p-2 bg-red-100 text-red-600 rounded-lg hover:bg-red-200 transition-colors" title="Hapus">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
                        </svg>
                      </button>
                    </div>
                  </td>
                </tr>
                
              </tbody>
            </table>
          </div>
           <div class="p-4 border-t border-gray-100 flex justify-between items-center text-sm text-gray-500 bg-gray-50">
            <span>Menampilkan 1-2 dari 4 data</span>
            <div class="flex space-x-2">
              <button class="px-3 py-1 rounded border bg-white hover:bg-gray-100 disabled:opacity-50">Prev</button>
              <button class="px-3 py-1 rounded border bg-blue-600 text-white font-bold">1</button>
              <button class="px-3 py-1 rounded border bg-white hover:bg-gray-100">2</button>
              <button class="px-3 py-1 rounded border bg-white hover:bg-gray-100">Next</button>
            </div>
          </div>
        </div>

      </main>
</template>