import {defineStore} from 'pinia';


const useAppStore = defineStore({
    id: 'appStore',
    state: () => ({
        collapsed: false,
        currentPath: ''
    }),
    getters: {
        getCollapsed(): boolean {
            return this.collapsed
        },
        getCurrentPath(): string {
            return this.currentPath
        },
    },
    actions: {
        setCollapsed(collapsed: boolean) {
            this.collapsed = collapsed
        },
        setCurrentPath(currentPath: string) {
            this.currentPath = currentPath
        },
    }
});
export default useAppStore;