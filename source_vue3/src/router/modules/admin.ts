import {RouteRecordRaw} from "vue-router";

export default {
    path: '/admin',
    component: () => import('@/pages/AdminHome.vue'),
    meta: {canAdmin: true, title: '景点分析大数据中心管理后台'},
    redirect: '/admin/scenic-spot',
    children: [
        {
            path: 'users',
            name: 'AdminUsers',
            component: () => import('@/pages/admin/Users.vue'),
            meta: {canAdmin: true, title: '用户管理'},
        },
        {
            path: 'files',
            name: 'AdminFiles',
            component: () => import('@/pages/admin/Files.vue'),
            meta: {canAdmin: true, title: '文件管理'},
        },
        {
            path: 'logs',
            name: 'AdminLogs',
            component: () => import('@/pages/admin/Logs.vue'),
            meta: {canAdmin: true, title: '操作日志'},
        },
        {
            path: 'scenic-spot',
            name: 'ScenicSpot',
            component: () => import('@/pages/admin/ScenicSpot.vue'),
            meta: {canAdmin: true, title: '景点管理'},
        },
    ],
} as RouteRecordRaw