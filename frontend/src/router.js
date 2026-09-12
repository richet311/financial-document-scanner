import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './pages/LandingPage.vue'
import ScanPage from './pages/ScanPage.vue'
import DashboardPage from './pages/DashboardPage.vue'

const routes = [
  { path: '/', name: 'home', component: LandingPage },
  { path: '/scan', name: 'scan', component: ScanPage },
  { path: '/dashboard', name: 'dashboard', component: DashboardPage },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
