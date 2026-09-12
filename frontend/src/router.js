import { createRouter, createWebHistory } from 'vue-router'
import ScanPage from './pages/ScanPage.vue'
import DashboardPage from './pages/DashboardPage.vue'

const routes = [
  { path: '/', name: 'scan', component: ScanPage },
  { path: '/dashboard', name: 'dashboard', component: DashboardPage },
]

export const router = createRouter({
  history: createWebHistory(),
  routes,
})
