#!/bin/bash
#
# This script downloads the JENDL-5 Alpha-particle sublibrary
# 
# Usage: bash ./download_data.sh

# URL архива
url="https://wwwndc.jaea.go.jp/ftpnd/ftp/JENDL/jendl5-a.tar.gz"
# Имя архива
archive="jendl5-a.tar.gz"
# Директория для распаковки
extract_dir="./"

# Скачиваем архив
echo "Скачивание архива..."
curl -L -o "$archive" "$url"

# Проверяем, успешно ли скачан архив
if [ $? -ne 0 ]; then
    echo "Ошибка: Не удалось скачать архив."
    exit 1
fi

# Создаем директорию для распаковки, если её нет
echo "Создание директории для распаковки..."
mkdir -p "$extract_dir"

# Распаковываем архив
echo "Распаковка архива..."
tar -xvzf "$archive" -C "$extract_dir"

# Проверяем, успешно ли распакован архив
if [ $? -ne 0 ]; then
    echo "Ошибка: Не удалось распаковать архив."
    exit 1
fi

echo "Архив успешно скачан и распакован в директорию $extract_dir."

rm "jendl5-a.tar.gz"

echo "Архив удалён, данные находятся в директории $extract_dir."