

<template>

    <el-container>
        <!-- <el-header class='el-header-horizontal'><img src="./assets/header.png" class='header'></el-header> -->
        <el-header>
          <img src="./assets/header.png">
        </el-header>
        <el-container>

          <el-aside width="200px" class="aside">
            <el-col :span="50">
              <el-menu
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b">
                <!-- <el-menu-item index="1" disabled> -->
                  
                  
                <!-- </el-menu-item> -->
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
            <!-- <div id="nav">
              <router-link to="/">Home</router-link> |
              
            </div> -->
              <router-view/>
              </div>
          </el-main>
            <el-footer>Footer</el-footer>
          </el-container>
        </el-container>
      

      
  </el-container>
  
</template>

<style>
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
  /* padding-left: -20%!important; */
}

.main-part{
  margin-top: -2%;
}

.header{
  height:200%;
  width: 100%;
  padding-left: -100%;
  /* display: flex; */
}

.el-menu-demo{
  padding-left: -100%!important;
}

.el-header{
  justify-content: space-between;
  padding-left: 0%!important;
  height: 5%!important;
}

/* .el-aside{
  position: absolute;
}

.el-main{
  position: absolute;
} */


</style>


<script>
 
export default{
  
  methods: {
    route1 () {
      this.$router.push('/chat')
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





