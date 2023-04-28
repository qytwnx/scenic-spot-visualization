<script setup lang="ts">

import * as echarts from "echarts";
import {onMounted} from "vue";

var barChart: echarts.ECharts;

// 树状图 工人数量

const barChartOption = (param: CommonModel.CountVo[]) => barChart.setOption({
    tooltip: {
        trigger: 'axis',
        axisPointer: {
            type: 'shadow'
        }
    },
    grid: {
        top: '8%',
        left: '3%',
        right: '4%',
        bottom: '3%',
        containLabel: true
    },
    dataZoom: [
        //滑动条
        {
            xAxisIndex: 0, //这里是从X轴的0刻度开始
            show: false, //是否显示滑动条，不影响使用
            type: "inside", // 这个 dataZoom 组件是 slider 型 dataZoom 组件
            startValue: 0, // 从头开始。
            endValue: 4, // 一次性展示几个。
        },
    ],
    xAxis: [
        {
            type: 'category',
            data: param, // 表数据,
            min: 0,
            // max: 4,
            axisTick: {
                show: false,
            },
            axisLabel: {
                show: true,
                interval: 0,
                fontSize: `0.1rem`,
                // rotate: 45,
                formatter: function (value: string, index: any) {
                    const b = value.split(' ')
                    if (b.length > 2) {
                        return b[0] + ' ' + b[1] + '\n\n' + b[2]
                    } else {
                        return value.replace(' ', '\n\n')
                    }
                },
                color: '#6861a6'
            },
            axisLine: {
                show: true,
                lineStyle: {
                    color: '#e0e6f1'
                }
            }
        }
    ],
    yAxis: {
        type: 'value',
        splitLine: false,
        splitNumber: 3,
        splitArea: {
            show: true,
            areaStyle: {
                color: ['#f7f7ff', 'rgba(250,250,250,0.3)']
            }
        },//斑马纹背景
        // y轴的字体样式
        axisLabel: {
            show: true,
            color: '#5266c0',
            fontSize: `0.13rem`,
        },
        // y轴的颜色和宽度
        axisLine: {
            show: true,
            lineStyle: {
                color: '#e0e6f1'
            }
        }
    },
    series: [
        {
            name: '数量',
            type: 'bar',
            data: param,
            barWidth: '20%',
            barGap: '10%',/*多个并排柱子设置柱子之间的间距*/
            itemStyle: {
                borderRadius: 20,
                color: function (params: { dataIndex: number; }) {
                    if (params.dataIndex % 2 === 0) {
                        return (new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                            offset: 1,
                            color: '#a8aeff'
                        },
                            {
                                offset: 0,
                                color: '#97b0ff'
                            }
                        ]))
                    }
                    return (new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 1,
                        color: '#6d8ee3'
                    },
                        {
                            offset: 0,
                            color: '#3d48a6'
                        }
                    ]))
                }
            }
        }
    ]
})

onMounted(() => {
    barChart = echarts.init(document.getElementById('sales')!)
    barChartOption([])
    const tableData1 = ["Management 管理", "Steel structure 钢结构", "Finishing 装修", "Civil 土建", "MEP 机电", "MISC 其他"]
    // const x = this.tableData.x//x轴
    // const y = this.tableData.y//y轴
    //
    // if (x.length > 0 && y.length > 0) {
    //     this.timechartes = setInterval(function () {
    //         // 每次向后滚动一个，最后一个从头开始。
    //         if (option.dataZoom[0].endValue == x.length) {
    //             option.dataZoom[0].endValue = 4;
    //             option.dataZoom[0].startValue = 0;
    //         } else {
    //             option.dataZoom[0].endValue = option.dataZoom[0].endValue + 1;
    //             option.dataZoom[0].startValue = option.dataZoom[0].startValue + 1;
    //         }
    //         myChart.setOption(option)
    //     }, 2000);
    // }

    // 绘制图表
    // barChart.setOption(option)
    window.addEventListener('resize', () => {
        barChart.resize()
    })
})

</script>

<template>
    <div id="sales" style="width: 58.6rem; height: 18rem"></div>
</template>


<style lang="scss" scoped>

</style>