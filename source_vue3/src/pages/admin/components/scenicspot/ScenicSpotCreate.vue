<script setup lang="ts">
import {computed} from "vue";
import {reactive, ref} from 'vue'
import type {FormInstance} from 'element-plus'
import {ElMessage, ElNotification} from "element-plus";
import useScenicSpots from "@/composables/useScenicSpots";
import ImageUploads from "@/components/upload/ImageUploads.vue";

const {scenicSpotsAdd} = useScenicSpots()
const ruleFormRef = ref<FormInstance>()

interface IProps {
    visible: boolean
}

const props = withDefaults(defineProps<IProps>(), {
    visible: false,
})
const emit = defineEmits(['onClose', 'onSubmit'])
const dialogVisible = computed({
    get: () => props.visible,
    set: () => {
        emit('onClose')
    }
})
const closeDialog = () => {
    emit('onClose')
}

const fromData = reactive<ScenicSpotsModel.ScenicSpotsAddDto>({
    address: "",
    city: "",
    comment: "",
    heat: "",
    image: "",
    info: "",
    introduction: "",
    level: "",
    name: "",
    price: "",
    province: "",
    sales: ""
})

const handleSubmit = (formEl: FormInstance | undefined) => {
    if (!formEl) return
    formEl.validate(async (valid) => {
        if (valid) {
            const res = await scenicSpotsAdd(fromData as ScenicSpotsModel.ScenicSpotsAddDto)
            if (res.code === 200) {
                formEl.resetFields()
                ElNotification({
                    title: 'Success',
                    message: '新增成功',
                    type: 'success',
                })
                emit('onSubmit')
            } else {
                ElMessage.error(res.message || '新增失败')
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
            title="创建景点"
            width="30%"
    >
        <el-form
                ref="ruleFormRef"
                :model="fromData"
                status-icon
                label-width="80px"
        >
            <el-form-item label="景区名称" prop="name"
                          :rules="[
                                { required: true, message: '景区名称不能为空' },
                            ]">
                <el-input v-model="fromData.name" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="景区等级"
                          prop="level"
                          :rules="[
                                { required: true, message: '景区等级不能为空' },
                            ]"
            >
                <el-input v-model="fromData.level" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="所在省"
                          prop="province"
                          :rules="[
                                { required: true, message: '所在省不能为空' },
                            ]"
            >
                <el-input v-model="fromData.province" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="所在市"
                          prop="city"
                          :rules="[
                                { required: true, message: '所在市不能为空' },
                            ]"
            >
                <el-input v-model="fromData.city" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="地址"
                          prop="address"
                          :rules="[
                                { required: true, message: '地址不能为空' },
                            ]"
            >
                <el-input v-model="fromData.address" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="简介"
                          prop="introduction"
                          :rules="[
                                { required: true, message: '简介不能为空' },
                            ]"
            >
                <el-input v-model="fromData.introduction" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="热度"
                          prop="heat"
                          :rules="[
                                { required: true, message: '热度不能为空' },
                            ]"
            >
                <el-input v-model="fromData.heat" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="价格"
                          prop="price"
                          :rules="[
                                { required: true, message: '价格不能为空' },
                            ]"
            >
                <el-input v-model="fromData.price" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="月销"
                          prop="sales"
                          :rules="[
                                { required: true, message: '月销不能为空' },
                            ]"
            >
                <el-input v-model="fromData.sales" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="图片"
                          prop="image"
                          :rules="[
                                { required: true, message: '图片不能为空' },
                            ]"
            >
                <ImageUploads v-model:value="fromData.image"/>
            </el-form-item>
            <el-form-item label="资讯"
                          prop="info"
                          :rules="[
                                { required: true, message: '资讯不能为空' },
                            ]"
            >
                <el-input v-model="fromData.info" type="text" autocomplete="off"/>
            </el-form-item>
            <el-form-item label="评论"
                          prop="comment"
                          :rules="[
                                { required: true, message: '评论不能为空' },
                            ]"
            >
                <el-input v-model="fromData.comment" type="text" autocomplete="off"/>
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