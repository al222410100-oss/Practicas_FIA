import itertools

proposiciones = int(input("¿Cuántas proposiciones quiere evaluar? "))
valores = [True, False]
combinaciones = list(itertools.product(valores, repeat=proposiciones))
letras = [chr(80 + i) for i in range(proposiciones)]

if proposiciones == 2:
    # Encabezado para 2 proposiciones (P y Q)
    print(f"{'P':<6} | {'Q':<6} | {'P and Q':<8} | {'P ∨ Q':<6} | {'P -> Q':<7} | {'P <-> Q':<8}")
    print("-" * 55)

    for P, Q in combinaciones:
        and_val = P and Q
        or_val = P or Q
        condicional = (not P) or Q
        bicondicional = (P == Q)
        
        print(f"{str(P):<6} | {str(Q):<6} | {str(and_val):<8} | {str(or_val):<6} | {str(condicional):<7} | {str(bicondicional):<8}")

else:
    # Encabezado adaptativo para N proposiciones
    encabezado_vars = " | ".join([f"{var:<6}" for var in letras])
    print(f"{encabezado_vars} | {'AND (Todas)':<12} | {'OR (Al menos una)':<18}")
    
    ancho_total = (proposiciones * 9) + 35
    print("-" * ancho_total)

    for combo in combinaciones:
        fila_vars = " | ".join([f"{str(val):<6}" for val in combo])
        and_general = all(combo)
        or_general = any(combo)
        
        print(f"{fila_vars} | {str(and_general):<12} | {str(or_general):<18}")
