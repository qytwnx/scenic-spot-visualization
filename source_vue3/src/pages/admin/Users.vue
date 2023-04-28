<script setup lang="ts">
import {reactive, ref} from "vue";
import useUser from "@/composables/useUser";
import {ElMessage, ElNotification} from "element-plus";
import UserCreate from "@/pages/admin/components/user/UserCreate.vue";
import UserUpdate from "@/pages/admin/components/user/UserUpdate.vue";

const {userDelete, passwordReset, userPage} = useUser()

const query = reactive<UserModel.UserQueryDto>({
    account: "", name: "", pageNum: 1, pageSize: 10
})
const total = ref<number>(0)
const tableData = ref<UserModel.UserVo[]>([])
const createVisible = ref<boolean>(false)
const updateVisible = ref<boolean>(false)
const currentUser = ref<UserModel.UserVo>({
    account: "", createTime: "", id: 0, name: "", role: "", updateTime: ""
})

const loadPage = async () => {
    const res = await userPage({...query})
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
    if (query.name.length === 0 && query.account.length === 0) {
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
    if (query.name.length !== 0 || query.account.length !== 0) {
        query.name = ''
        query.account = ''
        loadPage()
    }
}

const handleCreate = () => {
    createVisible.value = true
}
const handleDelete = async (id: number) => {
    const res = await userDelete(id)
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
const handleUpdate = (item: any) => {
    currentUser.value = item
    updateVisible.value = true
}
const handleResetPassword = async (account: string) => {
    const res = await passwordReset(account)
    if (res.code === 200) {
        ElNotification({
            title: 'Success',
            message: '重置密码成功',
            type: 'success',
        })
    } else {
        ElMessage.error(res.message || '重置密码失败')
    }
}
</script>

<template>
    <div>
        <el-card class="mb-2">
            <template #header>
                <div class="font-bold">
                    <span>用户管理</span>
                </div>
            </template>
            <div class="flex items-center">
                <div class="flex items-center">
                    <span class="w-12">姓名:</span>
                    <div class="w-52">
                        <el-input v-model="query.name" placeholder="请输入"/>
                    </div>
                </div>
                <div class="flex items-center ml-5">
                    <span class="w-16">手机号:</span>
                    <div class="w-52">
                        <el-input v-model="query.account" placeholder="请输入"/>
                    </div>
                </div>
            </div>
            <div class="flex my-2 justify-end">
                <el-button type="info" size="small" @click="resetSearch">重置</el-button>
                <el-button type="primary" size="small" @click="handleSearch">搜索</el-button>
            </div>
        </el-card>
        <el-card>
            <div class="mb-2 flex justify-end">
                <el-button type="primary" size="small" @click="handleCreate">添加</el-button>
            </div>
            <div>
                <el-table
                    :data="tableData"
                    style="width: 100%"
                >
                    <template #empty>
                        <el-empty description="暂无数据"/>
                    </template>
                    <el-table-column fixed align="center" prop="id" label="ID"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="name" label="姓名"/>
                    <el-table-column align="center" prop="account" label="手机号"/>
                    <el-table-column align="center" prop="role" label="角色">
                        <template #default="scope">
                            {{ scope?.row?.role === 'super_admin' ? '超级管理员' : '管理员' }}
                        </template>
                    </el-table-column>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="createTime" label="创建时间"/>
                    <el-table-column align="center" :show-overflow-tooltip="true" prop="updateTime" label="更新时间"/>
                    <el-table-column align="center" fixed="right" label="操作" width="200">
                        <template #default="scope">
                            <el-button link type="success" size="small" v-if="scope.row?.role !== 'super_admin'" @click="handleUpdate(scope.row)">更新信息
                            </el-button>
                            <el-button link type="warning" size="small" @click="handleResetPassword(scope.row.id)">
                                重置密码
                            </el-button>
                            <el-button link type="danger" size="small" v-if="scope.row?.role !== 'super_admin'"
                                       @click="handleDelete(scope.row.id)">删除
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
            <UserCreate :visible="createVisible"
                        @on-close="() => createVisible = false"
                        @on-submit="() => {
                     createVisible = false;
                     loadPage()
                   }"/>
            <UserUpdate :visible="updateVisible"
                        :old-data="currentUser"
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