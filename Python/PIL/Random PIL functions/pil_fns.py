from PIL import Image

# TODO: handle images of 2 different dimensions
def pic_diffs(pic1, pic2):

	# read in pics
	img1 = Image.open(pic1)
	img2 = Image.open(pic2)
	pix1 = img1.load()
	pix2 = img2.load()

	# figure out dimensions
	xdim = img1.size[0]
	ydim = img1.size[1]

	outimg = Image.new('RGB', (xdim, ydim), "black")  # create outfile
	outpix = outimg.load()  # create the pixel map

	# run through each pixel
	for x in range(outimg.size[0]):
		for y in range(outimg.size[1]):
			# if same, print same to outfile
			if (pix1[x,y] == pix2[x,y]):
				outpix[x,y] = pix1[x,y]
			# if different, print red to outfile
			else:
				outpix[x,y] = (255, 0, 0)

	# save image
	outimg.save("pic_diffs_outfile.png")


# Enlarges an img size by a given int val
def pic_increase(picin, mult):
	img = Image.open(picin)
	pix = img.load()

	xdim = img.size[0]
	ydim = img.size[1]

	outimg = Image.new('RGBA', (xdim*mult, ydim*mult), "white")
	outpix = outimg.load()

	for x in range(xdim*mult):
		for y in range(ydim*mult):
			outpix[x,y] = pix[x/mult,y/mult]

	outimg.save("big_x" + str(mult) + "_" + picin)
	# outimg.save("heads.png")


# Shrinks an img size by a given factor
def pic_reduce(picin, mult):
	img = Image.open(picin)
	pix = img.load()

	xdim = img.size[0]
	ydim = img.size[1]

	outimg = Image.new('RGBA', (xdim/mult, ydim/mult), "blue")
	outpix = outimg.load()

	for x in range(xdim/mult):
		for y in range(ydim/mult):
			avg_color = (0, 0, 0)
			for i in range(mult):
				for j in range(mult):
					pix_color = (pix[x*mult+i, y*mult+j][0], pix[x*mult+i, y*mult+j][1], pix[x*mult+i, y*mult+j][2])
					avg_color = (avg_color[0] + pix_color[0], avg_color[1] + pix_color[1], avg_color[2] + pix_color[2])
			outpix[x,y] = (avg_color[0]/(mult*mult), avg_color[1]/(mult*mult), avg_color[2]/(mult*mult))
	outimg.save("small_1|" + str(mult) + "_" + picin)


# test lines
pic_diffs("1.png", "2.png");
pic_increase("pepe.png", 3)
pic_reduce("pepe.png", 4)


















