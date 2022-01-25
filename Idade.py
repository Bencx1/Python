idade = int(input("Digite a idade da pessoa: "))
if idade > 18:
    print("Maior idade, já pode ser preso")
elif idade > 16:
    print("Infanto juvenil")
else:
    print("Menor idade")
