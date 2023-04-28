<script setup lang="ts">
import {onMounted, ref} from "vue";
import {Vue3SeamlessScroll} from "vue3-seamless-scroll";
import useScenicSpots from "@/composables/useScenicSpots";

const {scenicSpotsIndexInfo} = useScenicSpots()

const list = ref<CommonModel.CountVo[]>([]);

onMounted(() => {
    scenicSpotsIndexInfo().then(res => {
        if (res?.code === 200) {
            list.value = res.data
        }
    })
})

</script>

<template>
    <vue3-seamless-scroll :hover="true" :limitScrollNum="2"  :list="list" class="scroll">
        <div class="item" v-for="(item, index) in list" :key="index">
            <div>
                <div class="text-[#3ba272] text-lg">{{ item.name }}</div>
                <div style="color: #ee6666">{{ item.value }}</div>
            </div>
        </div>
    </vue3-seamless-scroll>
</template>


<style lang="scss" scoped>
.scroll {
  width: 27rem;
  height: 10rem;
  overflow: hidden;
}

.scroll .item {
  //height: 9rem;
  padding: 3px 0;
  border-bottom: 0.15rem #04b0c5 dashed;
  overflow: hidden;
}

</style>