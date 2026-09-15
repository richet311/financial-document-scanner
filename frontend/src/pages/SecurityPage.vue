<script setup>
const measures = [
  {
    title: 'Signature-based file validation',
    text: 'Uploads are checked against their real file signature (magic bytes), not just the extension, and read in bounded 64KB chunks so an oversized file is rejected before it is fully read into memory.',
  },
  {
    title: 'Rate limiting on every route',
    text: 'Every API route is rate-limited by client IP with slowapi, including a tighter limit on the login endpoint to slow down credential guessing.',
  },
  {
    title: 'JWT-protected routes',
    text: 'The analysis-history endpoint requires a bearer token issued by a rate-limited login endpoint. Credentials are compared with a constant-time check to avoid timing side-channels.',
  },
  {
    title: 'No file persistence',
    text: 'The original uploaded file is never written to disk. Only derived insights (classification, extracted fields, insight text) are kept, in memory, for the current server session, and are cleared on restart.',
  },
  {
    title: 'Locked-down CORS',
    text: 'Cross-origin requests are restricted to an explicit allow list of frontend origins rather than left open.',
  },
  {
    title: 'Security response headers',
    text: 'Every response carries X-Content-Type-Options, X-Frame-Options, and Referrer-Policy headers to reduce MIME sniffing, clickjacking, and referrer leakage.',
  },
]

const limitations = [
  'The demo login is a single hardcoded credential pair, not a real user system, so analysis history is a single shared list rather than scoped per account.',
  'The in-memory history store is not persistent; it resets whenever the backend restarts.',
  'This is a portfolio demo, not an audited production system. Treat it as a reference for the patterns, not a drop-in compliance solution.',
]
</script>

<template>
  <div class="security-page">
    <header class="page-header">
      <h1>Security &amp; privacy</h1>
      <p class="page-subtitle">
        This project treats security as a first-class feature. Here is
        everything the backend does to protect data in transit, in memory,
        and at the API boundary.
      </p>
    </header>

    <div class="measures">
      <div v-for="measure in measures" :key="measure.title" class="measure-card">
        <h2>{{ measure.title }}</h2>
        <p>{{ measure.text }}</p>
      </div>
    </div>

    <section class="limitations">
      <span class="accent-bar"></span>
      <h2>Known limitations</h2>
      <ul>
        <li v-for="item in limitations" :key="item">{{ item }}</li>
      </ul>
    </section>
  </div>
</template>

<style scoped>
.measures {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: var(--space-4);
  margin-bottom: var(--space-7);
}

.measure-card h2 {
  font-size: 1rem;
  color: var(--color-accent);
  margin-bottom: var(--space-2);
}

.measure-card p {
  font-size: 0.88rem;
  color: var(--color-text-muted);
}

.limitations {
  background: var(--color-surface-muted);
  border-radius: var(--radius-md);
  padding: var(--space-6);
}

.limitations h2 {
  font-size: 1.15rem;
  margin-bottom: var(--space-3);
}

.limitations ul {
  margin: 0;
  padding-left: 1.1rem;
  color: var(--color-text-muted);
  font-size: 0.9rem;
  display: flex;
  flex-direction: column;
  gap: var(--space-2);
}
</style>
