<template>
<div>
    <el-row>
        <el-col :span="5" v-for="(o, index) in 4" :key="o" :offset="index > 0 ? 4 : 0">
            <el-card :body-style="{ padding: '10px' }" shadow ="hover">
                <img src="https://shadow.elemecdn.com/app/element/hamburger.9cf7b091-55e9-11e9-a976-7f4d0b07eef6.png" class="image">
                <div style="padding: 14px;">
                    <span>好吃的汉堡</span>
                    <div class="bottom clearfix">
                        <el-button type="text" class="button">操作按钮</el-button>
                    </div>
                </div>
            </el-card>
        </el-col>
    </el-row>
</div>
</template>

<script>
    export default {
        name: "houseItem.vue"
    }
</script>

<style scoped>

</style>