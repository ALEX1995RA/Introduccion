pregunta = 'Agrega un numero y te dire si es par o impar: \r\n'
pregunta += '(Escribe "cerrar" para salir de la aplicación)\r\n'
preguntar = True
while preguntar:
   numero = input(pregunta)
if numero == 'cerrar':
    preguntar = False
else:
  numero = int(numero)

if numero % 2 == 0: 
    print(f'El numero {numero} es Par')
else:
    print(f'El numero {numero} es impar')

