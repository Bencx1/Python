#for n in range(101, 0 , -1):
 #   print(n)

x=1;
#while x<=15:
 #   print(x);
  #  x=x+1

qtd = 0
soma = 0
media = 0
valor = float(input("Digite um valor: "))

while (valor > 0.0):
    soma = soma + valor
    qtd = qtd + 1
    #entrada de valores
    valor = float(input("Digite um valor: "))

#caso digite um valor negativo o laço encerra
media = soma / qtd
print("\n Total de soma: ",soma)
print("\n Quantidade de valores digitados: ", qtd)
print("\n Média dos valores: ",media)