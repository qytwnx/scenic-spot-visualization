import {NavigationGuardNext, RouteLocationNormalized, Router} from 'vue-router'
import pinia from "@/store/store";
import useAppStore from "@/store/useAppStore";
import useUserStore from "@/store/useUserStore";

const appStore = useAppStore(pinia)
const userStore = useUserStore(pinia)

export default (router: Router) => {
    router.beforeEach(beforeEach)
}

function beforeEach(to: RouteLocationNormalized, from: RouteLocationNormalized, next: NavigationGuardNext) {
    appStore.setCurrentPath(to.path)
    if (to.meta.title) {
        document.title = to.meta.title as string + ' | ' + '景点分析大数据中心'
    }
    console.log(11)
    if (to.meta.canAdmin && !userStore.getUser() && !userStore.getToken()) {
        next('/auth/login')
    } else {
        next()
    }
}