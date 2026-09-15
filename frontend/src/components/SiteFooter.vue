<script setup>
const year = new Date().getFullYear()
</script>

<template>
  <footer class="site-footer">
    <div class="footer-inner">
      <div class="footer-brand">
        <span class="footer-wordmark">Financial Document Scanner</span>
        <p class="footer-disclaimer">
          Independent portfolio project, not affiliated with any bank or
          financial institution. All sample documents are synthetic.
        </p>
      </div>

      <nav class="footer-links">
        <RouterLink to="/privacy">Privacy</RouterLink>
        <RouterLink to="/terms">Terms</RouterLink>
        <a href="https://github.com/richet311/financial-document-scanner" target="_blank" rel="noopener">
          GitHub
        </a>
      </nav>
    </div>
    <div class="footer-bottom">© {{ year }} Financial Document Scanner</div>
  </footer>
</template>

<style scoped>
.site-footer {
  border-top: 1px solid var(--color-border);
  margin-top: var(--space-7);
}

.footer-inner {
  max-width: var(--container-max);
  margin: 0 auto;
  padding: var(--space-6);
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: var(--space-6);
  flex-wrap: wrap;
}

.footer-wordmark {
  font-weight: 600;
  font-size: 0.95rem;
}

.footer-disclaimer {
  color: var(--color-text-faint);
  font-size: 0.8rem;
  max-width: 48ch;
  margin-top: var(--space-2);
}

.footer-links {
  display: flex;
  gap: var(--space-5);
  font-size: 0.85rem;
}

.footer-links a {
  color: var(--color-text-muted);
  text-decoration: none;
}

.footer-links a:hover {
  color: var(--color-text);
}

.footer-bottom {
  max-width: var(--container-max);
  margin: 0 auto;
  padding: 0 var(--space-6) var(--space-6);
  font-size: 0.76rem;
  color: var(--color-text-faint);
}

@media (max-width: 640px) {
  .footer-inner {
    padding: var(--space-5) var(--space-4);
  }

  .footer-bottom {
    padding: 0 var(--space-4) var(--space-5);
  }
}
</style>
