<template>
    <el-container style="width:100%;float:left;">
        <el-header class="historyheader">
            <p style="font-size:xx-large">History</p> 
            <el-button id="freshButton" @click="GetHistory"><el-icon><Upload /></el-icon></el-button>
        </el-header>
        <el-main>
            <el-table class="ranktable" :data="historylist" :default-sort="{prop:'id' ,order:'ascending'}">
                <el-table-column label="Id" class="tablecolumn" prop="id"></el-table-column>
                <el-table-column label="Time" class="tablecolumn" prop="time"></el-table-column>
            </el-table>
        </el-main>
    </el-container>
</template>

<script setup lang="ts">
import axios from 'axios';
import {ref,defineComponent} from 'vue';
import { Upload } from '@element-plus/icons-vue';
interface historylist {
    int: number,
    time: string;
}

const historylist = ref<historylist[]>([])

async function GetHistory()
{
    const response = await axios.get('http://localhost:5000/time')
    console.log(response.data)
    historylist.value = response.data

}
</script>

<style>
.historyheader
{
    height:20%;
    max-height:200px;
    min-height:20px;
    width:100%;
    justify-content:center;
    align-content:center;
    background-color:yellowgreen;
}
</style>