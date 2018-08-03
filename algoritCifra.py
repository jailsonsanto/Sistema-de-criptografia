def cifrar(msg,key):
    #codificar
    alf = "abcdefghijklmnopqrstuvwxyz \
ABCDEFGHIJKLMNOPQRSTUWXYZ"
    '''
    for c in alf:
        alf = alf + c.upper()
    alf = alf + " "
    '''
    tam = len(alf)

    msg_cif = ""  

    for letra in msg.lower():
        pos = alf.find(letra)
        pos = pos + key
        if pos >= tam:
            pos = pos % tam
        msg_cif = msg_cif + alf[pos]
        
    return msg_cif
def decifrar(msg_cif,key):
     #decodificar
     alf = "abcdefghijklmnopqrstuvwxyz \
ABCDEFGHIJKLMNOPQRSTUWXYZ"
     tam = len(alf)
     key = key % tam
     msg = ""
     for letra in msg_cif:
         pos = alf.find(letra)
         pos = pos - key
         msg = msg + alf[pos]
         
     return msg_cif

def unicode(inicio = 0,fim = 65546):
    chars = ""
    for x in range(inicio,fim):
        chars = chars + chr(x)
    return chars
    
