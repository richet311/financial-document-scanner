import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './pages/LandingPage.vue'
import ScanPage from './pages/ScanPage.vue'
import DashboardPage from './pages/DashboardPage.vue'
import ScanDetailPage from './pages/ScanDetailPage.vue'
import SamplesPage from './pages/SamplesPage.vue'
import PrivacyPage from './pages/PrivacyPage.vue'
import TermsPage from './pages/TermsPage.vue'
import LoginPage from './pages/LoginPage.vue'
import { authStore } from './store/auth'

const routes = [
  { path: '/', name: 'home', component: LandingPage },
  { path: '/scan', name: 'scan', component: ScanPage },
  { path: '/dashboard', name: 'dashboard', component: DashboardPage, meta: { requiresAuth: true } },
  {
    path: '/dashboard/scans/:id',
    name: 'scan-detail',
    component: ScanDetailPage,
    meta: { requiresAuth: true },
  },
  { path: '/samples', name: 'samples', component: SamplesPage },
  { path: '/privacy', name: 'privacy', component: PrivacyPage },
  { path: '/terms', name: 'terms', component: TermsPage },
  { path: '/login', name: 'login', component: LoginPage },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach(async (to) => {
  if (!to.meta.requiresAuth) return true

  // The initial Supabase session lookup is async; wait for it once so a
  // signed-in user isn't briefly bounced to /login on a hard page refresh.
  while (authStore.loading) {
    await new Promise((resolve) => setTimeout(resolve, 25))
  }

  if (!authStore.user) {
    return { path: '/login' }
  }
  return true
})
