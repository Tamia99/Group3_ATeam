
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    // 定义状态
    state: {
        author: 'group 3 A Team',
        recommendation:[],
        status: "1"
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