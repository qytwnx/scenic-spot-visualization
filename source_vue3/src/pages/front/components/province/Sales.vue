<script setup lang="ts">
import * as echarts from "echarts";
import {onMounted, ref} from "vue";
import useScenicSpots from "@/composables/useScenicSpots";
import {useRoute} from "vue-router";

const {scenicSpotsProvinceSales} = useScenicSpots()
const route = useRoute()
var barChart: echarts.ECharts;

// 树状图 工人数量
const x_data = ref<string[]>([])
const y_data = ref<number[]>([])


let option = {
    calculable: true,
    grid: {
        top: "15%",
        left: "2%",
        right: "2%",
        bottom: "6%",
        containLabel: true,
    },
    tooltip: {
        trigger: "axis",
        axisPointer: {
            type: "cross"
        },
        textStyle: {
            align: 'left'
        }
    },
    // 区域缩放
    dataZoom: [
        { // 第一个 dataZoom 组件
            type: 'inside',
            xAxisIndex: 0, // 表示这个 dataZoom 组件控制 第一个 xAxis
            startValue: 0, // 数据窗口范围的起始数值index
            endValue: 10, // 数据窗口范围的结束数值index
        },
    ],
    xAxis: {
        type: 'category',
        data: x_data.value,
        axisTick: {
            //是否显示刻度线
            show: true,
        },
        axisLabel: {
            show: true,
            color: '#ffffff',
            interval: 0,
            fontSize: `0.73rem`,
            formatter: function (params: string) {
                var newParamsName = "";
                var paramsNameNumber = params.length;
                var provideNumber = 5; //一行显示几个字
                var rowNumber = Math.ceil(paramsNameNumber / provideNumber);
                if (paramsNameNumber > provideNumber) {
                    for (var p = 0; p < rowNumber; p++) {
                        var tempStr = "";
                        var start = p * provideNumber;
                        var end = start + provideNumber;
                        if (p == rowNumber - 1) {
                            tempStr = params.substring(start, paramsNameNumber);
                        } else {
                            tempStr = params.substring(start, end) + "\n";
                        }
                        newParamsName += tempStr;
                    }
                } else {
                    newParamsName = params;
                }
                return newParamsName;
            }
        },
        // y轴的颜色和宽度
        axisLine: {
            show: true,
            lineStyle: {
                color: '#e0e6f1'
            }
        }
    },
    yAxis: {
        type: 'value',
        axisLabel: {
            show: true,
            color: '#ffffff',
            fontSize: `0.73rem`,
        },
        // y轴的颜色和宽度
        axisLine: {
            show: true,
            lineStyle: {
                color: '#e0e6f1'
            }
        },
        splitLine: {
            show: false
        }
    },
    series: [
        {
            data: y_data.value,
            type: 'bar',
            itemStyle: {
                //颜色样式部分
                borderRadius: [10, 10, 0, 0],
                label: {
                    show: true,
                    position: "top",
                    textStyle: {
                        color: "lightpink",
                    },
                },
                //   柱状图颜色渐变
                color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
                    {offset: 0, color: "#8277E9"},
                    {offset: 1, color: "#CC77E9"},
                ]),
            }
        },
    ],
}
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
    barChart = echarts.init(document.getElementById('sales-charts')!)
    scenicSpotsProvinceSales(provinces.value.find((province: {
        name: string;
        tag: string
    }) => province.tag === route.params.tag as string)!.name).then(res => {
        if (res?.code === 200) {
            x_data.value = res.data.x
            y_data.value = res.data.y
            option = {
                calculable: true,
                grid: {
                    top: "15%",
                    left: "2%",
                    right: "2%",
                    bottom: "6%",
                    containLabel: true,
                },
                tooltip: {
                    trigger: "axis",
                    axisPointer: {
                        type: "cross"
                    },
                    textStyle: {
                        align: 'left'
                    }
                },
                // 区域缩放
                dataZoom: [
                    { // 第一个 dataZoom 组件
                        type: 'inside',
                        xAxisIndex: 0, // 表示这个 dataZoom 组件控制 第一个 xAxis
                        startValue: 0, // 数据窗口范围的起始数值index
                        endValue: 10, // 数据窗口范围的结束数值index
                    },
                ],
                xAxis: {
                    type: 'category',
                    data: x_data.value,
                    axisTick: {
                        //是否显示刻度线
                        show: true,
                    },
                    axisLabel: {
                        show: true,
                        color: '#ffffff',
                        interval: 0,
                        fontSize: `0.73rem`,
                        formatter: function (params: string) {
                            var newParamsName = "";
                            var paramsNameNumber = params.length;
                            var provideNumber = 5; //一行显示几个字
                            var rowNumber = Math.ceil(paramsNameNumber / provideNumber);
                            if (paramsNameNumber > provideNumber) {
                                for (var p = 0; p < rowNumber; p++) {
                                    var tempStr = "";
                                    var start = p * provideNumber;
                                    var end = start + provideNumber;
                                    if (p == rowNumber - 1) {
                                        tempStr = params.substring(start, paramsNameNumber);
                                    } else {
                                        tempStr = params.substring(start, end) + "\n";
                                    }
                                    newParamsName += tempStr;
                                }
                            } else {
                                newParamsName = params;
                            }
                            return newParamsName;
                        }
                    },
                    // y轴的颜色和宽度
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: '#e0e6f1'
                        }
                    }
                },
                yAxis: {
                    type: 'value',
                    axisLabel: {
                        show: true,
                        color: '#ffffff',
                        fontSize: `0.73rem`,
                    },
                    // y轴的颜色和宽度
                    axisLine: {
                        show: true,
                        lineStyle: {
                            color: '#e0e6f1'
                        }
                    },
                    splitLine: {
                        show: false
                    }
                },
                series: [
                    {
                        data: y_data.value,
                        type: 'bar',
                        itemStyle: {
                            //颜色样式部分
                            borderRadius: [10, 10, 0, 0],
                            label: {
                                show: true,
                                position: "top",
                                textStyle: {
                                    color: "lightpink",
                                },
                            },
                            //   柱状图颜色渐变
                            color: new echarts.graphic.LinearGradient(0, 1, 0, 0, [
                                {offset: 0, color: "#8277E9"},
                                {offset: 1, color: "#CC77E9"},
                            ]),
                        }
                    },
                ],
            }
            option && barChart.setOption(option)
        }
    })
    // 绘制图表
    window.addEventListener('resize', () => {
        barChart.resize()
    })
})
setInterval(() => {
    if (option!.dataZoom[0].endValue == y_data.value.length - 1) {
        option.dataZoom[0].endValue = 10
        option.dataZoom[0].startValue = 0
    } else {
        option.dataZoom[0].endValue = option.dataZoom[0].endValue + 1
        option.dataZoom[0].startValue = option.dataZoom[0].startValue + 1
    }
    barChart.setOption(option)
}, 2000)
</script>

<template>
    <div id="sales-charts" style="width: 58.6rem; height: 18rem"></div>
</template>


<style lang="scss" scoped>

</style>