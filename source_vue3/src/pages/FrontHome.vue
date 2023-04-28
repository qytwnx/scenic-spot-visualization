<script setup lang="ts">
import FrontHeader from "@/components/layout/FrontHeader.vue";
import {onMounted, onUnmounted} from "vue";
import useDraw from "@/utils/autoResize";
const {appRef, calcRate, windowDraw, unWindowDraw} = useDraw()
onUnmounted(() => {
    unWindowDraw()
})
onMounted(() => {
    windowDraw()
    calcRate()
})
</script>

<template>
    <div class="front-home-class">
        <div id="index" ref="appRef">
            <FrontHeader style="width: 100%; height: 4.5rem; display: flex; justify-content: center"/>
            <div style="width: 100%; height: 60rem; margin-top: 1.5rem;">
                <RouterView/>
            </div>
        </div>
    </div>
</template>


<style lang="scss" scoped>
#index {
  background-image: url(@/assets/images/index-bg-6.png);
  background-repeat: no-repeat;
  background-size: 100% 100%;
  width: 1920px;
  height: 1080px;
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  transform-origin: left top;
}

.front-home-class {
  @apply w-full h-full bg-black select-none overflow-hidden;
}
</style>