def is_prime(num):
    for i in range(1, num+1):
        if ((num % i) == 0):
            if (i != num) and (i != 1) or (num == 1):
                return False
    else:
           return True

n = int(input("Digite um número: "))
if is_prime(n) == True:
     print ("É primo!")
else:
     print ("Não é primo!")
    