print ("Bienenido al sistema para diagnostico de dispositivos ")

nombre= input ("Cual es tu nombre ")

print ("Bienvenido", nombre )

dispositivo = int (input ("¿Cual es tu dispositivo? 1-  Celular 2-Computadora "))

if dispositivo == 1: 
    problema = int (input ("¿Que problema presentas 1-No enciende 2-No se escucha 3-Se traba "))

    if problema == 1: 
        bateria =input  ("¿Tiene bateria? (s/n) ") == "s"
        if bateria == "s":
            pantalla= input  ("¿Logras ver algo en la pantalla? (s/n)") == "s" 
            if pantalla == "n":
                print ("No tiene solucion")
    elif problema == 2: 
        volumen = input ("Tienes el volumen al maximo? (s/n)")
        if volumen == "s":
            print (nombre, "Te recomiendo llevar tu dispositivo a la plaza de la tecnologia ")
        if volumen == "n": 
            print ("Sube el volumen ")
    elif problema ==3 : 
        actualizar = input ("Tienes actualizaciones pendientes? (s/n)")
        if actualizar == "s":
            print ("Te recomiendo reiniciar tu ",dispositivo )
        if actualizar =="n":
            print ("Te recomiendo actualices el ", dispositivo) 

if dispositivo == 2: 
    problema = int (input ("¿Que problema presentas 1-No enciende 2-No se escucha 3-Se traba "))

    if problema == 1: 
            bateria =input  ("¿Tiene bateria? (s/n) ") == "s"
            if bateria == "s":
                pantalla= input  ("¿Logras ver algo en la pantalla? (s/n)") == "s" 
                if pantalla == "n":
                    print ("No tiene solucion")
    elif problema == 2: 
            volumen = input ("Tienes el volumen al maximo? (s/n)")
            if volumen == "s":
                print (nombre, "Te recomiendo llevar tu dispositivo a la plaza de la tecnologia ")
            if volumen == "n": 
                print ("Sube el volumen ")
    elif problema ==3 : 
            actualizar = input ("Tienes actualizaciones pendientes? (s/n)")
            if actualizar == "s":
                print ("Te recomiendo reiniciar tu ",dispositivo )
            if actualizar =="n":
                print ("Te recomiendo actualices el ", dispositivo) 







