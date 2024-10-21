from PIL import Image
import os

def minify_image(image_path, output_path, quality=85, convert_to_webp=False):
    try:
        # Abre a imagem
        img = Image.open(image_path)
        
        # Converte para WebP, se necessário
        if convert_to_webp:
            output_path = os.path.splitext(output_path)[0] + ".webp"
            img.save(output_path, "webp", quality=quality, optimize=True)
        else:
            img.save(output_path, quality=quality, optimize=True)
        
        print(f"Imagem minificada salva em: {output_path}")
    except Exception as e:
        print(f"Erro ao minificar a imagem {image_path}: {e}")

def minify_images_in_directory(directory, output_directory, quality=85, convert_to_webp=False):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(directory, filename)
            output_path = os.path.join(output_directory, filename)
            minify_image(image_path, output_path, quality, convert_to_webp)

if __name__ == "__main__":
    input_directory = "/app/images/input"
    output_directory = "/app/images/output"
    quality = 100  # Ajuste a qualidade aqui
    convert_to_webp = True  # Mude para False se não quiser converter para WebP

    minify_images_in_directory(input_directory, output_directory, quality, convert_to_webp)
