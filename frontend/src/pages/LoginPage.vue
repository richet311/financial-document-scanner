<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { signIn, signUp } from '../store/auth'

const router = useRouter()

const mode = ref('sign-in')
const email = ref('')
const password = ref('')
const error = ref('')
const info = ref('')
const submitting = ref(false)

function toggleMode() {
  mode.value = mode.value === 'sign-in' ? 'sign-up' : 'sign-in'
  error.value = ''
  info.value = ''
}

async function onSubmit() {
  error.value = ''
  info.value = ''
  submitting.value = true
  try {
    if (mode.value === 'sign-in') {
      await signIn(email.value, password.value)
      router.push('/dashboard')
    } else {
      await signUp(email.value, password.value)
      info.value = 'Account created. Check your email to confirm, then sign in.'
      mode.value = 'sign-in'
    }
  } catch (err) {
    error.value = err.message
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <div class="login-page">
    <div class="login-box">
      <h1>{{ mode === 'sign-in' ? 'Sign in' : 'Create an account' }}</h1>
      <p class="subtitle">
        {{
          mode === 'sign-in'
            ? 'Sign in to see your saved scan history and reports.'
            : 'Create an account to start saving your scan history.'
        }}
      </p>

      <form class="login-form" @submit.prevent="onSubmit">
        <label>
          Email
          <input v-model="email" type="email" required autocomplete="email" />
        </label>
        <label>
          Password
          <input v-model="password" type="password" required autocomplete="current-password" minlength="6" />
        </label>
        <button type="submit" class="btn btn-primary" :disabled="submitting">
          {{ submitting ? 'Please wait...' : mode === 'sign-in' ? 'Sign in' : 'Create account' }}
        </button>
      </form>

      <p v-if="error" class="error">{{ error }}</p>
      <p v-if="info" class="info">{{ info }}</p>

      <button type="button" class="toggle-link" @click="toggleMode">
        {{ mode === 'sign-in' ? "Don't have an account? Create one" : 'Already have an account? Sign in' }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.login-page {
  display: flex;
  justify-content: center;
  padding-top: var(--space-7);
}

.login-box {
  width: 100%;
  max-width: 380px;
}

.login-box h1 {
  font-size: 1.6rem;
  margin-bottom: var(--space-2);
}

.subtitle {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  margin-bottom: var(--space-5);
}

.login-form {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
}

.login-form label {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.login-form input {
  padding: var(--space-2) var(--space-3);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  background: var(--color-bg);
  color: var(--color-text);
  font-size: 0.95rem;
}

.error {
  color: var(--color-danger);
  font-size: 0.85rem;
  margin-top: var(--space-3);
}

.info {
  color: var(--color-success);
  font-size: 0.85rem;
  margin-top: var(--space-3);
}

.toggle-link {
  background: none;
  border: none;
  color: var(--color-primary);
  font-size: 0.85rem;
  margin-top: var(--space-5);
  cursor: pointer;
  padding: 0;
}
</style>
