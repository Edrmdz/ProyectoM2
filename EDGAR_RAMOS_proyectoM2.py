#Proyecto Modulo 2 ...
#1 logitud de una frase, indentificar la longitud de la palabra ingresada,
#La palabra correcta debe tener 4 a 8 letras

opcion = input("Indicador de cuadrantes (1) o Medidor de longitud de palabras (2): ")   #Menu para elegir programa
if opcion == '1':                                   #dirige a programa de los cuadrantes
    palabra = str(input("Ingresa una palabra: "))    #ingresando palabra
    tamano = len(palabra)                       #guardando tamaño en variable
#print ("tamaño de la palabra es ", tamano)

    if tamano >3 and tamano <9:                 # comparando si esta entre 4 a 8 letras
        print ("Palabra correcta")
    elif tamano < 4:
        print ("Faltan letras, solo tienes", tamano, " letras,")
    elif tamano > 8:
        print("Sobran letras, tiene ", tamano, " letras")
            #break
# segundo programa
# ingresa coordenadas e identifica el cuadrante. 
#no se permite ceros
if opcion == '2':                                           # dirige al programa de las coordenadas
    x = int(input("Ingresa el valor de X: "))               #Ingresa valor de X
    while x == 0:                                           #compara que sea cero, se sale del ciclo al ser diferente de cero
        print ("No se permite CERO, ingresa otro valor")
        x = int(input("Ingresa el valor de X: "))           #pide otro valor y lo guarda en la misma variable, se reinicia ciclo

    y = int(input("Ingresa el valor de Y: "))               #ingresa valor de Y
    while y == 0:                                           #ciclo while para no guardar valor de cero                                     
        print ("No se permite CERO, ingresa otro valor")
        x = int(input("Ingresa el valor de y: "))

    print ("La coordenada es ", x, ",", y,)                 #se imprime formato de coordenadas.              

    if x>0 and y>0:                                         # X,Y 
        print("Esta en el Cuadrante I")
    if x>0 and y<0:                                         # X,-Y
        print("Esta en el Cuadrante IV")
    if x<0 and y>0:                                         #-X.Y
        print("Esta en el Cuadrante II")                    
    if x<0 and y<0:                                         #-X,-X
        print("Esta en el Cuadrante III")


