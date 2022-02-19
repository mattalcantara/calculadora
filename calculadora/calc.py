import os
from flask import Flask, jsonify, request, abort, redirect, url_for, render_template
from math import sqrt
from CalculadoraBasica import calculate

app = Flask(_name_)

def main():
    return render_template('calc.html')

@approute('/calc')
def calculadoraweb():
    valor1=request.args.get('v1')
    valor2=request.args.get('v2')
    operacao = request.args.get('operacao')
    try:
        v1 = int(valor1)
    except ValueError:
        abort(404)
    try:
        v2 = int(valor2)
    except ValueError:
        abort(404)
    calcula = CalculadoraBasica()
    if operacao == 'soma':
        resultadoCalculado = calcula.somar(v1,v2)
    elif operacao == 'subtracao':
        resultadoCalculado = calcula.subtrair(v1,v2)
    elif operacao == 'divisao':
        if v2 == 0:
            abort(422)
        else:
            resultadoCalculado = calcula.dividir(v1,v2)
    elif operacao == "multiplicacao":
        resultadoCalculado = calcula.multiplicar(v1,v2)
    else:
        abort(404)
    return str(resultadoCalculado)

@app.route('/calculaform', methods=['POST','GET'])
def calculaform():
    valor1=request.form['v1']
    valor2=request.form['v2']
    operacao=request.form['operacao']
    print(operacao)
    
    try:
        v1 = int(valor1)
    except ValueError:
        abort(404)
    try:
        v2 = int(valor2)
    except ValueError:
        abort(404)
    calcula = CalculadoraBasica()
    if operacao == '+':
        resultadoCalculado = calcula.somar(v1, v2)
    elif operacao == '-':
        resultadoCalculado = calcula.subtrair(v1, v2)
    elif operacao == '/':
        if v2 == 0:
            abort(422)
        else:
            resultadoCalculado = calcula.dividir(v1, v2)
        if operacao == '*':
            resultadoCalculado = calcula.multiplicar(v1, v2)
        else:
            abort(404)
    return str(resultadoCalculado)


if __name__ == "__main__":
    port = int(os.environ.get("PORT",5005))
    app.run(host='127.0.0.1', port=port)

