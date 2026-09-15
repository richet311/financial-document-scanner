<script setup>
import { useRouter } from 'vue-router'
import ProductPreview from '../components/ProductPreview.vue'

const router = useRouter()

const ICONS = {
  shield:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M12 3 L19 6 V11 C19 16 16 19.5 12 21 C8 19.5 5 16 5 11 V6 Z" /><path d="M9 12 L11 14 L15 9.5" /></svg>',
}

const pipeline = [
  {
    label: 'Extract',
    text: 'Reads embedded PDF text directly, or falls back to OCR for scanned documents and images.',
  },
  {
    label: 'Classify',
    text: 'Identifies whether the document is a pay stub, bank statement, or budget sheet.',
  },
  {
    label: 'Analyze',
    text: 'Pulls out the relevant financial fields and calculates income, expenses, and savings rate.',
  },
  {
    label: 'Understand',
    text: 'Presents the results as a plain-language financial insight.',
  },
]

const privacyPoints = [
  'Files are validated before processing.',
  'Uploads are processed in memory.',
  'Original files are not permanently stored.',
  'API endpoints are rate limited.',
]

function goToScan() {
  router.push('/scan')
}

function goToSamples() {
  router.push('/samples')
}

function goToPrivacy() {
  router.push('/privacy')
}
</script>

<template>
  <div class="landing">
    <section class="hero">
      <div class="hero-content">
        <h1>Understand your financial<br /> documents instantly.</h1>
        <p class="hero-subtitle">
          Upload a bank statement, pay stub, or budget sheet. Get extracted
          data and financial insights back in seconds.
        </p>

        <div class="hero-actions">
          <button class="btn btn-primary" @click="goToScan">Scan a document</button>
          <button class="btn btn-secondary" @click="goToSamples">View sample documents</button>
        </div>

        <p class="trust-note">
          <span class="icon" v-html="ICONS.shield"></span>
          Files are processed in memory and are not permanently stored.
        </p>
      </div>

      <div class="hero-visual">
        <ProductPreview />
      </div>
    </section>

    <section class="pipeline-section">
      <h2 class="section-heading">How it works</h2>
      <div class="pipeline-list">
        <div v-for="item in pipeline" :key="item.label" class="pipeline-row">
          <span class="pipeline-label">{{ item.label }}</span>
          <span class="pipeline-text">{{ item.text }}</span>
        </div>
      </div>
    </section>

    <section class="privacy-band">
      <span class="privacy-icon icon" v-html="ICONS.shield"></span>
      <div class="privacy-copy">
        <h2 class="section-heading">Your documents stay private.</h2>
        <ul class="privacy-list">
          <li v-for="point in privacyPoints" :key="point">{{ point }}</li>
        </ul>
        <button class="privacy-link" @click="goToPrivacy">Read the full privacy policy</button>
      </div>
    </section>

    <section class="cta-banner">
      <h2 class="section-heading">See what your documents can tell you.</h2>
      <p>Scan a document and receive structured financial insights in seconds.</p>
      <button class="btn btn-primary" @click="goToScan">Scan a document</button>
    </section>
  </div>
</template>

<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  gap: var(--space-6);
}

.hero {
  display: flex;
  align-items: center;
  gap: var(--space-7);
}

.hero-content {
  flex: 1 1 58%;
}

.hero-visual {
  flex: 1 1 42%;
  display: flex;
  justify-content: center;
}

.hero h1 {
  font-size: 2.75rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.15;
  margin-bottom: var(--space-4);
}

.hero-subtitle {
  color: var(--color-text-muted);
  font-size: 1.05rem;
  max-width: 46ch;
  margin-bottom: var(--space-5);
}

.hero-actions {
  display: flex;
  gap: var(--space-3);
  flex-wrap: wrap;
  margin-bottom: var(--space-4);
}

.trust-note {
  display: flex;
  align-items: center;
  gap: var(--space-2);
  font-size: 0.82rem;
  color: var(--color-text-faint);
}

.trust-note .icon {
  width: 15px;
  height: 15px;
  color: var(--color-text-faint);
}

.trust-note .icon :deep(svg) {
  width: 15px;
  height: 15px;
}

.section-heading {
  font-size: 1.4rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: var(--space-5);
}

.pipeline-list {
  display: flex;
  flex-direction: column;
}

.pipeline-row {
  display: flex;
  gap: var(--space-6);
  padding: var(--space-4) 0;
  border-bottom: 1px solid var(--color-border);
}

.pipeline-row:first-child {
  padding-top: 0;
}

.pipeline-row:last-child {
  border-bottom: none;
}

.pipeline-label {
  flex: 0 0 140px;
  font-weight: 600;
}

.pipeline-text {
  flex: 1;
  color: var(--color-text-muted);
  max-width: 62ch;
}

.privacy-band {
  display: flex;
  align-items: flex-start;
  gap: var(--space-4);
  padding: var(--space-6) 0;
  border-top: 1px solid var(--color-border);
}

.privacy-icon {
  flex-shrink: 0;
  color: var(--color-primary);
  margin-top: 2px;
}

.privacy-icon :deep(svg) {
  width: 22px;
  height: 22px;
}

.privacy-copy .section-heading,
.cta-banner .section-heading {
  font-size: 1.15rem;
  margin-bottom: var(--space-3);
}

.privacy-list {
  margin: 0 0 var(--space-3);
  padding: 0;
  list-style: none;
  display: grid;
  grid-template-columns: repeat(2, auto);
  gap: var(--space-2) var(--space-6);
  color: var(--color-text-muted);
  font-size: 0.85rem;
}

.privacy-list li {
  display: flex;
  align-items: center;
  gap: var(--space-2);
}

.privacy-list li::before {
  content: '';
  width: 4px;
  height: 4px;
  border-radius: 50%;
  background: var(--color-text-faint);
  flex-shrink: 0;
}

.privacy-link {
  background: none;
  border: none;
  padding: 0;
  color: var(--color-primary);
  font-size: 0.85rem;
  font-weight: 500;
  cursor: pointer;
}

.privacy-link:hover {
  text-decoration: underline;
}

.cta-banner {
  text-align: center;
  padding: var(--space-6) var(--space-5);
  border-top: 1px solid var(--color-border);
}

.cta-banner p {
  color: var(--color-text-muted);
  margin-bottom: var(--space-5);
}

@media (max-width: 860px) {
  .hero {
    flex-direction: column;
    align-items: stretch;
  }

  .hero h1 {
    font-size: 2.1rem;
  }

  .hero h1 br {
    display: none;
  }

  .pipeline-row {
    flex-direction: column;
    gap: var(--space-1);
  }

  .pipeline-label {
    flex: none;
  }

  .privacy-band {
    flex-direction: column;
  }

  .privacy-list {
    grid-template-columns: 1fr;
  }
}
</style>
