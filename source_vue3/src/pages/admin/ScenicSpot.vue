<script setup lang="ts">
import {reactive, ref} from "vue";
import useScenicSpots from "@/composables/useScenicSpots";
import {ElMessage, ElNotification} from "element-plus";
import Create from "@/pages/admin/components/scenicspot/ScenicSpotCreate.vue";
import Update from "@/pages/admin/components/scenicspot/ScenicSpotUpdate.vue";

const {scenicSpotsDelete, scenicSpotsDeleteBatch, scenicSpotsPage} = useScenicSpots()

const query = reactive<ScenicSpotsModel.ScenicSpotsQueryDto>({
    name: "", pageNum: 1, pageSize: 10
})
const total = ref<number>(0)
const tableData = ref<ScenicSpotsModel.ScenicSpotsVo[]>([])
const createVisible = ref<boolean>(false)
const updateVisible = ref<boolean>(false)
const currentData = ref<ScenicSpotsModel.ScenicSpotsVo>({
    address: "",
    city: "",
    comment: "",
    createTime: "",
    heat: "",
    id: 0,
    image: "",
    info: "",
    introduction: "",
    level: "",
    name: "",
    price: "",
    province: "",
    sales: "",
    updateTime: ""
})
const loadPage = async () => {
    const res = await scenicSpotsPage({...query})
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
    if (query.name.length === 0) {
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
    if (query.name.length !== 0) {
        query.name = ''
        loadPage()
    }
}
const handleDelete = async (id: number) => {
    const res = await scenicSpotsDelete(id)
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
const handleSelectionChange = (val: ScenicSpotsModel.ScenicSpotsVo[]) => {
    multipleSelection.value = val.map((item) => {
        return item.id
    })
}

const handleDeleteBatch = async () => {
    if (multipleSelection.value?.length === 0) {
        ElMessage.error('请选择后再批量删除')
        return
    }
    const res = await scenicSpotsDeleteBatch({ids: multipleSelection.value})
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


const handleCreate = () => {
    createVisible.value = true
}

const handleUpdate = (item: ScenicSpotsModel.ScenicSpotsVo) => {
    currentData.value = item
    updateVisible.value = true
}
</script>

<template>
    <div>
        <el-card class="mb-2">
            <template #header>
                <div class="font-bold">
                    <span>景点管理</span>
                </div>
            </template>
            <div class="flex items-center">
                <div class="flex items-center">
                    <span class="w-20">景点名称:</span>
                    <div class="w-52">
                        <el-input v-model="query.name" placeholder="请输入"/>
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
                <el-button type="primary" size="small" @click="handleCreate">添加</el-button>
                <el-button type="warning" size="small" @click="handleDeleteBatch">批量删除</el-button>
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
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="name" label="景区名字"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="level" label="景区等级"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="province" label="所在省"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="city" label="所在市"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="address" label="地址"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="introduction" label="简介"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="heat" label="热度"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="price" label="价格"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="sales" label="月销"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="image" label="景点图片"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="info" label="资讯"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="comment" label="评论"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="createTime" label="创建时间"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="updateTime" label="更新时间"/>
                    <el-table-column align="center" fixed="right" label="操作" width="100">
                        <template #default="scope">
                            <el-button link type="success" size="small"  @click="handleUpdate(scope.row)">更新
                            </el-button>
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
            <Create :visible="createVisible"
                        @on-close="() => createVisible = false"
                        @on-submit="() => {
                     createVisible = false;
                     loadPage()
                   }"/>
            <Update :visible="updateVisible"
                        :old-data="currentData"
                        @on-close="() => updateVisible = false"
                        @on-submit="() => {
                     updateVisible = false;
                     loadPage()
                   }"/>
        </el-card>
    </div>
</template>

<style lang="scss" scoped>

</style>