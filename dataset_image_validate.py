import os
from PIL import Image, UnidentifiedImageError
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.utils import shuffle


# Função personalizada para verificar se uma imagem está válida
def validate_image(path):
    try:
        with Image.open(path) as img:
            img.verify()  # Verifica se a imagem é válida
        return True
    except (UnidentifiedImageError, IOError):
        print(f"Arquivo inválido ou corrompido: {path}")
        os.remove(path)  # Remove a imagem inválida
        print(f"Arquivo removido: {path}")
        return False


# Gerar dados com imagens válidas organizadas por classe
def load_and_group_by_class(directory):
    """Carrega imagens válidas, agrupando por pasta de classe."""
    class_images = {}
    for root, dirs, files in os.walk(directory):
        for dir_name in dirs:
            class_path = os.path.join(root, dir_name)
            valid_images = [
                os.path.join(class_path, file)
                for file in os.listdir(class_path)
                if validate_image(os.path.join(class_path, file))
            ]
            class_images[dir_name] = valid_images
    return class_images


# Função para balancear as classes, equalizando o número de amostras
def balance_classes(class_images):
    """Equaliza o número de imagens entre as classes."""
    # Encontrando o menor número de imagens entre as classes
    min_samples = min(len(images) for images in class_images.values())

    # Reduzindo todas as classes ao menor tamanho
    balanced_images = {}
    for class_name, images in class_images.items():
        shuffled_images = shuffle(images, random_state=42)  # Aleatoriza as imagens
        balanced_images[class_name] = shuffled_images[:min_samples]  # Limita ao menor tamanho
        # Apagar as imagens não utilizadas
        for unused_image in shuffled_images[min_samples:]:
            os.remove(unused_image)
            print(f"Arquivo não utilizado removido: {unused_image}")
    return balanced_images


# Função para padronizar imagens para formato RGB
def process_image(image_path, target_size=(150, 150)):
    """Redimensiona e converte a imagem para RGB."""
    with Image.open(image_path) as img:
        img = img.resize(target_size)  # Redimensiona
        if img.mode != "RGB":
            img = img.convert("RGB")  # Converte para RGB se necessário
        return np.array(img)


# Processo principal
def main():
    # Caminho para o diretório com datasets
    image_directory = "./content/train"  # Ajuste para seu caminho de entrada

    # Carrega imagens válidas e organiza por classe
    class_images = load_and_group_by_class(image_directory)

    if not class_images:
        print("Nenhuma imagem válida encontrada no diretório!")
        return

    # Balancear as classes
    balanced_images = balance_classes(class_images)

    # Preparando imagens no formato adequado para o modelo
    images = []
    labels = []
    target_size = (224, 224)
    class_to_idx = {class_name: idx for idx, class_name in enumerate(balanced_images.keys())}
    for class_name, image_paths in balanced_images.items():
        for path in image_paths:
            img = process_image(path)  # Processar e padronizar imagem
            images.append(img)
            labels.append(class_to_idx[class_name])

    # Converter para arrays numpy
    images = np.array(images) / 255.0  # Normalizando para o intervalo [0, 1]
    labels = np.array(labels)

    # Criar DataGenerator
    datagen = ImageDataGenerator()
    generator = datagen.flow(images, labels, batch_size=32)

    print(f"Classes balanceadas: {list(balanced_images.keys())}")
    print(f"Número de amostras por classe: {len(next(iter(balanced_images.values())))}")


# Rodar o código principal
if __name__ == "__main__":
    main()
