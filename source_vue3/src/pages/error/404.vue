<script setup lang="ts">

import router from "@/router";
</script>

<template>
    <div class="w-full h-full flex flex-col items-center justify-center">
        <img src="@/assets/images/404.svg" class="w-96 h-96" alt="404">
        <el-button type="danger" @click="() => {router.back()}" text>返回上一页</el-button>
    </div>
</template>


<style lang="scss" scoped>

</style>