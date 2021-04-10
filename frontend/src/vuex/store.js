
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
    // 定义状态
    state: {
        author: 'group 3 A Team',
        recommendation:[]
    },
    mutations:{
        newRecommendation (state,msg){
            state.recommendation = msg
        }
    }
})

export default store