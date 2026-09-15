<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

function goToSecurity() {
  router.push('/security')
}

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

const securityPoints = [
  'Every upload is checked by size and real file signature, not just its extension.',
  'Rate limiting on every API route, keyed by client IP.',
  'The original file is never stored; only derived insights are kept, in memory.',
]

function goToScan() {
  router.push('/scan')
}
</script>

<template>
  <div class="landing">
    <section class="hero">
      <div class="hero-content">
        <h1>Turn financial documents into clear, actionable insights</h1>
        <p class="hero-subtitle">
          Upload a pay stub, bank statement, or budget sheet and see extraction,
          classification, and budgeting analysis run end to end, without
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
      </div>
      <div class="hero-visual">
        <svg class="hero-illustration" viewBox="0 0 220 190" fill="none">
          <rect x="30" y="24" width="108" height="138" rx="8" transform="rotate(-8 30 24)" fill="rgba(255,255,255,0.04)" stroke="rgba(255,255,255,0.22)" stroke-width="1.5" />
          <rect x="46" y="18" width="108" height="138" rx="8" transform="rotate(-2 46 18)" fill="rgba(255,255,255,0.07)" stroke="rgba(255,255,255,0.32)" stroke-width="1.5" />
          <rect x="58" y="16" width="108" height="138" rx="8" fill="rgba(255,255,255,0.1)" stroke="rgba(255,255,255,0.5)" stroke-width="1.5" />
          <line x1="74" y1="44" x2="148" y2="44" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-linecap="round" />
          <line x1="74" y1="60" x2="148" y2="60" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-linecap="round" />
          <line x1="74" y1="76" x2="120" y2="76" stroke="rgba(255,255,255,0.45)" stroke-width="2" stroke-linecap="round" />
          <rect x="58" y="96" width="108" height="10" rx="5" fill="var(--color-accent)" />
          <rect x="182" y="118" width="10" height="32" rx="3" fill="var(--color-accent)" opacity="0.85" />
          <rect x="198" y="98" width="10" height="52" rx="3" fill="var(--color-accent)" opacity="0.55" />
          <rect x="166" y="134" width="10" height="16" rx="3" fill="var(--color-accent)" opacity="0.55" />
        </svg>
        <span class="hero-visual-caption">Document intelligence pipeline</span>
      </div>
    </section>

    <section class="capabilities-section">
      <h2 class="section-heading">Capabilities of this scanner for finance</h2>
      <p class="section-subtitle">
        A small, self-contained pipeline that goes from a raw document to a
        classified type and plain-language budgeting insight.
      </p>
      <div class="capabilities">
        <div v-for="capability in capabilities" :key="capability.title" class="capability-card">
          <span class="capability-icon icon" v-html="ICONS[capability.icon]"></span>
          <h3>{{ capability.title }}</h3>
          <p>{{ capability.text }}</p>
        </div>
      </div>
    </section>

    <section class="spotlight">
      <div class="spotlight-visual">
        <svg class="spotlight-illustration" viewBox="0 0 200 190" fill="none">
          <circle cx="100" cy="96" r="82" stroke="var(--color-border)" stroke-width="1.5" stroke-dasharray="3 7" />
          <circle cx="38" cy="56" r="5" fill="var(--color-accent)" opacity="0.3" />
          <circle cx="164" cy="66" r="4" fill="var(--color-accent)" opacity="0.5" />
          <circle cx="150" cy="144" r="6" fill="var(--color-accent)" opacity="0.28" />
          <path
            d="M100 30 L150 48 V92 C150 128 128 152 100 164 C72 152 50 128 50 92 V48 Z"
            fill="var(--color-accent-soft)"
            stroke="var(--color-accent)"
            stroke-width="2.5"
            stroke-linejoin="round"
          />
          <path d="M78 96 L94 112 L124 78" stroke="var(--color-accent)" stroke-width="6" stroke-linecap="round" stroke-linejoin="round" />
        </svg>
      </div>
      <div class="spotlight-content">
        <span class="accent-bar"></span>
        <h2>Built with privacy and security in mind</h2>
        <p class="spotlight-intro">
          This is a portfolio project, so it treats security as a first-class
          feature rather than an afterthought.
        </p>
        <ul class="spotlight-list">
          <li v-for="point in securityPoints" :key="point">{{ point }}</li>
        </ul>
        <button class="btn btn-secondary spotlight-link" @click="goToSecurity">
          See the full security approach
        </button>
      </div>
    </section>

    <section class="steps-section">
      <h2 class="section-heading">How it works</h2>
      <div class="steps">
        <div v-for="(step, index) in steps" :key="step.title" class="step">
          <div class="step-number">{{ String(index + 1).padStart(2, '0') }}</div>
          <span class="step-icon icon" v-html="ICONS[step.icon]"></span>
          <h3>{{ step.title }}</h3>
          <p>{{ step.text }}</p>
        </div>
      </div>
    </section>

    <section class="cta-banner">
      <div>
        <h2>Ready to see it in action?</h2>
        <p>Try it with a sample document. Nothing is stored, no account required.</p>
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
  display: flex;
  align-items: center;
  gap: var(--space-7);
}

.hero-content {
  flex: 1 1 56%;
  padding: var(--space-4) 0;
}

.hero h1 {
  font-size: 2.3rem;
  max-width: 18ch;
  margin-bottom: var(--space-4);
  color: var(--color-text);
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
  font-weight: 700;
  font-size: 1rem;
}

.hero-stat-label {
  font-size: 0.78rem;
  color: var(--color-text-muted);
}

.hero-visual {
  position: relative;
  flex: 1 1 44%;
  background: linear-gradient(150deg, #262626 0%, #141414 100%);
  border-radius: var(--radius-lg);
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 280px;
}

.hero-visual::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: var(--color-accent);
}

.hero-illustration {
  width: 220px;
  height: 190px;
}

.hero-visual-caption {
  position: absolute;
  left: var(--space-5);
  bottom: var(--space-5);
  font-size: 0.75rem;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: rgba(255, 255, 255, 0.55);
}

.section-heading {
  font-size: 1.5rem;
  color: var(--color-text);
  margin-bottom: var(--space-2);
}

.section-subtitle {
  color: var(--color-text-muted);
  max-width: 64ch;
  margin-bottom: var(--space-5);
}

.capabilities {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: var(--space-4);
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
  font-size: 1.02rem;
  color: var(--color-accent);
  margin-bottom: var(--space-2);
}

.capability-card p {
  font-size: 0.88rem;
  color: var(--color-text-muted);
}

.spotlight {
  display: flex;
  align-items: center;
  gap: var(--space-7);
}

.spotlight-visual {
  flex: 1 1 34%;
  background: var(--color-surface-muted);
  border-radius: var(--radius-lg);
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 220px;
}

.spotlight-illustration {
  width: 170px;
  height: 162px;
}

.spotlight-content {
  flex: 1 1 66%;
}

.spotlight-content h2 {
  font-size: 1.4rem;
  margin-bottom: var(--space-3);
}

.spotlight-intro {
  color: var(--color-text-muted);
  margin-bottom: var(--space-4);
  max-width: 60ch;
}

.spotlight-list {
  margin: 0 0 var(--space-4);
  padding-left: 1.1rem;
  color: var(--color-text-muted);
  font-size: 0.9rem;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}

.spotlight-link {
  align-self: flex-start;
}

.steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: var(--space-5);
}


.step-number {
  font-weight: 700;
  font-size: 0.78rem;
  letter-spacing: 0.08em;
  color: var(--color-text-faint);
  margin-bottom: var(--space-2);
}

.step-icon {
  width: 34px;
  height: 34px;
  border-radius: var(--radius-sm);
  background: var(--color-accent-soft);
  color: var(--color-accent);
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
  color: var(--color-accent);
  margin-bottom: var(--space-2);
}

.step p {
  font-size: 0.85rem;
  color: var(--color-text-muted);
}

.cta-banner {
  background: var(--color-primary);
  color: white;
  border-radius: var(--radius-md);
  padding: var(--space-6);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: var(--space-5);
  flex-wrap: wrap;
}

.cta-banner h2 {
  font-size: 1.4rem;
  margin-bottom: var(--space-2);
}

.cta-banner p {
  color: rgba(255, 255, 255, 0.75);
  font-size: 0.9rem;
}


@media (max-width: 760px) {
  .hero {
    flex-direction: column;
  }

  .hero-visual {
    min-height: 160px;
  }

  .capabilities {
    grid-template-columns: 1fr;
  }

  .spotlight {
    flex-direction: column;
  }
}
</style>
