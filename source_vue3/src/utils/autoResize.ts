import { ref } from 'vue'

export default function useDraw() {
    const appRef = ref();
    const scale = {
        width: '1',
        height: '1',
    };
    const baseWidth = 1920;
    const baseHeight = 1080;
    const baseProportion = parseFloat((baseWidth / baseHeight).toFixed(5));
    const calcRate = () => {
        const currentRate = parseFloat((window.innerWidth / window.innerHeight).toFixed(5));
        if (appRef.value) {
            if (currentRate > baseProportion) {
                scale.width = ((window.innerHeight * baseProportion) / baseWidth).toFixed(5);
                scale.height = (window.innerHeight / baseHeight).toFixed(5);
                appRef.value.style.transform = `scale(${scale.width}, ${scale.height}) translate(-50%, -50%)`;
            } else {
                scale.height = ((window.innerWidth / baseProportion) / baseHeight).toFixed(5);
                scale.width = (window.innerWidth / baseWidth).toFixed(5)
                appRef.value.style.transform = `scale(${scale.width}, ${scale.height}) translate(-50%, -50%)`;
            }
        }
    };

    const resize = () => {
            calcRate();
    };
    const windowDraw = () => {
        window.addEventListener('resize', resize);
    };
    const unWindowDraw = () => {
        window.removeEventListener('resize', resize);
    };

    return {
        appRef,
        calcRate,
        windowDraw,
        unWindowDraw
    }
}