from PIL import ImageDraw, ImageFont

class ImageProcessor:
    def __init__(self, image_data):
        if image_data and isinstance(image_data, tuple) and len(image_data) == 2:
            self.image, self.image_path = image_data
            if self.image:
                path_display = self.image_path if self.image_path else "из памяти"
                print(f"Изображение {path_display} передано в ImageProcessor.")
    
    def apply_black_white_filter(self):
        if self.image is None:
            print("Нет изображения для обработки")
            return
        
        if self.image.mode != 'L':
            self.image = self.image.convert('L')
            print("Применен черно-белый фильтр")
        else:
            print("Изображение уже в черно-белом формате")
    
    def add_text(self, text="Вариант 2", position=(10, 10)):
        if self.image is None:
            print("Нет изображения для добавления текста")
            return
        
        image_with_text = self.image.copy()
        draw = ImageDraw.Draw(image_with_text)
        
        font = ImageFont.load_default()
        
        draw.text(position, text, fill="white" if self.image.mode == 'L' else "black", font=font)
        
        self.image = image_with_text
        print(f"Добавлен текст: '{text}'")
    
    
    def apply_filter(self, filter_type='blur'):
        from PIL import ImageFilter
        
        if self.image is None:
            print("Нет изображения для применения фильтра")
            return
        
        if filter_type == 'blur':
            self.image = self.image.filter(ImageFilter.BLUR)
            print("Применен фильтр размытия")
        elif filter_type == 'contour':
            self.image = self.image.filter(ImageFilter.CONTOUR)
            print("Применен контурный фильтр")
        elif filter_type == 'detail':
            self.image = self.image.filter(ImageFilter.DETAIL)
            print("Применен фильтр детализации")
        else:
            print(f"Фильтр '{filter_type}' не найден")
    
    def get_processed_image(self):
        return self.image

