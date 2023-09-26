from flask import Flask, render_template, redirect, request, flash
import mysql.connector

app = Flask(__name__)
app.config['SECRET_KEY'] = 'IFRN'


conect_BD = mysql.connector.connect(host='localhost', database='colecao', user='pavaodjango', password='GuGu81787339&')
if conect_BD.is_connected():
    print('conectado')

@app.route('/')
def home():
    return render_template('login-page.html')


@app.route('/log', methods=['POST'])
def login():
    usuario = request.form.get('username')
    password = request.form.get('password')
    if usuario == 'pavao' and password == '123':
        return render_template('colecao.html')
    else:
        flash('Usuário inválido')
        return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
