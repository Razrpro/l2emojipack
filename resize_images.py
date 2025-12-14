from PIL import Image
import os

def resize_images(input_folder='img', output_folder='img_resized', size=(100, 100)):
    """
    Изменяет размер всех изображений в папке до заданного размера.
    
    Args:
        input_folder: папка с исходными изображениями
        output_folder: папка для сохранения изменённых изображений
        size: размер (ширина, высота) в пикселях
    """
    # Создаём папку для результатов, если её нет
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Поддерживаемые форматы изображений
    supported_formats = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff')
    
    # Получаем список всех файлов изображений
    image_files = [f for f in os.listdir(input_folder) 
                   if f.lower().endswith(supported_formats)]
    
    if not image_files:
        print(f"В папке '{input_folder}' не найдено изображений")
        return
    
    # Сортируем файлы по дате создания
    image_files_with_time = []
    for filename in image_files:
        file_path = os.path.join(input_folder, filename)
        creation_time = os.path.getctime(file_path)
        image_files_with_time.append((filename, creation_time))
    
    # Сортируем по времени создания
    image_files_with_time.sort(key=lambda x: x[1])
    image_files = [f[0] for f in image_files_with_time]
    
    print(f"Найдено изображений: {len(image_files)}")
    print(f"Изменяю размер до {size[0]}x{size[1]}px (с нумерацией по дате создания)...\n")
    
    # Обрабатываем каждое изображение
    for i, filename in enumerate(image_files, 1):
        try:
            # Полный путь к файлу
            input_path = os.path.join(input_folder, filename)
            
            # Получаем расширение файла
            name, ext = os.path.splitext(filename)
            
            # Формируем новое имя с порядковым номером
            new_filename = f"{i}_{name}{ext}"
            output_path = os.path.join(output_folder, new_filename)
            
            # Открываем изображение
            img = Image.open(input_path)
            
            # Изменяем размер с сохранением качества
            # LANCZOS - высококачественный алгоритм ресэмплинга
            img_resized = img.resize(size, Image.Resampling.LANCZOS)
            
            # Сохраняем результат
            img_resized.save(output_path)
            
            print(f"[{i}/{len(image_files)}] {new_filename} - готово")
            
        except Exception as e:
            print(f"[{i}/{len(image_files)}] {filename} - ошибка: {e}")
    
    print(f"\nГотово! Изображения сохранены в папке '{output_folder}'")

if __name__ == "__main__":
    resize_images()
