<template>
    <div id = "q">
      
        <!-- <el-steps :active="active" finish-status="success">
            <el-step title="步骤 1">

                

            </el-step>
            


            <el-step title="步骤 2">



            </el-step>



            <el-step title="步骤 3">



            </el-step>
        </el-steps>

        <el-button style="margin-top: 12px;" @click="next">下一步</el-button>
 -->




        <h1>Here is the questions page</h1><br>
        <el-form ref="form" :model="form" label-width="80px">
            <el-form-item >
                <span>Q1 Please identifies the general zoning classification.</span><br>
                <el-select v-model="form.classification" placeholder="please choose">
                    <el-option
                            v-for="item in form.classifications"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="">
                <span>Q2 What size of house do you want?(sqft)</span>
                <el-input v-model="form.inputSize" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item>
                <span>Q3 Please choose the flatness property.</span><br>
                <el-select v-model="form.flatness" placeholder="please choose">
                    <el-option
                            v-for="item in form.flatnesses"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>

            <el-form-item>
                <span>Q4 Please choose type of utilities.</span><br>
                <el-select v-model="form.utility" placeholder="please choose">
                    <el-option
                            v-for="item in form.utilities"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q5 Please choose the neighborhood.</span><br>
                <el-select v-model="form.neighborhood" placeholder="please choose">
                    <el-option
                            v-for="item in form.neighborhoods"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q6 Please choose the style of dwelling.</span><br>
                <el-select v-model="form.style" placeholder="please choose">
                    <el-option
                            v-for="item in form.styles"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q7 Which year do you prefer the house had been built?</span><br>
                <el-date-picker
                        v-model="form.year"
                        type="year"
                        placeholder="choose year"
                        format="yyyy"
                        value-format="yyyy">
                </el-date-picker>
            </el-form-item>
            <el-form-item>
                <span>Q8 Please choose the type of roof.</span><br>
                <el-select v-model="form.roof" placeholder="please choose">
                    <el-option
                            v-for="item in form.roofs"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q9 Please choose the type of masonry veneer.</span><br>
                <el-select v-model="form.vaneer" placeholder="please choose">
                    <el-option
                            v-for="item in form.vaneers"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q10 Please choose the type of foundation.</span><br>
                <el-select v-model="form.foundation" placeholder="please choose">
                    <el-option
                            v-for="item in form.foundations"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="">
                <span>Q11 What size of basement do you want?</span>
                <el-input v-model="form.basement" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item>
                <span>Q12 Please choose the type of heating.</span><br>
                <el-select v-model="form.heating" placeholder="please choose">
                    <el-option
                            v-for="item in form.heatings"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item >
                <span>Q13 Do you want a central air conditioning?</span><br>
                <el-select v-model="form.air" placeholder="please choose">
                    <el-option
                            v-for="item in form.airs"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item >
                <span>Q14 Please choose the type of electrical system.</span><br>
                <el-select v-model="form.electrical" placeholder="please choose">
                    <el-option
                            v-for="item in form.electricals"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="">
                <span>Q15 What size of above grade (ground) living area do you want?</span>
                <el-input v-model="form.living" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item>
                <span>Q16 How many full bathrooms do you want?</span><br>
                <el-input-number v-model="form.fullbath" @change="handleChange" :min="0" :max="10" label="full bathroom"></el-input-number>
            </el-form-item>
            <el-form-item>
                <span>Q17 How many half bathrooms do you want?</span><br>
                <el-input-number v-model="form.halfbath" @change="handleChange" :min="0" :max="10" label="half bathroom"></el-input-number>
            </el-form-item>
            <el-form-item>
                <span>Q18 How many bedrooms(above ground) do you want?</span><br>
                <el-input-number v-model="form.bedroom" @change="handleChange" :min="0" :max="10" label="bedroom"></el-input-number>
            </el-form-item>
            <el-form-item>
                <span>Q19 How many kitchens(above ground) do you want?</span><br>
                <el-input-number v-model="form.kitchen" @change="handleChange" :min="0" :max="10" label="kitchen"></el-input-number>
            </el-form-item>
            <el-form-item>
                <span>Q20 How many rooms(total rooms above ground) do you want?</span><br>
                <el-input-number v-model="form.room" @change="handleChange" :min="0" :max="30" label="room" ></el-input-number>
            </el-form-item>
            <el-form-item>
                <span>Q21 How many fire places do you want?</span><br>
                <el-input-number v-model="form.fire" @change="handleChange" :min="0" :max="5" label="fire"></el-input-number>
            </el-form-item>
            <el-form-item label="">
                <span>Q22 What size of garage in car capacity do you want?</span><br>
                <el-input-number v-model="form.garage" @change="handleChange" :min="0" :max="10" label="garage"></el-input-number>
            </el-form-item>
            <el-form-item >
                <span>Q23 Do you want a wood deck?</span><br>
                <el-select v-model="form.deck" placeholder="please choose">
                    <el-option
                            v-for="item in form.decks"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item >
                <span>Q24 Do you want a pool?</span><br>
                <el-select v-model="form.pool" placeholder="please choose">
                    <el-option
                            v-for="item in form.pools"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item label="">
                <span>Q25 What price of house do you prefer?</span>
                <el-input v-model="form.price" placeholder="please enter"></el-input>
            </el-form-item>
        </el-form>
        <!-- <p>
            Copyright&nbsp;&copy;&nbsp;{{author}} - 2021 All rights reserved
        </p> -->

    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Questions.vue",
        props:['message'],
        data() {
            return {
                qtype: this.message[0],
                information:[],
                visible:undefined,
                // active: 0,
                form: {
                    classification:"",
                    inputSize:"",
                    flatness:"",
                    utility:"",
                    neighborhood:"",
                    style:"",
                    year:undefined,
                    roof:"",
                    vaneer:"",
                    foundation:"",
                    basement:"",
                    heating:"",
                    air:"",
                    electrical:"",
                    living:"",
                    fullbath:undefined,
                    halfbath:undefined,
                    bedroom:undefined,
                    kitchen:undefined,
                    room:undefined,
                    fire:undefined,
                    garage:undefined,
                    deck:"",
                    pool:"",
                    price:"",
                    classifications: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'A',
                        label: 'Agriculture'
                    }, {
                        value: 'C',
                        label: 'Commercial'
                    }, {
                        value: 'FV',
                        label: 'Floating Village Residential'
                    }, {
                        value: 'I',
                        label: 'Industrial'
                    }, {
                        value: 'RH',
                        label: 'Residential High Density'
                    },{
                        value: 'RL',
                        label: 'Residential Low Density'
                    },{
                        value: 'RP',
                        label: 'Residential Low Density Park'
                    },{
                        value: 'RM',
                        label: 'Residential Medium Density'
                    },
                    ],
                    flatnesses: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'Lvl',
                        label: 'Near Flat/Level'
                    }, {
                        value: 'Bnk',
                        label: 'Banked - Quick and significant rise from street grade to building'
                    }, {
                        value: 'HLF',
                        label: 'Hillside - Significant slope from side to side'
                    }, {
                        value: 'Low',
                        label: 'Depression'
                    },
                    ],
                    utilities: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'AllPub',
                        label: 'All public Utilities (E,G,W,& S)'
                    }, {
                        value: 'NoSewr',
                        label: 'Electricity, Gas, and Water (Septic Tank)'
                    }, {
                        value: 'NoSeWa',
                        label: 'Electricity and Gas Only'
                    }, {
                        value: 'ELO',
                        label: 'Electricity only'
                    },
                    ],
                    neighborhoods: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'Blmngtn',
                        label: 'Bloomington Heights'
                    }, {
                        value: 'Blueste',
                        label: 'Bluestem'
                    }, {
                        value: 'BrDale',
                        label: 'Briardale'
                    }, {
                        value: 'BrkSide',
                        label: 'Brookside'
                    },{
                        value: 'ClearCr',
                        label: 'Clear Creek'
                    }, {
                        value: 'CollgCr',
                        label: 'College Creek'
                    }, {
                        value: 'Crawfor',
                        label: 'Crawford'
                    }, {
                        value: 'Edwards',
                        label: 'Edwards'
                    },{
                        value: 'Gilbert',
                        label: 'Gilbert'
                    }, {
                        value: 'IDOTRR',
                        label: 'Iowa DOT and Rail Road'
                    }, {
                        value: 'MeadowV',
                        label: 'Meadow Village'
                    }, {
                        value: 'Mitchel',
                        label: 'Mitchell'
                    },{
                        value: 'Names',
                        label: 'North Ames'
                    }, {
                        value: 'NoRidge',
                        label: 'Northridge'
                    }, {
                        value: 'NPkVill',
                        label: 'Northpark Villa'
                    }, {
                        value: 'NridgHt',
                        label: 'Northridge Heights'
                    },{
                        value: 'NWAmes',
                        label: 'Northwest Ames'
                    }, {
                        value: 'OldTown',
                        label: 'Old Town'
                    }, {
                        value: 'SWISU',
                        label: 'South & West of Iowa State University'
                    }, {
                        value: 'Sawyer',
                        label: 'Sawyer'
                    },{
                        value: 'SawyerW',
                        label: 'Sawyer West'
                    }, {
                        value: 'Somerst',
                        label: 'Somerset'
                    }, {
                        value: 'StoneBr',
                        label: 'Stone Brook'
                    }, {
                        value: 'Timber',
                        label: 'Timberland'
                    },{
                        value: 'Veenker',
                        label: 'Veenker'
                    },
                    ],
                    styles: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: '1Story',
                        label: 'One Story'
                    }, {
                        value: '1.5Fin',
                        label: 'One and one-half story: 2nd level finished'
                    }, {
                        value: '1.5Unf',
                        label: 'One and one-half story: 2nd level unfinished'
                    }, {
                        value: '2Story',
                        label: 'Two story'
                    }, {
                        value: '2.5Fin',
                        label: 'Two and one-half story: 2nd level finished'
                    },{
                        value: '2.5Unf',
                        label: 'Two and one-half story: 2nd level unfinished'
                    },{
                        value: 'SFoyer',
                        label: 'Split Foyer'
                    },{
                        value: 'SLvl',
                        label: 'Split Level'
                    },
                    ],
                    roofs: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'Flat',
                        label: 'Flat'
                    }, {
                        value: 'Gable',
                        label: 'Gable'
                    }, {
                        value: 'Gambrel',
                        label: 'Gabrel (Barn)'
                    }, {
                        value: 'Hip',
                        label: 'Hip'
                    }, {
                        value: 'Mansard',
                        label: 'Mansard'
                    },{
                        value: 'Shed',
                        label: 'Shed'
                    },
                    ],
                    vaneers: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'BrkCmn',
                        label: 'Brick Common'
                    }, {
                        value: 'BrkFace',
                        label: 'Brick Face'
                    }, {
                        value: 'CBlock',
                        label: 'Cinder Block'
                    }, {
                        value: 'None',
                        label: 'None'
                    }, {
                        value: 'Stone',
                        label: 'Stone'
                    },
                    ],
                    foundations: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'BrkTil',
                        label: 'Brick & Tile'
                    }, {
                        value: 'CBlock',
                        label: 'Cinder Block'
                    }, {
                        value: 'PConc',
                        label: 'Poured Contrete'
                    }, {
                        value: 'Slab',
                        label: 'Slab'
                    }, {
                        value: 'Stone',
                        label: 'Stone'
                    },{
                        value: 'Wood',
                        label: 'Wood'
                    },
                    ],
                    heatings: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'Floor',
                        label: 'Floor Furnace'
                    }, {
                        value: 'GasA',
                        label: 'Gas forced warm air furnace'
                    }, {
                        value: 'GasW',
                        label: 'Gas hot water or steam heat'
                    }, {
                        value: 'Grav',
                        label: 'Gravity furnace'
                    }, {
                        value: 'OthW',
                        label: 'Hot water or steam heat other than gas'
                    },{
                        value: 'Wall',
                        label: 'Wall furnace'
                    },
                    ],
                    airs: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 0,
                        label: 'No'
                    }, {
                        value: 1,
                        label: 'Yes'
                    },
                    ],
                    electricals: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 'SBrkr',
                        label: 'Standard Circuit Breakers & Romex'
                    }, {
                        value: 'FuseA',
                        label: 'Fuse Box over 60 AMP and all Romex wiring (Average)'
                    }, {
                        value: 'FuseF',
                        label: '60 AMP Fuse Box and mostly Romex wiring (Fair)'
                    }, {
                        value: 'FuseP',
                        label: '60 AMP Fuse Box and mostly knob & tube wiring (poor)'
                    }, {
                        value: 'Mix',
                        label: 'Mixed'
                    },
                    ],
                    decks: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 0,
                        label: 'No'
                    }, {
                        value: 1,
                        label: 'Yes'
                    },
                    ],
                    pools: [{
                        value: -1,
                        label: 'It does not matter'
                    },{
                        value: 0,
                        label: 'No'
                    }, {
                        value: 1,
                        label: 'Yes'
                    },
                    ],
                },
            }
        },
        computed: {
            author () {
                return this.$store.state.author
            }
        },
        created() {
          /*alert(this.qtype)*/
          this.qtype = this.message[0]
          this.getInformation()

        },
      methods: {
            getInformation(){
              /*this.form.inputSize = 1*/
              /*this.form.classification = this.form.classifications[0].value*/
              if (this.qtype==0||this.qtype==2){
                /*this.form.inputSize = 1*/
                if(this.message[18]===-1){
                  this.form.bedroom = undefined
                }
                else{
                  this.form.bedroom = this.message[18]
                }
                if(this.message[16]===-1){
                  this.form.fullbath = undefined
                }
                else{
                  this.form.fullbath = this.message[16]
                }
                if(this.message[17]===-1){
                  this.form.halfbath = undefined
                }
                else{
                  this.form.halfbath = this.message[17]
                }
                if(this.message[19]===-1){
                  this.form.kitchen = undefined
                }
                else{
                  this.form.kitchen = this.message[19]
                }
                if(this.message[22]===-1){
                  this.form.garage = undefined
                }
                else{
                  this.form.garage = this.message[22]
                }
                if(this.message[21]===-1){
                  this.form.room = undefined
                }
                else{
                  this.form.room = this.message[21]
                }
                this.form.inputSize = this.message[2]
               /* this.form.bedroom = this.message[18]
                this.form.fullbath = this.message[16]
                this.form.halfbath = this.message[17]
                this.form.kitchen = this.message[19]
                this.form.garage = this.message[23]
                this.form.room = this.message[21]*/
                this.form.price = this.message[25]
                /*alert(this.message[5])*/
                for (let i=0;i<this.form.neighborhoods.length;i++){
                  if (this.message[5]==this.form.neighborhoods[i].value||this.message[5]==""){
                    this.form.neighborhood = this.message[5]
                  }
                }
                for (let i=0;i<this.form.utilities.length;i++){
                  if (this.message[4]==this.form.utilities[i].value||this.message[4]==""){
                    this.form.utility = this.message[4]
                  }
                }
                for (let i=0;i<this.form.styles.length;i++){
                  if (this.message[6]==this.form.styles[i].value||this.message[6]==""){
                    this.form.style = this.message[6]
                  }
                }
                for (let i=0;i<this.form.heatings.length;i++){
                  if (this.message[12]==this.form.heatings[i].value||this.message[12]==""){
                    this.form.heating = this.message[12]
                  }
                }
                for (let i=0;i<this.form.airs.length;i++){
                  if (this.message[13]==this.form.ais[i].value||this.message[13]==""){
                    this.form.air = this.message[13]
                  }
                }
                /*alert(this.form.room)*/
                /*this.form.neighborhood = this.message[5]*/
              }
            },
            handleChange(value) {
                console.log(value);
            },
            realrecommend(data){
              const path = 'http://localhost:5000/api/recommend'
                axios.post(path, data)
                    .then(response => {
                       /* alert("successful submission")*/

                        let all = response.data.result
                        this.$store.commit("newRecommendation",all)
                        this.$store.commit("newStatus","1")
                        /*alert(this.$store.state.status)*/
                        console.log(this.$store.state.recommendation)
                        this.visible = false
                        this.$notify({
                          title: 'Success',
                          message: 'successful submission',
                          type: 'success'
                        });
                        /*alert("successful submission")*/
                    })
                    .catch((error) => {
                        // eslint-disable-next-line
                        console.log(error)

                    })
            },
            recommend(){
              /*alert(typeof this.form.room)*/

                let data = [this.form.classification,this.form.inputSize,this.form.flatness,this.form.utility,this.form.neighborhood,
                            this.form.style,this.form.year,this.form.roof,this.form.vaneer,this.form.foundation,this.form.basement,
                            this.form.heating,this.form.air,this.form.electrical,this.form.living,this.form.fullbath,this.form.halfbath,
                            this.form.bedroom,this.form.kitchen,this.form.room,this.form.fire,this.form.garage,this.form.deck,
                            this.form.pool,this.form.price]
                let invalidcount = 0
                /*alert(this.form.deck)*/
                for(let i = 0;i<data.length;i++){
                  if (data[i]===undefined || data[i]===""||data[i]=== -1){
                    /*console.log("in",data[i])*/
                    data[i]= -1
                    invalidcount++
                  }
                }
                /*alert(invalidcount)*/
                if (invalidcount>19){
                    this.$confirm('Sorry, information provided is not enough! Lack of information may lead to inaccurate recommendations, do you confirm to continue recommendation ?', '', {
                      confirmButtonText: 'confirm',
                      cancelButtonText: 'no,I will provide more information',
                      type: 'warning'
                      }).then(() => {
                        this.visible = false
                        /*this.realrecommend(data)*/
                        this.visible = false
                        /*return this.visible*/
                        /*this.recommend()*/
                      }).catch(() => {
                        this.visible = true
                        /*return this.visible*/
                    });
                }
                else {
                  /*this.realrecommend(data)*/
                  this.visible = false
                }
                return this.visible
            }
            // next() {
            //     this.active++;
            // }
        }
    }
</script>

<style scoped>
.el-select{
    background: #ffffff !important;
    color: #ffffff !important;
}

</style>