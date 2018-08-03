from  algoritCifra import cifrar,decifrar

msg = input("Digite uma mensagem para ser cifrada: ")
key = int(input("Digite o tamanho da chave: "))

#msg_cif = algoritCifra.cifrar(msg,key)

msg_cif = cifrar(msg,key)
print(msg_cif)
nova = decifrar(msg,key)
print(nova)
