import { reactive } from 'vue'
import { supabase } from '../lib/supabaseClient'

export const authStore = reactive({
  session: null,
  user: null,
  loading: true,
})

supabase.auth
  .getSession()
  .then(({ data }) => {
    authStore.session = data.session
    authStore.user = data.session?.user ?? null
  })
  .catch((err) => {
    console.error('Could not reach Supabase for the current session:', err.message)
  })
  .finally(() => {
    authStore.loading = false
  })

supabase.auth.onAuthStateChange((_event, session) => {
  authStore.session = session
  authStore.user = session?.user ?? null
  authStore.loading = false
})

export async function signUp(email, password) {
  const { error } = await supabase.auth.signUp({ email, password })
  if (error) throw new Error(error.message)
}

export async function signIn(email, password) {
  const { error } = await supabase.auth.signInWithPassword({ email, password })
  if (error) throw new Error(error.message)
}

export async function signOut() {
  await supabase.auth.signOut()
}
