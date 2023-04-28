import { createRouter, createWebHashHistory } from 'vue-router'
import routes from '@/router/modules/index'
import guard from './guard'

const router = createRouter({
    history: createWebHashHistory(),
    routes,
})

guard(router)

export default router