## Dashに自作htmlを組み込みたい！ サンプルソース

このリポジトリ内容の紹介については、以下記事をご覧ください。
[Dashに自作htmlを組み込みたい！ ～html埋め込み編～]()
[Dashに自作htmlを組み込みたい！ ～callback関連付け編～]()

このリポジトリに含まれている内容
・minimak_app
　今回のサンプルの元ネタ。
　内容は[公式ページのA Minimal Dash App](https://dash.plotly.com/minimal-app)と全く同じものです。

・enbedding_html
　上記のソースに、htmlで書いたタイトルとドロップダウンメニューを組み込んだものです。
　htmlとDashの共存まではできていますが、ドロップダウンメニューの値を変更してもグラフの再描画がされません。

・associate_callback
　ドロップダウンメニューの変更内容がグラフ描画へ連動する完成版です。