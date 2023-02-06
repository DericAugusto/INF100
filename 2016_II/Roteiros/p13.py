import imagens

im = imagens.Imagem('fruits.jpg')
im.mostrar()

# Produz imagem só com a informação de luminância (tons de cinza)
for y in range(0,im.altura):
    for x in range(0,im.largura):
        r, g, b = im[y][x]
        luminancia = int( 0.299 * r + 0.587 * g + 0.114 * b )
        im[y][x] = (luminancia, luminancia, luminancia)
im.mostrar()

# Reler a imagem
im.abrir('fruits.jpg')

# Produz imagem espelhada
for y in range(0,im.altura):
    for x in range(0,im.largura//2):
        im[y][x], im[y][im.largura-1-x] = im[y][im.largura-1-x], im[y][x]
im.mostrar()

# Produz imagem em tom de "sepia"
for y in range(0,im.altura):
    for x in range(0,im.largura):
        r, g, b = im[y][x]
        r2 = min( 255, int( r * 0.393 + g * 0.769 + b * 0.189 ))
        g2 = min( 255, int( r * 0.349 + g * 0.686 + b * 0.168 ))
        b2 = min( 255, int( r * 0.272 + g * 0.534 + b * 0.131 ))   
        im[y][x] =  (r2, g2, b2)
im.mostrar()
