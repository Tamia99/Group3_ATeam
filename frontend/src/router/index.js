import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import HouseList from "../components/HouseList"
import Recommend from "../components/Recommend"
import Chat from "../components/Chat";
import Welcome from "../Welcome";




Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Welcome',
    component: Welcome
  },
  {
    path: '/welcome',
    name: 'Welcome',
    component: Welcome
  },
  // {
  //   path: '/about',
  //   name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  // },
  {
    path: '/Chat',
    name: 'Chat',
    component: Chat,
    meta:{
      keepAlive:true
    }
  },
  // {
  //   path: '/Chat',
  //   name: 'Chat',
  //   component: Chat
  // },
  {
    path: '/house',
    name: 'house',
    component: HouseList,
    meta:{
      keepAlive:true
    }
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: Recommend,

  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
