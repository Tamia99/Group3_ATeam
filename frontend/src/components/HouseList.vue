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
                :data="tableData"
                border
                stripe
                height="500"
                >
            <el-table-column
                    fixed
                    prop="id"
                    label="id"
                    width="80"
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

export default {
    data() {
        return {
            houses:"test",
            tableData: [{
                id: "id",
                price: "p",
                room: "r",
                area: "a",
                neighborhood: "n"
            }]
        }
    },

    created:function(){
        const path = 'http://localhost:5000/api/allHouses'
        axios.get(path)
            .then(response => {
                let all = response.data.house;
                this.tableData.push({id:response.data.house[0][0],price:response.data.house[0][80],room:response.data.house[0][54],area:response.data.house[0][4],neighborhood:response.data.house[0][12]})
                let i = 0;
                while (i< all.length){
                    this.tableData.push({id:all[i][0],price:all[i][80],room:all[i][54],area:all[i][4],neighborhood:all[i][12]})
                    i++
                }

            })
            .catch(error => {
                console.log(error)
            })
    },
    methods: {}
}
</script>

<style scoped>
.el-input {
    width: 500px;
    padding-right: 50%;

}
</style>
