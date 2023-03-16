<template>
    <el-container style="width:100%;float:left;">
        <el-header class="rankheader">
            <p style="font-size:xx-large">RankList</p> 
            <el-button id="freshButton" @click="GetData"><el-icon><RefreshRight /></el-icon></el-button>
        </el-header>
        <el-main>
            <el-table class="ranktable" :data="ranking" :default-sort="{prop:'num' ,order:'descending'}">
                <el-table-column label="Question" class="tablecolumn" prop="que"></el-table-column>
                <el-table-column label="Ask Number" class="tablecolumn" prop="num"></el-table-column>
            </el-table>
        </el-main>
    </el-container>
</template>
<script setup lang="ts">
import { RefreshRight } from '@element-plus/icons-vue';
import axios from 'axios';
import {ref,onMounted,defineComponent} from 'vue'
import Axios from 'axios';

interface RankingItem {
    que: string,
    num: number;
}

const ranking = ref<RankingItem[]>([])

const data = ref([])
async function GetData()
{
    const response = await axios.get('http://localhost:5000/transfer')
    //console.log(response.data)
    for(var i = 0 ; i < response.data.length ; i ++)
    {
        const result = ranking.value.find(item => item.que == response.data[i].que);
        console.log(response.data[i].que);
        if(result)
        {
            for(var j = 0 ; j < ranking.value.length ; j ++)
                 if(ranking.value[j].que == response.data[i].que)
                 {
                    ranking.value[j].num = ranking.value[j].num ;
                    console.log("update")
                    break;
                 }
        }
        else
        {
            ranking.value.push({que:response.data[i].que , num:response.data[i].rank});
            console.log("push")
        }
    }
    console.log(ranking.value)
}
</script>

<style>
.ranktable
{
    width:100%;
}
.rankheader
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