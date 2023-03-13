<template>
  <el-config-provider namespace="ep">
    <div style="display: flex;width:100%;height:100%;">
      <BaseSide />
      <div id="root_div" style="background-color: aqua;justify-content: center;align-content: center;width:100%;vertical-align: middle;height: 80%;">
        <!--img alt="Vue logo" class="element-plus-logo" src="./assets/logo.png" /-->
        <dial /><br>
      </div>
    </div>
  </el-config-provider>
</template>
<style>
#app {
  text-align: center;
  color: var(--ep-text-color-primary);
}

.element-plus-logo {
  width: 50%;
}
</style>
