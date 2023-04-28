<script setup lang="ts">
import * as echarts from "echarts";
import {onMounted} from "vue";
import useScenicSpots from "@/composables/useScenicSpots";

var frontClassifyChart: echarts.ECharts;
const {scenicSpotsIndexLevel} = useScenicSpots()
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

onMounted(() => {
    var frontClassifyChartDomMap = document.getElementById('front-classify-chart')!;
    frontClassifyChart = echarts.init(frontClassifyChartDomMap);
    scenicSpotsIndexLevel().then(res => {
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