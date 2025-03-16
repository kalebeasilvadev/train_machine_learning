import os
import random
import shutil
import argparse


def split_dataset(source_dir, train_base="train", validate_base="validate", validate_ratio=0.2):
    # Obtém o nome da pasta (ex.: "cats" de "./content/cats")
    folder_name = os.path.basename(os.path.normpath(source_dir))
    train_dir = os.path.join(train_base, folder_name)
    validate_dir = os.path.join(validate_base, folder_name)

    # Cria as pastas de destino se não existirem
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validate_dir, exist_ok=True)

    # Lista os arquivos da pasta de origem (apenas arquivos, sem subpastas)
    files = [f for f in os.listdir(source_dir) if os.path.isfile(os.path.join(source_dir, f))]

    # Embaralha os arquivos para uma divisão aleatória
    random.shuffle(files)

    # Define a quantidade de arquivos para o conjunto de validação
    n_validate = int(len(files) * validate_ratio)
    validate_files = files[:n_validate]
    train_files = files[n_validate:]

    # Copia os arquivos para a pasta train
    for f in train_files:
        shutil.copy2(os.path.join(source_dir, f), os.path.join(train_dir, f))

    # Copia os arquivos para a pasta validate
    for f in validate_files:
        shutil.copy2(os.path.join(source_dir, f), os.path.join(validate_dir, f))

    print(
        f"Divisão concluída: {len(train_files)} arquivos em '{train_dir}' e {len(validate_files)} arquivos em '{validate_dir}'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script para dividir arquivos em conjuntos de train e validate."
    )
    parser.add_argument(
        "source",
        help="Caminho da pasta de origem com os arquivos. Exemplo: ./content/cats"
    )
    parser.add_argument(
        "--train_base",
        default="train",
        help="Pasta base para os arquivos de treino (default: train)"
    )
    parser.add_argument(
        "--validate_base",
        default="validate",
        help="Pasta base para os arquivos de validação (default: validate)"
    )
    parser.add_argument(
        "--ratio",
        type=float,
        default=0.2,
        help="Proporção de arquivos para o conjunto de validação (default: 0.2)"
    )
    args = parser.parse_args()

    split_dataset(args.source, args.train_base, args.validate_base, args.ratio)
