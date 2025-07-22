
from PIL import Image
import random

# 画像サイズ（タイル可能）
width, height = 512, 512

# 基本となる羊皮紙の色
base_color = (244, 241, 233) # #f4f1e9

# 新しい画像を生成
image = Image.new('RGB', (width, height), base_color)
pixels = image.load()

# ピクセルごとにランダムなノイズを加えて質感を出す
for i in range(width):
    for j in range(height):
        # 各色チャンネルにランダムな値を加える
        rand_val = random.randint(-15, 15)
        r = max(0, min(255, base_color[0] + rand_val))
        g = max(0, min(255, base_color[1] + rand_val))
        b = max(0, min(255, base_color[2] + rand_val))
        pixels[i, j] = (r, g, b)

# 画像を保存
image.save('/Users/okamoto/code/2025-7-22-test/images/parchment-bg.png')

print("Background texture generated and saved as parchment-bg.png")
