<script setup lang="ts">
import {reactive, ref} from "vue";
import useFiles from "@/composables/useFiles";
import {ElMessage, ElNotification} from "element-plus";

const {filePage} = useFiles()
const query = reactive<FilesModel.FilesQueryDto>({
    name: "", pageNum: 1, pageSize: 10, type: ""
})
const total = ref<number>(0)
const tableData = ref<FilesModel.FilesVo[]>([])

const loadPage = async () => {
    const res = await filePage({...query})
    if (res.code === 200) {
        tableData.value = res.data.records
        total.value = res.data.total
    } else {
        ElMessage.error(res.message)
    }
}
loadPage()
const handleSizeChange = (val: number) => {
    query.pageSize = val
    loadPage()
}
const handleCurrentChange = (val: number) => {
    query.pageNum = val
    loadPage()
}

const handleSearch = () => {
    if (query.name.length === 0 && query.type.length === 0) {
        ElNotification({
            title: 'Warning',
            message: '请输入内容后进行搜索',
            type: 'warning',
        })
        return
    }
    loadPage()
}

const resetSearch = () => {
    if (query.name.length !== 0 || query.type.length !== 0) {
        query.name = ''
        query.type = ''
        loadPage()
    }
}

const handleDownload = (url: string) => {
    window.open(url)
}
</script>

<template>
    <div>
        <el-card class="mb-2">
            <template #header>
                <div class="font-bold">
                    <span>文件管理</span>
                </div>
            </template>
            <div class="flex items-center">
                <div class="flex items-center">
                    <span class="w-16">文件名:</span>
                    <div class="w-52">
                        <el-input v-model="query.name" placeholder="请输入"/>
                    </div>
                </div>
                <div class="flex items-center ml-5">
                    <span class="w-20">文件类型:</span>
                    <div class="w-52">
                        <el-input v-model="query.type" placeholder="请输入"/>
                    </div>
                </div>
            </div>
            <div class="flex my-2 justify-end">
                <el-button type="info" size="small" @click="resetSearch">重置</el-button>
                <el-button type="primary" size="small" @click="handleSearch">搜索</el-button>
            </div>
        </el-card>
        <el-card>
            <el-table
                    :data="tableData"
                    style="width: 100%"
            >
                <template #empty>
                    <el-empty description="暂无数据"/>
                </template>
                <el-table-column fixed align="center" prop="id" label="ID"/>
                <el-table-column align="center" :show-overflow-tooltip="true" prop="name" label="文件名称"/>
                <el-table-column align="center" prop="type" label="类型"/>
                <el-table-column align="center" prop="size" label="大小"/>
                <el-table-column align="center" :show-overflow-tooltip="true" prop="url" label="链接"/>
                <el-table-column align="center" :show-overflow-tooltip="true" prop="uploader" label="上传用户">
                    <template #default="scope">
                        {{scope?.row?.uploader?.name}}
                    </template>
                </el-table-column>
                <el-table-column align="center" :show-overflow-tooltip="true" prop="createTime" label="创建时间"/>
                <el-table-column align="center" :show-overflow-tooltip="true" prop="updateTime" label="更新时间"/>
                <el-table-column align="center" fixed="right" label="操作" width="100">
                    <template #default="scope">
                        <el-button link type="success" size="small" @click="handleDownload(scope.row.url)">下载</el-button>
                    </template>
                </el-table-column>
            </el-table>
            <div class="my-3 flex justify-end">
                <el-pagination
                        v-model:current-page="query.pageNum"
                        v-model:page-size="query.pageSize"
                        :page-sizes="[10, 20, 30, 50]"
                        :small="true"
                        :background="true"
                        layout="total, sizes, prev, pager, next"
                        :total="total"
                        @size-change="handleSizeChange"
                        @current-change="handleCurrentChange"
                />
            </div>
        </el-card>
    </div>
</template>

<style lang="scss" scoped>

</style>