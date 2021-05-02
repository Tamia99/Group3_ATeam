<template>
<div>
  <p>house detail</p>
  <p>{{message}}</p>
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

  methods:{

  }
}
</script>

<style scoped>

</style>