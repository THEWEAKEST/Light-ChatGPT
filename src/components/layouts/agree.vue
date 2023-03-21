<template>
    <el-container style="width:100%;float:left;">
        <el-header class="agreeheader">
            <p style="font-size:xx-large">AgreeList</p>
            <el-button id="freshButton" @click="GetData"><el-icon><RefreshRight /></el-icon></el-button>
        </el-header>
        <el-main>
            <el-table class="agreetable" :data="agreeing" :default-sort="{prop:'num' ,order:'descending'}">
                <el-table-column label="Question" class="tablecolumn" prop="que"></el-table-column>
                <el-table-column label="Agree Number" class="tablecolumn" prop="num"></el-table-column>
                <el-table-column label="vote" class="tablecolumn"><el-button @click="voteup()">up</el-button><el-button @click="votedown()">down</el-button></el-table-column>
            </el-table>
        </el-main>
    </el-container>
</template>
<script setup lang="ts">
import { Location, RefreshRight } from '@element-plus/icons-vue';
import axios from 'axios';
import {ref,onMounted,defineComponent} from 'vue'
import Axios from 'axios';

interface AgreeItem {
    que: string,
    num: number;
}

const agreeing = ref<AgreeItem[]>([])

const data = ref([])
function voteup()
{
    for(var i=0;i<agreeing.value.length;i++)
        if(agreeing.value[i].que == "Do you know Genshin Impact")
            agreeing.value[i].num ++ ;
}
function votedown()
{
    for(var i=0;i<agreeing.value.length;i++)
        if(agreeing.value[i].que == "Do you know Genshin Impact")
            agreeing.value[i].num -- ;
}
async function GetData()
{
    const response = await axios.get('http://localhost:5000/transfer')
    //console.log(response.data)
    for(var i = 0 ; i < response.data.length ; i ++)
    {
        const result = agreeing.value.find(item => item.que == response.data[i].que);
        console.log(response.data[i].que);
        if(result)
        {
            for(var j = 0 ; j < agreeing.value.length ; j ++)
                 if(agreeing.value[j].que == response.data[i].que)
                 {
                    agreeing.value[j].num = agreeing.value[j].num ;
                    console.log("update")
                    break;
                 }
        }
        else
        {
            agreeing.value.push({que:response.data[i].que , num:response.data[i].rank});
            console.log("push")
        }
    }
    for(var i=0;i<agreeing.value.length;i++)
        if(agreeing.value[i].num>=5)
            agreeing.value[i].num -= 5;
        else
            agreeing.value[i].num = 0;
    console.log(agreeing.value)
}
</script>

<style>
.agreetable
{
    width:100%;
}
.agreeheader
{
    height:20%;
    max-height:200px;
    min-height:20px;
    width:100%;
    justify-content:center;
    align-content:center;
    background-color:olivedrab;
}
</style>