<template>
<v-app>
  <v-card width="500px" class="mx-auto mt-5">
    <v-card-title>
      <h1>クレジットカード登録</h1>
    </v-card-title>
    カード登録前に利用規約をご確認ください。<br>
    ※カード登録ボタンが表示されていない場合、ブラウザをリロードしてください。
    <div class="scroll_area">
      利用規約だよ
      眺めだよ
      ととえも眺めだよ
    </div>
    <payjp-checkout
      v-bind:api-key="payjpApiKey"
      text="利用規約に同意してカード情報を登録する"
      submit-text="上記の内容で登録する"
      name-placeholder="田中 太郎"
      v-on:created="onTokenCreated"
      v-on:failed="onTokenFailed">
    </payjp-checkout>
  </v-card>
</v-app>
</template>

<style>
.scroll_area {
  overflow-y: scroll;
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'ConfirmRegistration',
  data () {
    return {
      payjpApiKey: process.env.VUE_APP_PAYJP_PUBLIC_KEY
    }
  },
  mounted: function() {},
  methods: {
    async onTokenCreated(response) {
      const registerCreditcardThis = this
      const payjpToken = response.id
      let params = new URLSearchParams()
      params.append("token", payjpToken)
      axios.post(
        `${process.env.VUE_APP_API_ENDPOINT}/register_payjp?cfat=${this.$store.getters.accessToken}`,
        params,
        {
          headers: {
            "Authorization": this.$store.getters.idToken
          }
        }
      ).then(function() {
        registerCreditcardThis.$router.push({path: "/"})
      }).catch(function(error) {
        console.log(error)
      })
    },
    onTokenFailed: function(status, error) {
      console.log(status)
      console.log(error)
    }
  }
}
</script>