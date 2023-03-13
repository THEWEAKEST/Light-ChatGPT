<template>
    <div style="margin-bottom: 20px;width: 100px;justify-content: center;align-content: center;">
      <el-button round="10px" size="large" @click="addTab(editableTabsValue)">
        add a new chat
      </el-button>
    </div>
    <el-tabs
      v-model="editableTabsValue"
      tab-position="left"
      type="card"
      class="demo-tabs"
      closable
      @tab-remove="removeTab"
    >
      <el-tab-pane
        v-for="item in editableTabs"
        :key="item.name"
        :label="item.title"
        :name="item.name"
      >
        {{ item.content }}
      </el-tab-pane>
    </el-tabs>
  </template>
  <script lang="ts" setup>
  import { ref } from 'vue'
  
  let tabIndex = 1
  const editableTabsValue = ref('1')
  const editableTabs = ref([
    {
      title: 'Welcome',
      name: '1',
      content: 'Hello World',
    }
  ])
  
  const addTab = (targetName: string) => {
    const newTabName = `${++tabIndex}`
    editableTabs.value.push({
      title: 'No.' + tabIndex + ' chat',
      name: newTabName,
      content: 'New Tab content',
    })
    editableTabsValue.value = newTabName
  }
  const removeTab = (targetName: string) => {
    const tabs = editableTabs.value
    let activeName = editableTabsValue.value
    if (activeName === targetName) {
      tabs.forEach((tab, index) => {
        if (tab.name === targetName) {
          const nextTab = tabs[index + 1] || tabs[index - 1]
          if (nextTab) {
            activeName = nextTab.name
          }
        }
      })
    }
  
    editableTabsValue.value = activeName
    editableTabs.value = tabs.filter((tab) => tab.name !== targetName)
  }
  </script>
  <style>
  .demo-tabs > .el-tabs__content {
    padding: 32px;
    color: #6b778c;
    font-size: 32px;
    font-weight: 600;
  }
  </style>
  