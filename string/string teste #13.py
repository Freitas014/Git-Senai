texto = input("Digite um texto: ")
#pontuacao = [".", ",", ":", ";", "!", "?"] # INÚTIL

# remove os sinais de pontuação
#for p in pontuacao: # INÚTIL
   # texto = texto.replace(p,"")

# split deovlve lista com palvras como itens
numero_palavras = len(texto) # se colocar dentro do parenteses "texto.split()" começa a contar palavras em vez de caracteres
print("Número de palavras: ", numero_palavras)