<script setup>
import { ref } from 'vue'
import UploadDropzone from '../components/UploadDropzone.vue'
import ResultsPanel from '../components/ResultsPanel.vue'

const apiBaseUrl = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

const selectedFile = ref(null)
const result = ref(null)
const error = ref('')
const submitting = ref(false)

const ICONS = {
  document:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="5" y="3" width="14" height="18" rx="2" /><line x1="8" y1="8" x2="16" y2="8" /><line x1="8" y1="12" x2="16" y2="12" /><line x1="8" y1="16" x2="13" y2="16" /></svg>',
  scan:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="4" y="4" width="16" height="16" rx="2" /><line x1="4" y1="12" x2="20" y2="12" stroke-width="2" /><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none" /></svg>',
  layers:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M12 3 L21 8 L12 13 L3 8 Z" /><path d="M3 13 L12 18 L21 13" /><path d="M3 17.5 L12 22.5 L21 17.5" /></svg>',
  chart:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="20" x2="20" y2="20" /><rect x="6" y="13" width="3" height="7" fill="currentColor" stroke="none" /><rect x="11" y="9" width="3" height="11" fill="currentColor" stroke="none" /><rect x="16" y="5" width="3" height="15" fill="currentColor" stroke="none" /></svg>',
}

const capabilities = [
  {
    icon: 'document',
    title: 'Direct text extraction',
    text: 'Born-digital PDFs get their embedded text pulled directly, no OCR pass needed.',
  },
  {
    icon: 'scan',
    title: 'OCR for scans & images',
    text: 'Scanned pages and photos fall back to EasyOCR automatically.',
  },
  {
    icon: 'layers',
    title: 'Document classification',
    text: 'A trained model labels the document type: pay stub, bank statement, or budget sheet.',
  },
  {
    icon: 'chart',
    title: 'Plain-language insights',
    text: 'Withholding rate, savings rate, and overspending flags, generated from the extracted fields.',
  },
]

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
    <section class="hero">
      <h1>Turn financial documents into clear, actionable insights</h1>
      <p class="hero-subtitle">
        Upload a pay stub, bank statement, or budget sheet and see extraction,
        classification, and budgeting analysis run end to end.
      </p>
      <div class="hero-stats">
        <div class="hero-stat">
          <span class="hero-stat-value">PDF · PNG · JPEG</span>
          <span class="hero-stat-label">Supported formats</span>
        </div>
        <div class="hero-stat">
          <span class="hero-stat-value">OCR + ML</span>
          <span class="hero-stat-label">Extraction pipeline</span>
        </div>
        <div class="hero-stat">
          <span class="hero-stat-value">In-memory only</span>
          <span class="hero-stat-label">File handling</span>
        </div>
      </div>
    </section>

    <section class="capabilities">
      <div v-for="capability in capabilities" :key="capability.title" class="capability-card card">
        <span class="capability-icon icon" v-html="ICONS[capability.icon]"></span>
        <h3>{{ capability.title }}</h3>
        <p>{{ capability.text }}</p>
      </div>
    </section>

    <section class="scan-section">
      <h2>Scan a document</h2>
      <UploadDropzone @file-selected="onFileSelected" />

      <div v-if="submitting" class="status-line">Analyzing document…</div>
      <p v-if="error" class="error">{{ error }}</p>

      <ResultsPanel v-if="result" :result="result" />
    </section>
  </div>
</template>

<style scoped>
.scan-page {
  display: flex;
  flex-direction: column;
  gap: var(--space-7);
}

.hero {
  background: linear-gradient(135deg, var(--color-primary-soft), var(--color-surface));
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-7) var(--space-6);
}

.hero h1 {
  font-size: 2rem;
  max-width: 24ch;
  margin-bottom: var(--space-3);
}

.hero-subtitle {
  color: var(--color-text-muted);
  max-width: 56ch;
  margin-bottom: var(--space-6);
}

.hero-stats {
  display: flex;
  gap: var(--space-6);
  flex-wrap: wrap;
}

.hero-stat {
  display: flex;
  flex-direction: column;
  gap: var(--space-1);
}

.hero-stat-value {
  font-weight: 600;
  font-size: 1rem;
}

.hero-stat-label {
  font-size: 0.78rem;
  color: var(--color-text-muted);
}

.capabilities {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--space-4);
}

.capability-card {
  padding: var(--space-5);
}

.capability-icon {
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  background: var(--color-primary-soft);
  color: var(--color-primary);
  align-items: center;
  justify-content: center;
  margin-bottom: var(--space-3);
}

.capability-icon :deep(svg) {
  width: 18px;
  height: 18px;
}

.capability-card h3 {
  font-size: 0.98rem;
  margin-bottom: var(--space-2);
}

.capability-card p {
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.scan-section h2 {
  font-size: 1.15rem;
  margin-bottom: var(--space-4);
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
