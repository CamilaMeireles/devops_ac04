import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')

def fibo_seq():
    limite = 50

    n1 = 0
    n2 = 1
    cont = 2

    fibo = "0, 1, "

    while cont < limite:
       n3 = n1 + n2
       fibo = fibo + str(n3) + ", "
       n1 = n2
       n2 = n3
       cont = cont + 1

    return fibo


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
