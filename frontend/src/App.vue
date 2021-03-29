<template>

  
  <el-container>
    <el-header>
    
  

    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect"
    background-color="#545c64"
    text-color="#fff"
    active-text-color="#ffd04b">
  <el-menu-item index="1" @click="route1">Smart Chatting</el-menu-item>
  <el-menu-item index="2" @click="route2">Recommendation</el-menu-item>
  <el-menu-item index="3" @click="route3">House Resources</el-menu-item>
    
  
</el-menu>
<div class="line"></div>


</el-header>


    <el-container>
      


      <el-main>
        <div id="app">
          <div id="nav">
            <router-link to="/">Home</router-link> |
            <!-- <router-link to="/chat">Chat</router-link> -->
          </div>
          <router-view/>
        </div>
      </el-main>
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
}
</style>


<script>
 
export default {
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



