<script setup lang="ts">
import type {UploadProps, UploadRawFile, UploadUserFile} from 'element-plus'
import {ref, watch} from "vue";
import {Plus} from "@element-plus/icons-vue";
import {serviceIp} from "@/utils/request"
import useUserStore from "@/store/useUserStore";
import {ElMessage, ElNotification} from "element-plus";

const userStore = useUserStore()

const uploadUrl = serviceIp + '/files/upload'
const headers = {
    Authorization: 'Bearer ' + userStore.getToken(),
}
interface IProps {
    value: string
}

const imageUrl = ref<string>('')
const props = withDefaults(defineProps<IProps>(), {
    value: ''
})
const emit = defineEmits(['update:value'])
watch(() => props.value, (val) => {
    imageUrl.value = val || ''
}, {immediate: true})

const handleUploadSuccess: UploadProps['onSuccess'] = (response, uploadFile) => {
    if (response?.code === 200) {
        imageUrl.value = response?.data
        emit('update:value', imageUrl.value)
        ElNotification({
            title: 'Success',
            message: '上传成功',
            type: 'success',
        })
    } else {
        ElMessage.error(response?.message || '上传失败')
    }
}
</script>

<template>
    <div>
        <el-upload
                class="avatar-uploader"
                :action="uploadUrl"
                :headers="headers"
                :limit="1"
                accept=".png"
                :show-file-list="false"
                :on-success="handleUploadSuccess"
        >
            <img v-if="imageUrl" :src="imageUrl" class="avatar" alt=""/>
            <el-icon v-else class="avatar-uploader-icon">
                <Plus/>
            </el-icon>
        </el-upload>
    </div>
</template>


<style lang="scss" scoped>
.avatar-uploader .avatar {
  width: 178px;
  height: 178px;
  display: block;
}
</style>

<style>
.avatar-uploader .el-upload {
    border: 1px dashed var(--el-border-color);
    border-radius: 6px;
    cursor: pointer;
    position: relative;
    overflow: hidden;
    transition: var(--el-transition-duration-fast);
}

.avatar-uploader .el-upload:hover {
    border-color: var(--el-color-primary);
}

.el-icon.avatar-uploader-icon {
    font-size: 28px;
    color: #8c939d;
    width: 178px;
    height: 178px;
    text-align: center;
}
</style>