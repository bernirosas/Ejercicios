def encriptar(msg: bytearray) -> bytearray:
    A = bytearray()
    B = bytearray()
    C = bytearray()
    for i in range(0, len(msg), 3):
        A += msg[i: i + 1]
        B += msg[i + 1: i + 2]
        C += msg[i + 2: i + 3]
    suma = 0
    suma += A[0]
    if len(B) % 2 == 0:  # par
        pos_1 = int(len(B)/2)
        pos_2 = int(len(B)/2 - 1)
        suma += (B[pos_1] + B[pos_2])
    if len(B) % 2 != 0:  # impar
        suma += B[int((len(B) - 1)/2)]
    suma += C[-1]
    msg_final = bytearray()
    if suma % 2 == 0:  # par
        msg_final += bytearray(b"\x00")
        msg_final += C + A + B
    if suma % 2 != 0:  # impar
        msg_final += bytearray(b"\x01")
        msg_final += A + C + B
    return msg_final


def desencriptar(msg: bytearray) -> bytearray:
    n = msg[0:1]
    resto = msg[1:]
    largo_c = int(len(resto)//3)
    largo_b = largo_c
    largo_a = largo_c
    if int(len(resto) % 3) == 2:
        largo_b += 1
    if int(len(resto) % 3) >= 1:
        largo_a += 1
    if n[0] == 0:  # C + A + B
        C = resto[:largo_c]
        A = resto[largo_c:largo_a + largo_c]
        B = resto[largo_a + largo_c:]
    if n[0] != 0:  # A + C + B
        A = resto[:largo_a]
        C = resto[largo_a:largo_a + largo_c]
        B = resto[largo_a + largo_c:]
    msj = bytearray()
    for i in range(0, int(len(resto)//3)):
        msj += A[i:i+1]
        msj += B[i:i+1]
        msj += C[i:i+1]
    if int(len(resto) % 3) >= 1:
        msj += A[int(len(resto)//3):int(len(resto)//3)+1]
    if int(len(resto) % 3) == 2:
        msj += B[int(len(resto)//3):int(len(resto)//3)+1]
    return msj


if __name__ == "__main__":
    # Testear encriptar
    msg_original = bytearray(b'\x05\x08\x03\x02\x04\x03\x05\x09\x05\x09\x01')
    msg_esperado = bytearray(b'\x01\x05\x02\x05'
                             b'\x09\x03\x03\x05\x08\x04\x09\x01')

    msg_encriptado = encriptar(msg_original)
    if msg_encriptado != msg_esperado:
        print("[ERROR] Mensaje escriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje escriptado correctamente")
    # Testear desencriptar
    msg_desencriptado = desencriptar(msg_esperado)
    if msg_desencriptado != msg_original:
        print("[ERROR] Mensaje descencriptado erroneamente")
    else:
        print("[SUCCESSFUL] Mensaje descencriptado correctamente")
