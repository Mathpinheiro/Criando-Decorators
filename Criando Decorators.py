from datetime import datetime

def decorator_desafio(funcao):
    def desafio():
        print (datetime.now())
        funcao()
        print(datetime.now())
    return desafio
@decorator_desafio
def compra_realizada():
    print('COMPRA REALIZADA')

compra_realizada()