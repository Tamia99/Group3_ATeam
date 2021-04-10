<template>
    <div>
        <h1>Here to see recommendations for you</h1>
        <el-table
                :data= tableData
                border
                stripe
        >
            <el-table-column
                    fixed
                    prop="id"
                    label="id"
            >
            </el-table-column>
            <el-table-column
                    fixed
                    prop="price"
                    label="Price"
            >
            </el-table-column>
            <el-table-column
                    fixed
                    prop="room"
                    label="Room Count"
            >
            </el-table-column>
            <el-table-column
                    fixed
                    prop="area"
                    label="Area"
            >
            </el-table-column>
            <el-table-column
                    fixed
                    prop="neighborhood"
                    label="Neighborhood"
            >
            </el-table-column>
            <el-table-column
                    fixed
                    prop="type"
                    label="Sale Type"
            >
            </el-table-column>
            <el-table-column
                    fixed="right"
                    label="Actions"
                    width="100">
                <template slot-scope="scope">
                    <el-button @click="handleClick(scope.row)" type="text" size="small">View Detail</el-button>
                </template>
            </el-table-column>
        </el-table>
    </div>

</template>

<script>
    import axios from "axios";
    export default{
        data() {
            return {
                tableData: []
            }
        },
        created:function(){
            this.setTable()
        },
        computed: {

        },
        methods:{
            setTable(){
                /*this.tableData.push({id:"all[i][0]",price:"p",room:"r",area:"a",neighborhood:"n",type:"t"})*/
                let all = this.$store.state.recommendation
                let i = 0
                while (i<all.length){
                    let p = all[i][80]
                    let r = all[i][54]
                    let a = all[i][4]
                    let n = all[i][12]
                    let t = all[i][2]
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
                    this.tableData.push({id:all[i][0],price:p,room:r,area:a,neighborhood:n,type:t})
                    i++
                }

            }
        }
    }
</script>