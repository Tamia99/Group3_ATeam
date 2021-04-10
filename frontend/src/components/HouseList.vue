<template>
    <!-- <h1>This is the houseList page</h1> -->
    
    <div>
        <el-breadcrumb separator-class="el-icon-arrow-right">
            <!-- <el-breadcrumb-item>All Resources</el-breadcrumb-item> -->
        </el-breadcrumb>

        
        <el-input placeholder="Please input your key words">
                <!-- <el-select v-model="select" slot="prepend" placeholder="请选择">
                    <el-option label="餐厅名" value="1"></el-option>
                    <el-option label="订单号" value="2"></el-option>
                    <el-option label="用户电话" value="3"></el-option>
                </el-select> -->
            <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>

        <!--<br>
        <span>{{houses}}</span>-->
        <el-table
                :data="tableData.slice((currentPage - 1) * pageSize, currentPage*pageSize)"
                border
                stripe
                :default-sort = "{prop: 'price', order: 'descending'}"
                >
            <el-table-column
                    fixed
                    prop="price"
                    label="Price"
                    sortable
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
        <el-pagination
                @size-change="handleSizeChange"
                @current-change="handleCurrentChange"
                :current-page="currentPage"
                :page-sizes="[10, 20, 30, 40]"
                :page-size="10"
                layout="total, sizes, prev, pager, next, jumper"
                :total="currentTotal">
        </el-pagination>
    </div>
    
</template>

<script>
import axios from "axios";

export default {
    data() {
        return {
            currentTotal: 0,
            currentPage: 1,
            pageSize: 10,
            tableData: []
        }
    },

    created:function(){
        this.getList()

    },
    methods: {
        async getList(){
            const path = 'http://localhost:5000/api/allHouses'
            axios.get(path)
                .then(response => {
                    let all = response.data.house;
                    this.currentTotal = all.length
                    let i = 0;
                    while (i< all.length){
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

                        this.tableData.push({price:p,room:r,area:a,neighborhood:n,type:t})
                        i++
                    }

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
.el-input {
    width: 500px;
    padding-right: 50%;

}
</style>
