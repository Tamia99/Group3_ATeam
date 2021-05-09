<template>
    <div id = "all">
        <div id="message_box">
            <div id="message_show" class="message_show">
                <div v-for="item in myMessages" :key="item.id">
                    <div class="message_time">
                        <span>{{item.time}}</span>
                    </div>
                    <div class="message_is_me" v-if="item.content != null">
                        <div class="col_is_me">
                            <el-avatar src = "https://p2.ssl.qhimgs1.com/sdr/400__/t01966a42b78d397e1c.jpg"></el-avatar>
                        </div>
                        <div class="message_is_me_content">
                            <span v-html="item.content"></span>
                        </div>
                    </div>
                    <div class="message_not_me" v-if="item.content === 'Testcontent'">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2018-12-02/032658178.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <span>Sorry! I cannot understand.</span>
                        </div>
                    </div>
                    <div class="message_not_me" v-if="item.content === 'Testcontent'">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2018-12-02/032658178.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <span @click="dialogVisible = true">Can you answer some questions so we can recommend house for you.</span>
                            <el-button id="ok" size="medium" type="primary" @click="dialogVisible = true">OK</el-button>
                        </div>
                    </div>

                  <div class="message_not_me" v-if="item.reply != null">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2018-12-02/032658178.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <span v-html="item.reply"></span>
                        </div>
                        <!--<div class="message_not_me_content" v-if="status ==='0'">
                            <router-link to="/recommend">Click to see our recommendation for you.</router-link>
                        </div>-->
                  </div>
                    <!--<div class="message_not_me" v-if="status ==='0'&& item.content != null">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2018-12-02/032658178.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <router-link to="/recommend">Click to see our recommendation for you.</router-link>
                        </div>
                    </div>-->
                </div>
              <div class="message_not_me" v-if="status">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2018-12-02/032658178.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <router-link to="/recommend">{{this.recommendLink}}</router-link>
                        </div>
              </div>
              <div class="message_not_me" v-if="questionType[0]==0||questionType[0]==2">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2018-12-02/032658178.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <span @click="dialogVisible = true" v-bind:style="styleObject">Click here to get the questionnaire.</span>
                        </div>
              </div>
            </div>
            <div id="message_send">
                <br/>
                <el-input
                        type="textarea"
                        :autosize="{ minRows: 5, maxRows: 8}"
                        placeholder="Please enter your message"
                        v-model="textarea"
                        maxlength="300"
                        show-word-limit
                        clearable
                >
                </el-input>
                <br/>
                <el-button id="send" size="medium" type="primary" @click="sendMessage()">send</el-button>
            </div>
        </div>
        <el-dialog
                title=" "
                :visible.sync="dialogVisible"
                width="30%"
                :before-close="handleClose"
                fullscreen = true
                id="q"

        >
            <Questions ref="questionnaire" :message = "questionType"  ></Questions><!--v-on:="closeDialogue = 'handleClose'"-->
            <span slot="footer" class="dialog-footer">
                        <el-button @click="dialogVisible = false">Cancel</el-button>
                        <!--<el-button type="primary" @click="dialogVisible = false">Submit</el-button>-->
                        <el-button type="primary" @click= "submit()">Submit</el-button>
                    </span>
        </el-dialog>

    </div>
</template>

<script>
    import axios from 'axios'
    import Questions from '../components/Questions.vue'
    export default {
        name: 'Chat.vue',
        components: {Questions: Questions},
        status:false,
        mounted () {
            this.scrollToBottom()
        },
        data: function () {
            return {
              rstatus:this.$store.state.status,
              styleObject: {
                color: "#660099",
                textDecoration:"underline",
              },
                recommendLink:"Click here to get our recommendations for you.",
                isRecommend:false,
                isReloadData:true,
                textarea: '',
                myMessages: [
                 /* {time: "testtime"},
                  {content: 'Testcontent'},*/
                  {reply:"Welcome to the Smart House Recommendation Assistant"},
                  {reply: "Do you need us to recommend suitable housing information for you?"}],
                /*myMessages: [],*/
                messageTime: [],
                time: 'now',
                randomNumber:0,
                dialogVisible: false,
                /*总对话数*/
                processNumber:0,
                /*正在进行的对话次数*/
                currentProcess:0,
              //问卷类型， 0为选填，1为直接推荐，2为必填
                questionType:[1],

            }
        },

        updated: function () {
            this.scrollToBottom()
        },
        watch:{
          rstatus(newVal, oldVal) {
            alert(newVal)
          }
        },
        methods: {
         /* handleClose:function(data){
              alert(data)
          },*/
          reload () {
            this.isReloadData = false
            this.$nextTick(() => {
              this.isReloadData = true
            })
          },
            // 滚动条自动保持在底部
            scrollToBottom: function () {
                this.$nextTick(() => {
                    var container = this.$el.querySelector('#message_show')
                    container.scrollTop = container.scrollHeight
                })
            },
          //处理文本换行
            preText (pretext) {
              return pretext.replace(/\r\n/g, '<br/>').replace(/\n/g, '<br/>')
            },
            sendMessage () {
                let yy = new Date().getFullYear()
                let mm = new Date().getMonth() + 1
                let dd = new Date().getDate()
                let hh = new Date().getHours()
                let mf = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes()
                let ss = new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds()
                var time = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + mf + ':' + ss
                var message =  this.preText(this.textarea)
                if(message.match(/^[ ]+$/)||message===""){
                    /*alert("invalid null message")*/
                  this.$notify.error({
                    message: 'Invalid null message,please try again',
                    duration: 2000
                  });
                }
                else{
                    this.myMessages.push({ time: time })
                    this.myMessages.push({ content: message })
                    /*this.myMessages.push({ reply: message })*/
                    this.process(message)
                    /*this.status = "1"*/
                    /*this.$store.commit("newStatus",this.status)*/
                }
                this.textarea = ''
                this.randomNumber = this.getRandomFromBackend()

            },
            process(message){
                const path = 'http://localhost:5000/api/nlp'
                let data = [message,this.processNumber,this.currentProcess]
                axios.post(path, data)
                    .then(response => {
                      let re = response.data.reply
                      /*alert(re[1])
                      alert(re[2])*/
                      this.processNumber = re[1]
                      this.currentProcess = re[2]
                      if (re[1]==16&&re[2]==0){//选填问卷
                        this.questionType[0] = 0
                        this.questionType = this.questionType.concat(re[3])
                        this.currentProcess = 1
                        this.processNumber = 17
                        /*this.questionType.push(this.dialogVisible)*/

                      }
                      else if(re[1]==17&&re[2]==0){//直接推荐
                          this.myMessages.push({ reply: "Since you choose not to fill the questionnaire, we will directly find houses for you according to your answers above." })
                          /*this.myMessages.push({ reply: "The system is working, please wait for a while." })*/
                          this.questionType[0] = 1
                      /*  this.$refs.questionnaire.recommend(re[3])*/
                        this.$store.commit("newRecommendation",re[3])
                        this.$store.commit("newStatus","1")
                        this.status = true
                        /*this.$nextTick(() => {
                          this.status = true
                        })*/
                        this.textarea = " "
                        this.textarea = ""
                        this.recommendLink = "Click here to get our recommendations for you."
                        /*this.status = */
                        /*this.reload()*/
                        /*alert(this.$store.state.recommendation)*/
                        /*this.$router.push("/recommend");*/
                      }
                      else if(re[1]==15){//有回复，填必填问卷
                        let rep = this.preText(re[0])
                        this.myMessages.push({ reply: rep })
                        this.questionType[0] = 2
                        this.questionType = this.questionType.concat(re[3])
                        this.currentProcess = 1
                        this.processNumber = 17
                      }
                      else{
                        this.status = false
                        let rep = this.preText(re[0])
                        this.myMessages.push({ reply: rep })
                      }

                    })
                    .catch((error) => {
                        console.log(error)

                    })

            },
            submit(){
                /*let a = this.$refs.questionnaire.recommend()*/
              let data = [this.$refs.questionnaire.form.classification,this.$refs.questionnaire.form.inputSize,this.$refs.questionnaire.form.flatness,this.$refs.questionnaire.form.utility,this.$refs.questionnaire.form.neighborhood,
                            this.$refs.questionnaire.form.style,this.$refs.questionnaire.form.year,this.$refs.questionnaire.form.roof,this.$refs.questionnaire.form.vaneer,this.$refs.questionnaire.form.foundation,this.$refs.questionnaire.form.basement,
                            this.$refs.questionnaire.form.heating,this.$refs.questionnaire.form.air,this.$refs.questionnaire.form.electrical,this.$refs.questionnaire.form.living,this.$refs.questionnaire.form.fullbath,this.$refs.questionnaire.form.halfbath,
                            this.$refs.questionnaire.form.bedroom,this.$refs.questionnaire.form.kitchen,this.$refs.questionnaire.form.room,this.$refs.questionnaire.form.fire,this.$refs.questionnaire.form.garage,this.$refs.questionnaire.form.deck,
                            this.$refs.questionnaire.form.pool,this.$refs.questionnaire.form.price]
              /*let a = [this.$refs.questionnaire.form.price , this.$refs.questionnaire.form.pool]*/
              let invalidcount = 0
                for(let i = 0;i<data.length;i++){
                  if (data[i]===undefined || data[i]===""||data[i]=== -1){
                    /*console.log("in",data[i])*/
                    data[i]= -1
                    invalidcount++
                  }
                }
                if (invalidcount>19&&invalidcount!=25){
                    this.$confirm('Sorry, information provided is not enough! Lack of information may lead to inaccurate recommendations, do you confirm to continue recommendation ?', '', {
                      confirmButtonText: 'confirm',
                      cancelButtonText: 'no,I will provide more information',
                      type: 'warning'
                      }).then(() => {
                        this.$refs.questionnaire.realrecommend(data)
                        this.dialogVisible = false
                        this.questionType[0] = 1
                        this.myMessages.push({ reply: "The system is working, please wait for a while." })
                        /*this.status = true*/
                        let that = this
                        setTimeout(function() {
                          that.textarea = " "
                          that.textarea = ""
                          that.status = true
                          /*alert("1")*/
                        },8000);
                      }).catch(() => {
                        this.dialogVisible = true
                    });
                }
                else if(invalidcount==25&&this.dialogVisible==true){
                  this.$notify.error({
                    message: 'You must provide at least one feature for us to recommendation, please try again!',
                    duration: 5000
                  });
                }
                else {
                  /*alert("else")*/
                  this.$refs.questionnaire.realrecommend(data)
                  this.dialogVisible = false
                  this.questionType[0] = 1
                  /*this.status = true*/
                  this.myMessages.push({ reply: "The system is working, please wait for a while." })
                  let that = this
                        setTimeout(function() {
                          that.textarea = " "
                          that.textarea = ""
                          that.status = true
                          /*alert("1")*/
                        },8000);
                }
                /*this.dialogVisible = false*/

            },


        }
    }
</script>

<style scoped>
    /*.el-button{
        background-color: #66A4AC;

    }*/
    /*#all{
        background: #C2DDE4;
    }*/
    #message_box{
        border: 1px solid #d7dae2;
        border-radius: 4px ;
        background: #f4f5f7;
        box-shadow: 0 1px 2px rgba(0, 0, 0, .12);
        width: 80%;
        height: 650px;
        margin: 0 auto;
        margin-top: 20px;
    }
    #message_show{
        height: 430px;
        border-bottom: 1px solid #000000;
        overflow-y:auto;
    }
    .message_time{
        text-align: center;
        font-size: 15px;
        color: gray;
        padding: 10px 0px;
    }
    .message_is_me{
        width: 100%;
        float: right;
        overflow: hidden;
    }
    .message_is_me_content{
        float: right;
        color: white;
        margin: 10px;
        padding: 10px;
        border-radius: 8px 0px 8px 8px ;
        background: #06565B;
        max-width: 70%;
        width: fit-content;
        word-wrap: break-word;
        word-break: break-all;
        overflow: hidden;
    }
    .col_is_me{
        width: 40px;
        float: right;
        padding: 0px 10px;
    }
    .message_not_me{
        width: 100%;
        float: left;
        overflow: hidden;
    }
    .message_not_me_content{
        float: left;
        margin: 10px;
        padding: 10px;
        border-radius: 0px 8px 8px 8px ;
        background: white;
        width: fit-content;
        max-width: 70%;
        word-wrap: break-word;
        word-break: break-all;
        overflow: hidden;
    }
    .col_not_me{
        width: 40px;
        float: left;
        padding: 0px 10px;
    }
    #message_send{
        padding-left: 10px;
        width: 97%;
    }
    #send{
        float: right;
        margin-top: 20px;
    }

</style>
