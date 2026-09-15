import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './pages/LandingPage.vue'
import ScanPage from './pages/ScanPage.vue'
import DashboardPage from './pages/DashboardPage.vue'
import SamplesPage from './pages/SamplesPage.vue'
import SecurityPage from './pages/SecurityPage.vue'
import AboutPage from './pages/AboutPage.vue'

const routes = [
  { path: '/', name: 'home', component: LandingPage },
  { path: '/scan', name: 'scan', component: ScanPage },
  { path: '/dashboard', name: 'dashboard', component: DashboardPage },
  { path: '/samples', name: 'samples', component: SamplesPage },
  { path: '/security', name: 'security', component: SecurityPage },
  { path: '/about', name: 'about', component: AboutPage },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
