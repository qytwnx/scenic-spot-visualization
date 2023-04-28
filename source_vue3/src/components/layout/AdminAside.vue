<script setup lang="ts">
import useAppStore from "@/store/useAppStore";
import router from "@/router";
import {
    User,
    Files,
    List,
    Guide,
} from '@element-plus/icons-vue'
import {ref, watch} from "vue";

const appStore = useAppStore()
const defaultActive = ref<string>(String(router.currentRoute.value?.name) || '')

watch(() => router.currentRoute.value.name, (val) => {
    defaultActive.value = String(val) || ''
}, {immediate: true})

const handleSelect = (key: string) => {
    router.push({name: key})
}
</script>

<template>
    <div>
        <el-menu
                :default-active="defaultActive"
                class="el-menu-vertical-custom"
                :collapse="appStore.getCollapsed"
                :collapse-transition="false"
                @select="handleSelect"
        >
            <el-menu-item index="AdminUsers">
                <el-icon>
                    <User/>
                </el-icon>
                <template #title>用户管理</template>
            </el-menu-item>
            <el-menu-item index="AdminFiles">
                <el-icon>
                    <Files/>
                </el-icon>
                <template #title>文件管理</template>
            </el-menu-item>
            <el-menu-item index="AdminLogs">
                <el-icon>
                    <List/>
                </el-icon>
                <template #title>操作日志</template>
            </el-menu-item>

            <el-menu-item index="ScenicSpot">
                <el-icon>
                    <Guide />
                </el-icon>
                <template #title>景点管理</template>
            </el-menu-item>
        </el-menu>
    </div>
</template>

<style lang="scss" scoped>
:deep(.el-menu) {
  border-right: none;
}

.el-menu-vertical-custom:not(.el-menu--collapse) {
  width: 192px;
}
</style>