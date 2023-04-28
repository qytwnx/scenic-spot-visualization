<script setup lang="ts">
import useUserStore from "@/store/useUserStore";
import useUser from "@/composables/useUser";
import {ElMessage, ElNotification, FormInstance, FormRules} from "element-plus";
import {ref, reactive} from "vue";
import router from "@/router";
import {Message, Lock} from "@element-plus/icons-vue";

const userStore = useUserStore()
const {loginUser} = useUser();

const ruleFormRef = ref<FormInstance>()
const fromData = reactive<UserModel.UserLoginDto>({
    account: '',
    password: '',
})

const validateUserAccount = (rule: any, value: any, callback: any) => {
    if (value === '') {
        callback(new Error('手机号不能为空'))
    }
    setTimeout(() => {
        const checkRule = /^(?:(?:\+|00)86)?1\d{10}$/
        if (!checkRule.test(value)) {
            callback(new Error('您输入的手机号不合法'));
        } else {
            callback();
        }
    }, 10);
}

const validateUserPassword = (rule: any, value: any, callback: any) => {
    if (value === '') {
        callback(new Error('密码不能为空'))
    }
    setTimeout(() => {
        const checkRule = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,16}$/
        if (!checkRule.test(value)) {
            callback(new Error('密码至少8个字符，至少1个大写字母，1个小写字母和1个数字'));
        } else {
            callback();
        }
    }, 10);
}

const rules = reactive<FormRules>({
    account: [{validator: validateUserAccount, trigger: 'blur'}],
    password: [{validator: validateUserPassword, trigger: 'blur'}],
})

const handleSubmit = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.validate(async (valid) => {
        if (valid) {
            const res = await loginUser(fromData as UserModel.UserLoginDto)
            if (res.code === 200) {
                userStore.setUser(res.data.user)
                userStore.setToken(res.data.token)
                await router.push({path: '/'})
                ElNotification({
                    title: 'Success',
                    message: '登录成功',
                    type: 'success',
                })
                formEl.resetFields()

            } else {
                ElMessage.error(res.message || '登录失败')
            }
        } else {
            ElMessage.error('表单输入不完整')
            return
        }
    })
}

const handleWatchEnter = (e: KeyboardEvent) => {
    const key = window.event ? e.keyCode : e.which;
    if (key === 13) {
        handleSubmit(ruleFormRef.value)
    }
}
document.addEventListener('keydown', handleWatchEnter);
</script>

<template>
    <section class="login-container">
        <section class="login-card">
            <header class="flex flex-col items-center justify-center my-14 font-bold text-blue-600 animate-pulse">
                <span class="text-3xl">景点分析大数据中心</span>
                <span class="text-2xl mt-3">——登录</span>
            </header>
            <el-form
                    ref="ruleFormRef"
                    :model="fromData"
                    status-icon
                    :rules="rules"
                    class="px-5 w-full opacity-100"
            >
                <el-form-item prop="account">
                    <el-input v-model="fromData.account" placeholder="请输入手机号" :prefix-icon="Message"
                              type="text"
                              autocomplete="off"/>
                </el-form-item>
                <el-form-item prop="password">
                    <el-input v-model="fromData.password" placeholder="请输入密码" :prefix-icon="Lock"
                              type="password"
                              autocomplete="off"/>
                </el-form-item>
                <el-form-item>
                    <el-button type="primary" @click="handleSubmit(ruleFormRef)" round class="w-full">登录
                    </el-button>
                </el-form-item>
            </el-form>
        </section>
    </section>
</template>


<style lang="scss" scoped>
.login-container {
  background-image: url(@/assets/images/login-bg.png);
  @apply w-full h-full bg-center bg-cover flex items-center justify-end;

  .login-card {
    @apply w-96 h-96 bg-white rounded mx-60 opacity-80 shadow-2xl;
  }
}
</style>