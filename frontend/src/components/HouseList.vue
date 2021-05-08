<template>
  <div>
    <el-row>
      <el-col :span="6">
        <el-input
            size="small"
            placeholder= "search for blocks"
            v-model="textarea"
            clearable
            class="inputSearch"></el-input>
  	    
      </el-col>
      <el-button @click="sortandsearch()" class="buttonSearch" style="height: 8%!important" icon="el-icon-search">Search</el-button>
      <el-col :span="10"></el-col>
      <el-col :span="2">
        <p class="sortText">Sort by:</p>
      </el-col>
      <el-col :span="3">
        <el-select v-model="values" placeholder="please choose" @change="sortandsearch()" class="sortBy">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value">
          </el-option>
        </el-select>
      </el-col>
      
    </el-row>
    <el-divider></el-divider>
    <div v-if="this.houses.length==0&&this.loading==false">
      <p>No Result</p>
    </div>
    <el-row v-loading="loading" gutter="20" >
      <el-col :span="6" v-for="item in houses.slice((currentPage - 1) * pageSize, currentPage*pageSize)" :key="item.id">
            <el-card :body-style="{ paddingLeft: '20px'}" shadow ="hover" @click.native = "openDetail(item.id)" class="cards">
                <img :src="item.pic" class="image">
                <div style="padding: 14px;">
<!--                   
                    <h2>Price: $2000</h2>
                    <span>1 bd, 1 ba, 288 sqft</span>
                    <br>
                    <span>neighborhood</span>
                    <h2>{{item.id}}</h2> -->

                    <h2>{{item.price}}</h2>
                    <span>{{ item.room }}</span>
                    <br>
                    <span>{{ item.neighborhood }}</span>
                    <br>
                    <span>{{ item.type }}</span>
                   
                </div>
            </el-card>
            <el-dialog
                :visible.sync="dialogVisible"
                width="80%"
                height="60%"
                :before-close="handleClose">
                <Detail :message = "thisHouse"></Detail>
                <!--<el-button @click="similar()">View 10 similar houses</el-button>-->
            </el-dialog>
        </el-col>
    </el-row>
    <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-size="12"
                :page-sizes="[12, 24, 36, 48]"
                layout="total,sizes, prev, pager, next, jumper"
                :total="currentTotal">
    </el-pagination>


</div>
    
</template>
<script>
    import axios from "axios";
    import HouseDetail from "@/components/HouseDetail";
    export default {
      name: "houseItem.vue",
      components: {Detail: HouseDetail},
      data(){
          return{
            src:"",
            textarea:"",
            matchn:[],
            currentTotal: 0,
            currentPage: 1,
            pageSize: 12,
            /*houses:['All', 'work', 'play', 'makes', 'jack', 'dull', 'boy', ',', 'work', 'play'],*/
            houses:[],
            dialogVisible: false,
            houseId:0,
            details:[],
            thisHouse:[],
            values:"",
            loading: true,
            options: [{
              value: 1,
              label: 'price(High to low)'
            }, {
              value: 2,
              label: 'size(High to low)'
            }, {
              value: 3,
              label: 'bedroom count(High to low)'
            }, {
              value: 4,
              label: 'bathroom count(High to low)'
            },{
              value: 5,
              label: 'price(Low to High)'
            }, {
              value: 6,
              label: 'size(Low to High)'
            }, {
              value: 7,
              label: 'bedroom count(Low to High)'
            }, {
              value: 8,
              label: 'bathroom count(Low to High)'
            }, {
              value: 9,
              label: 'neighbourhood'
            }],
          }
      },
      created:function(){
        this.values = this.options[8].value
        this.getList()
      },
      /*computed:{
        getsrc(id){
              /!*return "./components/pictures/"+id+".JPG"*!/
              return "./pictures/" + id + ".jpg"
          },
      },*/
      methods:{
          getsrc(id){
              /*return "./components/pictures/"+id+".JPG"*/
              return "./pictures/" + "1.jpg"
          },
        similar(){
          this.$store.commit("newStatus","2")
          /*alert(this.$store.state.status)*/
          this.$router.push({ path:'/recommend'  })
          this.dialogVisible = false
        },
        sortandsearch(){
          //先执行排序
          /*this.houses = []
          this.getList()
          this.houses = ["nl","mkl"]*/
          //模糊搜索
          let nList = ["Bloomington Heights","Bluestem","Briardale","Brookside","Clear Creek",
            "College Creek","Crawford","Edwards","Gilbert","Iowa DOT and Rail Road","Meadow Village",
            "Mitchell","North Ames","Northridge","Northpark Villa","Northridge Heights","Northwest Ames",
            "Old Town","South & West of Iowa State University","Sawyer","Sawyer West","Somerset",
            "Stone Brook","Timberland","Veenker"]
          let n =[]
          for (var i = 0; i < nList.length; i++) {
            if (nList[i].toLowerCase().indexOf(this.textarea.toLowerCase()) >= 0) {
              let n1 = nList[i]
              if (n1 == "Bloomington Heights"){
                n1 = "Blmngtn"
              }
              else if (n1 == "Bluestem"){
                n1 = "Blueste"
              }
              else if (n1 == "Briardale"){
                n1 = "BrDale"
              }
              else if (n1 == "Brookside"){
                n1 = "BrkSide"
              }
              else if (n1 == "Clear Creek"){
                n1 = "ClearCr"
              }
              else if (n1 == "College Creek"){
                n1 = "CollgCr"
              }
              else if (n1 == "Crawford"){
                n1 = "Crawfor"
              }
              else if (n1 == "Edwards"){
                n1 = "Edwards"
              }
              else if (n1 == "Gilbert"){
                n1 = "Gilbert"
              }
              else if (n1 == "Iowa DOT and Rail Road"){
                n1 = "IDOTRR"
              }
              else if (n1 == "Meadow Village"){
                n1 = "MeadowV"
              }
              else if (n1 == "Mitchel"){
                n1 = "Mitchell"
              }
              else if (n1 == "North Ames"){
                n1 = "NAmes"
              }
              else if (n1 == "Northridge"){
                n1 = "NoRidge"
              }
              else if (n1 == "Northpark Villa"){
                n1 = "NPkVill"
              }
              else if (n1 == "Northridge Heights"){
                n1 = "NridgHt"
              }
              else if (n1 == "Northwest Ames"){
                n1 = "NWAmes"
              }
              else if (n1 == "Old Town"){
                n1 = "OldTown"
              }
              else if (n1 == "South & West of Iowa State University"){
                n1 = "SWISU"
              }
              else if (n1 == "Sawyer"){
                n1 = "Sawyer"
              }
              else if (n1 == "Sawyer West"){
                n1 = "SawyerW"
              }
              else if (n1 == "Somerset"){
                n1 = "Somerst"
              }
              else if (n1 == "Stone Brook"){
                n1 = "StoneBr"
              }
              else if (n1 == "Timberland"){
                n1 = "Timber"
              }
              else if (n1 == "Veenker"){
                n1 = "Veenker"
              }
              n.push(n1);
            }
          }
          this.matchn = n
         /* alert(this.matchn)*/
          this.houses = []
          if(this.matchn.length!=0){
            this.getList()
          }

          /*let h = []
          alert(this.houses[0].neighborhood)
          for (var i = 0;i<this.houses.length;i++){
            if(n.indexOf(this.houses[i].neighborhood) > -1){
              h.push(this.houses[i])
            }
          }
          this.houses = h*/

        },
        openDetail(id){
          this.houseId = id
          let i = 0
          while(i<this.details.length){
            if (id == this.details[i][0]){
              this.thisHouse = this.details[i]
            }
            i++
          }
          // this.thisHouse = this.thisHouse.concat(this.houses[0])
          for(let j=0;j<this.houses.length;j++){
            if (id == this.houses[j].id){
              this.thisHouse = this.thisHouse.concat(this.houses[j])
            }
          }
          this.dialogVisible = true
        },
        getList(){
            const path = 'http://localhost:5000/api/allHouses'
            let data = [this.values,this.matchn]
            axios.post(path,data)
                .then(response => {
                   /* alert("s")*/
                    let all = response.data.house;
                    let list = []
                    this.details = all
                    this.currentTotal = all.length
                    let i = 0;
                    while (i< all.length){
                        let ID = all[i][0]
                        let p = all[i][80]
                        let a = all[i][4]/*mianji*/
                        let n = all[i][12]
                        let t = all[i][2]
                        let bd = all[i][51]/*bedroom*/
                        let ba = all[i][50]*0.5+all[i][49]/*bathroom*/
                        let r = a.toString() + " sqft"
                        let src = require("../assets/pictures/" + ID + ".jpg")
                        if (ba == 1||ba == 0){
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
                        this.houses.push({id:ID,price:p,room:r,neighborhood:n,type:t,pic:src})
                        i++
                    }
                    this.loading = false
                })
                .catch(error => {
                    console.log(error)
                })
        },
        handleSizeChange(val) {
            this.pageSize = val
            console.log(`每页 ${val} 条`);
        },
        handleCurrentChange(val) {
            this.currentPage = val
            console.log(`当前页: ${val}`);
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

.buttonSearch{
  margin-left: 0.5%;
  background-color: rgb(29, 142, 180);
  color: white;
}

.inputSearch{
  margin-top: 1%;
}

.sortText{
  margin-top: 9%;
  margin-bottom: -2%;
  margin-left: 40%;
}

.sortBy{
  margin-bottom: -3%;
  margin-left: 5%;
}

/* .cards{
  border-radius: 10px;
} */


</style>

