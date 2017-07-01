from flask import Flask, request, Response
import estructuras
from estructuras import *

app = Flask("Web Service Flask")

lista = estructuras.lista_juegossss()
abb = estructuras.ABinarios()

################### ARBOL #########################
@app.route('/metodoWeb', methods=['POST'])
def hola():
    parametro = str(request.form['nombre'])
    return 'Hola '+str(parametro)+' Exitos'

@app.route('/ingresaABB', methods=['POST'])
def ingresa():
    user = str(request.form['usuario'])
    passw = str(request.form['passw'])
    conectado = str(request.form['conectado'])
    lista = estructuras.lista_juegossss()
    nodo = estructuras.NodoArbol(user, passw, conectado, lista)
    abb.agregar(nodo)
    abb.graficar(abb.raiz)
    return 'ya'

@app.route('/loginABB', methods=['POST'])
def logear():
    user = str(request.form['usuario'])
    passw = str(request.form['passw'])
    if abb.login(abb.raiz, user, passw) == True:
        return 'si'
    else:
        return 'no'

########################### Lista ######################################
@app.route('/ingresaLista', methods=['POST'])
def ingresa():
    user = str(request.form['usuario'])
    partida = str(request.form['partida'])
    oponente = str(request.form['oponente'])
    trealizados = str(request.form['trealizados'])
    tfallados = str(request.form['tfallados'])
    tacertados = str(request.form['tacertados'])
    resultado = str(request.form['resultado'])
    daño = str(request.form['daño'])
    lista = estructuras.lista_juegossss()
    abb.add_a_lista(abb.raiz, user,partida,oponente,trealizados,tfallados,racertados,resultado,daño)
    abb.muestra_lista(abb.raiz, user)
    return 'ya'

############################## Matriz ####################################################
@app.route('/ingresaMatriz', methods=['POST'])
def ingresa():
    user = str(request.form['usuario'])
    partida = str(request.form['partida'])
    barco = str(request.form['barco'])
    posx = str(request.form['posx'])
    posy = str(request.form['posy'])

    lista = estructuras.lista_juegossss()
    abb.add_a_matriz(abb.raiz, user,partida,barco,posx,posy)
    abb.grafica_matriz(abb.raiz, user, partida)
    return 'ya'

if __name__ == "__main__":
    app.run()