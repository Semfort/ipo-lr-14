from PIL import Image

class ImageHandler:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None
    
    def load_image(self):
        try:
            self.image = Image.open(self.image_path)
            print(f"Изображение загружено, его размер: {self.image.size}.")
            
            self.image = self.image.rotate(90, expand=True)
            print("Изображение повернуто на 90 градусов")
            
        except FileNotFoundError:
            print(f"Ошибка: Файл не найден - {self.image_path}")
    
    def crop(self):
        if self.image is None:
            print("Нет изображения для обрезки")
            return
        
        width, height = self.image.size
        
        left = (width - 150) // 2
        top = (height - 150) // 2
        right = left + 150
        bottom = top + 150
        
        self.image = self.image.crop((left, top, right, bottom))
        print(f"Изображение обрезано до 150x150")
    
    def resize_image(self, width=None, height=None):
        if self.image is None:
            print("Нет изображения для изменения размера")
            return

        if width and height:
            new_size = (width, height)
        else:
            print("Не указаны размеры для изменения")
            return
        
        self.image = self.image.resize(new_size)
        print(f"Размер изображения изменен на {new_size}")
    
    def save_image(self, output_path="result.jpg"):
        if self.image is None:
            print("Нет изображения для сохранения")
            return
        
        try:
            self.image.save(output_path)
            print(f"Изображение сохранено: {output_path}")
            return output_path
        except Exception as e:
            print(f"Ошибка при сохранении изображения: {e}")
            return None
    
    def get_image_for_processing(self):
        if self.image and self.image_path:
            return (self.image, self.image_path)
        return (None, None)


