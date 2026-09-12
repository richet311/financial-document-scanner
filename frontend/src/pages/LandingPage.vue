<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const ICONS = {
  document:
    '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"><rect x="5" y="3" width="14" height="18" rx="2" /><line x1="8" y1="8" x2="16" y2="8" /><line x1="8" y1="12" x2="16" y2="12" /><line x1="8" y1="16" x2="13" y2="16" /></svg>',
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

const steps = [
  {
    icon: 'upload',
    title: 'Upload',
    text: 'Drop in a pay stub, bank statement, or budget sheet as a PDF, PNG, or JPEG.',
  },
  {
    icon: 'scan',
    title: 'Extract & classify',
    text: 'Text is pulled out and the document type is identified automatically.',
  },
  {
    icon: 'shield',
    title: 'Get insights',
    text: 'See budgeting insights instantly. The original file is never stored.',
  },
]

function goToScan() {
  router.push('/scan')
}
</script>

<template>
  <div class="landing">
    <section class="hero">
      <span class="hero-eyebrow">Document intelligence</span>
      <h1>Turn financial documents into clear, actionable insights</h1>
      <p class="hero-subtitle">
        Upload a pay stub, bank statement, or budget sheet and see extraction,
        classification, and budgeting analysis run end to end &mdash; without
        it ever touching a real bank account.
      </p>
      <button class="btn btn-primary hero-cta" @click="goToScan">Scan a document</button>

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

    <section class="steps-section">
      <h2 class="section-heading">How it works</h2>
      <div class="steps">
        <div v-for="(step, index) in steps" :key="step.title" class="step">
          <div class="step-number">{{ index + 1 }}</div>
          <span class="step-icon icon" v-html="ICONS[step.icon]"></span>
          <h3>{{ step.title }}</h3>
          <p>{{ step.text }}</p>
        </div>
      </div>
    </section>

    <section class="capabilities-section">
      <h2 class="section-heading">Capabilities</h2>
      <div class="capabilities">
        <div v-for="capability in capabilities" :key="capability.title" class="capability-card card">
          <span class="capability-icon icon" v-html="ICONS[capability.icon]"></span>
          <h3>{{ capability.title }}</h3>
          <p>{{ capability.text }}</p>
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div>
        <h2>Ready to see it in action?</h2>
        <p>Try it with a sample document &mdash; nothing is stored, no account required.</p>
      </div>
      <button class="btn btn-primary" @click="goToScan">Scan a document</button>
    </section>
  </div>
</template>

<style scoped>
.landing {
  display: flex;
  flex-direction: column;
  gap: var(--space-7);
}

.hero {
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-7) var(--space-6);
  box-shadow: var(--shadow-sm);
}

.hero-eyebrow {
  display: inline-block;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-accent);
  margin-bottom: var(--space-3);
}

.hero h1 {
  font-family: var(--font-serif);
  font-style: italic;
  font-weight: 500;
  font-size: 2.6rem;
  max-width: 20ch;
  margin-bottom: var(--space-4);
  color: var(--color-primary);
}

.hero-subtitle {
  color: var(--color-text-muted);
  max-width: 56ch;
  margin-bottom: var(--space-5);
}

.hero-cta {
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

.section-heading {
  font-size: 0.78rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--color-text-faint);
  margin-bottom: var(--space-4);
}

.steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--space-5);
}

.step {
  position: relative;
  padding: var(--space-5);
  background: var(--color-surface);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
}

.step-number {
  position: absolute;
  top: var(--space-4);
  right: var(--space-4);
  font-family: var(--font-serif);
  font-style: italic;
  font-size: 1.3rem;
  color: var(--color-border);
}

.step-icon {
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  background: var(--color-primary-soft);
  color: var(--color-primary);
  align-items: center;
  justify-content: center;
  margin-bottom: var(--space-3);
}

.step-icon :deep(svg) {
  width: 18px;
  height: 18px;
}

.step h3 {
  font-size: 0.98rem;
  margin-bottom: var(--space-2);
}

.step p {
  font-size: 0.85rem;
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
  background: var(--color-accent-soft);
  color: var(--color-accent);
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

.cta-banner {
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-lg);
  padding: var(--space-6);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-5);
  flex-wrap: wrap;
}

.cta-banner h2 {
  font-family: var(--font-serif);
  font-style: italic;
  font-weight: 500;
  font-size: 1.5rem;
  margin-bottom: var(--space-2);
}

.cta-banner p {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
}
</style>
