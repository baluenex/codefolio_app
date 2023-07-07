<template>
<v-app>
  <v-card width="400px" class="mx-auto mt-5">
    <v-card-title>
      <h1>ログイン</h1>
    </v-card-title>
    <v-card-text>
      <v-form>
        <v-text-field v-model="userId" prepend-icon="mdi-account-circle" label="User ID" />
        <v-text-field v-model="password" prepend-icon="mdi-lock" type="password" label="Password" />
        <v-card-actions>
          <v-btn @click="signin()" :disabled="!userId||!password" class="info">ログイン</v-btn>
        </v-card-actions>
      </v-form>
    </v-card-text>
    <router-link to="/signup">新規登録がまだの方はこちら</router-link><br>
    <router-link to="/change-password">パスワードを忘れた方はこちら</router-link>
  </v-card>
</v-app>
</template>

<script>
import {
  CognitoUserPool,
  CognitoUser,
  AuthenticationDetails
} from 'amazon-cognito-identity-js'

export default {
  data () {
    return {
      userId: '',
      password: ''
    }
  },
  methods: {
    async signin () {
      // 後続処理で this.$stpre.commitとthis.$router.pushができなかったのでthisを新規で宣言する
      // https://qiita.com/ma7ma7pipipi/items/f20cb8a3589ef536cbc9?msclkid=f6d0d065c08c11ecbc4596afbea8e4e3
      const signInThis = this
      // cognitoでsignin処理を行い、取得したtokenをstoreに格納する
      const poolData = {
        UserPoolId: process.env.VUE_APP_POOL_ID,
        ClientId: process.env.VUE_APP_CLIENT_ID,
      };
      const userPool = new CognitoUserPool(poolData);
      const userData = {
        Username: this.userId,
        Pool: userPool,
      };
      const  cognitoUser = new CognitoUser(userData);
      const authenticationDetails = new AuthenticationDetails({
        Username: this.userId,
        Password: this.password
      });
      
      await cognitoUser.authenticateUser(authenticationDetails, {
        onSuccess: function(result){
          const accessToken = result.getAccessToken().getJwtToken();
          const idToken = result.getIdToken().getJwtToken();
          signInThis.$store.commit("setUserId", signInThis.userId)
          signInThis.$store.commit("setAccessToken", accessToken)
          signInThis.$store.commit("setIdToken", idToken)
          signInThis.$router.push({path: "/"})
        },
        onFailure: function(err) {
          console.log(err)
        }
      })
    }
  }
}
</script>