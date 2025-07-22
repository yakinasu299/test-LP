
from PIL import Image, ImageDraw, ImageFont

# 画像サイズ
width, height = 1200, 800

# 背景色（羊皮紙のような色）
background_color = (244, 241, 233) # R, G, B

# 画像を生成
image = Image.new('RGB', (width, height), background_color)
draw = ImageDraw.Draw(image)

# 簡単な地図要素を描画（サンプル）
# これはプレースホルダーです。より複雑な地図は専門のツールが必要です。
line_color = (109, 93, 75) # 茶色
draw.line((100, 100, 1100, 700), fill=line_color, width=2)
draw.line((100, 700, 1100, 100), fill=line_color, width=2)

# テキストを追加
try:
    # フォントは環境に依存するため、見つからない場合はデフォルトを使用
    font = ImageFont.truetype("Arial.ttf", 40)
except IOError:
    font = ImageFont.load_default()

draw.text((50, 50), "World Map", font=font, fill=line_color)

# 画像を保存
image.save('/Users/okamoto/code/2025-7-22-test/images/fantasy-map-bg.jpg')

print("Image generated and saved as fantasy-map-bg.jpg")
