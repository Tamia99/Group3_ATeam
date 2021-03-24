<template>
    <div>
        <h1>Here is the questions page</h1><br>
        <el-form ref="form" :model="form" label-width="80px">
            <el-form-item label="">
        <span>Q1 What size of house do you want?</span>
        <el-input v-model="form.inputSize" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item label="">
        <span>Q2 Do you want an air conditioner? If yes,what kind of air conditioner do you want?</span><br>
        <el-cascader
                :options="form.airConditioner"
                :props="{ checkStrictly: true }"
                placeholder="please choose"
                clearable></el-cascader>
            </el-form-item>
            <el-form-item label="">
        <span>Q3 What type of architectural style do you want?</span><br>
        <el-select v-model="form.architecture" placeholder="please choose">
            <el-option
                    v-for="item in form.architectures"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
            </el-option>
        </el-select>
            </el-form-item>
            <el-form-item label="">
        <span>Q4 What size of basement do you want?</span><br>
        <el-input v-model="form.inputBasement" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item >
        <span>Q5 What kind of bathroom do you want?</span><br>
        <el-select v-model="form.bathroom" placeholder="please choose">
            <el-option
                    v-for="item in form.bathrooms"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
            </el-option>
        </el-select>
            </el-form-item>
            <el-form-item >
        <span>Q6 How many bedroom do you want?</span><br>
        <el-input-number v-model="form.bedroom" @change="handleChange" :min="0" :max="20" label="bedroom"></el-input-number>
            </el-form-item>
            <el-form-item >
            <span>Q7 What type of building class do you want?</span><br>
            <el-select v-model="form.buildingClass" placeholder="please choose">
                <el-option
                        v-for="item in form.buildingClasses"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            </el-form-item>
            <el-form-item >
            <span>Q8 What building quality do you want?(1 for the best)</span><br>
            <el-slider v-model="form.quality" :min="1" :max="12"></el-slider>
            </el-form-item>
            <el-form-item >
            <span>Q10 Do you want a deck?</span><br>
            <el-select v-model="form.deck" placeholder="please choose">
                <el-option
                        v-for="item in form.decks"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            </el-form-item>
            <el-form-item>
            <span>Q11 How many fire places do you want?</span><br>
            <el-input-number v-model="form.fire" @change="handleChange" :min="0" :max="9" label="fire place"></el-input-number>
            </el-form-item>
            <el-form-item>
            <span>Q12 How many garages do you want?</span><br>
            <el-input-number v-model="form.garage" @change="handleChange" :min="0" :max="25" label="garage"></el-input-number>
            </el-form-item>
            <el-form-item>
            <span>Q13 Do you want a spa hot tub?</span><br>
            <el-select v-model="form.spa" placeholder="please choose">
                <el-option
                        v-for="item in form.spas"
                        :key="item.value"
                        :label="item.label"
                        :value="item.value">
                </el-option>
            </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q14 What type of heating or system do you want?</span><br>
                <el-select v-model="form.heating" placeholder="please choose">
                    <el-option
                            v-for="item in form.heatings"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q15 What type of property land use do you want?</span><br>
                <el-select v-model="form.property" placeholder="please choose">
                    <el-option
                            v-for="item in form.properties"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q16 How many rooms do you want?</span><br>
                <el-input v-model="form.room" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item>
                <span>Q17 What type of construction do you want?</span><br>
                <el-select v-model="form.construction" placeholder="please choose">
                    <el-option
                            v-for="item in form.constructions"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q18 How many units do you want?</span><br>
                <el-input v-model="form.unit" placeholder="please enter"></el-input>
            </el-form-item>
            <el-form-item >
                <span>Q19 Do you want a yard?</span><br>
                <el-select v-model="form.yard" placeholder="please choose">
                    <el-option
                            v-for="item in form.yards"
                            :key="item.value"
                            :label="item.label"
                            :value="item.value">
                    </el-option>
                </el-select>
            </el-form-item>
            <el-form-item>
                <span>Q20 Which year do you prefer the house had been built?</span><br>
                <el-date-picker
                        v-model="form.year"
                        type="year"
                        placeholder="choose year"
                        format="yyyy"
                        value-format="yyyy">
                </el-date-picker>
            </el-form-item>
            <el-form-item>
                <span>Q12 How many stories do you want?</span><br>
                <el-input-number v-model="form.story" @change="handleChange" :min="1" :max="41" label="story"></el-input-number>
            </el-form-item>
        <!--<span>Q1 What kind of house do you want?</span>-->
        <!--<el-select v-model="value" placeholder="please choose">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
        </el-select>
        <br>
        <el-input-number v-model="num" @change="handleChange" :min="0" :max="10" label="描述文字"></el-input-number>-->
        </el-form>
    </div>
</template>

<script>
    export default {
        name: "Questions.vue",
        data() {
            return {
                form: {
                    inputSize: '',
                    num: 0,
                    architecture:"",
                    inputBasement:"",
                    bathroom:"",
                    bedroom:"",
                    buildingClass:"",
                    quality:1,
                    deck:"",
                    fire:"",
                    garage:"",
                    spa:"",
                    heating:"",
                    property:"",
                    room:"",
                    unit:"",
                    year:"",
                    story:"",
                    airConditioner: [{
                        value: '13',
                        label: 'Yes',
                        children: [{
                            value: '1',
                            label: 'Central',
                        }, {
                            value: '3',
                            label: 'Evaporative Cooler',
                        }, {
                            value: '9',
                            label: 'Refrigeration',
                        }, {
                            value: '11',
                            label: 'Wall Unit',
                        }, {
                            value: '12',
                            label: 'Window Unit',
                        }],
                    },
                        {
                            value: '5',
                            label: 'None',
                        },
                    ],
                    architectures: [{
                        value: '2',
                        label: 'Bungalow'
                    }, {
                        value: '3',
                        label: 'Cape Cod'
                    }, {
                        value: '5',
                        label: 'Colonial'
                    }, {
                        value: '7',
                        label: 'Contemporary'
                    }, {
                        value: '8',
                        label: 'Conventional'
                    },{
                        value: '10',
                        label: 'French Provincial'
                    },{
                        value: '21',
                        label: 'Ranch/Rambler'
                    },{
                        value: '27',
                        label: 'Victorian'
                    },
                    ],
                    bathrooms: [{
                        value: 'nobathroom',
                        label: 'No bathroom'
                    }, {
                        value: 'fullbathroom',
                        label: 'Full bathroom'
                    }, {
                        value: 'threequarterbathroom',
                        label: 'Three quarter bathroom'
                    }, {
                        value: 'bothbathroom',
                        label: 'Both bathroom'
                    },
                    ],
                    buildingClasses: [{
                        value: '1',
                        label: 'Buildings having fireproofed structural steel frames carrying all wall, floor and roof loads. Wall, floor and roof structures are built of non-combustible materials.'
                    }, {
                        value: '2',
                        label: 'Buildings having fireproofed reinforced concrete frames carrying all wall floor and roof loads which are all non-combustible.'
                    }, {
                        value: '3',
                        label: 'Buildings having exterior walls built of a non-combustible material such as brick, concrete, block or poured concrete. Interior partitions and roof structures are built of combustible materials. Floor may be concrete or wood frame.'
                    }, {
                        value: '4',
                        label: 'Buildings having wood or wood and steel frames'
                    }, {
                        value: '5',
                        label: 'Specialized buildings that do not fit in any of the above categories'
                    },
                    ],
                    decks: [{
                        value: 'hasdeck',
                        label: 'Yes'
                    }, {
                        value: ' ',
                        label: 'No'
                    },
                    ],
                    spas: [{
                        value: 'homespahothub',
                        label: 'Home spa hot hub'
                    }, {
                        value: 'poolspahothub',
                        label: 'Pool spa hot hub'
                    }, {
                        value: 'poolnospahothub',
                        label: 'Pool no spa hot hub'
                    },
                        {
                            value: '0',
                            label: 'I do not want'
                        },
                    ],
                    heatings: [{
                        value: '1',
                        label: 'Baseboard'
                    }, {
                        value: '2',
                        label: 'Central'
                    }, {
                        value: '6',
                        label: 'Forced air'
                    }, {
                        value: '7',
                        label: 'Floor/Wall'
                    }, {
                        value: '10',
                        label: 'Gravity'
                    },
                    ],
                    properties: [{
                        value: '31',
                        label: 'Commercial/Office/Residential Mixed Used'
                    }, {
                        value: '47',
                        label: 'Store/Office (Mixed Use)'
                    }, {
                        value: '246',
                        label: 'Duplex (2 Units, Any Combination)'
                    }, {
                        value: '247',
                        label: 'Triplex (3 Units, Any Combination)'
                    }, {
                        value: '248',
                        label: 'Quadruplex (4 Units, Any Combination)'
                    },
                        {
                            value: '0',
                            label: 'Not clear'
                        },
                    ],
                    constructions: [{
                        value: '4',
                        label: 'Concrete'
                    }, {
                        value: '6',
                        label: 'Frame'
                    }, {
                        value: '10',
                        label: 'Metal'
                    }, {
                        value: '11',
                        label: 'Manufactured'
                    }, {
                        value: '13',
                        label: 'Masonry'
                    },
                        {
                            value: '0',
                            label: 'Not clear'
                        },
                    ],
                    yards: [{
                        value: 'hasyard',
                        label: 'Yes'
                    }, {
                        value: ' ',
                        label: 'No'
                    },
                    ],
                },
            }
        },
        methods: {
            handleChange(value) {
                console.log(value);
            }
        }
    }
</script>

<style scoped>

</style>