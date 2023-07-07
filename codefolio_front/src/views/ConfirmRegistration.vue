<template>
<v-app>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>
      <h1>登録確認</h1>
    </v-card-title>
    <a>メールアドレスに届いた確認番号を入力してください。</a>
    <v-card-text>
      <v-form>
        <v-text-field v-model="username" prepend-icon="mdi-account-circle" label="ユーザー名" readonly />
        <v-text-field v-model="confirmNumber" prepend-icon="mdi-numeric" label="登録確認番号" />
        <v-card-actions>
          <v-btn @click="confirm()" class="info">認証する</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>
  </v-card>
</v-app>
</template>

<style>
</style>

<script>
import {
  CognitoUserPool,
  CognitoUser
} from 'amazon-cognito-identity-js'

export default {
  name: 'ConfirmRegistration',
  data () {
    return {
      username: '',
      confirmNumber: '',
      isLoading: false
    }
  },
  mounted: function() {
    this.username = this.$store.getters.userId
  },
  methods: {
    async confirm() {
      this.confirm = true
      // 後続処理で this.$router.pushができなかったのでthisを新規で宣言する
      // https://qiita.com/ma7ma7pipipi/items/f20cb8a3589ef536cbc9?msclkid=f6d0d065c08c11ecbc4596afbea8e4e3
      const confirmThis = this
      
      const poolData = {
        UserPoolId: process.env.VUE_APP_POOL_ID,
        ClientId: process.env.VUE_APP_CLIENT_ID,
      };
      const userPool = new CognitoUserPool(poolData);
      const username = this.username;
      const confirmNumber = this.confirmNumber;

      const userData = {
        Username: username,
        Pool: userPool
      }
      const cognitoUser = new CognitoUser(userData)

      await cognitoUser.confirmRegistration(confirmNumber, true, function (err, result) {
        if (err) {
          console.log(err)
        } else {
          console.log(result)
          // 成功したらユーザー情報をDBに登録する。
          // 上のthis宣言をここで使う
          confirmThis.$router.push({path: "/signin"})
        }
      })
    }
  }
}
</script>