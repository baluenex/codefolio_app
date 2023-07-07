<template>
  <div class="footer">
    <p>© 2022 CODE FOLIO</p>
    <router-link to="/terms-conditions">利用規約</router-link><br>
    <router-link to="/privacy-policy">プライバシーポリシー</router-link>
  </div>
</template>

<script>
export default {
  name: 'Footer'
}
</script>

<style>
.footer {
    background-color: #01579B;
}
</style>
