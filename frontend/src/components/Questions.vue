<template>
    <div>
        <h1>Here is the questions page</h1><br>
        <span>Q1 What kind of house do you want?</span>
        <el-select v-model="value" placeholder="please choose">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
        </el-select>
        <br>
        <el-input-number v-model="num" @change="handleChange" :min="0" :max="10" label="描述文字"></el-input-number>
    </div>
</template>

<script>
    export default {
        name: "Questions.vue",
        data() {
            return {
                num: 0,
                options: [{
                    value: '选项1',
                    label: '黄金糕'
                }, {
                    value: '选项2',
                    label: '双皮奶'
                }, {
                    value: '选项3',
                    label: '蚵仔煎'
                }, {
                    value: '选项4',
                    label: '龙须面'
                }, {
                    value: '选项5',
                    label: '北京烤鸭'
                }],
                value: ''
            }
        },
        methods: {
            handleChange(value) {
                console.log(value);
            }
        }
    }
</script>

<style scoped>

</style>