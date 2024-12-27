import sys 
import os  


os.environ['GRUPO_NUMERO'] = sys.argv[1] #Establece una variable de entorno con el primer argumento del script 

#Modificación de los archivos html para que salga el número del grupo pasado como parámetro
# Nombre del archivo HTML de productpage
productpagehtml = "templates/productpage.html"

# Abrir el archivo HTML para lectura y escritura
with open(productpagehtml, 'r') as archivo:
    contenido = archivo.read()

# Modificar el contenido reemplazando el título
nuevo_titulo = "{% block title %}Simple Bookstore App" + os.environ['GRUPO_NUMERO'] + "{% endblock %}"
contenido_modificado = contenido.replace('{% block title %}Simple Bookstore App{% endblock %}', nuevo_titulo)

# Sobrescribir el archivo con el nuevo contenido
with open(productpagehtml, 'w') as archivo:
    archivo.write(contenido_modificado)


# Nombre del archivo HTML index.html
indexhtml = "templates/index.html"

# Abrir el archivo HTML para lectura y escritura
with open(indexhtml, 'r') as archivo:
    contenido = archivo.read()

# Modificar el contenido reemplazando el título
nuevo_titulo_index = "{% block title %}Simple Bookstore App" + os.environ['GRUPO_NUMERO'] + "{% endblock %}"

contenido_modificado_index = contenido.replace('{% block title %}Simple Bookstore App{% endblock %}', nuevo_titulo_index)

# Sobrescribir el archivo con el nuevo contenido
with open(indexhtml, 'w') as archivo:
    archivo.write(contenido_modificado_index)
