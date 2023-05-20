import random
import string

def gerar_senha(comprimento, caracteres):
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha
    
    
def main():
    comprimento = int(input("Digite o comprimento da senha desejada: "))
    letras = input("Deseja incluir letras maiúsculas? (S/N): ")
    numeros = input("Deseja incluir números? (S/N): ")
    simbolos = input("Deseja incluir símbolos? (S/N): ")
    
    caracteres = string.ascii_lowercase  
    if letras.upper() == 'S':
        caracteres += string.ascii_uppercase 

    if numeros.upper() == 'S':
        caracteres += string.digits  

    if simbolos.upper() == 'S':
        caracteres += string.punctuation  

    senha = gerar_senha(comprimento, caracteres)
    print("Senha gerada:", senha)
    
if __name__ == '__main__':
    main()
 
    
