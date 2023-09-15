import Cookies from "js-cookie"
import router from "@/router";
import axios from "axios";
import {ElLoading, ElMessage} from "element-plus";

const baseURL = 'http://127.0.0.1:8100'
const service = axios.create({
    baseURL: baseURL,
    timeout: 20000 // 请求超时时间
})
let loading: any;

service.interceptors.request.use(
    (config: any) => {
        loading = ElLoading.service({
            lock: true,
            text: 'Loading',
            background: 'rgba(255,255,255,0.1)',
        })
        if (config.headers['authorization'] !== undefined) {
            return
        }
        config.headers['Content-Type'] = 'application/json;charset=utf-8';
        let token = Cookies.get("token") ? Cookies.get("token") : null
        if (token !== null) {
            config.headers['authorization'] = 'Bearer ' + token;  // 设置请求头
        }
        return config
    },
    error => {
        return Promise.reject(error)
    });

service.interceptors.response.use(
    response => {
        loading.close()
        let res = response;
        if (res.data.code === 401) {
            Cookies.remove("user")
            Cookies.remove("token")
            return
        } else if (res.data.code === 403) {
            router.replace('/error/403')
            return
        }
        return res.data;
    },
    error => {
        loading.close()
        console.log('err' + error)
        let {message} = error;
        if (message == "Network Error") {
            message = "后端接口连接异常";
        } else if (message.includes("timeout")) {
            message = "系统接口请求超时";
        } else if (message.includes("Request failed with status code")) {
            message = "系统接口" + message.substr(message.length - 3) + "异常";
        }
        ElMessage.error(message)
        return Promise.reject(error)
    })

export default service
export const serviceIp = baseURL
