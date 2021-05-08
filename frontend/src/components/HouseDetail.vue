<template>
<div>
  <h1>{{message}}
    <!-- <el-row :gutter="24"> -->
      

      <!-- <el-column :span="12"> -->
        <!-- <img class="logo" height=60px src="./teamlogo-black.png" style="margin-top:-2%; margin-left:80%"> -->
      <!-- </el-column>  -->
      <!-- <el-column :span="12" style=""> -->

        
        
        <!-- <nobr class="head" style="padding-left:0%; margin-bottom:100%">Details of This House</nobr> -->
      <!-- </el-column>    -->
    <!-- </el-row> -->
    </h1>
  <el-row :gutter="24">
    
    <el-column :span="6">
      <div>
      <el-button class="tag1" style="border:none; margin-left:88%;margin-top:-200%; width:80px!important;"><i class="el-icon-collection-tag">Tab</i></el-button>
      </div>
      <div>
      <img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2287568211,2342036693&fm=26&gp=0.jpg" class="image">
    </div>
    </el-column>
    
    
    <el-column :span="6">
      
      <div>
      <el-tabs v-model="activeName" @tab-click="handleClick">
    <el-tab-pane label="Environment" name="first">
      <p>
          <nobr class="title">
          Neighborhood:
          </nobr>
          <!-- {{message[12]}} -->
          {{replaceNeigh(message[12])}}
        </p>
      <p>
          <nobr class="title">
          Zoning: 
          </nobr>
          {{replaceZon(message[2])}}
        </p>
        <p>
          <nobr class="title">
          Proximity Conditions:
          </nobr>
          {{replacePro(message[13])}}
        </p>
    </el-tab-pane>


    <el-tab-pane label="Area" name="second">
      <p>
          <nobr class="title">
          Lot Area:
          </nobr>
          {{message[4]}}
        </p>
        <p>
          <nobr class="title">
          Total Squarefeet of Basement:
          </nobr>
          {{message[38]}}
        </p>
        <p>
          <nobr class="title">
          First Floor sqft:
          </nobr>
          {{message[43]}}
        </p>
        <p>
          <nobr class="title">
          Second Floor sqft:
          </nobr>
          {{message[44]}}
        </p>
        <p>
          <nobr class="title">
          Above Grade Living Area sqft:
          </nobr>
          {{message[46]}}
        </p>
        <p>
          <nobr class="title">
          Size of Garage(sqft):
          </nobr>
          {{message[62]}}
        </p>
        <p>
          <nobr class="title">
          Pool Area:
          </nobr>
          {{message[71]}}
        </p>
    </el-tab-pane>


    <el-tab-pane label="Living Condition" name="third">
      <p>
          <nobr class="title">
          Utilities:
          </nobr>
          {{replaceUti(message[9])}}
        </p>
        <p>
          <nobr class="title">
          Roof Material:
          </nobr>
          {{replaceR(message[22])}}
        </p>
        <p>
          <nobr class="title">
          Height of Basement:
          </nobr>
          {{replaceBaseH(message[30])}}
        </p>
        <p>
          <nobr class="title">
          Heating:
          </nobr>
          {{replaceHeat(message[39])}}
        </p>
        <p>
          <nobr class="title">
          Central Air Conditioning:
          </nobr>
          {{replaceCen(message[41])}}
        </p>
        <p>
          <nobr class="title">
          Electrical System:
          </nobr>
          {{replaceElec(message[42])}}
        </p>
        <p>
          <nobr class="title">
          Bathroom Number:
          </nobr>
          {{message[49] + message[50]*0.5}}
        </p>
        <p>
          <nobr class="title">
          Bedroom Number(above Grade):
          </nobr>
          {{message[51]}}
        </p>
        <p>
          <nobr class="title">
          Kitchen Number(above Grade):
          </nobr>
          {{message[52]}}
        </p>
        <p>
          <nobr class="title">
          Fireplace Number:
          </nobr>
          {{message[56]}}
        </p>
        <p>
          <nobr class="title">
          Garage Location:
          </nobr>
          {{replaceGara(message[58])}}
        </p>
        <p>
          <nobr class="title">
          Size of Garage(car capacity):
          </nobr>
          {{message[61]}}
        </p>
    </el-tab-pane>


    <el-tab-pane label="Type and Style" name="fourth">
      <p>
          <nobr class="title">
          Dwelling Type:
          </nobr>
          {{replaceDweType(message[15])}}
        </p>
        <p>
          <nobr class="title">
          Dwelling Style:
          </nobr>
          {{replaceDweStyle(message[16])}}
        </p>
    </el-tab-pane>


    <el-tab-pane label="Duration" name="fifth">
      <p>
          <nobr class="title">
          Year Built:
          </nobr>
          {{message[19]}}
        </p>
    </el-tab-pane>


    <el-tab-pane label="Build Condition" name="sixth">
      <p>
          <nobr class="title">
          Foundation:
          </nobr>
          {{replaceFound(message[29])}}
        </p>
    </el-tab-pane>


    <el-tab-pane label="Sale" name="seventh">
        <p>
          <nobr class="title">
          Type of Sale:
          </nobr>
          {{replaceSaleType(message[78])}}
        </p>
        <p>
          <nobr class="title">
          Sale Condition:
          </nobr>
          {{replaceSaleCon(message[79])}}
        </p>
    </el-tab-pane>
  </el-tabs>
  </div> 
    </el-column>
    
  </el-row>  
  
  <!-- <p class="body"> -->
    <!-- <el-row :gutter="10"> -->
      <!-- <el-column :span="2" class="leftSide"> -->
        <!-- 为什么不换行 -->
        <!-- <img src="https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=2287568211,2342036693&fm=26&gp=0.jpg" class="image"><br> -->
      <!-- </el-column> -->
      <!-- <el-column :span="8" class="rightSide"> -->
        
        <!-- {{message}} -->
      <!-- </el-column> -->
    <!-- </el-row> -->
  <!-- </p> -->
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
      activeName: 'first',
    }

  },

  methods:{
    replaceNeigh(n1){
        if(n1 == "Blmngtn"){
          n1 = "Bloomington Heights"
        }
        else if (n1 == "Blueste"){
          n1 = "Bluestem"
        }
        else if (n1 == "BrDale"){
          n1 = "Briardale"
        }
        else if (n1 == "BrkSide"){
          n1 = "Brookside"
        }
        else if (n1 == "ClearCr"){
          n1 = "Clear Creek"
        }
        else if (n1 == "CollgCr"){
          n1 = "College Creek"
        }
        else if (n1 == "Crawfor"){
          n1 = "Crawford"
        }
        else if (n1 == "Edwards"){
          n1 = "Edwards"
        }
        else if (n1 == "Gilbert"){
          n1 = "Gilbert"
        }
        else if (n1 == "IDOTRR"){
          n1 = "Iowa DOT and Rail Road"
        }
        else if (n1 == "MeadowV"){
          n1 = "Meadow Village"
        }
        else if (n1 == "Mitchel"){
          n1 = "Mitchell"
        }
        else if (n1 == "NAmes"){
          n1 = "North Ames"
        }
        else if (n1 == "NoRidge"){
          n1 = "Northridge"
        }
        else if (n1 == "NPkVill"){
          n1 = "Northpark Villa"
        }
        else if (n1 == "NridgHt"){
          n1 = "Northridge Heights"
        }
        else if (n1 == "NWAmes"){
          n1 = "Northwest Ames"
        }
        else if (n1 == "OldTown"){
          n1 = "Old Town"
        }
        else if (n1 == "SWISU"){
          n1 = "South & West of Iowa State University"
        }
        else if (n1 == "Sawyer"){
          n1 = "Sawyer"
        }
        else if (n1 == "SawyerW"){
          n1 = "Sawyer West"
        }
        else if (n1 == "Somerst"){
          n1 = "Somerset"
        }
        else if (n1 == "StoneBr"){
          n1 = "Stone Brook"
        }
        else if (n1 == "Timber"){
          n1 = "Timberland"
        }
        else if (n1 == "Veenker"){
          n1 = "Veenker"
        }
        return n1
    },

    replaceZon(n1){
        if(n1 == "A"){
          n1 = "Agriculture"
        }
        else if (n1 == "C"){
          n1 = "Commercial"
        }
        else if (n1 == "FV"){
          n1 = "Floating Village Residential"
        }
        else if (n1 == "I"){
          n1 = "Industrial"
        }
        else if (n1 == "RH"){
          n1 = "Residential High Density"
        }
        else if (n1 == "RL"){
          n1 = "Residential Low Density"
        }
        else if (n1 == "RP"){
          n1 = "Residential Low Density Park"
        }
        else if (n1 == "RM"){
          n1 = "Residential Medium Density"
        }
        return n1
    },

    replacePro(n1){
        if(n1 == "Artery"){
          n1 = "Adjacent to arterial street"
        }
        else if (n1 == "Feedr"){
          n1 = "Adjacent to feeder street"
        }
        else if (n1 == "Norm"){
          n1 = "Normal"
        }
        else if (n1 == "RRNn"){
          n1 = "Within 200' of North-South Railroad"
        }
        else if (n1 == "RRAn"){
          n1 = "Adjacent to North-South Railroad"
        }
        else if (n1 == "PosN"){
          n1 = "	Near positive off-site feature--park, greenbelt, etc."
        }
        else if (n1 == "PosA"){
          n1 = "Adjacent to postive off-site feature"
        }
        else if (n1 == "RRNe"){
          n1 = "Within 200' of East-West Railroad"
        }
        else if (n1 == "RRAe"){
          n1 = "Adjacent to East-West Railroad"
        }
        return n1
    },

    replaceUti(n1){
        if(n1 == "AllPub"){
          n1 = "All public Utilities (E,G,W,& S)	"
        }
        else if (n1 == "NoSewr"){
          n1 = "Electricity, Gas, and Water (Septic Tank)"
        }
        else if (n1 == "NoSeWa"){
          n1 = "Electricity and Gas Only"
        }
        else if (n1 == "ELO"){
          n1 = "Electricity only"
        }
        return n1
    },

    replaceR(n1){
        if(n1 == "ClyTile"){
          n1 = "Clay or Tile"
        }
        else if (n1 == "CompShg"){
          n1 = "Standard (Composite) Shingle"
        }
        else if (n1 == "Membran"){
          n1 = "Membrane"
        }
        else if (n1 == "Tar&Grv"){
          n1 = "Gravel & Tar"
        }
        else if (n1 == "WdShake"){
          n1 = "Wood Shakes"
        }
        else if (n1 == "WdShngl"){
          n1 = "Wood Shingles"
        }
        return n1
    },

    replaceBaseH(n1){
        if(n1 == "Ex"){
          n1 = "Excellent (100+ inches)"
        }
        else if (n1 == "Gd"){
          n1 = "Good (90-99 inches)"
        }
        else if (n1 == "TA"){
          n1 = "Typical (80-89 inches)"
        }
        else if (n1 == "Fa"){
          n1 = "Fair (70-79 inches)"
        }
        else if (n1 == "Po"){
          n1 = "Poor (<70 inches)"
        }
        else if (n1 == "NA"){
          n1 = "No Basement"
        }
        return n1
    },

    replaceHeat(n1){
        if(n1 == "Floor"){
          n1 = "Floor Furnace"
        }
        else if (n1 == "GasA"){
          n1 = "Gas forced warm air furnace"
        }
        else if (n1 == "GasW"){
          n1 = "Gas hot water or steam heat"
        }
        else if (n1 == "Grav"){
          n1 = "Gravity furnace"
        }
        else if (n1 == "OthW"){
          n1 = "Hot water or steam heat other than gas"
        }
        else if (n1 == "Wall"){
          n1 = "Wall furnace"
        }
        return n1
    },

    replaceCen(n1){
        if(n1 == "Y"){
          n1 = "Yes"
        }
        else if (n1 == "N"){
          n1 = "No"
        }
        return n1
    },

    replaceElec(n1){
        if(n1 == "SBrkr"){
          n1 = "Standard Circuit Breakers & Romex"
        }
        else if (n1 == "FuseA"){
          n1 = "Fuse Box over 60 AMP and all Romex wiring (Average)"
        }
        else if (n1 == "FuseF"){
          n1 = "60 AMP Fuse Box and mostly Romex wiring (Fair)"
        }
        else if (n1 == "FuseP"){
          n1 = "60 AMP Fuse Box and mostly knob & tube wiring (poor)"
        }
        else if (n1 == "Mix"){
          n1 = "Mixed"
        }
        return n1
    },

    replaceGara(n1){
        if(n1 == "2Types"){
          n1 = "More than one type of garage"
        }
        else if (n1 == "Attchd"){
          n1 = "Attached to home"
        }
        else if (n1 == "Basment"){
          n1 = "Basement Garage"
        }
        else if (n1 == "BuiltIn"){
          n1 = "Built-In (Garage part of house - typically has room above garage)"
        }
        else if (n1 == "CarPort"){
          n1 = "Car Port"
        }
        else if (n1 == "Detchd"){
          n1 = "Detached from home"
        }
        else if (n1 == "NA"){
          n1 = "No Garage"
        }
        return n1
    },

    replaceDweType(n1){
        if(n1 == "1Fam"){
          n1 = "Single-family Detached"
        }
        else if (n1 == "2FmCon"){
          n1 = "Two-family Conversion; originally built as one-family dwelling"
        }
        else if (n1 == "Duplx"){
          n1 = "Duplex"
        }
        else if (n1 == "TwnhsE"){
          n1 = "Townhouse End Unit"
        }
        else if (n1 == "TwnhsI"){
          n1 = "Townhouse Inside Unit"
        }
        return n1
    },

    replaceDweStyle(n1){
        if(n1 == "1Story"){
          n1 = "One story"
        }
        else if (n1 == "1.5Fin"){
          n1 = "One and one-half story: 2nd level finished"
        }
        else if (n1 == "1.5Unf"){
          n1 = "One and one-half story: 2nd level unfinished"
        }
        else if (n1 == "2Story"){
          n1 = "Two story"
        }
        else if (n1 == "2.5Fin"){
          n1 = "Two and one-half story: 2nd level finished"
        }
        else if (n1 == "2.5Unf"){
          n1 = "Two and one-half story: 2nd level unfinished"
        }
        else if (n1 == "SFoyer"){
          n1 = "Split Foyer"
        }
        else if (n1 == "SLvl"){
          n1 = "Split Level"
        }
        return n1
    },

    replaceFound(n1){
        if(n1 == "BrkTil"){
          n1 = "Brick and Tile"
        }
        else if (n1 == "CBlock"){
          n1 = "Cinder Block"
        }
        else if (n1 == "PConc"){
          n1 = "Poured Contrete"
        }
        return n1
    },

    replaceSaleType(n1){
        if(n1 == "WD"){
          n1 = "Warranty Deed - Conventional"
        }
        else if (n1 == "CWD"){
          n1 = "Warranty Deed - Cash"
        }
        else if (n1 == "VWD"){
          n1 = "Warranty Deed - VA Loan"
        }
        else if (n1 == "New"){
          n1 = "Home just constructed and sold"
        }
        else if (n1 == "COD"){
          n1 = "Court Officer Deed/Estate"
        }
        else if (n1 == "Con"){
          n1 = "Contract 15% Down payment regular terms"
        }
        else if (n1 == "ConLw"){
          n1 = "Contract Low Down payment and low interest"
        }
        else if (n1 == "ConLI"){
          n1 = "Contract Low Interest"
        }
        else if (n1 == "ConLD"){
          n1 = "Contract Low Down"
        }
        else if (n1 == "Oth"){
          n1 = "Other"
        }
        return n1
    },

    replaceSaleCon(n1){
        if(n1 == "Normal"){
          n1 = "Normal Sale"
        }
        else if (n1 == "Abnorml"){
          n1 = "Abnormal Sale -  trade, foreclosure, short sale"
        }
        else if (n1 == "AdjLand"){
          n1 = "Adjoining Land Purchase"
        }
        else if (n1 == "Alloca"){
          n1 = "Allocation - two linked properties with separate deeds, typically condo with a garage unit"
        }
        else if (n1 == "Family"){
          n1 = "Sale between family members"
        }
        else if (n1 == "Partial"){
          n1 = "Home was not completed when last assessed (associated with New Homes)"
        }
        return n1
    }
  }
}
</script>

<style scoped>

.rightSide{
  padding-left: 100px!important;
}

h1{
  margin-top: -3%!important;
}

.body{
  margin-top: 3%;
}

.title{
  font-weight: bold;
}

.image{
  width:50%;
}

.tag1{

  /* padding-bottom: 50%!important; */
  padding-left: -1000%;
  font-size: 15px!important;
}

.el-tabs{
  width:45%;
  /* height: 60%!important; */
  margin-left: 53%;
  margin-top: -20%;
}

.el-tab-pane{
  overflow-x:hidden;
  overflow-y:auto;
  height:150px;
}

.el-icon-collection-tag{
  
}

/* .head{
  padding-top: -50%;
} */

/* .el-tab-pane{
  background-color: #66A4AC;
} */

</style>