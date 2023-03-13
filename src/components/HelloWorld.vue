<script setup lang="ts">
import { ref } from "vue";

defineProps<{ msg: string }>();

const count = ref(0);
const input = ref("element-plus");

const curDate = ref('')

</script>

<template>
  <h1>{{msg}}</h1>
  <p>This is a local chat bot</p>
  <p>Click '+' on the left to start a conversation</p>
  <!-- example components -->
</template>

<style>
.ep-button {
  margin: 4px;
}
.ep-button + .ep-button {
  margin-left: 0;
  margin: 4px;
}
</style>
