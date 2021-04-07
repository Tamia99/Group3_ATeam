<template>

  
  
    <!-- <el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
      background-color="#545c64"
      text-color="#fff"
      active-text-color="#ffd04b">
        <el-menu-item index="1" @click="route1">Smart Chatting</el-menu-item>
        <el-menu-item index="2" @click="route2">Recommendation</el-menu-item>
        <el-menu-item index="3" @click="route3">House Resources</el-menu-item>
      </el-menu>
      <div class="line"></div>
    </el-header> -->

    <!-- <el-container>
      <el-main>
        <div id="app"> -->
            <!-- <div id="nav">
              <router-link to="/">Home</router-link> |
              
            </div> -->
          <!-- <router-view/>
        </div>
      </el-main>
    </el-container> -->
    <!-- <el-header>
        <el-menu :default-active="activeIndex" class="el-menu-demo" @select="handleSelect"
            background-color="#545c64"
            text-color="#fff"
            active-text-color="#ffd04b"
            >

        </el-menu>
        
      </el-header> -->

    <el-container>
        <el-header>header</el-header>

      
        <el-container>
          <el-aside width="200px">
            <el-col :span="50">
              <el-menu
              
                default-active="2"
                class="el-menu-vertical-demo"
                @open="handleOpen"
                @close="handleClose"
                background-color="#545c64"
                text-color="#fff"
                active-text-color="#ffd04b">
                <!-- <el-submenu index="1">
                  <template slot="title">
                    <i class="el-icon-location"></i>
                    <span>导航一</span>
                  </template> -->
                  <!-- <el-menu-item-group>
                    <template slot="title">分组一</template>
                    <el-menu-item index="1-1">选项1</el-menu-item>
                    <el-menu-item index="1-2">选项2</el-menu-item>
                  </el-menu-item-group>
                  <el-menu-item-group title="分组2">
                    <el-menu-item index="1-3">选项3</el-menu-item>
                  </el-menu-item-group>
                  <el-submenu index="1-4">
                    <template slot="title">选项4</template>
                    <el-menu-item index="1-4-1">选项1</el-menu-item> -->
                  <!-- </el-submenu> -->
                <!-- </el-submenu> -->
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
            <!-- <el-footer>Footer</el-footer> -->
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
  height: 600px!important;
}

.main-part{
  margin-top: -2%;
}


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





