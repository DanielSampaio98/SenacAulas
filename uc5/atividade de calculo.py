a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))


if a == 0:
    if b == 0:
        print("A equação é não é determinada, pois a e b são ambos iguais a 0.")
    else:
        print("A equação vai fica impossivel, pois a é igual a 0 e b é diferente de 0.")
else:
    x = -b / a
    print(f"A solução da equação {a}x + {b} = 0 é x = {x}")
