<template>
    <div>
        <h1> This is Chat Page </h1>
        <div id="message_box">
            <div id="message_show" class="message_show">

                <div v-for="item in myMessages" :key="item.id">
                    <div class="message_time">
                        <span>{{item.time}}</span>
                    </div>
                    <div class="message_is_me">
                        <div class="col_is_me">
                            <el-avatar src="http://img.51miz.com/Element/00/77/27/49/25a8e39b_E772749_adadfc75.png!/quality/90/unsharp/true/compress/true/format/png"></el-avatar>
                        </div>
                        <div class="message_is_me_content">
                            <span>{{item.content}}</span>
                        </div>
                    </div>
                    <div class="message_not_me">
                        <div class="col_not_me">
                            <el-avatar src="http://img.qqzhi.com/uploads/2019-02-25/230332138.jpg"></el-avatar>
                        </div>
                        <div class="message_not_me_content">
                            <span>auto reply</span>
                        </div>
                    </div>
                </div>
            </div>
            <div id="message_send">
                <!--<textarea  id="input_box"  style="border:none;outline:none;background: #f4f5f7"></textarea>-->
                <br/>
                <el-input
                        type="textarea"
                        :autosize="{ minRows: 5, maxRows: 8}"
                        placeholder="Please enter your message"
                        v-model="textarea"
                        maxlength="300"
                        show-word-limit
                >
                </el-input>
                <br/>
                <el-button id="send" size="medium" type="primary" @click="sendMessage()">send</el-button>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        name: 'Chat.vue',
        mounted () {
            /* this.$nextTick(() => {
              this.$refs.main.scrollTop = this.$refs.content.scrollHeight
            }) */
            this.scrollToBottom()
        },
        data: function () {
            return {
                textarea: '',
                // eslint-disable-next-line standard/array-bracket-even-spacing
                myMessages: [ {time: ''}, {content: 'Test'}],
                messageTime: [],
                time: 'now'
            }
        },

        updated: function () { this.scrollToBottom() },

        methods: {
            // 滚动条自动保持在底部
            scrollToBottom: function () {
                this.$nextTick(() => {
                    var container = this.$el.querySelector('#message_show')
                    container.scrollTop = container.scrollHeight
                })
            },
            sendMessage () {
                let yy = new Date().getFullYear()
                let mm = new Date().getMonth() + 1
                let dd = new Date().getDate()
                let hh = new Date().getHours()
                let mf = new Date().getMinutes() < 10 ? '0' + new Date().getMinutes() : new Date().getMinutes()
                let ss = new Date().getSeconds() < 10 ? '0' + new Date().getSeconds() : new Date().getSeconds()
                var time = yy + '-' + mm + '-' + dd + ' ' + hh + ':' + mf + ':' + ss
                var message = this.textarea
                /* if (this.textarea !== null) {
                  this.myMessages.push({ content: message })
                } */
                this.messageTime.push({ time: time })
                /* this.messageTime = [{time: time}] */
                this.myMessages.push({ content: message })
                this.textarea = ''
            }
        }
    }
</script>

<style scoped>
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
        background: #409EFF;
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
