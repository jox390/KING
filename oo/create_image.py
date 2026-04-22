from PIL import Image, ImageDraw, ImageFont
import os

# إنشاء صورة بحجم 500x400 (حجم مناسب للمنتج)
width, height = 500, 400
image = Image.new('RGB', (width, height), '#f0f0f0')  # خلفية رمادية فاتحة

# إنشاء كائن رسم
draw = ImageDraw.Draw(image)

# محاولة استخدام خط جميل، وإلا استخدام الخط الافتراضي
try:
    font = ImageFont.truetype("arial.ttf", 40)
except:
    font = ImageFont.load_default()

# رسم النص في المنتصف
text = "Converse Air Force"
bbox = draw.textbbox((0, 0), text, font=font)
text_width = bbox[2] - bbox[0]
text_height = bbox[3] - bbox[1]
x = (width - text_width) // 2
y = (height - text_height) // 2

# رسم النص باللون الأسود
draw.text((x, y), text, fill='black', font=font)

# حفظ الصورة
image_path = os.path.join('Images', 'shoe.jpg')
image.save(image_path, 'JPEG')

print(f"تم إنشاء الصورة بنجاح: {image_path}")