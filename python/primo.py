def isPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def app():
    num = int(input('Escreva um numero: '))
    result = isPrimo(num)

    if result is True:
        print("É um número primo!")
    else:
        print ("Não é um número primo.")

if __name__== '__main__':
    app()