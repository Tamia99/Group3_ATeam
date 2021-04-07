<template>
    <!-- <h1>This is the houseList page</h1> -->
    
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <!-- <el-breadcrumb-item>All Resources</el-breadcrumb-item> -->
        </el-breadcrumb>

        
        <el-input placeholder="Please input your key words">
                <!-- <el-select v-model="select" slot="prepend" placeholder="请选择">
                    <el-option label="餐厅名" value="1"></el-option>
                    <el-option label="订单号" value="2"></el-option>
                    <el-option label="用户电话" value="3"></el-option>
                </el-select> -->
            <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
        
    </div>
    
</template>

<script>
export default {
    data() {
        return {}
    },
    created() {},
    methods: {}
}
</script>

<style scoped>
.el-input {
    width: 500px;
    padding-right: 50%;

}
</style>
