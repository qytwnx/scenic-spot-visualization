<script setup lang="ts">
import * as echarts from "echarts";
import {onMounted, ref} from "vue";
import useScenicSpots from "@/composables/useScenicSpots";
import {useRoute} from "vue-router";

const route = useRoute()

var frontClassifyChart: echarts.ECharts;
const {scenicSpotsProvinceLevel} = useScenicSpots()
const frontClassifyChartOption = (params: CommonModel.CountVo[], total: number) => frontClassifyChart.setOption({
    title: {
        text: ["{value|" + total + "}", "{name|总数}"].join("\n"),
        top: "center",
        left: "center",
        textStyle: {
            rich: {
                value: {
                    color: "#1dc1f5",
                    fontSize: 24,
                    fontWeight: "bold",
                    lineHeight: 20,
                },
                name: {
                    color: "#fff",
                    lineHeight: 20,
                },
            },
        },
    },
    tooltip: {
        trigger: "item",
        backgroundColor: "rgba(0,0,0,.6)",
        borderColor: "rgba(147, 235, 248, .8)",
        textStyle: {
            color: "#FFF",
        },
    },
    series: {
        type: 'pie',
        radius: ["40%", "70%"],
        tooltip: {show: true},
        label: {
            formatter: "{b|{b}}\n {per|{d}%}",
            rich: {
                b: {
                    color: "#fff",
                    fontSize: 12,
                    lineHeight: 26,
                },
                c: {
                    color: "#31ABE3",
                    fontSize: 14,
                },
                per: {
                    color: "#31ABE3",
                    fontSize: 14,
                },
            },
        },
        data: params,
        emphasis: {
            itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: 'rgba(0, 0, 0, 0.5)'
            }
        }
    }
})
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
onMounted(() => {
    var frontClassifyChartDomMap = document.getElementById('front-classify-chart')!;
    frontClassifyChart = echarts.init(frontClassifyChartDomMap);
    scenicSpotsProvinceLevel(provinces.value.find((province: {
        name: string;
        tag: string
    }) => province.tag === route.params.tag as string)!.name).then(res => {
        if (res?.code === 200) {
            const data = res?.data
            let total
            total = data.reduce((total:number, item:CommonModel.CountVo) => (total += Number(item.value)), 0)
            frontClassifyChartOption(data, total)
        } else {
            frontClassifyChartOption([], 0)
        }
    })
    window.onresize = function () {
        frontClassifyChart.resize();
    };
});
</script>

<template>
    <div id="front-classify-chart" class="w-full h-full"></div>
</template>


<style lang="scss" scoped>

</style>