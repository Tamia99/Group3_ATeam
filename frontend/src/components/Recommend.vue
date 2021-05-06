<template>
    <div>
      <div v-if="status == '0'">
          <el-row>
            <el-col :span="12">
                <img src="frontend/src/assets/zmd-1.jpg">
            </el-col>
            <el-col :span="12">
                
            </el-col>
          </el-row>
        
        <h1>Oops!There are no recommendations now.You can go to chat with the assistant or view  all house informations</h1>
        <router-link to="/chat">chat with our smart assistant</router-link>
        <br>
        <router-link to="/house">view all houses</router-link>
      </div>
      <div v-if="status != '0'">
        <h1>Here to see recommendations for you</h1>
        <el-row gutter="20" >
          <el-col :span="6" v-for="item in houses" :key="item.id">
            <el-card :body-style="{ padding: '20px' }" shadow ="hover" @click.native = "openDetail(item.id)">
                <img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2287568211,2342036693&fm=26&gp=0.jpg" class="image">
                <div style="padding: 14px;">
                    <!--<h2>Price: $2000</h2>
                    <span>1 bd, 1 ba, 288 sqft</span>
                    <br>
                    <span>neighborhood</span>-->
                    <h2>{{item.price}}</h2>
                    <span>{{ item.room }}</span>
                    <br>
                    <span>{{ item.neighborhood }}</span>
                    <br>
                    <span>{{ item.type }}</span>
                    <!-- <div class="bottom clearfix">
                        <el-button type="text" class="button">View Details</el-button>
                    </div> -->
                </div>
            </el-card>
            <el-dialog
                :visible.sync="dialogVisible"
                width="80%"
                height="60%"
                :before-close="handleClose">
                <!--<div style="width:500px">
                <img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2287568211,2342036693&fm=26&gp=0.jpg" class="image">
                </div>
                <span>这是一段信息</span>-->
                <Detail :message = "thisHouse"></Detail>
                <!-- <el-button @click="similar()">View 10 similar houses</el-button> -->
                <!--<span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
                </span>-->
            </el-dialog>
        </el-col>
      </el-row>
      <!--<el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-size="12"
                :page-sizes="[12, 24, 36, 48]"
                layout="total,sizes, prev, pager, next, jumper"
                :total="currentTotal">
      </el-pagination>-->
      <div v-if="this.houses.length!=0">
        <p>Please rate for the recommendation</p>
        <el-rate
          v-model="value"
          :colors="['#99A9BF', '#F7BA2A', '#FF9900']">
        </el-rate>
      </div>
        </div>
    </div>

</template>

<script>
    import axios from "axios";
    import HouseDetail from "@/components/HouseDetail";
    export default{
        name: "Recommend.vue",
        components: {Detail: HouseDetail},
        data() {
            return {
              currentTotal: 0,
              currentPage: 1,
              pageSize: 12,
              houses: [],
              dialogVisible: false,
              houseId:0,
              details:[],
              thisHouse:[],
              value: null,
              status:this.$store.state.status,
              iconClasses: ['icon-rate-face-1', 'icon-rate-face-2', 'icon-rate-face-3'], // 等同于 { 2: 'icon-rate-face-1', 4: { value: 'icon-rate-face-2', excluded: true }, 5: 'icon-rate-face-3' }
            }
        },
        created:function(){
            // alert("1")
            this.getList()
            /*alert(this.$store.state.status)*/
            this.status = this.$store.state.status
            // alert (this.houses[1])
        },
        updated() {
        //   this.status = this.$store.state.status
        //   this.getList()
        //   alert("2")
        },
        watched(){
        //    this.status = this.$store.state.status
        //    this.getList()
        //   alert("3")
        },
      mounted:function(){

        },
      computed: {

        },
        methods:{
            getList(){
                /*this.tableData.push({id:"all[i][0]",price:"p",room:"r",area:"a",neighborhood:"n",type:"t"})*/
                let all = this.$store.state.recommendation
                this.details = all
                // alert(all)
                let i = 0
                while (i<all.length){
                    let iD = all[i][0]
                    let p = all[i][80]
                    let a = all[i][4]/*mianji*/
                    let n = all[i][12]
                    let t = all[i][2]
                    let bd = all[i][51]/*bedroom*/
                    let ba = all[i][50]*0.5+all[i][49]/*bathroom*/
                    let r = a.toString() + " sqft"
                    if (ba == 1 || ba == 0){
                        r = ba.toString() + " ba " + r
                    }
                    else{
                        r = ba.toString() + " ba " + r
                    }
                    if (bd == 1||bd==0){
                        r = bd.toString() + " bd " + r
                    }
                    else{
                        r = bd.toString() + " bds " + r
                    }
                    if (n == "Blmngtn"){
                        n = "Bloomington Heights"
                    }
                    else if (n == "Blueste"){
                        n = "Bluestem"
                    }
                    else if (n == "BrDale"){
                        n = "Briardale"
                    }
                    else if (n == "BrkSide"){
                        n = "Brookside"
                    }
                    else if (n == "ClearCr"){
                        n = "Clear Creek"
                    }
                    else if (n == "CollgCr"){
                        n = "College Creek"
                    }
                    else if (n == "Crawfor"){
                        n = "Crawford"
                    }
                    else if (n == "Edwards"){
                        n = "Edwards"
                    }
                    else if (n == "Gilbert"){
                        n = "Gilbert"
                    }
                    else if (n == "IDOTRR"){
                        n = "Iowa DOT and Rail Road"
                    }
                    else if (n == "MeadowV"){
                        n = "Meadow Village"
                    }
                    else if (n == "Mitchel"){
                        n = "Mitchell"
                    }
                    else if (n == "NAmes"){
                        n = "North Ames"
                    }
                    else if (n == "NoRidge"){
                        n = "Northridge"
                    }
                    else if (n == "NPkVill"){
                        n = "Northpark Villa"
                    }
                    else if (n == "NridgHt"){
                        n = "Northridge Heights"
                    }
                    else if (n == "NWAmes"){
                        n = "Northwest Ames"
                    }
                    else if (n == "OldTown"){
                        n = "Old Town"
                    }
                    else if (n == "SWISU"){
                        n = "South & West of Iowa State University"
                    }
                    else if (n == "Sawyer"){
                        n = "Sawyer"
                    }
                    else if (n == "SawyerW"){
                        n = "Sawyer West"
                    }
                    else if (n == "Somerst"){
                        n = "Somerset"
                    }
                    else if (n == "StoneBr"){
                        n = "Stone Brook"
                    }
                    else if (n == "Timber"){
                        n = "Timberland"
                    }
                    else if (n == "Veenker"){
                        n = "Veenker"
                    }

                    if (t == "A"){
                        t = "Agriculture"
                    }
                    else if (t == "C"){
                        t = "Commercial"
                    }
                    else if (t == "FV"){
                        t = "Floating Village Residential"
                    }
                    else if (t == "I"){
                        t = "Industrial"
                    }
                    else if (t == "RH"){
                        t = "Residential High Density"
                    }
                    else if (t == "RL"){
                        t = "Residential Low Density"
                    }
                    else if (t == "RP"){
                        t = "Residential Low Density Park"
                    }
                    else if (t == "RM") {
                        t = "Residential Medium Density"
                    }
                    p = "$"+p
                    this.houses.push({id:iD,price:p,room:r,neighborhood:n,type:t})
                    i++
                }
                // alert(this.houses)

            },
            openDetail(id){
                this.houseId = id
                let i = 0
                /*alert(this.houseId)*/
                while(i<this.details.length){
                    // alert(this.details[i][0])
                    if (id == this.details[i][0]){
                        this.thisHouse = this.details[i]
                    }
                    i++
                }
                
                this.dialogVisible = true
            }
        }
    }
</script>
<style scoped>
.image {
    width: 100%;
    display: block;
  }

.el-row {
    margin-bottom: 20px;
    display: flex;
    flex-wrap: wrap
  }

.el-card {
    min-width: 100%;
    height: 100%;
  }
</style>