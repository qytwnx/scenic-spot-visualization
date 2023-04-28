<script setup lang="ts">
import {useRoute} from "vue-router";
import {onMounted, ref} from "vue";
import map from '@/assets/map/map.json';
import * as echarts from 'echarts';
import router from "@/router";
import {ChatDotRound} from "@element-plus/icons-vue";
import Amount from "@/pages/front/components/province/Amount.vue";
import Level from "@/pages/front/components/province/Level.vue";
import Comment from "@/pages/front/components/province/Comment.vue";
import Sales from "@/pages/front/components/province/Sales.vue";
import useScenicSpots from "@/composables/useScenicSpots";

const {scenicSpotsProvinceCountRanking} = useScenicSpots()

const route = useRoute()
if (route.params.tag === '') {
    router.back()
}

const source = JSON.stringify(map)
const target = JSON.parse(source)
var mapChart: echarts.ECharts;

const provinceTag = ref<string>(route.params.tag as string)
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
const mapChartOption = (params: CommonModel.CountVo[]) => mapChart.setOption({
    grid: {
        top: "0px",
        left: "0px",
        right: "0px",
        bottom: "0px"
    },
    tooltip: {
        show: true,
        trigger: "item",
        alwaysShowContent: false,
        backgroundColor: "rgba(255,255,255,0.81)",
        borderWidth: 0,
        borderColor: "rgba(0, 0, 0, 0.16);",
        hideDelay: 100,
        triggerOn: "mousemove",
        textStyle: {
            color: "#000",
            fontSize: "12",
            width: 20,
            height: 30,
        },
        extraCssText: 'box-shadow:0 0 3px rgba(0,0,0,0.3);',
        showDelay: 100,
        formatter: (params: { data: { name?: string, value?: number, example?: ScenicSpotsModel.ScenicSpotsVo } }) => {
            return params.data.example === null ? `<div style="width: 15rem; height: 2rem; padding: 0.5rem; overflow: hidden; color: #1370fb">
        <div style="display: flex; justify-content: space-between;margin-bottom: 0.5rem;">
            <span>${params?.data?.name}</span>
            <span>${params?.data?.value} 个</span>
        </div>
    </div>` : `<div style="width: 15rem; height: 18rem; padding: 0.5rem; overflow: hidden; color: #1370fb">
        <div style="display: flex; justify-content: space-between; border-bottom: 1px #ccc solid; margin-bottom: 0.5rem;">
            <span>${params?.data?.name}</span>
            <span>${params?.data?.value} 个</span>
        </div>
        <div style="font-size: 0.1rem">
            <header>最优推荐</header>
            <img src="${params?.data?.example?.image}" style="width: 100%; height: 8rem; object-fit: cover" alt="">
            <div>名称：${params?.data?.example?.name}</div>
            <div style="display: flex; justify-content: space-between">
                <div>价格：${params?.data?.example?.price}</div>
                <div>销量：${params?.data?.example?.sales}</div>
                <div>热度：${params?.data?.example?.heat}</div>
            </div>
            <div>资讯：${params?.data?.example?.info}</div>
            <div>位置：${params?.data?.example?.address}</div>
            <div>介绍：${params?.data?.example?.introduction}</div>
        </div>
    </div>`
        }
    },
    dataRange: {
        x: 'left',
        y: 'bottom',
        textStyle: {
            color: '#fff',
        },
        splitList: [
            {start: 11, label: '>11 高', color: '#e64546'},
            {start: 6, end: 10, label: '6 - 10  中', color: '#f57567'},
            {start: 1, end: 5, label: '1 - 5  低', color: '#ff9985'},
            {start: 0, end: 0, label: '无数据', color: '#ffe5db'}
        ]
    },
    series: [
        {
            name: '旅游景点可视化',
            type: 'map',
            map: provinceTag.value,
            label: {
                show: false,
                color: '#fff'
            },
            // aspectScale: 1.3,
            zoom: 1,
            // roam: true,
            scaleLimit: {
                min: 1,
                max: 1,
            },
            itemStyle: {
                borderWidth: 0,
                areaColor: 'rgba(64,158,255,0.53)',
            },
            emphasis: {
                label: {
                    color: '#ffffff',
                },
                itemStyle: {
                    areaColor: 'rgb(76,169,203)',
                    color: '#FFF',
                    borderWidth: 0,
                },
            },
            selectedMode: 'single',
            select: {
                disabled: false,
                label: {
                    color: '#FFFFFF',
                },
                itemStyle: {
                    areaColor: 'rgba(16,195,254, 0.4)',
                    borderWidth: 0,
                },
            },
            data: params,
        }
    ]
})

echarts.registerMap(provinceTag.value, target[provinceTag.value], {});
const countData = ref<CommonModel.CountProvinceVo[]>([])
onMounted(() => {
    var chartDomMap = document.getElementById('province-map-chart')!;
    mapChart = echarts.init(chartDomMap);
    scenicSpotsProvinceCountRanking(provinces.value.find((province: {
        name: string;
        tag: string
    }) => province.tag === route.params.tag as string)!.name).then(res => {
        if (res.code === 200) {
            countData.value = res.data
            mapChartOption(res.data);
        } else {
            mapChartOption([]);
        }
    })
    window.onresize = function () {
        mapChart.resize();
    };
})
</script>

<template>
    <section class="flex mx-2">
        <section>
            <dv-border-box8 style="width: 58rem; height: 60.3rem">
                <div id="province-map-chart" style="height: 100%; width: 100%; padding: 1rem"></div>
            </dv-border-box8>
        </section>
        <section class="ml-2">
            <section class="flex">
                <dv-border-box12 style="width: 29.8rem; height: 39.5rem; padding: 1rem">
                    <div class="text-white w-[27.8rem] h-[37.5rem] flex flex-col items-center">
                        <dv-decoration-7 style="width:11rem;height:2rem;">
                            <div class="font-bold text-lg text-[#1dc1f5] mx-2">
                                景点数量排名
                            </div>
                        </dv-decoration-7>
                        <div class="w-full h-[35rem]">
                            <Amount :data="countData"/>
                        </div>
                    </div>
                </dv-border-box12>
                <section>
                    <dv-border-box13 style="width: 30.8rem; height: 22.5rem; padding: 1rem">
                        <div class="text-white w-[28.8rem] h-[20.5rem] flex flex-col items-center">
                            <dv-decoration-7 style="width:11rem;height:2rem;">
                                <div class="font-bold text-lg text-[#1dc1f5] mx-2">景点等级分析</div>
                            </dv-decoration-7>
                            <div class="w-full h-[18.5rem]">
                                <Level/>
                            </div>
                        </div>
                    </dv-border-box13>
                    <dv-border-box6 :color="['#5169b8', 'red']" style="width: 30.8rem; height: 17rem; padding: 1rem">
                        <div class="text-white w-[28.8rem] h-[15rem] flex flex-col items-center">
                            <div class="font-bold text-lg text-[#1dc1f5] mx-2 flex items-center">
                                <el-icon class="mr-2">
                                    <ChatDotRound/>
                                </el-icon>
                                游客评论
                            </div>
                            <Comment/>
                        </div>
                    </dv-border-box6>
                </section>

            </section>
            <section class="mt-1">
                <dv-border-box13 style="width: 60.6rem; height: 20.5rem; padding: 1rem">
                    <div class="text-white w-[58.6rem] h-[18.5rem] flex flex-col items-center">
                        <dv-decoration-7 style="width:11rem;height:2rem;">
                            <div class="font-bold text-lg text-[#1dc1f5] mx-2">
                                游客量分析
                            </div>
                        </dv-decoration-7>
                        <Sales/>
                    </div>
                </dv-border-box13>
            </section>

        </section>
    </section>
</template>


<style lang="scss" scoped>

</style>