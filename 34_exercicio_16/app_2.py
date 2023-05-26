salario = float (input ("Insira o valor do salário do funcionário: R$ "))

aumento = float ( input ("Insira o aumento (em %) para esse funcionário: "))
total = salario + (salario * (aumento/100))

print ( "O novo salário é de R$%.2f" % total)