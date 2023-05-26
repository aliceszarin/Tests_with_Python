renda = int (input ("Insira a renda do usuário: R$ "))

if renda < 2000:
    print ("Foi liberado R$1000 de limite para você!")

elif renda < 4000:
    print ("Foi liberado R$2000 de limite para você!")

elif renda < 10000:
    print ("Foi liberado R$3000 de limite para você!")

elif renda > 10000:
    print ("Falar com o gerente do seu banco!")