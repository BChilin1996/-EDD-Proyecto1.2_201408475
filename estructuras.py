import os
#NODO MATRIZ
class NodoMatriz:

    def __init__(self, bandera, yes, equis):
        self.bandera = bandera
        self.yes = yes
        self.equis = equis
        self.arriba = None
        self.abajo = None
        self.derecha = None
        self.izquierda = None
        self.atras = None
        self.adelante = None

    def getBandera(self):
        return self.bandera

    def setBandera(self, nCorreo):
        self.bandera = nCorreo

    def getYes(self):
        return self.yes

    def getEquis(self):
        return self.equis


#MATRIZ
class Matriz:

    def __init__(self):
        self.inicioHorizontal = None
        self.inicioVertical = None

    def ingresar(self, bandera, yes, equis):
        nuevoNodoMatriz = NodoMatriz(bandera, yes, equis)

        if self.vacioHorizont() == True:
            nuevoNodoHorizontal = NodoMatriz("","",equis)
            self.inicioHorizontal = nuevoNodoHorizontal

        if self.vacioVerti() == True:
            nuevoNodoVertical = NodoMatriz("",yes,"")
            self.inicioVertical = nuevoNodoVertical

        ################# CREACION CABECERA HORIZONTAL #################

        tempHorizont = self.inicioHorizontal

        if self.existeHorizont(equis) == True:
            while tempHorizont.getEquis() != equis:
                tempHorizont = tempHorizont.derecha

        else:
            nuevoNodoHorizontal = NodoMatriz("","",equis)
            temp2 = None
            while tempHorizont != None and tempHorizont.getEquis() < equis:
                temp2 = tempHorizont
                tempHorizont = tempHorizont.derecha

            if tempHorizont != None and tempHorizont.getEquis() > equis:

                if tempHorizont == self.inicioHorizontal:
                    temp4 = self.inicioHorizontal
                    tempHorizont = nuevoNodoHorizontal
                    tempHorizont.izquierda = None
                    tempHorizont.derecha = temp4
                    temp4.izquierda = tempHorizont
                    self.inicioHorizontal = tempHorizont

                else:
                    temp4 = tempHorizont
                    tempHorizont = nuevoNodoHorizontal
                    temp2.derecha = tempHorizont
                    tempHorizont.derecha = temp4
                    temp4.izquierda = tempHorizont
                    tempHorizont.izquierda = temp2

            else:
                tempHorizont = nuevoNodoHorizontal
                temp2.derecha = tempHorizont
                tempHorizont.izquierda = temp2

        ################# APUNTADORES CON CABECERA HORIZONTAL #################

        if tempHorizont.abajo != None:
            temp5 = None
            while tempHorizont.abajo != None:
                temp5 = tempHorizont
                tempHorizont = tempHorizont.abajo
                if  tempHorizont.getYes() == yes or tempHorizont.getYes() > yes:
                    break

        if tempHorizont.getYes() == yes:
            if tempHorizont.atras != None:
                while tempHorizont.atras != None:
                    tempHorizont = tempHorizont.atras
            tempHorizont.atras = nuevoNodoMatriz
            nuevoNodoMatriz.adelante = tempHorizont

        elif tempHorizont.abajo != None and tempHorizont.abajo.getYes() > yes:
            temp6 = tempHorizont.abajo
            tempHorizont = nuevoNodoMatriz
            temp5.abajo = tempHorizont
            tempHorizont.abajo = temp6
            temp6.arriba = tempHorizont
            tempHorizont.arriba = temp5

        elif tempHorizont != None and tempHorizont.getYes() > yes:
            temp6 = tempHorizont
            tempHorizont = nuevoNodoMatriz
            temp5.abajo = tempHorizont
            tempHorizont.abajo = temp6
            temp6.arriba = tempHorizont
            tempHorizont.arriba = temp5

        else:
            tempHorizont.abajo = nuevoNodoMatriz
            nuevoNodoMatriz.arriba = tempHorizont

        ################# CREACION DE CABECERA VERTICAL #################

        tempVerti = self.inicioVertical

        if self.existeVerti(yes) == True:
            while tempVerti.getYes() != yes:
                tempVerti = tempVerti.abajo

        else:
            nuevoNodoVertical = NodoMatriz("", yes, "")
            temp3 = None
            while tempVerti != None and tempVerti.getYes() < yes:
                temp3 = tempVerti
                tempVerti = tempVerti.abajo

            if tempVerti != None and tempVerti.getYes() > yes:
                if tempVerti == self.inicioVertical:
                    temp4 = self.inicioVertical
                    tempVerti = nuevoNodoVertical
                    tempVerti.arriba = None
                    tempVerti.abajo = temp4
                    temp4.arriba = tempVerti
                    self.inicioVertical = tempVerti

                else:
                    temp4 = tempVerti
                    tempVerti = nuevoNodoVertical
                    temp3.abajo = tempVerti
                    tempVerti.abajo = temp4
                    temp4.arriba = tempVerti
                    tempVerti.arriba = temp3

            else:
                tempVerti = nuevoNodoVertical
                temp3.abajo = tempVerti
                tempVerti.arriba = temp3

        ################# INICIA APUNTADORES CON CABECERA VERTICAL #################

        if tempVerti.derecha != None:
            temp5 = None
            while tempVerti.derecha != None:
                temp5 = tempVerti
                tempVerti = tempVerti.derecha
                if  tempVerti.getEquis() == equis or tempVerti.getEquis() > equis:
                    break

        if tempVerti.getEquis() == equis and tempVerti.getBandera() != bandera:
            return

        elif tempVerti.derecha != None and tempVerti.derecha.getEquis() > equis:
            temp6 = tempVerti
            tempVerti = nuevoNodoMatriz
            temp5.derecha = tempVerti
            tempVerti.derecha = temp6
            temp6.izquierda = tempVerti
            tempVerti.izquierda = temp5

        elif tempVerti != None and  tempVerti.getEquis() != "" and tempVerti.getEquis() > equis:
            temp6 = tempVerti
            tempVerti = nuevoNodoMatriz
            temp5.derecha = tempVerti
            tempVerti.derecha = temp6
            temp6.izquierda = tempVerti
            tempVerti.izquierda = temp5

        else:
            tempVerti.derecha = nuevoNodoMatriz
            nuevoNodoMatriz.izquierda = tempVerti

    def vacioHorizont(self):
        if self.inicioHorizontal == None:
            return True
        else:
            return False

    def vacioVerti(self):
        if self.inicioVertical == None:
            return True
        else:
            return False

    def existeVerti(self, yes):
        temporal = self.inicioVertical
        while temporal != None:
            if temporal.getYes() == yes:
                return True
            else:
                temporal = temporal.abajo

        return False

    def existeHorizont(self, equis):
        temp = self.inicioHorizontal

        while temp != None:
            if temp.getEquis() == equis:
                return True
            else:
                temp = temp.derecha

        return False

    def buscarPorYes(self, yes):
        if self.vacioVerti() == False:
            aux = self.inicioVertical
            while aux != None and aux.getYes() != yes:
                aux = aux.abajo

            if aux.getYes() == yes:
                if aux.derecha != None:
                    cadena = ""
                    aux = aux.derecha
                    while aux != None:
                        cadena = cadena + aux.getBandera() + "@" + aux.getEquis() +"\n"
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                cadena = cadena + aux2.getBandera() + "@" + aux2.getEquis() + "\n"
                                aux2 = aux2.atras
                        aux = aux.derecha

                    return cadena


    def buscarPorEquis(self, equis):
        if self.vacioHorizont() == False:
            aux = self.inicioHorizontal
            while aux != None and aux.getEquis() != equis:
                aux = aux.derecha

            if aux.getEquis() == equis:
                if aux.abajo != None:
                    cadena = ""
                    aux = aux.abajo
                    while aux != None:
                        cadena = cadena + aux.getBandera() + "@" + aux.getEquis() +" || Letra = "+ aux.getYes()+"\n"
                        if aux.atras != None:
                            aux2 = aux.atras
                            while aux2 != None:
                                cadena = cadena + aux2.getBandera() + "@" + aux2.getEquis() +" || Letra = "+ aux.getYes()+"\n"
                                aux2 = aux2.atras
                        aux = aux.abajo

                    return cadena

    def eliminar(self, bandera, yes, equis):
        tempHorizont = self.inicioHorizontal
        tempVerti = self.inicioVertical
        temp1 = temp2 = None

        while tempHorizont != None and tempHorizont.getEquis() != equis:
            temp1 = tempHorizont
            tempHorizont = tempHorizont.derecha

        while tempVerti != None and tempVerti.getYes() != yes:
            temp2 = tempVerti
            tempVerti = tempVerti.abajo

        if tempHorizont != None and tempVerti != None and tempHorizont.getEquis() == equis and tempVerti.getYes() == yes:

            while tempHorizont != None and tempHorizont.getYes() != yes:
                temp3 = tempHorizont
                tempHorizont = tempHorizont.abajo

            while tempVerti != None and tempVerti.getEquis() != equis:
                temp4 = tempVerti
                tempVerti = tempVerti.derecha

            if tempHorizont != None and tempHorizont.atras != None:
                while tempHorizont.atras != None and tempHorizont.getBandera() != bandera:
                    temp3 = tempHorizont
                    tempHorizont = tempHorizont.atras

            if tempVerti != None and tempVerti.atras != None:
                while tempVerti.atras != None and tempVerti.getBandera() != bandera:
                    temp4 = tempVerti
                    tempVerti = tempVerti.atras

            ################ EMPIEZA ELIMINACION DE NODOS EN CABECERA HORIZONTAL
            if tempHorizont != None and tempHorizont.getBandera() == bandera:
                if temp3 != None and temp3.getBandera() == "":
                    if tempHorizont.atras != None:
                        temp3.abajo = tempHorizont.atras
                        tempHorizont.atras.arriba = temp3
                        if tempHorizont.abajo != None:
                            tempHorizont.atras.abajo = tempHorizont.abajo
                            tempHorizont.abajo.arriba = tempHorizont.atras
                    elif tempHorizont.abajo != None:
                        temp3.abajo = tempHorizont.abajo
                        tempHorizont.abajo.arriba = temp3
                    else:
                        temp3.abajo = None
                        if temp1 != None and temp3.derecha != None:
                            temp1.derecha = temp3.derecha
                            temp3.derecha.izquierda = temp1
                            temp3 = None
                        elif temp1 != None:
                            temp1.derecha = None
                            temp3 = None
                        elif temp3.derecha != None:
                            temp3.derecha.izquierda = None
                            self.inicioHorizontal = temp3.derecha
                            temp3 = None
                        else:
                            temp3 = self.inicioHorizontal = None

                elif temp3 != None:
                    if tempHorizont.adelante != None:
                        if tempHorizont.atras != None:
                            temp3.atras = tempHorizont.atras
                            tempHorizont.atras.adelante = temp3
                        else:
                            temp3.atras = None
                    elif tempHorizont.atras != None:
                        temp3.abajo = tempHorizont.atras
                        if tempHorizont.abajo != None:
                            tempHorizont.atras.abajo = tempHorizont.abajo
                            tempHorizont.abajo.arriba = tempHorizont.atras
                        tempHorizont.atras.arriba = temp3
                    elif tempHorizont.abajo != None:
                        temp3.abajo = tempHorizont.abajo
                        tempHorizont.abajo.arriba = temp3
                    else:
                        temp3.abajo = None

            ################ EMPIEZA ELIMINACION DE NODOS EN CABECERA VERTICAL
            if tempVerti != None and tempVerti.getBandera() == bandera:
                if temp4 != None and temp4.getBandera() == "":
                    if tempVerti.atras != None:
                        temp4.derecha = tempVerti.atras
                        tempVerti.atras.izquierda = temp4
                        if tempVerti.derecha != None:
                            tempVerti.atras.derecha = tempVerti.derecha
                            tempVerti.derecha.izquierda = tempVerti.atras
                    elif tempVerti.derecha != None:
                        temp4.derecha = tempVerti.derecha
                        tempVerti.derecha.izquierda = temp4
                    else:
                        temp4.derecha = None
                        if temp2 != None and temp4.abajo != None:
                            temp2.abajo = temp4.abajo
                            temp4.abajo.arriba = temp2
                            temp4 = None
                        elif temp2 != None:
                            temp2.abajo = None
                            temp4 = None
                        elif temp4.abajo != None:
                            temp4.abajo.arriba = None
                            self.inicioVertical = temp4.abajo
                            temp4 = None
                        else:
                            temp4 = self.inicioVertical = None
                elif temp4 != None:
                    if tempVerti.adelante != None:
                        if tempVerti.atras != None:
                            temp4.atras = tempVerti.atras
                            tempVerti.atras.adelante = temp4
                        else:
                            temp4.atras = None
                    elif tempVerti.atras != None:
                        temp4.derecha = tempVerti.atras
                        if tempVerti.derecha != None:
                            tempVerti.atras.derecha = tempVerti.derecha
                            tempVerti.derecha.izquierda = tempVerti.atras
                        tempVerti.atras.izquierda = temp4
                    elif tempVerti.derecha != None:
                        temp4.derecha = tempVerti.derecha
                        tempVerti.derecha.izquierda = temp4
                    else:
                        temp4.derecha = None

    def hacerGrafica(self):
        if self.vacioHorizont() == True or self.vacioVerti() == True:
            return
        else:
            file = open("matriz.dot", "w")
            file.write("digraph G\n{\n")
            tempHorizont = self.inicioHorizontal
            tempVerti = self.inicioVertical
            file.write("\"INICIO\"[label = \"Inicio\", style = filled, fillcolor=\"#0D5A73\", fontcolor=\"#A2E7FF\", shape=box]\n")
            file.write("\"INICIO\" -> \"n" + str(tempVerti.getYes()) + "\"\n")
            while tempVerti != None:
                file.write("\"n" + str(tempVerti.getYes()) + "\"[label = \"" + str(tempVerti.getYes()) + "\", style = filled, fillcolor=\"#E1E16E\", fontcolor=\"#040404\", shape=box]\n")
                if (tempVerti.abajo != None):
                    file.write("\"n" + str(tempVerti.getYes()) + "\" -> \"n" + str(tempVerti.abajo.getYes()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(tempVerti.abajo.getYes()) + "\" -> \"n" + str(tempVerti.getYes()) + "\"\n")

                if (tempVerti.derecha != None):
                    file.write("\"n" + str(tempVerti.derecha.getYes()) + "," + str(
                        tempVerti.derecha.getBandera()) + "," + str(
                        tempVerti.derecha.getEquis()) + "\"[label = \"" + str(
                        tempVerti.derecha.getBandera()) + "\", style = filled, fillcolor=\"#5C5C5A\", fontcolor=\"#FCFC29\", shape=circle]\n")
                    file.write("\"n" + str(tempVerti.getYes()) + "\" -> \"n" + str(tempVerti.derecha.getYes()) + ","+ str(tempVerti.derecha.getBandera()) +","+ str(tempVerti.derecha.getEquis()) + "\"[constraint=false];\n")
                    file.write("\"n" + str(tempVerti.derecha.getYes()) + ","+ str(tempVerti.derecha.getBandera()) +","+ str(tempVerti.derecha.getEquis()) + "\" -> \"n" + str(tempVerti.getYes()) + "\"[constraint=false];\n")
                    file.write("{rank=same; \"n" + str(tempVerti.getYes()) + "\"  \"n" + str(tempVerti.derecha.getYes()) + ","+ str(tempVerti.derecha.getBandera()) +","+ str(tempVerti.derecha.getEquis()) + "\"}\n")
                    file.write("{rank=same; \"n" + str(tempVerti.derecha.getYes()) + ","+ str(tempVerti.derecha.getBandera()) +","+ str(tempVerti.derecha.getEquis()) + "\"  \"n" + str(tempVerti.getYes()) + "\"}\n")
                    AUXtempVerti = tempVerti.derecha

                while (AUXtempVerti.derecha != None):
                    file.write("\"n" + str(AUXtempVerti.derecha.getYes()) + ","+ str(AUXtempVerti.derecha.getBandera()) +","+ str(AUXtempVerti.derecha.getEquis()) +"\"[label = \""
                               + str(AUXtempVerti.derecha.getBandera()) + "\", style = filled, fillcolor=\"#5C5C5A\", fontcolor=\"#FCFC29\", shape=circle]\n")
                    file.write("\"n" + str(AUXtempVerti.getYes()) + ","+ str(AUXtempVerti.getBandera()) +","+ str(AUXtempVerti.getEquis()) + "\" -> \"n"
                               + str(AUXtempVerti.derecha.getYes()) + ","+ str(AUXtempVerti.derecha.getBandera()) +","+ str(AUXtempVerti.derecha.getEquis()) + "\"[constraint=false];\n")
                    file.write("\"n" + str(AUXtempVerti.derecha.getYes()) + ","+ str(AUXtempVerti.derecha.getBandera()) +","+ str(AUXtempVerti.derecha.getEquis())
                               + "\" -> \"n" + str(AUXtempVerti.getYes()) + ","+ str(AUXtempVerti.getBandera()) +","+ str(AUXtempVerti.getEquis()) + "\"[constraint=false];\n")
                    file.write("{rank=same; \"n" + str(AUXtempVerti.getYes()) + ","+ str(AUXtempVerti.getBandera()) +","+ str(AUXtempVerti.getEquis()) + "\" \"n" + str(AUXtempVerti.derecha.getYes())
                               + ","+ str(AUXtempVerti.derecha.getBandera()) +","+ str(AUXtempVerti.derecha.getEquis()) + "\"}\n");
                    file.write("{rank=same; \"n" + str(AUXtempVerti.derecha.getYes()) + ","+ str(AUXtempVerti.derecha.getBandera()) +","+ str(AUXtempVerti.derecha.getEquis()) + "\" \"n"
                               + str(AUXtempVerti.getYes()) + ","+ str(AUXtempVerti.getBandera()) +","+ str(AUXtempVerti.getEquis()) + "\"}\n");

                    AUXtempVerti = AUXtempVerti.derecha

                tempVerti = tempVerti.abajo


            file.write("\"INICIO\" -> \"n" + str(tempHorizont.getEquis()) + "\"\n")
            file.write("{rank=same; \"INICIO\"  \"n" + str(tempHorizont.getEquis()) + "\"}\n")
            while tempHorizont != None:
                file.write("\"n" + str(tempHorizont.getEquis()) + "\"[label = \"" + str(tempHorizont.getEquis()) + "\", style = filled, fillcolor=\"#E1E16E\", fontcolor=\"#040404\", shape=box]\n")
                if (tempHorizont.derecha != None):
                    file.write("\"n" + str(tempHorizont.getEquis()) + "\" -> \"n" + str(tempHorizont.derecha.getEquis()) + "\"\n")
                    file.write("\"n" + str(tempHorizont.derecha.getEquis()) + "\" -> \"n" + str(tempHorizont.getEquis()) + "\"\n")
                    file.write("{rank=same; \"n" + str(tempHorizont.getEquis()) + "\"  \"n" + str(tempHorizont.derecha.getEquis()) + "\"}\n")
                    file.write("{rank=same; \"n" + str(tempHorizont.derecha.getEquis()) + "\"  \"n" + str(tempHorizont.getEquis()) + "\"}\n")

                if (tempHorizont.abajo != None):
                    file.write("\"n" + str(tempHorizont.getEquis()) + "\" -> \"n" + str(tempHorizont.abajo.getYes()) + ","+ str(tempHorizont.abajo.getBandera()) +","+ str(tempHorizont.abajo.getEquis()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(tempHorizont.abajo.getYes()) + ","+ str(tempHorizont.abajo.getBandera()) +","+ str(tempHorizont.abajo.getEquis()) + "\" -> \"n" + str(tempHorizont.getEquis()) + "\"\n")
                    AUXtempHorizont = tempHorizont.abajo

                while (AUXtempHorizont.abajo != None):
                    file.write("\"n" + str(AUXtempHorizont.getYes()) + ","+ str(AUXtempHorizont.getBandera()) +","+ str(AUXtempHorizont.getEquis()) + "\" -> \"n"
                               + str(AUXtempHorizont.abajo.getYes()) + ","+ str(AUXtempHorizont.abajo.getBandera()) +","+ str(AUXtempHorizont.abajo.getEquis()) + "\"[rankdir=UD];\n")
                    file.write("\"n" + str(AUXtempHorizont.abajo.getYes()) + ","+ str(AUXtempHorizont.abajo.getBandera()) +","+ str(AUXtempHorizont.abajo.getEquis())
                               + "\" -> \"n" + str(AUXtempHorizont.getYes()) + ","+ str(AUXtempHorizont.getBandera()) +","+ str(AUXtempHorizont.getEquis()) + "\"\n")

                    AUXtempHorizont = AUXtempHorizont.abajo

                tempHorizont = tempHorizont.derecha

            file.write("subgraph cluster_0 {\n")
            file.write("style=filled;\n")
            file.write("color=grey;\n")
            file.write("node [style=filled,color=white];\n")

            tempVerti = self.inicioVertical
            while tempVerti != None:

                if (tempVerti.derecha != None):
                    AUXtempVerti = tempVerti.derecha

                while (AUXtempVerti.derecha != None):
                    if AUXtempVerti.atras != None:
                        file.write("\"extra" + str(AUXtempVerti.getEquis()) + "\"[label = \"" + str(AUXtempVerti.derecha.getEquis()) + "\", style = filled, shape=box]\n")

                    if AUXtempVerti.atras != None:
                        file.write("\"extra" + str(AUXtempVerti.getEquis()) + "\"[label = \"" + str(
                            AUXtempVerti.getEquis()) + "\", style = filled, shape=box]\n")
                        file.write("\"n" + str(AUXtempVerti.atras.getYes()) + "," + str(
                            AUXtempVerti.atras.getBandera()) + "," + str(
                            AUXtempVerti.atras.getEquis()) + "\"[label = \"" + str(
                            AUXtempVerti.atras.getBandera())  + "\", style = filled, shape=circle]\n")
                        file.write("\"extra" + str(AUXtempVerti.getEquis()) + "\" -> \"n" + str(AUXtempVerti.atras.getYes()) + "," + str(
                            AUXtempVerti.atras.getBandera()) + "," + str(
                            AUXtempVerti.atras.getEquis()) +"\"\n")
                        file.write("\"n" + str(AUXtempVerti.atras.getYes()) + "," + str(
                            AUXtempVerti.atras.getBandera()) + "," + str(
                            AUXtempVerti.atras.getEquis()) + "\" -> \"extra" + str(AUXtempVerti.getEquis()) +"\"\n")
                        AUX2Verti = AUXtempVerti.atras

                        while (AUX2Verti.atras != None):
                            file.write("\"n" + str(AUX2Verti.atras.getYes()) + ","+ str(AUX2Verti.atras.getBandera()) +","+ str(AUX2Verti.atras.getEquis()) +"\"[label = \"" + str(AUX2Verti.atras.getBandera()) + "\", style = filled, shape=circle]\n")
                            file.write("\"n" + str(AUX2Verti.getYes()) + ","+ str(AUX2Verti.getBandera()) +","+ str(AUX2Verti.getEquis()) + "\" -> \"n"
                                       + str(AUX2Verti.atras.getYes()) + ","+ str(AUX2Verti.atras.getBandera()) +","+ str(AUX2Verti.atras.getEquis()) + "\"\n")
                            file.write("\"n" + str(AUX2Verti.atras.getYes()) + ","+ str(AUX2Verti.atras.getBandera()) +","+ str(AUX2Verti.atras.getEquis())
                                       + "\" -> \"n" + str(AUX2Verti.getYes()) + ","+ str(AUX2Verti.getBandera()) +","+ str(AUX2Verti.getEquis()) + "\"\n")

                            AUX2Verti = AUX2Verti.atras

                    AUXtempVerti = AUXtempVerti.derecha


                if AUXtempVerti.atras != None:
                    file.write("\"extra" + str(AUXtempVerti.getEquis()) + "\"[label = \"" + str(
                        AUXtempVerti.getEquis()) + "\", style = filled, shape=box]\n")
                    file.write("\"n" + str(AUXtempVerti.atras.getYes()) + "," + str(
                            AUXtempVerti.atras.getBandera()) + "," + str(
                            AUXtempVerti.atras.getEquis()) + "\"[label = \"" + str(
                            AUXtempVerti.atras.getBandera())  + "\", style = filled, shape=circle]\n")
                    file.write("\"extra" + str(AUXtempVerti.getEquis()) + "\" -> \"n" + str(AUXtempVerti.atras.getYes()) + "," + str(
                            AUXtempVerti.atras.getBandera()) + "," + str(
                            AUXtempVerti.atras.getEquis()) + "\"\n")
                    file.write("\"n" + str(AUXtempVerti.atras.getYes()) + "," + str(
                            AUXtempVerti.atras.getBandera()) + "," + str(
                            AUXtempVerti.atras.getEquis()) + "\" -> \"extra" + str(AUXtempVerti.getEquis()) +"\"\n")
                    AUX2Verti = AUXtempVerti.atras

                    while (AUX2Verti.atras != None):
                        file.write("\"n" + str(AUX2Verti.atras.getYes()) + ","+ str(AUX2Verti.atras.getBandera()) +","+ str(AUX2Verti.atras.getEquis()) +"\"[label = \"" + str(AUX2Verti.atras.getBandera()) + "\", style = filled, shape=circle]\n")
                        file.write("\"n" + str(AUX2Verti.getYes()) + ","+ str(AUX2Verti.getBandera()) +","+ str(AUX2Verti.getEquis()) + "\" -> \"n"
                            + str(AUX2Verti.atras.getYes()) + ","+ str(AUX2Verti.atras.getBandera()) +","+ str(AUX2Verti.atras.getEquis()) + "\"\n")
                        file.write("\"n" + str(AUX2Verti.atras.getYes()) + ","+ str(AUX2Verti.atras.getBandera()) +","+ str(AUX2Verti.atras.getEquis())
                            + "\" -> \"n" + str(AUX2Verti.getYes()) + ","+ str(AUX2Verti.getBandera()) +","+ str(AUX2Verti.getEquis()) + "\"\n")

                        AUX2Verti = AUX2Verti.atras

                tempVerti = tempVerti.abajo

            file.write("label = \"PROFUNDIDAD\";\n")
            file.write("}\n")
            file.write("}")
            file.close()
            os.system("dot -Tjpg matriz.dot > matriz.jpg")

# .
# .
# .
# .
# .
# .
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -
# -


#NODO LISTA USUARIOS
class Nodo:
    def __init__(self, nombrePartida, oponente, tiros_realizados,tiros_acertados,tiros_fallados,resultado,daño, matrix):
        self.nombrePartida = nombrePartida
        self.oponente = oponente
        self.tiros_realizados = tiros_realizados
        self.tiros_acertados = tiros_acertados
        self.tiros_fallados = tiros_fallados
        self.resultado = resultado
        self.daño = daño
        self.matrix = matrix
        self.siguiente = None
        self.anterior = None

    def get_nombrePartida(self):
        return self.nombrePartida

    def get_matrix(self):
        return self.matrix

    def get_oponente(self):
        return self.oponente

    def get_tiros_realizados(self):
        return self.tiros_realizados

    def get_tiros_acertados(self):
        return self.tiros_acertados

    def get_tiros_fallados(self):
        return self.tiros_fallados

    def get_resultado(self):
        return self.resultado

    def get_daño(self):
        return self.daño

#LISTA USUARIOS
class lista_juegossss:
    def __init__(self):
        self.inicio = None
        self.ultimo = None

    def vacia(self):
       return self.inicio==None

    def insertar(self, nombre, oponente, tiros_realizados, tiros_acertados, tiros_fallados, resultado, daño):
        matri = Matriz()
        if self.vacia():
            self.inicio = self.ultimo = Nodo(nombre, oponente, tiros_realizados, tiros_acertados, tiros_fallados, resultado, daño, matri)
        else:
            aux=self.ultimo
            self.ultimo=aux.siguiente = Nodo(nombre, oponente, tiros_realizados, tiros_acertados, tiros_fallados, resultado, daño, matri)
            self.ultimo.anterior = aux


    def mostrar(self):
       aux = self.inicio
       cadena= ""
       print("Oponente" +"    " +"T Realizados"+" " +"T Acertados"+" " +"T Fallados"+" "+"Resultado"+" "+"Daños")
       while aux:

           cadena=str(aux.oponente)+"          "+ str(aux.tiros_realizados)+"            "+ str(aux.tiros_acertados)+"            "+ str(aux.tiros_fallados)+"    "+ str(aux.resultado)+"    "+ str(aux.daño)
           print(cadena)
           aux = aux.siguiente

    def add_matrix(self, juego, bandera, x, y):
        if self.vacia() == False:
            aux = self.inicio
            while aux != self.ultimo:
                if juego != aux.get_nombrePartida():
                    aux = aux.siguiente
                else:
                    aux.get_matrix().ingresar(bandera, y, x)
                    return

            if juego == aux.get_nombrePartida():
                aux.get_matrix().ingresar(bandera, y, x)
                return


    def grafica_matrix(self, juego):
        if self.vacia() == False:
            aux = self.inicio
            while aux != self.ultimo:
                if juego != aux.get_nombrePartida():
                    aux = aux.siguiente
                else:
                    aux.get_matrix().hacerGrafica()
                    return

            if juego == aux.get_nombrePartida():
                aux.get_matrix().hacerGrafica()
                return


    def grafica_lista(self):
        if self.vacia() == False:
            archivo = open("grafica_lista.dot", "w")
            archivo.write("Digraph G {\n")
            aux = self.inicio
            i = 0
            while aux != self.ultimo:
                archivo.write("\"Nodo"+str(i)+"\"[label = \""+aux.get_nombrePartida()+" "+aux.get_oponente()+"\" style=filled]\n")
                archivo.write("\"Nodo"+str(i)+"\" -> \"Nodo"+str(i+1)+"\"[constraint=false];\n")
                archivo.write("\"Nodo"+str(i+1)+"\" -> \"Nodo"+str(i)+"\"[constraint=false];\n")
                i = i + 1
                aux = aux.siguiente

            archivo.write("\"Nodo" + str(i) + "\"[label = \"" + aux.get_nombrePartida() + " " + aux.get_oponente() + "\" style=filled]\n")
            archivo.write("\"Nodo"+str(i)+"\" -> \"Nodo"+str(0)+"\"[constraint=false];\n")
            archivo.write("\"Nodo"+str(0)+"\" -> \"Nodo"+str(i)+"\"[constraint=false];\n")

            archivo.write("}")
            archivo.close()
            os.system("dot -Tpng grafica_lista.dot -o grafica_lista.png")


class NodoArbol:
    def __init__(self, usuario, contrasena ,conectado, listaJuegos):
        self.usuario=usuario
        self.contrasena=contrasena
        self.conectado=conectado
        self.lista = listaJuegos
        self.izq=None
        self.der=None

    def getLista(self):
        return self.lista

    def getUsuario(self):
        return self.usuario

    def getPass(self):
        return self.contrasena

    def __str__(self):
        return "%s %s %s" %(self.usuario,self.contrasena,self.conectado)

class ABinarios:
    def __init__(self):
        self.raiz=None

    def agregar(self,elemento):
        if self.raiz==None:
            self.raiz=elemento
        else:
            aux = self.raiz
            padre=None
            while aux!=None:
                padre=aux
                if elemento.usuario >= aux.usuario:
                    aux=aux.der
                else:
                    aux=aux.izq
            if elemento.usuario >= padre.usuario:
                padre.der= elemento
            else:
                padre.izq = elemento

    def add_a_lista(self, elemento, usuario, nombre, oponente, tiros_realizados, tiros_acertados, tiros_fallados, resultado, daño):
        if elemento != None:
            if str(elemento.getUsuario()) == str(usuario):
                elemento.getLista().insertar(nombre, oponente, tiros_realizados, tiros_acertados, tiros_fallados, resultado, daño)
            else:
                self.add_a_lista(elemento.izq, usuario, nombre, oponente, tiros_realizados, tiros_acertados, tiros_fallados, resultado, daño)
                self.add_a_lista(elemento.der, usuario, nombre, oponente, tiros_realizados, tiros_acertados, tiros_fallados, resultado, daño)

    def add_a_matriz(self, elemento, usuario, nombre, bandera, x, y):
        if elemento != None:
            if str(elemento.getUsuario()) == str(usuario):
                elemento.getLista().add_matrix(nombre, bandera, x, y)
            else:
                self.add_a_matriz(elemento.izq, usuario, nombre, bandera, x, y)
                self.add_a_matriz(elemento.der, usuario, nombre, bandera, x, y)

    def muestra_lista(self, elemento, usuario):
        if elemento != None:
            if str(elemento.getUsuario()) == str(usuario):
                elemento.getLista().mostrar()
                elemento.getLista().grafica_lista()
            else:
                self.muestra_lista(elemento.izq, usuario)
                self.muestra_lista(elemento.der, usuario)

    def grafica_matriz(self, elemento, usuario, juego):
        if elemento != None:
            if str(elemento.getUsuario()) == str(usuario):
                elemento.getLista().grafica_matrix(juego)
            else:
                self.grafica_matriz(elemento.izq, usuario, juego)
                self.grafica_matriz(elemento.der, usuario, juego)

    def login(self, elemento, usuario, contra):
        if elemento != None:
                if str(elemento.getUsuario()) == str(usuario) and str(elemento.getPass()) == contra:
                    return True
                else:
                    return self.login(elemento.izq, usuario, contra)
                    return self.login(elemento.der, usuario, contra)


    def preorder(self,elemento):
        if elemento!=None:
            print(elemento)
            self.preorder(elemento.izq)
            self.preorder(elemento.der)

    def inorder(self, elemento):
        if elemento != None:
            self.inorder(elemento.izq)
            print(elemento)
            self.inorder(elemento.der)

    def postorder(self, elemento):
        if elemento != None:
            self.postorder(elemento.izq)
            self.postorder(elemento.der)
            print(elemento)


    def getRaiz(self):
        return self.raiz

    # def profundidad(self, arbol):
    #     if arbol != None:
    #         if self.profundidad(arbol.der) > self.profundidad(arbol.izq):
    #             return self.profundidad(arbol.der) + 1
    #         else:
    #             return self.profundidad(arbol.izq) + 1

    def graficar(self, elemento):
        if elemento != None:
            archivo = open("grafica_ABB.dot", "w")
            archivo.write("Digraph G {\n")
            archivo.write("node[shape=record]\n")
            archivo, self.iteraNodos(archivo, elemento)
            self.iteraciones(archivo, elemento)
            archivo.write("}")
            archivo.close()
            os.system("dot -Tpng grafica_ABB.dot -o grafica_ABB.png")

    def iteraNodos(self, archivo, elemento):
        archivo.write("nod" + elemento.getUsuario() + "[label=\"<f0>|<f1> " + elemento.getUsuario() + "|<f2>\"]\n")
        if elemento.izq != None:
            self.iteraNodos(archivo, elemento.izq)
        if elemento.der != None:
            self.iteraNodos(archivo, elemento.der)

    def iteraciones(self, archivo, elemento):
        if  elemento.izq != None:
            archivo.write("nod"+elemento.getUsuario()+": f0 -> nod"+elemento.izq.getUsuario()+"\n")
        if elemento.der != None:
            archivo.write("nod"+elemento.getUsuario()+": f2 -> nod"+elemento.der.getUsuario()+"\n")
        if elemento.izq != None:
            self.iteraciones(archivo, elemento.izq)
        if elemento.der != None:
            self.iteraciones(archivo, elemento.der)





# if __name__ == "__main__":
#     ab = ABinarios()
#     while(True):
#         print("---Menu--\n"+
#               "1.Agregar\n"
#               "2.Preorden")
#         num=input("Ingrese la opcion")
#         if num=="1":
#             usuario=input("Ingrese el usuario")
#             contrasena=input("Ingrese la contraseña")
#             conectado="No"
#             nod = NodoArbol(usuario,contrasena,conectado)
#             ab.agregar(nod)
#         elif num=="2":
#             print("Imprimiendo por Preorden")
#             ab.preorder(ab.getRaiz())


l = lista_juegossss()
abb = ABinarios()
nodo = NodoArbol("rafa", "123", "si", l)
abb.agregar(nodo)
l = lista_juegossss()
nodo = NodoArbol("bryand", "555", "si", l)
abb.agregar(nodo)
l = lista_juegossss()
nodo = NodoArbol("jose", "abc", "no", l)
abb.agregar(nodo)
l = lista_juegossss()
nodo = NodoArbol("popo", "a25", "no", l)
abb.agregar(nodo)
l = lista_juegossss()
nodo = NodoArbol("r2d2", "558", "no", l)
abb.agregar(nodo)
l = lista_juegossss()
nodo = NodoArbol("antonio", "ffa", "si", l)
abb.agregar(nodo)
l = lista_juegossss()
nodo = NodoArbol("zamba", "f5s5", "si", l)
abb.agregar(nodo)
l = lista_juegossss()
nodo = NodoArbol("a1ma", "sasf", "si", l)
abb.agregar(nodo)
print("************************** PRE ORDEN *********************************")
abb.preorder(abb.raiz)
print("************************** EN ORDEN **********************************")
abb.inorder(abb.raiz)
print("************************** POST ORDEN ********************************")
abb.postorder(abb.raiz)
abb.graficar(abb.raiz)

print("************************** LISTA JUEGOS ******************************")
abb.add_a_lista(abb.raiz, "r2d2", "partida1", "DDDDDDD", 5, 6, 3, "ganador", 50)
abb.add_a_lista(abb.raiz, "r2d2", "partida2", "CCCCCCC", 5, 6, 3, "ganador", 60)
abb.add_a_lista(abb.raiz, "r2d2", "partida3", "AAAAAAA", 5, 6, 3, "ganador", 70)
abb.add_a_lista(abb.raiz, "r2d2", "partida4", "BBBBBBB", 5, 6, 3, "ganador", 80)
abb.muestra_lista(abb.raiz, "r2d2")
abb.add_a_matriz(abb.raiz, "r2d2", "partida4", "1", "x2", "y4")
abb.add_a_matriz(abb.raiz, "r2d2", "partida4", "1", "x5", "y2")
abb.add_a_matriz(abb.raiz, "r2d2", "partida4", "1", "x1", "y7")
abb.add_a_matriz(abb.raiz, "r2d2", "partida4", "1", "x3", "y5")
abb.grafica_matriz(abb.raiz, "r2d2", "partida4")
print("************************** PROFUNDIDAD ******************************")

