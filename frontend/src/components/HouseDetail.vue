<template>
<div>
  <p>house detail</p>
  <p>
    <el-row>
      <el-column :span="8">
        <img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2287568211,2342036693&fm=26&gp=0.jpg" class="image"><br>
      </el-column>
      <el-column :span="8">
        Zoning: {{message[2]}}<br>
        {{message}}
      </el-column>
    </el-row>
  </p>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "HouseDetail.vue",
  props:['message'],

  data(){
    return {
      detail:[],
    }

  },

  methods:{
    
  }
}
</script>

<style scoped>

</style>