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
        print("Abriu a comunicação")
        print("esperando 1 byte de sacrifício")
        rxBuffer, nRx = com1.getData(1)
        com1.rx.clearBuffer()
        time.sleep(1)
        
        
        recebido = []
        while True:
            txLen, _ = com1.getData(1)
            print(txLen)
            if txLen != b'\xEE':
                #print("Dentro do While")  
                tx_int = int.from_bytes(txLen, byteorder='big')
                print(tx_int)   
                rxBuffer, nRx = com1.getData(tx_int)
                time.sleep(0.1)
                print(rxBuffer)
                recebido.append(rxBuffer)
            else:
                print("Saindo do While")
                print(enlace.getBuffer())
                print("depois do enlace")
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
