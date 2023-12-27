<template>
  <div class="progress-bar">
    <div class="progress" :style="{ width: progress + '%' }"></div>
  </div>
</template>

<script>
export default {
  props: {
    progress: {
      type: Number,
      default: 0,
    },
  },
};
</script>

<style>
.progress-bar {
  width: 400px;
  height: 20px;
  border: 1px solid #9bb7ff;
  border-radius: 10px;
  margin-top: 20px;
}

.progress {
  height: 100%;
  background-color: #dfe8fe;
  transition: width 5s; 
}
</style>