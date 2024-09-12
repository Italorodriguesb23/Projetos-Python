import random
import string

def gerador_senha(len_pass = 8):
    
    number_options = string.digits
    
    options = number_options

    senha_usuario = ""

    for i in range(0, len_pass):
        digit = random.choice(options)
        senha_usuario = senha_usuario + digit

    return senha_usuario

escolha_usuario = input("Quantos digitos na senha?")

if escolha_usuario.isdigit():
    escolha_usuario = int(escolha_usuario)
else:
    print("Entrada inválida!")
    quit()

response = gerador_senha(len_pass = escolha_usuario)
print(f"Senha gerada:\n{response}")
