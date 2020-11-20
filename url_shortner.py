import pyshorteners
# biblioteca python para encurtar os links

# Introduzir o link
link = input(" link: ")
shortener = pyshorteners.Shortener()
# Variável
x = shortener.tinyurl.short(link)
# Imprimir variável
print(x)