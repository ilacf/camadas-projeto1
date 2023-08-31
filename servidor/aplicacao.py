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
        txLen, _ = com1.getData(1)
        print(txLen)
        #print("Dentro do While")  
        tx_int = int.from_bytes(txLen, byteorder='big')
        print(tx_int)   
        rxBuffer, nRx = com1.getData(tx_int)
        time.sleep(0.1)
        print(rxBuffer)
        recebido.append(rxBuffer)

        qnts = len(rxBuffer)
        print("recebeu {} bytes" .format(len(rxBuffer)))

        com1.sendData(np.asarray(qnts))
        time.sleep(1)
        
       # for i in range(len(rxBuffer)):
        #    print("recebeu {}" .format(rxBuffer[i]))
            
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
