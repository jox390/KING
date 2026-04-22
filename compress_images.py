from PIL import Image
import os

# قائمة الصور المستخدمة في index.html
images = ['jordan4_first.jpg', 'airforce1.jpg', 'airmax_oreo.jpg']
input_dir = 'c:/Users/5580/Desktop/oo/Images'
output_dir = 'c:/Users/5580/Desktop/oo/Images/optimized'

os.makedirs(output_dir, exist_ok=True)

for img_name in images:
    input_path = os.path.join(input_dir, img_name)
    if os.path.exists(input_path):
        with Image.open(input_path) as img:
            # Resize to suitable web size (cover 400x300)
            img.thumbnail((400, 300), Image.Resampling.LANCZOS)
            output_path = os.path.join(output_dir, img_name)
            img.save(output_path, 'JPEG', quality=85, optimize=True)
            print(f'تم ضغط {img_name}: {os.path.getsize(input_path)} -> {os.path.getsize(output_path)} bytes')
    else:
        print(f'غير موجود: {input_path}')

print('انتهى ضغط الصور')

