from enlace import *
from enlaceRx import *
import time
import numpy as np
from random import randint

#   python -m serial.tools.list_ports

serialName = "COM3"


def main():
    try:
        print("Iniciou o main")

        com1 = enlace(serialName)
        
        com1.enable()
        time.sleep(.2)
        com1.sendData(b'00')
        time.sleep(0.1)
        print("Abriu a comunicação")

        comandos = [b'\x04\x00\x00\x00\x00', b'\x04\x00\x00\xBB\x00', b'\x03\xBB\x00\x00', b'\x03\x00\xBB\x00', b'\x03\x00\x00\xBB', b'\x02\x00\xAA', b'\x02\xBB\x00', b'\x01\x00', b'\x01\xBB']
        bytes = [4, 4, 3, 3, 3, 2, 2, 1, 1]
        qntd = randint(10, 30)
        print(f'{qntd} comandos')
        qntd_bytes = 0
        byte = b''
        for _ in range(qntd):
            tipo = randint(1, 9)
            qntd_bytes += bytes[tipo-1]
            byte += comandos[tipo-1]
            print(bytes[tipo-1], comandos[tipo-1])

        txBuffer = len(byte).to_bytes(1, byteorder='big') + byte
               
        print(txBuffer)
        print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))   
        
        com1.sendData(np.asarray(txBuffer)) 
        time.sleep(1)

        txSize = com1.tx.getStatus()
        print('enviou = {} bytes' .format(txSize))

        # receber quantidade de comandos recebida pelo server
        comeco = time.time()

        while time.time()-comeco < 5:
            if com1.rx.getIsEmpty() == False:
                rxBuffer, _ = com1.getData(1)
                print('*'*100)
                print(f"Servidor devolveu a informação de que recebeu {int.from_bytes(rxBuffer, byteorder='big')} comandos")
                print('*'*100)

                if int.from_bytes(rxBuffer, byteorder='big') == qntd:
                    print("A quantidade de comandos recebidos pelo server está correta!")
                else:
                    print("A quantidade de comandos recebidos pelo server está errada... :(")
                print("-------------------------")
                print("Comunicação encerrada")
                print("-------------------------")
                com1.disable()
                break

        print("Timeout :(")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        
if __name__ == "__main__":
    main()
