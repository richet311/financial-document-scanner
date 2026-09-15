<script setup>
import { useRouter } from 'vue-router'
import ProductPreview from '../components/ProductPreview.vue'

const router = useRouter()

const ICONS = {
  scan:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="4" y="4" width="16" height="16" rx="2" /><line x1="4" y1="12" x2="20" y2="12" stroke-width="2" /><circle cx="12" cy="12" r="1.4" fill="currentColor" stroke="none" /></svg>',
  layers:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M12 3 L21 8 L12 13 L3 8 Z" /><path d="M3 13 L12 18 L21 13" /><path d="M3 17.5 L12 22.5 L21 17.5" /></svg>',
  chart:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="20" x2="20" y2="20" /><rect x="6" y="13" width="3" height="7" fill="currentColor" stroke="none" /><rect x="11" y="9" width="3" height="11" fill="currentColor" stroke="none" /><rect x="16" y="5" width="3" height="15" fill="currentColor" stroke="none" /></svg>',
  upload:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M7 18a4 4 0 0 1-1-7.9A5 5 0 0 1 16 8a4.5 4.5 0 0 1 1 8.9" /><path d="M12 12v7" /><path d="M9.5 15.5 12 13l2.5 2.5" /></svg>',
  shield:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round" stroke-linecap="round"><path d="M12 3 L19 6 V11 C19 16 16 19.5 12 21 C8 19.5 5 16 5 11 V6 Z" /><path d="M9 12 L11 14 L15 9.5" /></svg>',
  bulb:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18h6" /><path d="M10 21h4" /><path d="M12 3a6 6 0 0 0-3.5 10.9c.6.45 1 1.15 1 1.9V16h5v-.2c0-.75.4-1.45 1-1.9A6 6 0 0 0 12 3Z" /></svg>',
}

const capabilities = [
  {
    icon: 'scan',
    title: 'Extract',
    text: 'Read embedded PDF text directly, or fall back to OCR for scanned documents.',
  },
  {
    icon: 'layers',
    title: 'Classify',
    text: 'Identify whether the document is a pay stub, bank statement, or budget sheet.',
  },
  {
    icon: 'chart',
    title: 'Analyze',
    text: 'Pull out the important financial values and calculate useful metrics.',
  },
  {
    icon: 'bulb',
    title: 'Understand',
    text: 'See the results as simple, readable financial insights.',
  },
]

const steps = [
  {
    number: '01',
    title: 'Upload',
    text: 'Upload a PDF, PNG, or JPEG.',
  },
  {
    number: '02',
    title: 'Process',
    text: 'Text is extracted and the document is classified.',
  },
  {
    number: '03',
    title: 'Review',
    text: 'View structured financial information and insights.',
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
        <h1>Understand your financial documents instantly.</h1>
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

    <section class="capabilities-section">
      <h2 class="section-heading">From document to insight in seconds</h2>
      <div class="capabilities">
        <div v-for="capability in capabilities" :key="capability.title" class="capability">
          <span class="capability-icon icon" v-html="ICONS[capability.icon]"></span>
          <h3>{{ capability.title }}</h3>
          <p>{{ capability.text }}</p>
        </div>
      </div>
    </section>

    <section class="steps-section">
      <h2 class="section-heading">How it works</h2>
      <div class="steps">
        <div class="steps-line" aria-hidden="true"></div>
        <div v-for="step in steps" :key="step.number" class="step">
          <div class="step-number">{{ step.number }}</div>
          <h3>{{ step.title }}</h3>
          <p>{{ step.text }}</p>
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
  flex: 1 1 52%;
}

.hero h1 {
  font-size: 2.75rem;
  font-weight: 700;
  letter-spacing: -0.03em;
  line-height: 1.1;
  max-width: 14ch;
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

.hero-visual {
  flex: 1 1 48%;
  display: flex;
  justify-content: center;
}

.section-heading {
  font-size: 1.6rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  margin-bottom: var(--space-6);
}

.capabilities {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: var(--space-6);
}

.capability-icon {
  color: var(--color-accent);
  margin-bottom: var(--space-3);
}

.capability-icon :deep(svg) {
  width: 22px;
  height: 22px;
}

.capability h3 {
  font-size: 1rem;
  margin-bottom: var(--space-2);
}

.capability p {
  font-size: 0.87rem;
  color: var(--color-text-muted);
  line-height: 1.5;
}

.steps {
  position: relative;
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: var(--space-6);
}

.steps-line {
  position: absolute;
  top: 15px;
  left: calc((100% - 2 * var(--space-6)) / 6);
  right: calc((100% - 2 * var(--space-6)) / 6);
  height: 1px;
  background: var(--color-border);
  z-index: 0;
}

.step {
  position: relative;
  z-index: 1;
  text-align: center;
}

.step-number {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  font-size: 0.78rem;
  font-weight: 700;
  color: var(--color-primary);
  margin-bottom: var(--space-3);
}

.step h3 {
  font-size: 1rem;
  margin-bottom: var(--space-1);
}

.step p {
  font-size: 0.87rem;
  color: var(--color-text-muted);
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
    max-width: none;
    font-size: 2.1rem;
  }

  .capabilities {
    grid-template-columns: repeat(2, 1fr);
  }

  .steps {
    grid-template-columns: 1fr;
    gap: var(--space-5);
  }

  .steps-line {
    display: none;
  }

  .privacy-band {
    flex-direction: column;
  }

  .privacy-list {
    grid-template-columns: 1fr;
  }
}
</style>
