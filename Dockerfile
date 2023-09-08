# 使用するベースイメージ
FROM python:3.8-slim-buster

# 必要なパッケージをインストール
RUN apt-get update && apt-get install -y ffmpeg

# コンテナ内で作業するディレクトリを設定
WORKDIR /app

# 必要なPythonパッケージをインストール
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションのコードとモデルをコンテナ内にコピー
COPY ./app /app
COPY ./models/deepspeech-0.9.3-models.pbmm /app/models/deepspeech-0.9.3-models.pbmm

# Flaskが使用するポートを開放
EXPOSE 5000

# アプリケーションを実行
CMD ["python", "main.py"]
