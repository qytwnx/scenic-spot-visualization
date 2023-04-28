<script setup lang="ts">
import {computed, reactive, ref, watch} from "vue";
import {ElMessage, ElNotification, FormInstance, FormRules} from "element-plus";
import useUser from "@/composables/useUser";

const {userUpdate} = useUser()
const ruleFormRef = ref<FormInstance>()

interface IProps {
    visible: boolean,
    oldData: UserModel.UserVo
}

const props = withDefaults(defineProps<IProps>(), {
    visible: false
})
const emit = defineEmits(['onClose', 'onSubmit'])
const fromData = reactive<UserModel.UserUpdateDto>({
    account: "", id: 0, name: ""
})

watch(() => props.oldData, (val) => {
    fromData.id = val.id || 0;
    fromData.name = val.name || '';
    fromData.account = val.account || '';
}, {immediate: true})

const dialogVisible = computed({
    get: () => props.visible,
    set: () => {
        emit('onClose')
    }
})
const closeDialog = () => {
    emit('onClose')
}

const validateUserName = (rule: any, value: any, callback: any) => {
    if (value === '') {
        callback(new Error('姓名不能为空'))
    }
    setTimeout(() => {
        if (value.length < 2) {
            callback(new Error('姓名长度至少两个字符'));
        } else {
            callback();
        }
    }, 10);
}

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

const rules = reactive<FormRules>({
    name: [{validator: validateUserName, trigger: 'blur'}],
    account: [{validator: validateUserAccount, trigger: 'blur'}]
})

const handleSubmit = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.validate(async (valid) => {
        if (valid) {
            const res = await userUpdate(fromData as UserModel.UserUpdateDto)
            if (res.code === 200) {
                ElNotification({
                    title: 'Success',
                    message: '更新成功',
                    type: 'success',
                })
                emit('onSubmit')
            } else {
                ElMessage.error(res.message || '更新失败')
            }
        } else {
            ElMessage.error('表单输入不完整')
            return
        }
    })
}
</script>

<template>
    <el-dialog
            v-model="dialogVisible"
            title="更新用户"
            width="30%"
    >
        <el-form
                ref="ruleFormRef"
                :model="fromData"
                status-icon
                :rules="rules"
                label-width="70px"
        >
            <el-form-item label="姓名" prop="name">
                <el-input v-model="fromData.name" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="手机号" prop="account">
                <el-input v-model="fromData.account" type="text" autocomplete="off"/>
            </el-form-item>
        </el-form>
        <template #footer>
      <span class="dialog-footer">
        <el-button size="small" @click="closeDialog">取消</el-button>
        <el-button size="small" type="primary" @click="handleSubmit(ruleFormRef)">
          确定
        </el-button>
      </span>
        </template>
    </el-dialog>
</template>


<style lang="scss" scoped>

</style>