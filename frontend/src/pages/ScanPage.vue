<script setup>
import { ref } from 'vue'
import UploadDropzone from '../components/UploadDropzone.vue'
import ResultsPanel from '../components/ResultsPanel.vue'
import { authStore } from '../store/auth'

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const selectedFile = ref(null)
const result = ref(null)
const error = ref('')
const submitting = ref(false)

function onFileSelected(file) {
  selectedFile.value = file
  result.value = null
  error.value = ''
  submitUpload()
}

async function submitUpload() {
  if (!selectedFile.value) return

  submitting.value = true
  result.value = null
  error.value = ''

  const formData = new FormData()
  formData.append('file', selectedFile.value)

  try {
    const headers = {}
    if (authStore.session) {
      headers.Authorization = `Bearer ${authStore.session.access_token}`
    }

    const response = await fetch(`${apiBaseUrl}/api/documents/upload`, {
      method: 'POST',
      headers,
      body: formData,
    })
    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.detail || `Upload failed with status ${response.status}`)
    }

    result.value = data
  } catch (err) {
    error.value = err.message
    console.error('Upload failed:', err)
  } finally {
    submitting.value = false
  }
}
</script>

<template>
  <div class="scan-page">
    <header class="page-header">
      <h1>Scan a document</h1>
      <p class="page-subtitle">
        Upload a sample pay stub, bank statement, or budget sheet to see the
        extraction, classification, and budgeting insights pipeline run.
      </p>
    </header>

    <UploadDropzone @file-selected="onFileSelected" />

    <div v-if="submitting" class="status-line">Analyzing document…</div>
    <p v-if="error" class="error">{{ error }}</p>

    <p v-if="result && !authStore.user" class="save-note">
      Sign in to automatically save results like this one to your account.
    </p>
    <p v-else-if="result && result.saved" class="save-note save-note-success">
      Saved to your account. View it on the Dashboard.
    </p>

    <ResultsPanel v-if="result" :result="result" />
  </div>
</template>

<style scoped>
.scan-page {
  display: flex;
  flex-direction: column;
}

.status-line {
  margin-top: var(--space-4);
  font-size: 0.88rem;
  color: var(--color-text-muted);
}

.error {
  margin-top: var(--space-4);
  color: var(--color-danger);
  font-size: 0.88rem;
}

.save-note {
  margin-top: var(--space-4);
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.save-note-success {
  color: var(--color-success);
}
</style>
