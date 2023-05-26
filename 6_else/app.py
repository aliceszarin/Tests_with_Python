poupanca = 200

saque = int (input ("Quanto você quer sacar?"))

if saque <= poupanca:
    print ("Você sacou R$%d" % saque)

else:
    print ("Você não tem saldo para sacar R$%d" %saque)
    print ("Sua poupança tem R$%d" % poupanca)

