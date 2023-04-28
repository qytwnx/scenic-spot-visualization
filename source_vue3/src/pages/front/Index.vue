<script setup lang="ts">
import {onMounted, ref} from "vue";
import map from '@/assets/map/map.json';
import * as echarts from 'echarts';
import {BellFilled, ChatDotRound} from "@element-plus/icons-vue";
import Level from "@/pages/front/components/index/Level.vue";
import Amount from "@/pages/front/components/index/Amount.vue";
import Heat from "@/pages/front/components/index/Heat.vue";
import Recommend from "@/pages/front/components/index/Recommend.vue";
import {ElNotification} from "element-plus";
import router from "@/router";
import useScenicSpots from "@/composables/useScenicSpots";
import Info from "@/pages/front/components/index/Info.vue";
import Comment from "@/pages/front/components/index/Comment.vue";

const {scenicSpotsIndexCountRanking} = useScenicSpots()
const source = JSON.stringify(map)
const target = JSON.parse(source)
var mapChart: echarts.ECharts;

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

const mapChartOption = (param: CommonModel.CountVo[]) => mapChart.setOption({
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
        backgroundColor: "#FFFFFF",
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
        showDelay: 100
    },
    dataRange: {
        x: 'left',
        y: 'bottom',
        textStyle: {
            color: '#fff',
        },
        splitList: [
            {start: 201, label: '>201 高', color: '#e64546'},
            {start: 101, end: 200, label: '101 - 200  中', color: '#f57567'},
            {start: 1, end: 100, label: '1 - 100  低', color: '#ff9985'},
            {start: 0, end: 0, label: '无数据', color: '#ffe5db'}
        ]
    },
    series: [
        {
            name: '旅游景点数量',
            type: 'map',
            map: 'china',
            label: {
                show: false,
                color: '#fff'
            },
            // aspectScale: 1.3,
            zoom: 1.25,
            // roam: true,
            // zoom:5,
            scaleLimit: {
                min: 1,
                max: 1.25,
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
            data: param,
        }
    ]
})

echarts.registerMap("china", target.china, {});
const countData = ref<CommonModel.CountVo[]>([])
onMounted(() => {
    var chartDomMap = document.getElementById('map-chart')!;
    mapChart = echarts.init(chartDomMap);
    scenicSpotsIndexCountRanking().then(res => {
        if (res?.code === 200) {
            countData.value = res.data
            mapChartOption(res.data)
        } else {
            mapChartOption([])
        }
    })
    //@ts-ignore
    mapChart.on('click', (e: { name: string, data: { name: string, value: number } }) => {
        if (e.name === '南海诸岛' || e.data.value === 0) {
            ElNotification({
                title: '提示',
                message: '暂无数据',
                type: 'info',
            })
            return
        }
        router.push({
            name: 'FrontProvince',
            params: {
                tag: provinces.value.find((province: {
                    name: string;
                    tag: string
                }) => province.name === e.name)!.tag
            }
        });
    });
    window.onresize = function () {
        mapChart.resize();
    };
});

</script>

<template>
    <section class="flex mx-2">
        <section>
            <dv-border-box12 style="width: 29.8rem; height: 38rem; padding: 1rem">
                <div class="text-white w-[27.8rem] h-[36rem] flex flex-col items-center">
                    <dv-decoration-7 style="width:11rem;height:2rem;">
                        <div class="font-bold text-lg text-[#1dc1f5] mx-2">
                            景点数量排名
                        </div>
                    </dv-decoration-7>
                    <div class="w-full h-[33.5rem]">
                        <Amount :data="countData"/>
                    </div>
                </div>
            </dv-border-box12>
            <dv-border-box13 style="width: 29.8rem; height: 22.5rem; padding: 1rem">
                <div class="text-white w-[27.8rem] h-[20.5rem] flex flex-col items-center">
                    <dv-decoration-7 style="width:11rem;height:2rem;">
                        <div class="font-bold text-lg text-[#1dc1f5] mx-2">景点等级分析</div>
                    </dv-decoration-7>
                    <div class="w-full h-[18.5rem]">
                        <Level/>
                    </div>
                </div>
            </dv-border-box13>
        </section>
        <section class="mx-2">
            <dv-border-box8 style="width: 58.5rem; height: 46rem">
                <div id="map-chart" style="height: 100%; width: 100%; padding: 1rem"></div>
            </dv-border-box8>
            <dv-border-box10 style="width: 58.5rem; height: 14rem; margin-top: 0.4rem;">
                <div class="text-white w-[58.5rem] h-[14rem] p-[1rem] flex">
                    <div class="w-[27rem] h-[12rem]">
                        <div class="flex justify-center font-bold text-lg text-[#1dc1f5] items-center ">
                            <el-icon class="mr-2">
                                <BellFilled/>
                            </el-icon>
                            景点资讯
                        </div>
                        <div class="w-full h-[10rem] overflow-hidden">
                            <Info/>
                        </div>
                    </div>
                    <dv-decoration2 :reverse="true" style="width: 2.5rem; height: 12rem;"/>
                    <div class="w-[27rem] h-[12rem]">
                        <div class="flex justify-center font-bold text-lg text-[#1dc1f5] items-center ">
                            <el-icon class="mr-2">
                                <ChatDotRound/>
                            </el-icon>
                            游客评论
                        </div>
                        <div class="w-full h-[10rem] overflow-hidden">
                            <Comment/>
                        </div>
                    </div>
                </div>
            </dv-border-box10>
        </section>
        <section>
            <dv-border-box12 style="width: 29.8rem; height: 38rem; padding: 1rem">
                <div class="text-white w-[27.8rem] h-[36rem] flex flex-col items-center">
                    <dv-decoration-7 style="width:11rem;height:2rem;">
                        <div class="font-bold text-lg text-[#1dc1f5] mx-2">
                            景点热度排名
                        </div>
                    </dv-decoration-7>
                    <div class="w-full h-[33.5rem]">
                        <Heat/>
                    </div>
                </div>
            </dv-border-box12>
            <dv-border-box13 style="width: 29.8rem; height: 22.5rem; padding: 1rem">
                <div class="text-white w-[27.8rem] h-[20.5rem] flex flex-col items-center">
                    <dv-decoration-7 style="width:11rem;height:2rem;">
                        <div class="font-bold text-lg text-[#1dc1f5] mx-2">
                            热门景点推荐
                        </div>
                    </dv-decoration-7>
                    <div class="w-full h-[18.5rem]">
                        <Recommend/>
                    </div>
                </div>
            </dv-border-box13>
        </section>
    </section>
</template>


<style lang="scss" scoped>

</style>