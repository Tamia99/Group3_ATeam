<template>
<div>
  <p>house detail</p>
  <p>{{message}}</p>
  <p>{{detail}}</p>
</div>
</template>

<script>
import axios from "axios";

export default {
  name: "HouseDetail.vue",
  props:['message'],
  data(){
    return {
      detail:[],
    }

  },
  created:function(){
    this.getDetail()
  },
  methods:{
    getDetail(){
      const path = 'http://localhost:5000/api/houseDetail'
      let data = [this.message]
      axios.post(path, data)
          .then(response => {

          })
          .catch((error) => {
            // eslint-disable-next-line
            console.log(error)

          })
    }
  }
}
</script>

<style scoped>

</style>