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
                            <el-avatar shape="square" icon=el-icon-user-solid></el-avatar>
                        </div>
                        <div class="message_is_me_content">
                            <span v-html="item.content"></span>
                        </div>
                    </div>
                    <div class="message_not_me" v-if="item.content === 'Testcontent'">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2019-02-25/230332138.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <span>Sorry! I cannot understand.</span>
                        </div>
                    </div>
                    <div class="message_not_me" v-if="item.content === 'Testcontent'">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2019-02-25/230332138.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <span>Can you answer some questions so we can recommend house for you.</span>
                            <el-button id="ok" size="medium" type="primary" @click="dialogVisible = true">OK</el-button>
                        </div>
                    </div>

                  <div class="message_not_me" v-if="item.reply != null">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2019-02-25/230332138.jpg"></el-avatar>
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
                            <el-avatar src="http://img.qqzhi.com/uploads/2019-02-25/230332138.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <router-link to="/recommend">Click to see our recommendation for you.</router-link>
                        </div>
                    </div>-->
                </div>
              <div class="message_not_me" v-if="status ==='0'">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2019-02-25/230332138.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <router-link to="/recommend">Click to see our recommendation for you.</router-link>
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
                id="q">
            <Questions  ref="questionnaire"></Questions>
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
        status:"1",
        mounted () {
            this.scrollToBottom()
        },
        data: function () {
            return {
                textarea: '',
                myMessages: [
                  {time: "testtime"},
                  {content: 'Testcontent'},
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

            }
        },

        updated: function () {
            this.scrollToBottom()
        },

        methods: {
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
                    alert("invalid null message")
                }
                else{
                    this.myMessages.push({ time: time })
                    this.myMessages.push({ content: message })
                    /*this.myMessages.push({ reply: message })*/
                    this.process(message)
                    this.status = "1"
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
                      let rep = this.preText(re[0] )
                      this.processNumber = re[1]
                      this.currentProcess = re[2]
                      this.myMessages.push({ reply: rep })
                    })
                    .catch((error) => {
                        console.log(error)

                    })

            },
            submit(){
                this.$refs.questionnaire.recommend();
                this.status = "0"
                this.dialogVisible = false
            },
           /* changeStatus(){
                if(this.$store.state.status=="0"){
                    this.status = this.$store.state.status
                    this.dialogVisible = false
                }
            },*/
            /*getRandom (){
                this.randomNumber = this.getRandomFromBackend()
            },
            getRandomFromBackend (){
                const path = 'http://localhost:5000/api/random'
                axios.get(path)
                    .then(response => {
                        this.randomNumber = response.data.randomNumber
                    })
                    .catch(error => {
                        console.log(error)
                    })
            },*/

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
