<script setup>
import { onMounted, ref } from 'vue'
import { useRoute } from 'vue-router'
import UploadDropzone from '../components/UploadDropzone.vue'
import ResultsPanel from '../components/ResultsPanel.vue'
import { authStore } from '../store/auth'
import { SAMPLE_DOCUMENTS, fetchSampleFile } from '../lib/sampleDocuments'

const route = useRoute()
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const selectedFile = ref(null)
const result = ref(null)
const error = ref('')
const submitting = ref(false)
const loadingSample = ref('')

function onFileSelected(file) {
  selectedFile.value = file
  result.value = null
  error.value = ''
  submitUpload()
}

async function useSample(doc) {
  error.value = ''
  loadingSample.value = doc.key
  try {
    const file = await fetchSampleFile(doc)
    onFileSelected(file)
  } catch (err) {
    error.value = err.message
  } finally {
    loadingSample.value = ''
  }
}

onMounted(() => {
  const sampleKey = route.query.sample
  const match = SAMPLE_DOCUMENTS.find((doc) => doc.key === sampleKey)
  if (match) useSample(match)
})

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
    </header>

    <UploadDropzone @file-selected="onFileSelected" />

    <p class="privacy-line">Uploads are processed in memory and are never permanently stored unless you sign in.</p>

    <div class="samples-row">
      <span class="samples-label">Try a sample:</span>
      <button
        v-for="doc in SAMPLE_DOCUMENTS"
        :key="doc.key"
        type="button"
        class="sample-chip"
        :disabled="loadingSample === doc.key"
        @click="useSample(doc)"
      >
        {{ loadingSample === doc.key ? 'Loading...' : doc.title }}
      </button>
    </div>

    <div v-if="submitting" class="status-line">Analyzing document...</div>
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
  max-width: 640px;
}

.page-header {
  margin-bottom: var(--space-4);
}

.page-header h1 {
  font-size: 1.5rem;
}

.privacy-line {
  font-size: 0.8rem;
  color: var(--color-text-faint);
  margin-top: var(--space-3);
}

.samples-row {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  flex-wrap: wrap;
  margin-top: var(--space-5);
  padding-top: var(--space-5);
  border-top: 1px solid var(--color-border);
}

.samples-label {
  font-size: 0.85rem;
  color: var(--color-text-muted);
  margin-right: var(--space-1);
}

.sample-chip {
  font-size: 0.82rem;
  font-weight: 500;
  color: var(--color-text);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-sm);
  padding: var(--space-1) var(--space-3);
  cursor: pointer;
  transition: border-color 0.15s ease, background-color 0.15s ease;
}

.sample-chip:hover:not(:disabled) {
  border-color: var(--color-text-faint);
  background: var(--color-surface-muted);
}

.sample-chip:disabled {
  opacity: 0.6;
  cursor: not-allowed;
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
