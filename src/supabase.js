import { createClient } from '@supabase/supabase-js'
const supabaseUrl = 'https://vtlusodnxzwanjjjboct.supabase.co'
const supabaseKey = "sb_publishable_kjdjityagtlUHcIwBuBkrw_fcPuYPJd"
export const supabase = createClient(supabaseUrl, supabaseKey)

