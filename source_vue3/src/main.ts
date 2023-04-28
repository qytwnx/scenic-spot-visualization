import {createApp} from 'vue'
import pinia from "@/store/store";
import './style.scss'
import App from './App.vue'
import 'element-plus/es/components/message/style/css'
import 'element-plus/theme-chalk/el-notification.css'
import 'element-plus/theme-chalk/el-loading.css'
import router from "@/router";
import DataVVue3 from '@kjgl77/datav-vue3'

const app = createApp(App);
app.use(pinia)
app.use(router)
app.use(DataVVue3)
app.mount('#app')
