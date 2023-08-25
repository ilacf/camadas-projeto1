from enlace import *
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
        time.sleep(1)
        print("Abriu a comunicação")

        comandos = [b'\x00\x00\x00\x00', b'\x00\x00\xBB\x00', b'\xBB\x00\x00', b'\x00\xBB\x00', b'\x00\x00\xBB', b'\x00\xAA', b'\xBB\x00', b'\x00', b'\xBB']
        bytes = [4, 4, 3, 3, 3, 2, 2, 1, 1]
        qntd = randint(10, 30)
        txBuffer = []
        for _ in range(qntd):
            tipo = randint(1, 9)
            txBuffer.append(bytes[tipo-1])
            txBuffer.append(comandos[tipo-1])
        txBuffer.append(b'\xEE')
       
        print("meu array de bytes tem tamanho {}" .format(len(txBuffer)))   
        
        com1.sendData(np.asarray(txBuffer)) 
        time.sleep(1)

        txSize = com1.tx.getStatus()
        print('enviou = {}' .format(txSize))

        print("-------------------------")
        print("Comunicação encerrada")
        print("-------------------------")
        com1.disable()
        
    except Exception as erro:
        print("ops! :-\\")
        print(erro)
        com1.disable()
        
if __name__ == "__main__":
    main()
