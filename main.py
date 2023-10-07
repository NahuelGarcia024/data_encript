from cryptography.fernet import Fernet

def generar_clave():
    return Fernet.generate_key()

def encriptar_texto(texto, clave):
    f = Fernet(clave)
    texto_encriptado = f.encrypt(texto.encode())
    return texto_encriptado

def desencriptar_texto(texto_encriptado, clave):
    f = Fernet(clave)
    texto_desencriptado = f.decrypt(texto_encriptado)
    return texto_desencriptado.decode()
# generar una clave
clave_secreta = generar_clave()
#texto a encriptar
texto_original = "Hola, este es un texto de prueba para encriptar"

#encriptar texto

texto_encriptado = encriptar_texto(texto_original, clave_secreta)

print("*"*100)
print(f"texto original: {texto_original}")
print("*"*100)
print(f"texto encriptado: {texto_encriptado}")


#desencriptar texto

texto_desencriptado = desencriptar_texto(texto_encriptado, clave_secreta)

print(f"texto desencriptado: {texto_desencriptado}")
print("*"*100)
