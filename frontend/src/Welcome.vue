<template>
<div>
    <el-card shadow="hover" class="card1">
    <div class="text1">
      Welcome to Smart Recommendation! <br>
    </div>
      <i class="el-icon-phone"></i>
      Phone abc-000000 to Express More Emergency Needs
    </el-card>
    <el-divider></el-divider>
    <el-carousel>
      <el-carousel-item v-for="item in imgList" :key="item.name" style="height:600px">
        <img :src="item.src" style="height:100%;width:100%;" alt="图片丢失了" :title="item.title" />
      </el-carousel-item>
    </el-carousel>
    <div>
        <el-card :body-style="{ padding: '0px', width:'500px!important'}">
        <img src="./assets/zmd-2.jpg" class="image" style="width:400px">
        <div style="padding: 14px;">
            <span>好吃的汉堡</span>
            <div class="bottom clearfix">
            <time class="time">{{ currentDate }}</time>
            <el-button type="text" class="button">操作按钮</el-button>
            </div>
        </div>
        </el-card>

        <el-card :body-style="{ padding: '0px', width:'500px!important'}">
        <img src="./assets/zmd-2.jpg" class="image" style="width:400px">
        <div style="padding: 14px;">
            <span>好吃的汉堡</span>
            <div class="bottom clearfix">
            <time class="time">{{ currentDate }}</time>
            <el-button type="text" class="button">操作按钮</el-button>
            </div>
        </div>
        </el-card>
    </div>
</div>
    
</template>



<style>
.el-carousel{
    padding-left: 0%!important;
    height: 800px!important;
    width: 100%;
}
.card1{
    
    background-color:rgb(115, 197, 193)!important;
    font-size: 18px;
    font-style:initial;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    /* padding-top: 20%!important; */
    padding-left: 0%!important;
    padding-right: 0%!important;
    /* height: 40px!important; */
    text-align: center!important;
    
}

.text1{
    font-size: 45px!important;
}
  /* .el-carousel__item h3 {
    color: #475669;
    font-size: 18px;
    opacity: 0.75;
    line-height: 300px;
    margin: 0;
  } */
  
 /*  .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
  }
  
  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  } */
</style>

<script>
    export default {
        
    data() {
        return {
            imgList: [
                {
                name: "1",
                src: require("@/assets/zmd-3.jpg"),
                title: "Comfortable Environment"
                },
                {
                name: "2",
                src: require("@/assets/zmd-2.jpg"),
                title: "Convenient to Work"
                },
                {
                name: "3",
                src: require("@/assets/zmd-1.jpg"),
                title: "Safe and Assured"
                },
                {
                name: "4",
                src: require("@/assets/zmd-4.jpg"),
                title: "Prosperous Surroundings"
                },
                {
                name: "5",
                src: require("@/assets/zmd-5.jpg"),
                title: "Flexible Decoration Style"
                }
            ]
        };
    }
    }

    
</script>