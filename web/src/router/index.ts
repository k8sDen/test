import {createRouter, createWebHistory} from 'vue-router'

const router = createRouter({
    history: createWebHistory(import.meta.env.BASE_URL),
    routes: [
        {
            path: '/',
            name: 'home',
            component: () => import('@/views/Main.vue')
        },
        {
            path: '/report/:id',
            name: 'report',
            component: () => import('@/views/Report.vue')
        },
    ]
})

export default router
