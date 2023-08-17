# Endereço da imagem a ser transmitida
imageR = "./imgs/image.png"

# Endereço da imagem a ser salva
imageW = "./imgs/recebidaCopia.png"

# Carrega a imagem
print("Carregando a imagem para transmissão:")
print(" - {}".format(imageR))
print("--------------------")
txBuffer = open(imageR, 'rb').read()

print("Salvando dados no arquivo:")
print(" - {}".format(imageW))
f = open(imageW, "wb")
f.write(rxBuffer)

# Fecha arquivo de imagem
f.close()