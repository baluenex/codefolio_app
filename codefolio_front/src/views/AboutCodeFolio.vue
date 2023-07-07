<template>
<v-app>
  <v-card>
    <v-card-title>
      <h1>Code Folioについて</h1>
    </v-card-title>
  </v-card>
  <v-list>
    <v-list-item>
      <v-list-item-icon><v-icon color="black">mdi-check-circle-outline</v-icon></v-list-item-icon>
      <v-list-item-content>
        このサイトでは、HTMLやCSSファイルをアップロードすることで、自分のWebサイトを持つことができます。<br>
        サーバーの用意やWordPressの設定は不要です。
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-icon><v-icon color="black">mdi-check-circle-outline</v-icon></v-list-item-icon>
      <v-list-item-content>
        クレジットカードが登録されるまで、ご利用料金はかかりません。<br>
        自分用のURLを作成するところまでは、無料でご利用いただけます。
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-icon><v-icon color="black">mdi-check-circle-outline</v-icon></v-list-item-icon>
      <v-list-item-content>
        このサイトでアップロードできるファイルの拡張子は.html .css .js .png .jpeg .jpg .ico .svgとなっております。<br>
        その他の拡張子はご利用いただけませんので、ご注意ください。<br>
        また一度にアップロードできるファイルは合計で6MBまでとなっております。ファイルサイズには注意してください。
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-icon><v-icon color="black">mdi-check-circle-outline</v-icon></v-list-item-icon>
      <v-list-item-content>
        ご利用料金は一ヵ月間のデータ転送量と、月末のデータ保存容量の合計から計算されます。<br>
        最初の1GBまでは2$、その後1GBごとに0.5$ずつ加算されていきます。端数は切り捨てで計算されます。<br>
        利用した翌月の第一営業日の為替相場に則り、クレジットカード決済が行われます。<br>
        （例）2022年1月の利用データ量合計が2GBで、2022年2月1日が1ドル110円だった場合。<br>
        (2 + 0.5) × 110 × 1.08 = 297（単位は円、税込）<br>
        を2022年2月に請求いたします。
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-icon><v-icon color="black">mdi-check-circle-outline</v-icon></v-list-item-icon>
      <v-list-item-content>
        複数システムのURLを分けて管理したい場合は、フォルダを分けてそれぞれのフォルダの中でindex.htmlを作成してください。<br>
        （例）product1とproduct2を分割して保存したい場合。<br>
        index.htmlと同じ階層にproduct1フォルダを作成し、中にindex.htmlを入れてください。<br>
        必要なcssファイル、jsファイル、imgデータも格納し、アップロードしてください。<br>
        フォルダ内の構成は下記のようになります。<br>
        ・index.html<br>
        ・product1/index.html<br>
        ・product1/css/index.css<br>
        ・product1/js/index.js<br>
        ・product1/img/sample.jpg<br>
        この時、URLは下記のようになります。<br>
        https://codefolio.co.jp/＜フォルダ名＞/product1/index.html
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-icon><v-icon color="black">mdi-check-circle-outline</v-icon></v-list-item-icon>
      <v-list-item-content>
        その他で不明点がある場合は、<router-link to="/qa">QandAページ</router-link>をご確認ください。<br>
        それでも解決しなかった場合は、下記のTwitterもしくはメールアドレスからご連絡ください。
      </v-list-item-content>
    </v-list-item>
    <v-list-item>
      <v-list-item-icon><v-icon color="black">mdi-check-circle-outline</v-icon></v-list-item-icon>
      <v-list-item-content>
        CODE FOLIOの会員登録は<router-link to="/signup">こちら</router-link>
      </v-list-item-content>
    </v-list-item>
  </v-list>
  <v-card>
    <v-card-title>
      <h2>開発者について</h2>
    </v-card-title>
    <v-card-title>
      <h3>はちぽち</h3>
    </v-card-title>
    <div>
      <p>
        自称サーバーサイドエンジニアだが、普段はフルスタックに働いている企業勤めのエンジニア。<br>
        デザインは苦手だが、フロントエンド、バックエンドをメインに、インフラも時々触っている。<br>
      </p>
    </div>
    <v-card-title>
      <h3>CODE FOLIOのTwitterアカウント</h3>
    </v-card-title>
    <div>
      <a href="https://twitter.com/code_folio_info" target="_blank">CODE FOLIO 公式</a>
    </div>
    <v-card-title>
      <h3>CODE FOLIOのお問い合わせ連絡先</h3>
    </v-card-title>
    <div>
      <a href="mailto:info.codefolio@gmail.com">info.codefolio@gmail.com</a>
    </div>
  </v-card>
</v-app>
</template>