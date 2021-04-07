import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import HouseList from "../components/HouseList"
import Recommend from "../components/Recommend"
import Chat from "../components/Chat";



Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/Chat',
    name: 'Chat',
    component: Chat
  },
  // {
  //   path: '/Chat',
  //   name: 'Chat',
  //   component: Chat
  // },
  {
    path: '/house',
    name: 'house',
    component: HouseList
  },
  {
    path: '/recommend',
    name: 'recommend',
    component: Recommend
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
