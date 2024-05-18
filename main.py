import random
import string

def gerar_senha():
    comprimento = int(input('Digite, em um valor numérico, o tamanho que deseja que sua senha tenha: '))
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    print(f'Sua senha gerada é: {senha}')

if __name__ == "__main__":
    gerar_senha()