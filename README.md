## Speech to Text App

### Overview
このアプリケーションは、アップロードされた音声ファイル（MP3またはWAV）をテキストに変換します。

### Requirements
Python 3.8
Flask
DeepSpeech
pydub
NumPy
soundfile

### Installation
Dockerを使用してアプリケーションを実行することが推奨されます。

Dockerビルド

```
docker build -t my_speech_to_text_app .
```
Docker Run
arduino
```
docker run -p 5000:5000 my_speech_to_text_app
```

アプリケーションはhttp://localhost:5000でアクセス可能です。

### Usage
アプリケーションを起動します。
ウェブブラウザでhttp://localhost:5000にアクセスします。
音声ファイル（MP3またはWAV）をアップロードします。
"Transcribe"ボタンを押します。
文字起こしが完了すると、テキストファイルがダウンロードされます。
このREADME.mdをプロジェクトのルートディレクトリに保存すれば、他の開発者やユーザーがこのアプリケーションを簡単に理解できるようになります。

### 備考
ルートディレクトリ配下にmodelsディレクトリを作成し、その中にdeepspeech-0.9.3-models.pbmmのモデルを配置するとappが起動します。


構造
.
├── Dockerfile
├── README.md
├── app
│   ├── main.py
│   └── templates
│       └── index.html
├── models
│   └── deepspeech-0.9.3-models.pbmm
└── requirements.txt