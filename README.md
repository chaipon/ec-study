# ec-study
Flask sample program for studying web system

# 環境作成

    > git clone https://github.com/ykachip/ec-study.git
    > cd ec-study
    > python -m venv .venv
    > .venv\Scripts\activate.ps1
    > pip install flask
    > pip install email_validator

# ローカル環境実行

    > flask --app study run

# Buil & Copy to AWS 

    > pip install build
    > python -m build --wheel
    > scp -i path_to_secreat_key dist/study-1.0.0-py2.py3-none-any.whl user_name@aws_ipaddress:~/

# AWS上でのInstall & 実行

    > mkdir ec-study
    > cd ec-study
    > python -m venv .venv
    > . .venv\bin\activate
    > pip install ../study-1.0.0-py2.py3-none-any.whl
    > pip install waitress
    > waitress-server --call 'study:create_app'


