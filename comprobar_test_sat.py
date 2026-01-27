import sys

FIRMA_CORRECTA = [89441954, 97970796]
def codificar_respuesta(respuesta):
    ascii_vals = [ord(c) for c in respuesta]
    chunks = [ascii_vals[i:i+4] for i in range(0, len(ascii_vals), 4)]
    firma = []
    for bloque in chunks:
        producto = 1
        for num in bloque:
            producto *= num
        firma.append(producto)
    return firma

if len(sys.argv) < 2:
    print("Uso correcto:")
    print("python comprobar_test_sat.py <letras de las respuestas del test en orden>")
    print("EJEMPLO: python comprobar_test_sat.py abcabca")
    sys.exit(1)

entrada = sys.argv[1].strip()

resultado = codificar_respuesta(entrada)

if resultado == FIRMA_CORRECTA:
    print("CORRECTO!!")
else:
    print("INCORRECTO")
