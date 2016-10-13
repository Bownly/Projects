from array import *
from PIL import Image
import math
import os


xdim = 3
ydim = 2
total = 0

colors = [  (0,   0,   0), 
			# (128, 128, 128), 
			(255, 255, 0),]


# generates all possible pics of a given dimension
def color_square(shade, index, arr):
	global total
	# end condition
	if index > xdim*ydim:
		if total%2 == 0:
			img = Image.new('RGB', (xdim, ydim), "black") # create a new black image
			pixels = img.load() # create the pixel map
			for x in range(img.size[0]):    # for every pixel:
			    for y in range(img.size[1]):
			        pixels[img.size[0]-x-1,img.size[1]-y-1] = (arr[y][x]) # set the colour accordingly

			# save image file
			filename = "genpics/" + str(total/20000) + "/" + str(total/2) + ".png"
			if not os.path.exists(os.path.dirname(filename)):
			    try:
			        os.makedirs(os.path.dirname(filename))
			    except OSError as exc: # Guard against race condition
			        if exc.errno != errno.EEXIST:
			            raise
			img.save(filename, "PNG")
		total += 1
		return

	# establish coords
	y = int(math.ceil(float(index / float(xdim))) - 1)
	x = int(index - y * xdim) - 1

	# color the square
	arr[y][x] = shade

	# recurse
	for color in colors:
		b = [[arr[x][y] for y in range(len(arr[0]))] for x in range(len(arr))]
		color_square(color, index+1, b)


# creates the image cooresponding to a given integer id
def decode_seed(x, y, seed):
	global total
	img = Image.new('RGB', (x, y), "black") # create a new black image
	pixels = img.load() # create the pixel map
	for i in range(x):
		for j in range(y):
			u = x - i - 1
			v = y - j - 1
			pow_num = math.pow(2, u*y+v)
			if int(pow_num) <= seed:
				seed -= pow_num
				pixels[v, u] = (0, 255, 255)
	filename = "genpics/" + str(int(total)/20000) + "_decoded/" + str(int(total)) + ".png"
	if not os.path.exists(os.path.dirname(filename)):
		    try:
		        os.makedirs(os.path.dirname(filename))
		    except OSError as exc: # Guard against race condition
		        if exc.errno != errno.EEXIST:
		            raise
	img.save(filename, "PNG")
	total += 1



# test lines
total = 0
reinj = int(math.pow(2, xdim*ydim))
for seed in range(int(reinj*0.5), int(reinj*.75)):
	decode_seed(xdim, ydim, seed)

total = 0
lst = [1] * xdim
lstlst = [lst] * ydim
for color in colors:
	color_square(color, 1, lstlst)








