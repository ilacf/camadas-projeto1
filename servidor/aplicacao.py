from enlace import *
import enlaceRx
import time
import numpy as np

serialName = "COM4"

def main():
    try:
        print("Iniciou o main")
        com1 = enlace(serialName)

        com1.enable()
        print("esperando 1 byte de sacrifício")
        rxBuffer, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(.1)
        
        print("Abriu a comunicação")
        
        recebido = []
        while True:
            txLen, _ = com1.getData(1)
            if txLen != b'\xEE':
                rxBuffer, nRx = com1.getData(int.from_bytes(txLen))
                recebido.append(rxBuffer)
            else:
                break

        print("recebeu {} bytes" .format(len(rxBuffer)))
        
        for i in range(len(rxBuffer)):
            print("recebeu {}" .format(rxBuffer[i]))
            
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
