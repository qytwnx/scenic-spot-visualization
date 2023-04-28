<script setup lang="ts">
import {reactive, onMounted} from "vue";
import dayjs from "dayjs";
import 'dayjs/locale/zh-cn.js'
import {Timer} from "@element-plus/icons-vue";
import router from "@/router";

dayjs.locale('zh-cn')

const timeInfo = reactive<{ setInterval: number | NodeJS.Timer, nowDate: string }>({
    setInterval: 0,
    nowDate: ''
})
const handleTime = () => {
    timeInfo.setInterval = setInterval(() => {
        const date = new Date()
        timeInfo.nowDate = dayjs(date).format('YYYY-MM-DD dddd HH: mm: ss')
    }, 1000)
}

onMounted(() => {
    handleTime()
})
</script>

<template>
    <section class="header-container">
        <header v-if="timeInfo.nowDate" style="position: absolute; z-index: 9999; left: 2.5rem; top: 2.5rem; color:#1dc1f5; font-size: 1.3rem; display: flex; align-items: center">
            <el-icon class="mr-1">
                <Timer/>
            </el-icon>
            {{ timeInfo.nowDate }}
        </header>
        <header style="position: absolute; z-index: 9999; right: 2.5rem; top: 2.3rem; color:#fff; font-size: 1.3rem; cursor: pointer">
            <dv-decoration11 style="width:9rem;height:3rem;" @click="() => {router.push({name: 'ScenicSpot'})}">
                <div class="mx-2 text-[#1dc1f5] font-serif mt-0.5">
                    后台管理
                </div>
            </dv-decoration11>
        </header>
        <section class="text-[3.4rem] font-bold text-white animate-pulse tracking-[2rem] flex items-center"
                 style="-webkit-text-stroke:0.15rem #00e3ff; -webkit-text-fill-color: transparent;">景点分析大数据中心
        </section>
    </section>
</template>


<style lang="scss" scoped>
.header-container {
  display: flex;
  width: 100%;
  margin-top: 0.5rem;
  background-image: url(@/assets/images/header-bg.svg);
  background-size: cover;
  background-position: center center;
}
</style>