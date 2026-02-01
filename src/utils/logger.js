// src/utils/logger.js
import { supabase } from '../supabase'

export async function logActivity(action, details) {
  try {
    // 1. Get Current User
    const { data: { user } } = await supabase.auth.getUser()
    if (!user) return

    // 2. Insert Log
    await supabase.from('audit_logs').insert({
      user_email: user.email,
      action: action,
      details: details
    })
  } catch (err) {
    console.error("Logging failed:", err) // Don't stop the app if logging fails
  }
}