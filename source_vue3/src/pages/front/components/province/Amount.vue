<script setup lang="ts">
import {reactive, watch} from "vue";

interface IProps {
    data: CommonModel.CountProvinceVo[];
}

const props = withDefaults(defineProps<IProps>(), {
    data: () => []
})

interface RankingBoard {
    data: CommonModel.CountProvinceVo[];
    waitTime?: number,
    rowNum?: number,
    unit: string;
}

const cityConfig = reactive<RankingBoard>({
    data: [],
    waitTime: 2000,
    rowNum: 7,
    unit: '个',
})

watch(() => props.data, (val) => {
    cityConfig.data = val
}, {immediate: true})

</script>

<template>
    <dv-scroll-ranking-board :config="cityConfig" style="width: 27.8rem; height: 35rem;"/>
</template>


<style lang="scss" scoped></style>