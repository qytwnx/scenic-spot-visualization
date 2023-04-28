<script setup lang="ts">
import {onMounted, ref} from "vue";
import {Vue3SeamlessScroll} from "vue3-seamless-scroll";
import useScenicSpots from "@/composables/useScenicSpots";

const {scenicSpotsIndexRecommend} = useScenicSpots()

const list = ref<ScenicSpotsModel.ScenicSpotsVo[]>([]);

onMounted(() => {
    scenicSpotsIndexRecommend().then(res => {
        if (res?.code === 200) {
            list.value = res.data
        }
    })
})

</script>

<template>
    <vue3-seamless-scroll :hover="true" :limitScrollNum="2" :singleHeight="140" :list="list" class="scroll">
        <div class="item" v-for="item in list" :key="item.id">
            <div style="display: flex;justify-content: space-between;flex-wrap: wrap; margin: 0.1rem 0">
                <div class="text-[#3ba272] text-lg">景点名称：<span>{{ item.name }}</span></div>
                <div style="color: #ee6666">等级：<span>{{ item.level }}</span></div>
            </div>
            <div style="display: flex;justify-content: space-between;flex-wrap: wrap; color: #fac858; margin: 0.1rem 0">
                <div>价格：<span>{{ item.price }}</span></div>
                <div>月销：<span>{{ item.sales }}</span></div>
                <div>热度：<span>{{ item.sales }}</span></div>
            </div>
            <div style="margin: 0.1rem 0">景点介绍：<span>{{ item.introduction }}</span></div>
            <div style="margin: 0.1rem 0">地址：<span>{{ item.address }}</span></div>
        </div>
    </vue3-seamless-scroll>
</template>


<style lang="scss" scoped>
.scroll {
  width: 27.8rem;
  height: 18.5rem;
  overflow: hidden;
}

.scroll .item {
  height: 9rem;
  padding: 3px 0;
  border-bottom: 0.15rem #04b0c5 dashed;
  overflow: hidden;
}

</style>