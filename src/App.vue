<template>
  <el-config-provider namespace="ep">
    <div style="display: flex;width:100%;height:100%;">
    <el-menu>
      <el-menu-item @click="SelectChat">Chat</el-menu-item>
      <el-menu-item @click="SelectRank">Rank</el-menu-item>
      <el-menu-item @click="SelectHistory">History</el-menu-item>
    </el-menu>
      <div id="root_div" v-if="pd == 0" style="background-color: aqua;justify-content: center;align-content: center;width:100%;vertical-align: middle;height: 100%;">
        <!--img alt="Vue logo" class="element-plus-logo" src="./assets/logo.png" /-->
        <dial /><br>
      </div>
      <div v-else-if="pd == 1" style="justify-content: center;align-content:center; width:100%; background-color:pink">
        <ranklist /><br>
        </div>
      <div v-else style="justify-content: center;align-content: center; width:100%;background-color: blue;">
        <history /><br>  
      </div>
    </div>
  </el-config-provider>
</template>
<script setup lang="ts">
  import {ref} from 'vue'
  const pd = ref(0)
  function SelectChat()
  {
    pd.value = 0;
    console.log(pd)
  }
  function SelectRank()
  {
    console.log(pd)
    pd.value = 1;
  }
  function SelectHistory()
  {
    console.log(pd)
    pd.value = 2;
  }

</script>
<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.element-plus-logo {
  width: 50%;
}
.SideTab
{
  background-color:blueviolet;
  width:10%;
  min-width:50px;
}
.SideElement
{
  width:100%;
  height:20%;

}
.SideButton
{
  width:100%;
  height:100%;
  border-radius:0px;
}
</style>
