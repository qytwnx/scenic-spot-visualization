<script setup lang="ts">
import router from "@/router";
import useUserStore from "@/store/useUserStore";

const userStore = useUserStore()
</script>

<template>
    <div class="w-full h-full flex flex-col items-center justify-center">
        <img src="@/assets/images/403.svg" class="w-96 h-96" alt="403">
        <el-space>
            <el-button type="danger" @click="() => {router.go(-1)}" text>返回上一页</el-button>
        </el-space>
    </div>
</template>


<style lang="scss" scoped>

</style>