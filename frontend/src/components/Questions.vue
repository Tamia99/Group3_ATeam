<template>
    <div>
        <h1>Here is the questions page</h1><br>
        <el-form ref="form" :model="form" label-width="80px">
            <el-form-item>
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
                <span>Q2 What size of house do you want?</span>
                <el-input v-model="form.inputSize" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item>
                <span>Q3 Please choose the flatness property.</span><br>
                <el-select v-model="form.flatness" placeholder="please choose">
                    <el-option
                            v-for="item in form.flatnessP"
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
                <el-input-number v-model="form.room" @change="handleChange" :min="0" :max="30" label="room"></el-input-number>
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
        <p>
            Copyright&nbsp;&copy;&nbsp;{{author}} - 2016 All rights reserved
        </p>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        name: "Questions.vue",
        data() {
            return {
                form: {
                    classification:"",
                    inputSize: '',
                    flatness:"",
                    utility:"",
                    neighborhood:"",
                    style:"",
                    year:"",
                    roof:"",
                    vaneer:"",
                    foudation:"",
                    basement:"",
                    heating:"",
                    air:"",
                    electrical:"",
                    living:"",
                    fullbath:"",
                    halfbath:"",
                    bedroom:"",
                    kitchen:"",
                    room:"",
                    fire:"",
                    garage:"",
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
                    flatnessP: [{
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
        methods: {
            handleChange(value) {
                console.log(value);
            },
            recommend(){
                let data = [this.form.classification,this.form.inputSize,this.form.flatness,this.form.utility,this.form.neighborhood,
                            this.form.style,this.form.year,this.form.roof,this.form.vaneer,this.form.foudation,this.form.basement,
                            this.form.heating,this.form.air,this.form.electrical,this.form.living,this.form.fullbath,this.form.halfbath,
                            this.form.bedroom,this.form.kitchen,this.form.room,this.form.fire,this.form.garage,this.form.deck,
                            this.form.pool,this.form.price]
               /* alert(data)*/
                const path = 'http://localhost:5000/api/recommend'
                axios.post(path, data)
                    .then(response => {
                       /* alert("successful submission")*/

                        let all = response.data.result
                        this.$store.commit("newRecommendation",all)
                        this.$store.commit("newStatus","0")
                        /*alert(this.$store.state.status)*/
                        console.log(this.$store.state.recommendation)
                        /*alert("successful submission")*/
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