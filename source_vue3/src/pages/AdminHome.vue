<script setup lang="ts">
import AdminHeader from "@/components/layout/AdminHeader.vue";
import AdminAside from "@/components/layout/AdminAside.vue";
import useAppStore from "@/store/useAppStore";
import router from "@/router";
import {Switch} from "@element-plus/icons-vue";
import useUser from "@/composables/useUser";
import store from "@/store/store";
import useUserStore from "@/store/useUserStore";
import {useRoute} from "vue-router";

const appStore = useAppStore()

const route = useRoute()
const userStore = useUserStore(store)
const {userCurrent} = useUser()


console.log(123)

const loadCurrentUser = async () => {
    const res = await userCurrent()
    if (res?.code === 200) {
        userStore.setUser(res.data)
    } else {
        userStore.remove()
    }
}
if (route.name !== 'Login')
    loadCurrentUser()
</script>

<template>
    <div class="admin-header">
        <AdminHeader/>
    </div>
    <div class="admin-main">
        <div class="admin-main-aside">
            <AdminAside/>
            <div class="px-3 py-6 flex items-center">
                <el-button type="primary" v-if="appStore.getCollapsed" :icon="Switch" circle
                           @click="() => {router.push({name: 'FrontIndex'})}"/>
                <el-button type="primary" v-else plain round class="w-full"
                           @click="() => {router.push({name: 'FrontIndex'})}">返回前台
                </el-button>
            </div>
        </div>
        <div class="admin-main-right">
            <RouterView/>
        </div>
    </div>
</template>


<style lang="scss" scoped>
.admin-header {
    @apply h-14 bg-white border-gray-300 border-b-2 flex items-center px-6 justify-between;
}

.admin-main {
    height: calc(100% - 56px);
    overflow: auto;
    @apply flex;
    .admin-main-aside {
        @apply w-auto h-full border-r-2 bg-white overflow-y-auto overflow-x-hidden flex flex-col justify-between;
    }

    .admin-main-right {
        @apply flex-1 overflow-auto p-3;
    }
}
</style>