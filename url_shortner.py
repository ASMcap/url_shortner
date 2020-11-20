import pyshorteners
import time

# Introduzir o link
link = input(" link: ")
shortener = pyshorteners.Shortener()
# Variável
x = shortener.tinyurl.short(link)
# Imprimir variável
print(x)
time.sleep(90)

# biblioteca python para encurtar os links
# biblioteca time para pausar o programa 90 segundos para poder copiar o novo link 
