# Usar una imagen base ligera de Python
FROM python:3.7.7-slim

# Establecer variables de entorno
ENV PYTHONUNBUFFERED=1 \
    GROUP_NUM=""

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    git \
    gcc \
    libffi-dev \
    libssl-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Clonar el repositorio en el contenedor
RUN git clone https://github.com/CDPS-ETSIT/practica_creativa2.git 

WORKDIR /practica_creativa2/bookinfo/src/productpage

# Modificar el archivo requirements.txt
RUN sed -i 's/urllib3==1.26.5/urllib3<1.25/' requirements.txt

# Copiar el script Python para actualizar el título
COPY update_title.py .

# Instalar dependencias de Python
RUN python3 -m pip install -r requirements.txt

# Exponer el puerto de la aplicación
EXPOSE 9080

# Comando por defecto para ejecutar la aplicación
CMD python3 update_title.py ${GROUP_NUM} && \
    python3 productpage_monolith.py 9080
