import { createClient, SupabaseClient } from '@supabase/supabase-js';

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || 'https://awtuyagramircsbjnjzy.supabase.co';
const supabaseAnonKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImF3dHV5YWdyYW1pcmNzYmpuanp5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3ODY0NzE1NTAsImV4cCI6MjEwMjA0NzU1MH0.YETc2c5vWFal1uS2PHU2yfhJ-3_9mtM1VbPjerBjzSU';

export function getSupabaseClient(): SupabaseClient {
  return createClient(supabaseUrl, supabaseAnonKey, {
    auth: {
      persistSession: true,
      autoRefreshToken: true,
    },
  });
}
