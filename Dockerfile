FROM python:3.12-slim

# コンテナ内で作業する場所
WORKDIR /workspace

# 開発で最低限使う Linux パッケージを入れる
# git: git add / commit / push 用
# curl, ca-certificates: 通信まわりの基本ツール
RUN apt-get update && \
    apt-get install --no-install-recommends -y \
    git \
    curl \
    ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Python ライブラリを入れる
# 今回は Iris の簡単な分析ができる最小構成
RUN pip install --no-cache-dir \
    numpy \
    pandas \
    scikit-learn \
    matplotlib \
    jupyter

# 起動後に bash を使えるようにする
CMD ["bash"]
