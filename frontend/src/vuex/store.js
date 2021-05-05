
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    // 定义状态
    state: {
        author: 'group 3 A Team',
        recommendation:[],
        status: "0"//0为未推荐，1为已在聊天界面推荐，2为从详情页找10个相似
    },
    mutations:{
        newRecommendation (state,msg){
            state.recommendation = msg
        },
        newStatus(state,msg){
            state.status = msg
        }
    }
})

export default store