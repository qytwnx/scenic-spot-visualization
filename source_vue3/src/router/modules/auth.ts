import {RouteRecordRaw} from "vue-router";

export default {
    path: '/auth',
    redirect: '/auth/login',
    meta: {canAdmin: false, title: '登录'},
    children: [
        {
            path: 'login',
            name: 'Login',
            component: () => import('@/pages/auth/Login.vue'),
            meta: {canAdmin: false, title: '登录'},
        }
    ],
} as RouteRecordRaw