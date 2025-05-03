import { createRouter, createWebHistory } from 'vue-router'
import FormCurrentHand from '@/views/FormCurrentHand.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('@/views/FormCurrentHand.vue'),
    },
    {
      path: '/dashboard',
      name: 'dashboard',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('@/components/HelloWorld.vue'),
    },
  ],
})

export default router
