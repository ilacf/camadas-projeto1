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
        tx_int = int.from_bytes(txLen, byteorder='big')
        print(tx_int)   
        rxBuffer, nRx = com1.getData(tx_int)
        time.sleep(0.1)
        print(rxBuffer)
        recebido.append(rxBuffer)

        quantidade = 0
        lista = list(rxBuffer)
        print(lista)
        for byte in lista:
            comand_list = [4,3,2,1]
            if byte in comand_list:
                quantidade += 1
        print(quantidade)

        # print("Enviando quantidade de comandos")
        # com1.sendData(np.asarray(quantidade).tobytes())
        # time.sleep(1)
        # print("Enviado")

        time.sleep(7)
        
        # print("Enviando quantidade de comandos + 1")
        # quantidade += 1
        # com1.sendData(np.asarray(quantidade).tobytes())
        # time.sleep(1)
        # print("Enviado")
            
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
