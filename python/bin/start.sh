#!/bin/bash

# PATHにPythonのローカルbinディレクトリを追加
export PATH=$PATH:/home/app/.local/bin

# uvicornを使用してアプリケーションを起動
uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload