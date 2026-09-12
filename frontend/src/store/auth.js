import { reactive } from 'vue'

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

export const authStore = reactive({
  token: '',
  username: '',
})

export async function login(username, password) {
  const response = await fetch(`${apiBaseUrl}/api/auth/login`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ username, password }),
  })
  const data = await response.json()

  if (!response.ok) {
    throw new Error(data.detail || 'Login failed.')
  }

  authStore.token = data.access_token
  authStore.username = username
}

export function logout() {
  authStore.token = ''
  authStore.username = ''
}
