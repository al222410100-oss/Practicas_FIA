print("Bienenido al sistema para diagnostico de dispositivos ")

nombre = input("Cual es tu nombre ")

print("Bienvenido", nombre)

dispositivo = int(input("¿Cual es tu dispositivo? 1- Celular 2-Computadora "))

if dispositivo == 1: 
    problema = int(input("¿Que problema presentas 1-No enciende 2-No se escucha 3-Se traba "))

    if problema == 1: 
        bateria = input("¿Tiene bateria? (s/n) ")
        if bateria == "s":
            pantalla = input("¿Logras ver algo en la pantalla? (s/n) ") 
            if pantalla == "n":
                print("No tiene solucion, llévalo a reparar la pantalla")
            if pantalla == "s":
                print("Te recomiendo forzar el reinicio de tu celular")
        if bateria == "n":
            print("Carga tu celular por al menos 15 minutos e intenta encenderlo de nuevo")

    elif problema == 2: 
        volumen = input("Tienes el volumen al maximo? (s/n) ")
        if volumen == "s":
            print(nombre, "Te recomiendo llevar tu dispositivo a la plaza de la tecnologia ")
        if volumen == "n": 
            print("Sube el volumen ")

    elif problema == 3: 
        actualizar = input("Tienes actualizaciones pendientes? (s/n) ")
        if actualizar == "s":
            print("Te recomiendo actualices el celular")
        if actualizar == "n":
            print("Te recomiendo reiniciar tu celular para liberar memoria RAM")

if dispositivo == 2: 
    problema = int(input("¿Que problema presentas 1-No enciende 2-No se escucha 3-Se traba "))

    if problema == 1: 
        cargador = input("¿Esta conectada a la corriente o tiene bateria? (s/n) ")
        if cargador == "s":
            pantalla = input("¿Logras ver algo en la pantalla o prende algun LED? (s/n) ") 
            if pantalla == "n":
                print("No tiene solucion simple, puede ser falla de la tarjeta madre o pantalla")
            if pantalla == "s":
                print("Intenta conectar la computadora a un monitor externo")
        if cargador == "n":
            print("Conecta el cargador a la computadora e intenta de nuevo")

    elif problema == 2: 
        volumen = input("Tienes el volumen al maximo? (s/n) ")
        if volumen == "s":
            print(nombre, "Te recomiendo llevar tu dispositivo a la plaza de la tecnologia ")
        if volumen == "n": 
            print("Sube el volumen en la barra de tareas ")

    elif problema == 3: 
        actualizar = input("Tienes actualizaciones pendientes? (s/n) ")
        if actualizar == "s":
            print("Te recomiendo actualices la computadora")
        if actualizar == "n":
            print("Abre el Administrador de tareas y cierra los programas que consuman mucho disco o RAM")