import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory('/'),
    routes: [
        {
            path: '/',
            name: 'about',
            component: () => import('../components/AboutView.vue')
        },
        {
            path: '/research',
            name: 'research',
            component: () => import('../components/ResearchView.vue')
        },
        {
            path: '/members',
            name: 'members',
            component: () => import('../components/TeamView.vue')
        },
        {
            path: '/publications',
            name: 'publications',
            component: () => import('../components/PublicationsView.vue')
        },
        {
            path: '/partners',
            name: 'partners',
            component: () => import('../components/PartnersView.vue')
        },
        {
            path: '/contact',
            name: 'contact',
            component: () => import('../components/ContactView.vue')
        }
    ]
})

export default router
