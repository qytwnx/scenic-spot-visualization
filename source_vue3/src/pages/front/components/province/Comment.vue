<script setup lang="ts">
import {onMounted, ref} from "vue";
import {Vue3SeamlessScroll} from "vue3-seamless-scroll";
import useScenicSpots from "@/composables/useScenicSpots";
import {useRoute} from "vue-router";

const {scenicSpotsProvinceComment} = useScenicSpots()
const route = useRoute()

const provinces = ref<CommonModel.IProvince[]>([
    {name: "北京市", tag: 'beijing'},
    {name: "天津市", tag: 'tianjin'},
    {name: "河北省", tag: 'hebei'},
    {name: "山西省", tag: 'shanxi'},
    {name: "内蒙古自治区", tag: 'neimenggu'},
    {name: "辽宁省", tag: 'liaoning'},
    {name: "吉林省", tag: 'jilin'},
    {name: "黑龙江省", tag: 'heilongjiang'},
    {name: "上海市", tag: 'shanghai'},
    {name: "江苏省", tag: 'jiangsu'},
    {name: "浙江省", tag: 'zhejiang'},
    {name: "安徽省", tag: 'anhui'},
    {name: "福建省", tag: 'fujian'},
    {name: "江西省", tag: 'jiangxi'},
    {name: "山东省", tag: 'shandong'},
    {name: "河南省", tag: 'henan'},
    {name: "湖北省", tag: 'hubei'},
    {name: "湖南省", tag: 'hunan'},
    {name: "广东省", tag: 'guangdong'},
    {name: "广西壮族自治区", tag: 'guangxi'},
    {name: "海南省", tag: 'hainan'},
    {name: "重庆市", tag: 'chongqing'},
    {name: "四川省", tag: 'sichuan'},
    {name: "贵州省", tag: 'guizhou'},
    {name: "云南省", tag: 'yunnan'},
    {name: "西藏自治区", tag: 'xizang'},
    {name: "陕西省", tag: 'shaanxi'},
    {name: "甘肃省", tag: 'gansu'},
    {name: "青海省", tag: 'qinghai'},
    {name: "宁夏回族自治区", tag: 'ningxia'},
    {name: "新疆维吾尔自治区", tag: 'xinjiang'},
    {name: "台湾省", tag: 'taiwan'},
    {name: "香港特别行政区", tag: 'hongkong'},
    {name: "澳门特别行政区", tag: 'macao'}
]);

const list = ref<CommonModel.CountVo[]>([]);

onMounted(() => {
    scenicSpotsProvinceComment(provinces.value.find((province: {
        name: string;
        tag: string
    }) => province.tag === route.params.tag as string)!.name).then(res => {
        if (res?.code === 200) {
            list.value = res.data
        }
    })
})

</script>

<template>
    <vue3-seamless-scroll :hover="true" :limitScrollNum="2" :list="list" class="scroll">
        <div class="item" v-for="(item, index) in list" :key="index">
            <div>
                <div class="text-[#3ba272] text-lg">{{ item.name }}</div>
                <div style="color: #00dcff">{{ item.value }}</div>
            </div>
        </div>
    </vue3-seamless-scroll>
</template>

<style lang="scss" scoped>
.scroll {
  width: 28.8rem;
  height: 14rem;
  overflow: hidden;
}

.scroll .item {
  //height: 9rem;
  padding: 3px 0;
  border-bottom: 0.15rem #04b0c5 dashed;
  overflow: hidden;
}

</style>