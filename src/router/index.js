import { createRouter, createWebHistory } from 'vue-router'
import { supabase } from '../supabase'

import Dashboard from '../views/Dashboard.vue'
import Login from '../views/Login.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/auth',
      name: 'login',
      component: Login,
      meta: { guestOnly: true }
    },
    {
      path: '/',
      name: 'dashboard',
      component: Dashboard,
      meta: {requiresAuth: true}
    }
  ]
})

// --- THE BOUNCER ---
router.beforeEach(async (to, from, next) => {
  // Check Supabase session status
  const { data: { session } } = await supabase.auth.getSession()

  // SCENARIO 1: Trying to enter a Protected Route (Dashboard) without login
  if (to.meta.requiresAuth && !session) {
    next('/auth')
    return
  }

  // SCENARIO 2: Trying to enter a Guest Route (Login) while ALREADY logged in
  if (to.meta.guestOnly && session) {
    next('/') // Kick them back to dashboard
    return
  }

  // Otherwise, let them pass
  next()
})

export default router