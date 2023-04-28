<script setup lang="ts">
import {onBeforeMount, onMounted, reactive, ref} from "vue";
import useScenicSpots from "@/composables/useScenicSpots";

const {scenicSpotsIndexHeatTop50} = useScenicSpots()

const isNull = ref<boolean>(false)

interface RankingBoard {
    data: CommonModel.CountVo[];
    waitTime?: number,
    rowNum?: number,
    unit?: string;
    colors?: string[];
    showValue: boolean;
}

const timer = ref<number | NodeJS.Timer | null>(null)
const currentIndex = ref<number>(0)
const allData = ref<CommonModel.CountVo[]>([])

const provinceConfig = reactive<RankingBoard>({
    data: [],
    waitTime: 3000,
    rowNum: 10,
    unit: '%',
    colors: ['#e062ae', '#fb7293', '#e690d1', '#32c5e9', '#96bfff'],
    showValue: true
})

onBeforeMount(() => {
    clear()
})

onMounted(() => {
    scenicSpotsIndexHeatTop50().then(res => {
        if (res.code === 200) {
            allData.value = res.data
        } else {
            isNull.value = true
        }
    })
    allData.value = allData.value.sort(({value: a}, {value: b}) => {
        if (a > b)
            return -1
        else if (a < b)
            return 1
        else
            return 0
    })
    transformData()
})
const clear = () => {
    if (timer.value) {
        clearInterval(timer.value)
        timer.value = null
    }
};

const polling = () => {
    if (timer.value) {
        return
    }
    let looper = (a: any) => {
        transformData()
    };
    timer.value = setInterval(looper, provinceConfig.waitTime);
};
const transformData = () => {
    if (currentIndex.value >= allData.value.length) {
        currentIndex.value = 0;
    }
    provinceConfig.data = allData.value.slice(currentIndex.value, currentIndex.value + provinceConfig.rowNum!)
    currentIndex.value += provinceConfig.rowNum!
    polling()
}
</script>

<template>
    <dv-capsule-chart v-if="!isNull" :config="provinceConfig" style="width: 27.8rem; height: 33.5rem;"/>
    <div v-else>暂无数据</div>

</template>


<style lang="scss" scoped></style>