<script setup lang="ts">
import {Expand, Fold} from "@element-plus/icons-vue";
import useAppStore from "@/store/useAppStore";
import router from "@/router";
import useUserStore from "@/store/useUserStore";

const userStore = useUserStore()
const appStore = useAppStore()

const toCenter = () => {
    router.push({path: '/admin/center'})
}

const toPassword = () => {
    router.push({path: '/admin/password'})
}
</script>

<template>
    <div class="header-left">
        <img class="logo" src="@/assets/images/logo.svg" alt="" draggable="false">
        <div class="title" @click="() => { router.push({path: '/admin'}) }">景点分析大数据中心管理后台</div>
        <div class="menu-switch">
            <el-icon @click="appStore.setCollapsed(!appStore.getCollapsed)" v-if="appStore.getCollapsed">
                <Expand/>
            </el-icon>
            <el-icon @click="appStore.setCollapsed(!appStore.getCollapsed)" v-if="!appStore.getCollapsed">
                <Fold/>
            </el-icon>
        </div>
    </div>
    <div class="header-right" v-if="userStore.getUser() !== null">
        <el-dropdown>
            <div class="text-black flex items-center text-base">
                <img  v-if="userStore.getUser()" src="@/assets/images/logo.svg"
                           class="mr-2 w-6 h-6" alt=""/>
                {{ userStore.getUser()?.name }}
            </div>
            <template #dropdown>
                <el-dropdown-menu>
                    <el-dropdown-item @click="userStore.logout()" >退出登录</el-dropdown-item>
                </el-dropdown-menu>
            </template>
        </el-dropdown>
    </div>
</template>

<style lang="scss" scoped>
.header-left {
  @apply flex items-center;
  .logo {
    @apply w-9;
  }

  .title {
    @apply font-bold text-xl m-3 select-none cursor-pointer;
  }

  .menu-switch {
    @apply flex items-center text-xl cursor-pointer hover:text-blue-500
  }
}

.header-right {
  @apply cursor-pointer flex;
}

:focus {
  outline: 0;
}
</style>