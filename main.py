import Image_process as im
import os

def main():
    handler = None
    
    while True:
        print("\n" + "="*50)
        
        if handler and handler.image:
            print(f"Изображение: {os.path.basename(handler.image_path)}")
            print(f"Размер: {handler.image.size}")
        else:
            print("Изображение не загружено")
        
        print("\n1. Загрузить")
        if handler and handler.image:
            print("2. Обрезать 150x150")
            print("3. Чёрно-белый фильтр")
            print("4. Добавить текст")
            print("5. Применить фильтр")
            print("6. Сохранить")
        print("0. Выход")
        
        choice = input("\nВыбор: ")
        
        if choice == "0":
            break
        
        elif choice == "1":
            path = input("Путь к изображению или его в название в той же папке: ")
            if os.path.exists(path):
                handler = im.ImageHandler(path)
                handler.load_image()
            else:
                print("Файл не найден")
        
        elif choice == "2" and handler:
            handler.crop()
            print("Обрезано")
        
        elif choice == "3" and handler:
            processor = im.ImageProcessor(handler.get_image_for_processing())
            processor.apply_black_white_filter()
            handler.image = processor.get_processed_image()
            print("Чёрно-белый фильтр применен")
        
        elif choice == "4" and handler:
            text = input("Текст: ")
            processor = im.ImageProcessor(handler.get_image_for_processing())
            processor.add_text(text)
            handler.image = processor.get_processed_image()
            print(f"Добавлен текст: {text}")
        
        elif choice == "5" and handler:
            filter_type = input("Фильтр (blur/contour/detail): ")
            processor = im.ImageProcessor(handler.get_image_for_processing())
            processor.apply_filter(filter_type)
            handler.image = processor.get_processed_image()
            print(f"Фильтр {filter_type} применен")
        
        elif choice == "6" and handler:
            name = input("Название нового файла: ")
            handler.save_image(name)
            print("Сохранено")
        
        else:
            print("Неверный выбор или изображение не загружено")

if __name__ == "__main__":
    main()