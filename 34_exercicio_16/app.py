salario = float (input ("Insira o valor do salário do funcionário: R$ "))

aumento = float ( input ("Insira o aumento (em %) para esse funcionário: "))

aumento = aumento / 100

print ("Salário do funcionário: R$", salario)
print ("Aumento recebido: R$", salario * aumento)
print ("Valor total do salário: R$ ", salario + (salario * aumento) )


