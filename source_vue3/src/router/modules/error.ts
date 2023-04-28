import {RouteRecordRaw} from "vue-router";

export default {
    path: '/error',
    redirect: '/error/404',
    meta: {canAdmin: false, title: 'error'},
    children: [
        {
            path: '404',
            name: '404',
            component: () => import('@/pages/error/404.vue'),
            meta: {canAdmin: false, title: '未找到资源'},
        },
        {
            path: '403',
            name: '403',
            component: () => import('@/pages/error/403.vue'),
            meta: {canAdmin: false, title: '暂无访问权限'},
        },
        {
            path: '/:any(.*)',
            name: '404',
            component: () => import('@/pages/error/404.vue'),
        },
    ],
} as RouteRecordRaw