<template>
<div>
    <el-carousel style=" margin-top:0%!important">
      <el-carousel-item v-for="item in imgList" :key="item.name" style="height:600px; margin-top:0%!important">
        <img :src="item.src" style="height:83%;width:100%;" alt="图片丢失了" :title="item.title" />
        
      </el-carousel-item>
      
    </el-carousel>
    
    <nobr style="padding-left:37%; font-size:25px; font-weight:bold;">What you can do HERE?</nobr>
    
    <div class="cards1">
      
          <el-card style="width:30%!important; margin-left:0%; margin-top:5%;" @click.native="route1">
            <img src="./components/chat.jpg" class="image" style="width:100%; height:100%;">
            <div style="padding-top: 15px;">
                <nobr style="font-weight:bold; font-size:15px; margin-bottom:20%!important">Smart Chatting Assistant</nobr><br>
                <div style="margin-top:6%;">
                  <nobr class="clicking">Click </nobr>
                  to chat freely with our intelligent assistant and get the most suitable choices for you!
                </div>
            </div>
        </el-card>

        <el-card style="width:30%!important; margin-left:33%; margin-top:-31.2%;" @click.native="route2">
            <img src="./components/pic4.jpg" class="image" style="width:100%; height:100%;">
            <div style="padding-top: 15px;">
                <nobr style="font-weight:bold; font-size:15px; margin-bottom:20%!important">Recommendations for you</nobr><br>
                <div style="margin-top:6%;">Don't know which homes suit you most? 
                  <nobr class="clicking"> Click </nobr>
                  and recognize them from our recommendations!
                </div>
            </div>
        </el-card>

        <el-card style="width:30%!important; margin-left:66%; margin-top:-31.2%;" @click.native="route3">
            <img src="./components/allhouses3.jpg" class="image" style="width:100%; height:100%;">
            <div style="padding-top: 15px;">
                <nobr style="font-weight:bold; font-size:15px; margin-bottom:20%!important">Various kinds of Homes</nobr><br>
                <div style="margin-top:6%;">No matter what you prefer, you will always find a satisfying home here!
                  <nobr class="clicking"> Click </nobr> to see them!
                </div>
            </div>
        </el-card>
        
    </div>

    <el-card style="width:100%!important;margin-top:45%">
            <img src="./components/pic-card.jpg" class="image" style="width:100%; height:100%;">
        
        </el-card>
    
</div>
    
</template>



<style scoped>
.el-carousel{
    padding-left: 0%!important;
    height: 600px!important;
    width: 100%;
    position:relative;
    z-index: 1;
    margin-top:10%!important;
}
.card1{
    
    background-color:rgb(115, 197, 193)!important;
    font-size: 18px;
    font-style:initial;
    font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
    padding-left: 0%!important;
    padding-right: 0%!important;
    text-align: center!important;
    
}

.cards1{
  position:absolute;
}

.text1{
    font-size: 45px!important;
}

.clicking{
  color: rgb(12, 163, 209);
}

</style>

// <script>
    export default {
        
      data() {
          return {
              imgList: [
                  // {
                  // name: "1",
                  // src: require("@/assets/pic-card.jpg"),
                  // title: "Comfortable Environment"
                  // },
                  {
                  name: "2",
                  src: require("@/assets/zmd-1.jpg"),
                  title: "Comfortable Environment"
                  },
                  {
                  name: "3",
                  src: require("@/assets/zmd-2.jpg"),
                  title: "Convenient to Work"
                  },
                  {
                  name: "4",
                  src: require("@/assets/zmd-3.jpg"),
                  title: "Safe and Assured"
                  },
                  {
                  name: "5",
                  src: require("@/assets/zmd-4.jpg"),
                  title: "Prosperous Surroundings"
                  },
                  {
                  name: "6",
                  src: require("@/assets/zmd-5.jpg"),
                  title: "Flexible Decoration Style"
                  }
              ],
              clientWidth: document.body.clientWidth
          };
          
      },
      mounted() {
          const that = this
          window.onresize = () => {
            return (() => {
              window.screenWidth = document.body.clientWidth
              that.clientWidth = window.screenWidth
            })()
          }
        },
      watch: {
        clientWidth(val) {
          if (!this.timer) {
            this.clientWidth = val
            this.timer = true
            let that = this
            setTimeout(function() {
              console.log(that.clientWidth)
              that.timer = false
            }, 400)
          }
        }
    },

    methods: {
      route1 () {
        this.$router.push('/Chat')
      },
      route2 () {
        this.$router.push('/recommend')
      },
      route3 () {
        this.$router.push('/house')
      }

  }
    }
    
</script>
