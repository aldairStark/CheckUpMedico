from flask import Flask, render_template, url_for

app = Flask(__name__)
#filtros personaliados
@app.add_template_filter
def Today(date):
   return date.strftime('%d-%m-%Y')
#app.add_template_filter(Today,'today')
@app.add_template_global
def repeat(s,n):
   return s * n
# app.add_template_global(repeat,'repeat')
from datetime import datetime

@app.route('/')
@app.route('/index')
def index():

    name = 'alex'
    friends =['Juan','Pedro','Alvaro','Daniel']
    date = datetime.now()

    return render_template(
       'index.html',
         name = name,
           friends= friends,
             date = date
             )

@app.route('/login')
def login():
 
 return render_template('Login/LogUser.html')

@app.route('/reporte')
def reporte():
 
 return render_template('Report/reports.html')

@app.route('/paquetes')
def paquetes():
 
 paquetes = 'UC-221'

 return render_template('Paquetes/paquetes.html', paquetes = paquetes)

from markupsafe import escape
@app.route('/code/<path:code>')
def code(code):
    return f'<code>{escape(code)}</code>'