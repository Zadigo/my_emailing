import { scrollToTop, loadView, loadLayout } from '@/composables/utils'
import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
    history: createWebHistory(),
    scrollBehavior: scrollToTop,
    routes: [
        {
            path: '/',
            redirect: '/app'
        },
        {
            path: '/app',
            component: loadLayout('DashboardLayout'),
            children: [
                {
                    path: '',
                    name: 'home_view',
                    component: loadView('CampaignsView')
                },
                {
                    path: ':id',
                    component: loadLayout('CampainWrapper'),
                    children: [
                        {
                            path: '',
                            name: 'campaign_view',
                            component: loadView('campaign/CampaignView')
                        },
                        {
                            path: ':seq/email',
                            name: 'email_view',
                            component: loadView('campaign/EmailView')
                        },
                        {
                            path: 'new',
                            name: 'new_campaign_view',
                            component: loadView('campaign/NewCampaignView')
                        },
                        {
                            path: 'leads',
                            name: 'leads_view',
                            component: loadView('campaign/LeadsView')
                        },
                        {
                            path: 'review',
                            name: 'review_view',
                            component: loadView('campaign/ReviewView')
                        }
                    ]
                },
            ]
        }
    ]
})

export default router
