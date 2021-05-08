

<template>
  <div>




<el-container>
  <el-header style="height: 80%!important;">

    <!-- <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect">
      <img height=70px src="./assets/teamlogo.png" style="padding-left:20px">
      
      </el-menu> -->
    <el-menu
      :default-active="activeIndex2"
      class="el-menu-demo"
      mode="horizontal"
      @select="handleSelect"
      
      text-color="#545c64"
      active-text-color="#ffd04b"
      style="margin-top:-0.5%; margin-bottom:-3%!important">
      <!-- background-color="#545c64" -->
        <!-- <img src="./assets/teamlogo.png"> -->
        <img height=70px src="./assets/teamlogo-black.png" style="padding-left:630px; margin-bottom:-1%; margin-right:0%!important;">
        <el-menu-item index="1" @click="route4"><i class="el-icon-s-home"></i></el-menu-item>
        <el-menu-item index="2" @click="route1 " style="font-weight:bold;"><i class="el-icon-chat-square"></i>Assistant</el-menu-item>
          
        <el-menu-item index="3" @click="route2"><i class="el-icon-aim"></i>Recommendations</el-menu-item>
        <el-menu-item index="4" @click="route3"><i class="el-icon-house"></i>Houses</el-menu-item>

        
      </el-menu>
      
  </el-header>
      <el-main class="main-part" >
        <div id="app">
          <keep-alive>
            <router-view v-if="$route.meta.keepAlive"></router-view>
          </keep-alive>
            <router-view v-if="!$route.meta.keepAlive"></router-view>
        </div>
      </el-main>
      <el-footer>
        
      </el-footer>
  <!-- <el-footer><img src="./assets/footer.png"></el-footer> -->
</el-container>
    
    
    

<!-- 
    <el-container>
        
        <el-header>
          <img src="./assets/header2.png">
        </el-header>
        <el-container>

          <el-aside width="200px" class="aside">
            <el-col :span="50">
              <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                background-color="#003A44"
                text-color="#fff"
                active-text-color="#ffd04b">
                
                <el-menu-item index="1" @click="route1">
                  <i class="el-icon-chat-square"></i>
                  Smart Chatting
                </el-menu-item>
                <el-menu-item index="2" @click="route2">
                  <i class="el-icon-aim"></i>
                  <span slot="title">Recommendations</span>
                </el-menu-item>
                <el-menu-item index="3" @click="route3">
                  <i class="el-icon-house"></i>
                  <span slot="title">Housing Resourses</span>
                </el-menu-item>
                <el-menu-item index="4">
                </el-menu-item>
              </el-menu>
            </el-col>
          </el-aside>
          <el-container>
            <el-main class="main-part">
              <div id="app">
            
              <router-view/>
              </div>
          </el-main>
            
          </el-container>
          
        </el-container>
      <el-footer><img src="./assets/footer.png"></el-footer>

      
  </el-container> -->

  </div>
</template>

<style>
  /* .el-container{
    background:  #66A4AC;
  }
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 60px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.el-menu-item{
  font-size: 20px;
  padding-left: 0%;
}

.el-menu-vertical-demo{
  height: 800px!important;
}

.main-part{
  margin-top: -2%;
}

.header{
  height:200%;
  width: 100%;
  padding-left: -100%;
}

.el-menu-demo{
  padding-left: -100%!important;
}

.el-header{
  justify-content: space-between;
  padding-left: 0%!important;
  height: 5%!important;
  width: 200px!important;
}

.el-footer{
  padding-top: 0.1%!important;
  padding-left: 0%!important;
}

.el-main{
  padding-top: 4%!important;
}

.el-aside{
  margin-top: -0.2%!important;
}
*/

.el-footer{
  padding-top: 0.1%!important;
  padding-left: 0%!important;
  padding-right: 0%!important;
  
}

.el-header{
  
  padding-left: 0%!important;
  padding-right: 0%!important;
  
  /* height: 120px!important; */
}

.el-menu{
  height: 80%!important;
}

.el-menu-item{
  font-size: 14px!important;
  /* display: flex; */
}

</style>


<script>
 
export default{
  
  methods: {
    route1 () {
      this.$router.push('/Chat')
    },
    route2 () {
      this.$router.push('/recommend')
    },
    route3 () {
      this.$router.push('/house')
    },
    route4 () {
      this.$router.push('/welcome')
    }

  }
  

}


</script>





