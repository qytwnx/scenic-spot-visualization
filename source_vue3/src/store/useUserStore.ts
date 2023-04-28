import {defineStore} from 'pinia'
import router from "@/router";
import Cookies from "js-cookie";


const useUserStore = defineStore('user', {
    state: () => ({
        user: {},
        token: ''
    }),
    actions: {
        setUser(user: UserModel.UserVo) {
            this.user = user
            Cookies.set('user', JSON.stringify(user), {expires: 24})
        },
        getUser() {
            return Cookies.get('user') === undefined ? null : JSON.parse(Cookies.get("user") || '')
        },
        setToken(token: string) {
            this.token = token
            Cookies.set('token', token, {expires: 24})
        },
        getToken() {
            return Cookies.get('token') === undefined ? null : Cookies.get("token" || '')
        },
        async logout() {
            Cookies.remove('user')
            Cookies.remove('token')
            await router.push({path: '/auth/login'})
        },
        remove() {
            Cookies.remove('user')
            Cookies.remove('token')
        }
    }
})

export default useUserStore