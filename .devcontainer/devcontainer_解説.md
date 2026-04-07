# devcontainer.json 解説

対象ファイル: `.devcontainer/devcontainer.json`

## まず前提
`devcontainer.json` は、**VS Code が Docker 環境にどう接続するか** を決めるファイルです。

JSON はコメントを自由に入れにくいので、今回は別でこの解説メモを置いています。

## 各項目の意味

### `name`
- Dev Container の名前です
- VS Code 上で見えるラベルみたいなものです

### `dockerComposeFile`
- どの `compose.yml` を使うかを指定しています
- 今回は `../compose.yml` を使っています

### `service`
- `compose.yml` に書かれているサービスのうち、どれに接続するかを表します
- 今回は `app` に入ります

### `workspaceFolder`
- コンテナの中で、VS Code が作業場所として開くディレクトリです
- 今回は `/workspace` を開きます

### `shutdownAction`
- VS Code を閉じたときの動作です
- `stopCompose` は、compose で立てたコンテナを止める設定です

### `customizations.vscode.extensions`
- コンテナに入ったときに使いたい VS Code 拡張機能です
- 今回は Python と Jupyter を入れています

### `customizations.vscode.settings`
- VS Code の設定です
- 今回は
  - Python のパス
  - 保存時フォーマット
  を最低限書いています

## ざっくり整理
- `Dockerfile` = コンテナの中身
- `compose.yml` = コンテナの起動方法
- `devcontainer.json` = VS Code からどう入るか
