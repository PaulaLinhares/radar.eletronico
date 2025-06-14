from pyparsing import alphanums

v=int(input("Digite a sua velocidade atual:"))
multa=(v-80)*7
print("Continue dirigindo com segurança!" if v<=80
      else print("Você excedeu a velocidade permitida de "
"80Km. E a sua multa a pagar é de R${}".format(multa)))