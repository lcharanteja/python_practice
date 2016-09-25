__author__ = 'charan'
from PIL import Image

img = Image.open("charan_py.jpg")
print(img.size)
print(img.format)

img.show()


from PIL import Image

img = Image.open("charan_py.jpg")
area = (200, 0, 2000, 1000)
cropped_img = img.crop(area)


img.show()
cropped_img.show()


from PIL import Image

one = Image.open("1.jpg")
img = Image.open("charan_py.jpg")

area = (0, 0, 480, 359)

img.paste(one, area)
img.show()

from PIL import Image

img = Image.open("charan_py.jpg")
print(img.mode)
r, g, b = img.split()

r.show()
g.show()
b.show()



from PIL import Image

img = Image.open("charan_py.jpg")
r, g, b = img.split()

new_img = Image.merge("RGB", (g, b, r))
new_img.show()


from PIL import Image

img = Image.open("charan_py.jpg")
img1 = Image.open("1.jpg")
area = (0, 0, 480, 359)
cropped_img = img.crop(area)
r1, g1, b1 = cropped_img.split()
r2, g2, b2 = img1.split()

new_img = Image.merge("RGB", (r1, g2, b1))
new_img.show()

from PIL import Image

img = Image.open("charan_py.jpg")
Square_img = img.resize((500, 500))
flip_img = img.transpose(Image.FLIP_LEFT_RIGHT)
spin_baby = img.transpose(Image.ROTATE_90)
Square_img.show()
flip_img.show()
spin_baby.show()


from PIL import Image

img = Image.open("charan_py.jpg")
black_white = img.convert("L")
black_white.show()

from PIL import Image
from PIL import ImageFilter

img = Image.open("charan_py.jpg")
blur = img.filter(ImageFilter.GaussianBlur)
detail = img.filter(ImageFilter.DETAIL)
edges = img.filter(ImageFilter.FIND_EDGES)

blur.show()
detail.show()
edges.show()