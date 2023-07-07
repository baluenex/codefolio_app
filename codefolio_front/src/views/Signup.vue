<template>
<v-app>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>
      <h1>新規ユーザー登録</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field v-model="username" prepend-icon="mdi-account-circle" label="ユーザー名" />
        <v-text-field v-model="email" prepend-icon="mdi-email" label="メールアドレス" />
        <v-text-field v-model="password" prepend-icon="mdi-lock" type="password" label="パスワード" />
        <p>
          <router-link to="/privacy-policy">プライバシーポリシー</router-link>と
          <router-link to="/terms-conditions">利用規約</router-link>に同意してユーザー登録を行う
        </p>
        <v-card-actions>
          <v-btn @click="signup()" :disabled="isLoading" class="info">登録</v-btn>
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
  CognitoUserAttribute
} from 'amazon-cognito-identity-js'
import axios from 'axios'

export default {
  name: 'Signup',
  data () {
    return {
      username: '',
      email: '',
      password: '',
      isLoading: false
    }
  },
  methods: {
    async signup() {
      this.isLoading = true
      // 後続処理で this.$router.pushができなかったのでthisを新規で宣言する
      // https://qiita.com/ma7ma7pipipi/items/f20cb8a3589ef536cbc9?msclkid=f6d0d065c08c11ecbc4596afbea8e4e3
      const signUpThis = this
      
      const username = this.username;
      const email = this.email;
      const password = this.password;

      axios.post(process.env.VUE_APP_API_ENDPOINT + "/create_user",
        JSON.stringify({
          username: username,
          email: email
        })
      ).then(() => {
        const dataEmail = { Name: 'email', Value: email };
        const attributeList = [];
        attributeList.push(new CognitoUserAttribute(dataEmail));
        
        const poolData = {
          UserPoolId: process.env.VUE_APP_POOL_ID,
          ClientId: process.env.VUE_APP_CLIENT_ID,
        };
        const userPool = new CognitoUserPool(poolData);
        userPool.signUp(username, password, attributeList, null)
      }).then(() => {
        signUpThis.$store.commit("setUserId", username)
        signUpThis.$router.push({path: "/confirm-registar"})
      }).catch(err => {
        console.log(err)
      }).finally(() => {
        this.isLoading = false
      })
    }
  }
}
</script>