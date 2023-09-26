x = 0
saldo = 0
while(x == 0):
    print("===================================")
    print("|  SAQUE  | DEPOSITO  | VER SALDO |")
    print("===================================")
    print("|    1    |     2     |     3     |")
    print("===================================")
    
    func = int(input("digite o numero da função desejada: "))
    
    match func:
        case 1:
            quant = int(input("digite quanto deseja sacar: "))
            print("===================================")
            
            if(quant > saldo ):
                print(" saque negado, saldo insuficiente: ")
            else:
                saldo = saldo - quant
                print(f" saque de R${quant} realizado, saldo de R${saldo}")
     
    
        case 2:
            quant = int(input("digite quanto deseja depositar: "))
            print("===================================")
            saldo = saldo + quant
            print(f" deposito de R${quant} concluido , saldo de R${saldo}")
        

        case 3:
            print(f" vossa beldade detem R${saldo}")
            print("===================================")
        
    print("-------------------------------------------")
    t = int(input("deseja continuar: (s/n) (0/1) "))
    print("-------------------------------------------")
    
    if( t == 1):
        x = 1
        print("-------------------------------------------")
        print(" obrigado por usar o banco alexandre => ")
        print("-------------------------------------------")
