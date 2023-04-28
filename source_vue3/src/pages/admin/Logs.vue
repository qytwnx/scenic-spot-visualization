<script setup lang="ts">
import {reactive, ref} from "vue";
import useLogs from "@/composables/useLogs";
import {ElMessage, ElNotification} from "element-plus";
import dayjs from "dayjs";

const {logsDelete, logsDeleteBatch, logsDeleteAll, logsPage} = useLogs()

const query = reactive<LogsModel.LogsQueryDto>({
    method: "", pageNum: 1, pageSize: 10
})
const total = ref<number>(0)
const tableData = ref<LogsModel.LogsVo[]>([])

const loadPage = async () => {
    const res = await logsPage({...query})
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
    if (query.method.length === 0) {
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
    if (query.method.length !== 0) {
        query.method = ''
        loadPage()
    }
}
const handleDelete = async (id: number) => {
    const res = await logsDelete(id)
    if (res.code === 200) {
        ElNotification({
            title: 'Success',
            message: '删除成功',
            type: 'success',
        })
        await loadPage()
    } else {
        ElMessage.error(res.message || '删除失败')
    }
}


const handleDeleteAll = async () => {
    const res = await logsDeleteAll()
    if (res.code === 200) {
        ElNotification({
            title: 'Success',
            message: '删除成功',
            type: 'success',
        })
        await loadPage()
    } else {
        ElMessage.error(res.message || '删除失败')
    }
}

const multipleSelection = ref<number[]>([])
const handleSelectionChange = (val: LogsModel.LogsVo[]) => {
    multipleSelection.value = val.map((item) => {
        return item.id
    })
}

const handleDeleteBatch = async () => {
    if (multipleSelection.value?.length === 0) {
        ElMessage.error('请选择后再批量删除')
        return
    }
    const res = await logsDeleteBatch({ids: multipleSelection.value})
    if (res.code === 200) {
        multipleSelection.value = []
        ElNotification({
            title: 'Success',
            message: '批量删除成功',
            type: 'success',
        })
        await loadPage()
    } else {
        ElMessage.error(res.message || '批量删除失败')
    }
}
</script>

<template>
    <div>
        <el-card class="mb-2">
            <template #header>
                <div class="font-bold">
                    <span>操作日志管理</span>
                </div>
            </template>
            <div class="flex items-center">
                <div class="flex items-center">
                    <span class="w-20">请求方法:</span>
                    <div class="w-52">
                        <el-input v-model="query.method" placeholder="请输入"/>
                    </div>
                </div>
            </div>
            <div class="flex my-2 justify-end">
                <el-button type="info" size="small" @click="resetSearch">重置</el-button>
                <el-button type="primary" size="small" @click="handleSearch">搜索</el-button>
            </div>
        </el-card>
        <el-card>
            <div class="mb-2 flex justify-start">
                <el-button type="warning" size="small" @click="handleDeleteBatch">批量删除
                </el-button>
                <el-button type="danger" size="small" @click="handleDeleteAll">
                    全部删除
                </el-button>
            </div>
            <div>
                <el-table
                        :data="tableData"
                        style="width: 100%"
                        @selection-change="handleSelectionChange"
                >
                    <template #empty>
                        <el-empty description="暂无数据"/>
                    </template>
                    <el-table-column type="selection" width="55"/>
                    <el-table-column fixed align="center" prop="id" label="ID"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="method" label="请求方法"/>
                    <el-table-column align="center" prop="url" label="请求地址"/>
                    <el-table-column align="center" prop="ip" label="请求IP"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="operationTime"
                                     label="请求时间"/>
                    <el-table-column align="center" fixed="right" label="操作" width="100">
                        <template #default="scope">
                            <el-button link type="danger" size="small" @click="handleDelete(scope.row.id)">删除
                            </el-button>
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
            </div>
        </el-card>
    </div>
</template>

<style lang="scss" scoped>

</style>