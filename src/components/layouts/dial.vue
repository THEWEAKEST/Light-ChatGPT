<template>
    <el-container id="main">
        <el-header id="HeadLine" style="min-height:200px;justify-content: center;align-content: center;">
            <p style="font-size:xx-large">GENERAL</p><br>
            <el-button @click="SaveHistory">SAVE<el-icon><Download/></el-icon></el-button>
            <el-button @click="LoadHistory">LOAD<el-icon><Upload/></el-icon></el-button><br>
            <el-input-number v-model="HistoryId" :min="1" :max="99"></el-input-number>
            
        </el-header>
        <el-main id="chatbox">
            <el-scrollbar>
            <div class="message-layout-zone" v-for="chatword in userchat" :key="chatword.id">
                <div style="width:100%; min-height:150px;">
                    <div :class="chatword.class">        <!--bind class with chat-zone class-->
                        {{chatword.text}}
                    </div><br><br><br>
                </div>
            </div>
            </el-scrollbar>
        </el-main>
    
    <form  id="input-form">
        <input type="text" id="input-field" v-model="userinput" autocomplete="on" list="options"/><br>
            <datalist id="options">
                <option value="Are you a real AI"/>
                <option value="Do you know Genshin Impact"/>
                <option value="Hello"/>
                <option value="How do you connect with MySQL?"/>
                <option value="What is Battlefield2042"/>
                <option value="What is Call of Duty Modern Warfame II @2022"/>
                <option value="What is Python"/>
                <option value="What is Taishan College"/>
                <option value="Where is Taishan"/>
                <option value="Who are you"/>
            </datalist>   
        <!--Don't miss the '/'-->
        <el-button id="submit-button" @click="SubmitFunction">Submit</el-button> <!--If this is Button it 
            will refresh the web when click.
            But el-button won't.
            I don't know why-->
    </form>
    </el-container>
</template> 

<script setup lang="ts">
import {ref} from 'vue'
import axios from 'axios';
import { ElInputNumber } from 'element-plus';
interface msg
{
    message:string;
}
interface getans
{
    ans:string;
}
const usernum = ref(0)
const userchat = ref([{id:usernum.value++,text:"Hello ! I'm MiniChatGPT let's talk!",class: "bot-chat-zone"}]) /*remember the value*/
const userinput = ref("")
const HistoryId = ref(0)
let return_ans:getans;
async function SubmitFunction()
{
    /*console.log(userinput.value)*/
    const nowmessage = userinput
    if(nowmessage.value == "")
    {
        console.log("It's empty!")
        return ;
    }
    /*console.log(nowmessage.value)*/
    userchat.value.push({id: usernum.value++ , text: nowmessage.value ,class:"user-chat-zone"})
    const transdata:msg={message:nowmessage.value};
    await axios.post<getans>('http://localhost:5000/transfer',transdata).then(response => {console.log(response.data); return_ans = response.data; }).catch(error => {console.log(error.data);});
    console.log("get the ans:")
    console.log(return_ans.ans)
    userchat.value.push({id: usernum.value++ , text: return_ans.ans ,class:"bot-chat-zone"})
    userinput.value=""
}
async function SaveHistory()
{
    await axios.post("http://localhost:5000/sendhistory",userchat.value).then(response => {console.log(response.data);}).catch(error => {console.log(error.data)});
}
async function LoadHistory()
{
    console.log(HistoryId.value)
    console.log(userchat.value)
    await axios.post("http://localhost:5000/history",HistoryId.value).then(response => {console.log(response.data);userchat.value = response.data}).catch(error => {console.log(error.data)});
    console.log(userchat.value)
}
</script>

<style>
.message-layout-zone
{
    min-height:150px;
}
.chat-message {
    display: inline-block;
}

#main
{
    background-color: #95ec69;
}

.user-chat-zone            /*.for class # for id*/
{
    max-width:600px;
    background-color:lightpink;
    border-color:peru;
    float:right;
    border-radius: 5px;
    font-size:xx-large;
    white-space:pre-wrap;
    justify-content: left;
}
.bot-chat-zone
{
    max-width:600px;
    background-color:orange;
    border-radius:5px;
    float:left;
    border-color:deeppink;
    font-size:xx-large;
    white-space:pre-wrap;
    justify-content: left;
}
#chatbox {
    background-color:lightblue;
    border: 1px solid #ccc;
    border-radius: 3px;
    height: 100%;
    max-height:1000px;
    margin: 0 0 20px;
    overflow-y: scroll;
    padding: 10px;
}
/*
￼
#chatbox {
    border: 1px solid #ccc;
    border-radius: 3px;
    height: 550px;
    margin: 0 0 20px;
    overflow-y: scroll;
    padding: 10px;
}
*/
.chat-message {
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 10px;
}

.user {
    background-color: #95ec69;
    color: #333;
}

.chatbot {
    background-color: #ffffff;
    color: #333;
}

#input-form {
    width:100%;
    height:100px;
    margin-top: 20px;
    display: flex;
    justify-content: center;
    align-items: center;
    resize:vertical;
    display:flex;
}

#input-field {
    max-width:50%;
    padding: 10px;
    font-size: 16px;
    border-radius: 5px;
    border: none;
    flex-grow: 1;
    background-color:antiquewhite;
    resize:vertical;
    display:felx;
}

#submit-button {
    margin-left: 10px;
    padding: 10px 20px;
    background-color: #4caf50;
    color: #fff;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

#submit-button:hover {
    background-color: #3e8e41;
}
</style>