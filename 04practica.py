valores = [True, False ]

proposiciones= int (input ("¿Cuantas proposiciones quiere evaluar? "))

print ("P \t Q \t P and Q \t P ∨ Q \tP -> Q \t P <-> Q ")
print ("-" * 50)


for P in valores:
        for Q in valores:
            resultado= P and Q 
            conjuncion = P or Q
            condicional = (not P) or Q 
            bicondicional = P == Q

        print (P,  "\t", Q, "\t", resultado,"\t",  conjuncion ,"\t", condicional,"\t", bicondicional, "\t",)