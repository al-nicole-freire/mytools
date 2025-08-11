import math
from decimal import Decimal, getcontext

# PI_INT que é uma string que representa as 100 primeiras casas decimais do número pi
getcontext().prec = 102
PI_INT = str(Decimal(math.pi))[2:100]

# E_INT que é uma string que representa as 100 primeiras casas decimais do número neperiano  
E_INT = str(Decimal(math.e))[2:100]
# Uma função chamada pi_real que dado um número natural N maior que 0 e menor que 100 que retorna uma string de uma aproximação pro número pi com N casa decimais
def pi_real(N):
    if N>0 and N < 100:
        pi_desejado = str(Decimal(math.pi))[2:N+2]
        return pi_desejado
    else:
        N = int(input("Valor não suportado. Digite outro valor "))
        return pi_real(N)

# Uma função chamada e_real que dado um número natural N maior que 0 e menor que 100 que retorna uma string de uma aproximação pro número neperiano com N casa decimais
def e_real(N):
    if N>0 and N < 100:
        e_desejado = str(Decimal(math.e))[2:N+2]
        return e_desejado
    else:
        N = int(input("Valor não suportado. Digite outro valor "))
        return e_real(N)