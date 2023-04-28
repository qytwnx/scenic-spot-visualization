import {RouteRecordRaw} from "vue-router";


export default {
    path: '/',
    component: () => import('@/pages/FrontHome.vue'),
    redirect: '/index',
    meta: {canAdmin: false, title: '景点分析大数据中心'},
    children: [
        {
            path: 'index',
            name: 'FrontIndex',
            component: () => import('@/pages/front/Index.vue'),
            meta: {canAdmin: false, title: '首页'},
        },
        {
            path: 'province/:tag',
            name: 'FrontProvince',
            component: () => import('@/pages/front/Province.vue'),
            meta: {canAdmin: false, title: '省'},
        }
    ],
} as RouteRecordRaw