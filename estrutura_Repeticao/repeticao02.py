usuario = input("Digite o nome de usuário: ")
senha = input("Digite sua Senha: ")
while usuario == senha:
    senha = input("Senha igual ao usuário. Digite uma senha Diferente do seu nome de Ususario: ")

print(usuario+'\n'+senha)