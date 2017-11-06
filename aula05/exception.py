try:
    x = int(input('Digite primeiro numero '))
    y = int(input('Digite segundo numero '))
    print(x+y)
    if x ==3:
        raise Exception('Numero Invalido')

except Exception as e:
    print('Digite numero inteiro')
    print(e)