<template>
<v-app>
  <v-card>
    <v-card-title>
      <h1>QandA</h1>
    </v-card-title>
  </v-card>
  <v-expansion-panels>
    <v-expansion-panel>
      <v-expansion-panel-header>
        1. CODE FOLIOはサーバーレンタルサービスですか？
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        本サービスはAWSというクラウドサービスと契約をしているため、サーバーレンタル代行サービスという扱いになります。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        2. Googleなど他のサービスからログインしたいのですが。
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        将来的に実装予定ですが、現在はサービス利用開始時にアカウントを新規作成していただく必要があります。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        3. 料金形態について
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        別ページに料金詳細を記載しているので確認してね
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        4. 複数の作品を表示したい場合の対処法
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        別ページに本サイトの使い方詳細を記載しているので確認してね
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        5. 安いけどサイトのスピードは遅くならないのか
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        遅くなりません。本サービスではお客様にUPしていただいたHTMLファイルは、キャッシュさせて表示しているので高速です。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        6. ファイルをUPしたはずが、サイトをリロードしてもファイルの更新が反映されません。
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        キャッシュの更新に時間がかかる場合がございます。反映まで最大で24時間かかります。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        7. SPA（Single Page Application）を使うことは可能か。
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        使用することはできません。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        8. CI/CDはには対応していないのか。
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        対応しておりません。また、対応する予定はありません。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        9. 自分で取得したドメインを利用することは可能ですか？
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        不可能です。またAWS側の仕様により、本サービスでそういった対応を行う予定はありません。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        10. サーバーがダウンした場合、どういった対応がなされるか？
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        AWS公式サイトより。サーバーがダウンすることはありません。またサーバーがダウンする場合、日本のインフラが壊滅しておりWebサイトどころの話ではないと思われます。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        11. アップしたファイルのバックアップは？
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        AWS公式サイトより。お客様のデータは自動でバックアップを取っています。個人、または所属企業の機密に関わる情報はアップロードしないでください。
      </v-expansion-panel-content>
    </v-expansion-panel>
    <v-expansion-panel>
      <v-expansion-panel-header>
        12. なぜ本サイトはデザインが非常にダサいのか。
      </v-expansion-panel-header>
      <v-expansion-panel-content>
        サービス開発者がサーバーサイドエンジニアだからです。デザインについては、改修案件を近日中に公開する予定です。
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-expansion-panels>
</v-app>
</template>