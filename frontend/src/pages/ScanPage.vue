<script setup>
import { ref } from 'vue'
import UploadDropzone from '../components/UploadDropzone.vue'
import ResultsPanel from '../components/ResultsPanel.vue'

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
    const response = await fetch(`${apiBaseUrl}/api/documents/upload`, {
      method: 'POST',
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

    <ResultsPanel v-if="result" :result="result" />
  </div>
</template>

<style scoped>
.scan-page {
  display: flex;
  flex-direction: column;
}

.page-header {
  margin-bottom: var(--space-5);
}

.page-header h1 {
  font-family: var(--font-serif);
  font-style: italic;
  font-weight: 500;
  font-size: 1.7rem;
  color: var(--color-primary);
  margin-bottom: var(--space-2);
}

.page-subtitle {
  color: var(--color-text-muted);
  font-size: 0.9rem;
  max-width: 60ch;
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
</style>
