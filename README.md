# pdf-rename

pdfファイルを読んだ内容でファイル名を変更してコピーするサンプルコード

1.ビルド

```bash
docker compose up -d
```

2.吐かれるディレクトリ作成

```bash
mkdir dist
```

3.実行

```bash
docker exec -it $(docker ps -aqf "name=pdf-rename") /bin/bash -c "cd /src && python3 main.py"
```

4.掃除

```bash
. cleanup.sh
```
