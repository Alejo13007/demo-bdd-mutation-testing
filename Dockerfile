# Partimos de un Linux que ya trae Python
FROM python:3.13-slim

# Carpeta de trabajo dentro del contenedor
WORKDIR /app

# Instalamos pytest, pytest-bdd y mutmut
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el proyecto
COPY . .

# Al entrar, abre una terminal
CMD ["bash"]