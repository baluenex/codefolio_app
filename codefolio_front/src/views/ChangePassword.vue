<template>
<v-app>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>
      <h1>パスワード再設定</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field v-model="username" prepend-icon="mdi-account-circle" label="ユーザー名" />
        <v-text-field v-model="password" prepend-icon="mdi-lock" type="password" label="新しいパスワード" />
        <v-card-actions>
          <v-btn @click="sendResetEmail()" class="info">送信する</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>
    <v-card-text>
      <v-form>
        <v-text-field v-model="verificationCode" prepend-icon="mdi-numeric" label="メールで届いたコード" />
        <v-card-actions>
          <v-btn @click="changePassword()" class="info">認証する</v-btn>
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
  data () {
    return {
      username: '',
      password: '',
      verificationCode: ''
    }
  },
  methods: {
    sendResetEmail () {
      const poolData = {
        UserPoolId: process.env.VUE_APP_POOL_ID,
        ClientId: process.env.VUE_APP_CLIENT_ID,
      };
      const userPool = new CognitoUserPool(poolData);
      const cognitoUser = new CognitoUser({
        Username: this.username,
        Pool: userPool
      })
      cognitoUser.forgotPassword({
        onSuccess: function(result) {
          console.log(result)
        },
        onFailure: function(err) {
          alert(err)
        }
      })
    },
    async changePassword() {
      const changePasswordThis = this
      const newPassword = this.password
      const verificationCode = this.verificationCode
      const poolData = {
        UserPoolId: process.env.VUE_APP_POOL_ID,
        ClientId: process.env.VUE_APP_CLIENT_ID,
      };
      const userPool = new CognitoUserPool(poolData);
      const cognitoUser = new CognitoUser({
        Username: this.username,
        Pool: userPool
      })
      await cognitoUser.confirmPassword(verificationCode, newPassword, function(err, result) {
        if (err) {
          alert(err)
        } else {
          console.log(result)
          changePasswordThis.router.push({path: "/signin"})
        }
      })
    }
  }
}
</script>