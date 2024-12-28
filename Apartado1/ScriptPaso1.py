#Hacemos las importaciones necesarias
import sys #Este módulo proporciona acceso a algunas variables utilizadas o mantenidas por el intérprete
import os  #Este módulo permite interactuar con el sistema operativo



os.environ['GRUPO_NUMERO'] = sys.argv[1]  #Establece una variable de entorno con el primer argumento del script que corresponde con el número de grupo de la pareja el 08
puerto = sys.argv[2]

os.system("git clone https://github.com/CDPS-ETSIT/practica_creativa2.git")  #Clona un repositorio de GitHub
os.system("sudo apt update") # Actualiza los paquetes de sistema
os.system("sudo apt -y install python3") # Instala Python 3
os.system("sudo apt -y install pip") # Instala pip (administrador de paquetes de Python)

#Lee el archivo requirements.txt y modifica una dependencia específica ya que sino daba una incompatibilidad al ejecutarlo
with open("practica_creativa2/bookinfo/src/productpage/requirements.txt","r") as file: 
    requirements = file.read()

with open("practica_creativa2/bookinfo/src/productpage/requirements.txt","w") as file:
    requirements = requirements.replace("urllib3==1.26.5", "urllib3<1.25")
    file.write(requirements)
#Instala las dependencias del proyecto desde requirements.txt
os.system("pip3 install -r 'practica_creativa2/bookinfo/src/productpage/requirements.txt'")

#Modificación de los archivos html para que salga el número del grupo pasado como parámetro

#Nombre del archivo HTML de productpage
productpagehtml = "practica_creativa2/bookinfo/src/productpage/templates/productpage.html"

#Abrir el archivo HTML para lectura y escritura
with open(productpagehtml, 'r') as archivo:
    contenido = archivo.read()

#Modificar el contenido reemplazando el título
nuevo_titulo = "{% block title %}Simple Bookstore App" + os.environ['GRUPO_NUMERO'] + "{% endblock %}"
contenido_modificado = contenido.replace('{% block title %}Simple Bookstore App{% endblock %}', nuevo_titulo)

#Sobrescribir el archivo con el nuevo contenido
with open(productpagehtml, 'w') as archivo:
    archivo.write(contenido_modificado)

rule_name = "http-allow-" + sys.argv[2]  # Nombre de la regla
#Comando para crear la regla de firewall con gcloud
command = f'sudo gcloud compute firewall-rules create {rule_name} --allow=tcp:{puerto} --source-ranges="0.0.0.0/0"'
#Ejecutar el comando en la línea de comandos
os.system(command)

#Lanza la aplicación utilizando el archivo productpage_monolith.pyo y el puerto 9080
os.system(f"python3 practica_creativa2/bookinfo/src/productpage/productpage_monolith.py {puerto}")
