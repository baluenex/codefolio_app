<template>
<v-app>
  <v-card>
    <v-card-title>
      <h1>マイページ</h1>
    </v-card-title>
    こんにちは、{{ username }}さん
  </v-card>
  <v-card>
    <div class="directoryNotExists" v-if=!isDirectoryExists>
      <v-card-text>
      <p>
        まずはあなたのWebページを用意します。<br>
        URLを作成してください。
      </p>
      <v-form>
        <v-text-field v-model="dirName" prepend-icon="mdi-account-circle" label="URL Name" />
        <v-card-actions>
          <v-btn @click="checkDirectoryExists()" :disabled="!dirName" class="info">利用可能確認</v-btn>
        </v-card-actions>
        <p v-if=isDirectoryNameChecked&&!isUsableDirName>このURLはすでに使用中のため、ご利用になれません</p>
        <p>
          あなたのページは<br>
          {{ portfolioUrl }}/{{ dirName }}/index.html<br>
          になります。
        </p>
        <v-card-actions>
          <v-btn @click="createDirectory()" :disabled="!isUsableDirName" class="info">登録する</v-btn>
        </v-card-actions>
      </v-form>
      </v-card-text>
    </div>
  </v-card>
  <v-card v-if=isDirectoryExists>
    あなたのページは<br>
    <a v-bind:href="`${portfolioUrl}/${dirName}/index.html`" target="_blank">
      {{ portfolioUrl }}/{{ dirName }}/index.html<br>
    </a>
    です。
  </v-card>
  <v-card>
    <div class="creditCardNotRegistered" v-if=!isCreditCardRegistered>
      クレジットカードが未登録です。<br>
      カード登録は<router-link to="/register-creditcard">こちら</router-link>から。
    </div>
    <div class="directoryExists" v-if=isDirectoryExists>
      <div class="creditCardNotRegistered" v-if=!isCreditCardRegistered>
        ファイルのアップロードや削除機能は、クレジットカード登録完了後にご利用いただけます。
      </div>
      <div class="creditCardRegistered" v-if=isCreditCardRegistered>
        <h2>ディレクトリに保存済みのファイル一覧</h2>
        <div>
          <label v-for="file in files" :key="file.Key">
            <input v-model="deleteFiles" type="checkbox" :value="file.Key" :disabled="file.Key=='index.html'">{{ file.Key }}<br>
          </label>
        </div>
        <v-btn @click="deleteFile()" class="light-blue darken-4">ファイルを削除する</v-btn>
        <section>
          <h2>ファイルアップロード</h2>
          <div class="fileUploadInputs">
            <label class="fileUpload">
              ファイルを選択
              <input class="fileUploadInput" type="file" @change="selectedFile" multiple accept=".html, .css, .js, .png, .jpg, .jpeg, .svg, .ico">
            </label>
            <label class="fileUpload">
              フォルダを選択
              <input class="fileUploadInput" type="file" @change="selectedFolder" multiple webkitdirectory accept=".html, .css, .js, .png, .jpg, .jpeg, .svg, .ico">>
            </label>
          </div>
          <div>
            <a v-for="file in uploadedFiles" :key="file.name">
              {{ file.name }}<br>
            </a>
          </div>
          <div>
            <a v-for="file in uploadedFolders" :key="file.name">
              {{ file.webkitRelativePath }}<br>
            </a>
          </div>
          <v-btn @click="upload()" class="light-blue darken-4">アップロード</v-btn>
        </section>
      </div>
    </div>
  <div class="aboutCodeFolio">
    本サービスについては<router-link to="/about-codefolio">こちら</router-link>をご一読ください。
  </div>
  </v-card>
</v-app>
</template>

<style>
h2 {
  margin: 1rem 0 1rem 0;
}

.fileUploadInputs {
  margin: 1rem 0 1rem 0;
}

.fileUpload {
  color: #AAAAAA; /* ラベルテキストの色を指定する */
  background-color: #006DD9;/* ラベルの背景色を指定する */
  padding: 10px; /* ラベルとテキスト間の余白を指定する */
  border: double 4px #AAAAAA;/* ラベルのボーダーを指定する */
  margin: 0 5px 0 5px;
}

.fileUploadInput {
  display:none; /* アップロードボタンのスタイルを無効にする */
}
</style>

<script>
import axios from 'axios'

export default {
  name: 'Mypage',
  data () {
    return {
      portfolioUrl: process.env.VUE_APP_PORTFOLIO_URL,
      username: '',
      isDirectoryExists: false,
      isCreditCardRegistered: false,
      dirName: '',
      isUsableDirName: false,
      isDirectoryNameChecked: false,
      files: [],
      uploadedFiles: null,
      uploadedFolders: null,
      deleteFiles: []
    }
  },
  async created() {
    this.username = this.$store.getters.userId
    await this.getUser()
    await this.getFiles()
  },
  methods: {
    async getUser() {
      const mypageThis = this
      await axios.get(
        `${process.env.VUE_APP_API_ENDPOINT}/get_user?cfat=${this.$store.getters.accessToken}`,
        {
          headers: {
            "Authorization": this.$store.getters.idToken
          }
        }
      ).then(function(response) {
        const user = JSON.parse(response.data.body).user
        mypageThis.dirName = user.dirName
        mypageThis.isDirectoryExists = user.isDirectoryRegistered
        mypageThis.isCreditCardRegistered = user.isPayjpRegistered
      }).catch(function(error) {
        console.log(error)
        mypageThis.$router.push({path: "/signin"})
      })
    },
    async getFiles() {
      const mypageThis = this
      await axios.get(
        `${process.env.VUE_APP_API_ENDPOINT}/get_files?dirName=${this.dirName}`,
        {
          headers: {
            "Authorization": this.$store.getters.idToken
          }
        }
      ).then(function(response) {
        const result = JSON.parse(response.data.body)
        mypageThis.files = result.files
      }).catch(function(error) {
        console.log(error)
      })
    },
    async checkDirectoryExists() {
      const re = /[0-9a-zA-Z\\-\\_]{3,255}/.test(this.dirName)
      if (!re) {
        alert("URLは半角英数字（大文字含む）と-（ハイフン）と_（アンダーバー）を用いてください。")
      }
      const mypageThis = this
      axios.get(
        `${process.env.VUE_APP_API_ENDPOINT}/directory_exists?dirName=${this.dirName}`,
        {
          headers: {
            "Authorization": this.$store.getters.idToken
          }
        }
      ).then(function(response) {
        const result = JSON.parse(response.data.body)
        mypageThis.isUsableDirName = !result.isExists
        mypageThis.isDirectoryNameChecked = true
      }).catch(function(error) {
        console.log(error)
      })
    },
    async createDirectory() {
      const mypageThis = this
      const dirName = mypageThis.dirName
      let params = new URLSearchParams()
      params.append("dirName", dirName)
      axios.post(
        `${process.env.VUE_APP_API_ENDPOINT}/register_directory?cfat=${this.$store.getters.accessToken}`,
        params,
        {
          headers: {
            "Authorization": this.$store.getters.idToken
          }
        }
      ).then(function(response) {
        console.log(response)// response never usedって怒られるので消さない
        mypageThis.$router.go({path: mypageThis.$router.currentRoute.path, force: true})
      }).catch(function(error) {
        console.log(error)
      })
    },
    selectedFile(event) {
      // 選択された File の情報を保存しておく
      event.preventDefault()
      this.uploadedFiles = event.target.files
    },
    selectedFolder(event) {
      // 選択された File の情報を保存しておく
      event.preventDefault()
      this.uploadedFolders = event.target.files
    },
    async upload() {
      const mypageThis = this
      // バックエンドの制約で6MG以上は送れないのでバリデーションを作成する
      let fileSize = 0 // unit: Byte
      let formData = new FormData()
      // ファイルを格納
      if (this.uploadedFiles) {
        for (let i=0; i<this.uploadedFiles.length; i++) {
          formData.append("file", this.uploadedFiles[i])
          fileSize = fileSize + this.uploadedFiles[i].size
        }
      }
      // フォルダの中身を格納
      if (this.uploadedFolders) {
        for (let i=0; i<this.uploadedFolders.length; i++) {
          formData.append(this.uploadedFolders[i].webkitRelativePath, this.uploadedFolders[i])
          fileSize = fileSize + this.uploadedFolders[i].size
        }
      }
      if (!this.uploadedFiles && !this.uploadedFolders) {
        alert("ファイルをアップロードしてください。")
      } else if (fileSize >= 6291456) {
        alert("ファイルが多すぎます。アップロードするファイルを減らしてください。")
      } else {
        axios.post(
          `${process.env.VUE_APP_API_ENDPOINT}/upload_files?cfat=${this.$store.getters.accessToken}`,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data"
            }
          }
        ).then(function(response) {
          console.log(response)
        }).catch(function(error) {
          console.log(error)
        }).finally(function() {
          mypageThis.$router.go({path: mypageThis.$router.currentRoute.path, force: true})
        })
      }
    },
    async deleteFile() {
      const mypageThis = this
      if (this.deleteFiles.length === 0) {
        alert("ファイルを選択してください")
      } else {
        axios.delete(
          `${process.env.VUE_APP_API_ENDPOINT}/delete_files?cfat=${this.$store.getters.accessToken}`,
          {
            data: {files: this.deleteFiles}
          }
        ).then(function(response) {
          console.log(response)// response never usedって怒られるので消さない
        }).catch(function(error) {
          console.log(error)
          alert("ファイルの削除に失敗しました")
        }).finally(function() {
          mypageThis.$router.go({path: mypageThis.$router.currentRoute.path, force: true})
        })
      }
      
    } 
  }
}
</script>