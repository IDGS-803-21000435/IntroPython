'''
los diccionarios son formatos tipo JSON (Clave - Valor)
'''

miDiccionario={"Matricula":21000435,"nombre":"Victor","Apellido":"Medina"}

print(miDiccionario)
print(type(miDiccionario))

miDiccionario["Apellido"]="Nada"
print(miDiccionario)

miDiccionario["correo"]="correo"
print(miDiccionario)