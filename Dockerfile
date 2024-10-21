# Use a imagem Python oficial
FROM python:3.9-slim

# Define o diretório de trabalho
WORKDIR /app

# Copia o script Python para o contêiner
COPY minify_images.py /app/

# Instala as dependências necessárias
RUN pip install Pillow

# Cria os diretórios para entrada e saída de imagens
RUN mkdir -p /app/images/input /app/images/output

# Define o comando padrão para executar o script Python
CMD ["python", "minify_images.py"]
