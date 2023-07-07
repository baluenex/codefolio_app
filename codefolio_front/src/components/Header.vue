<template>
  <div class="header">
    <router-link to="/"><img class="headerImg" v-bind:src="headerImg"></router-link>
  </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      headerImg: require("../../public/CODEFOLIO_LOGO2.png")
    }
  }
}
</script>

<style>
.headerImg {
  width: 400px;
}
</style>
