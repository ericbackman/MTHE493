# MTHE 493 Midterm Presentation

# LIBRARIES

# Place used libraries here.

from PIL import Image
import time

# Import photo with a coloured region and white background.

img = Image.open('spiral2.png')
img.show()
size = img.size
pixels = img.load()

# Convert photo to a matrix (a list of lists) u_n where u_n[i][j] = 1 if pixel [i][j] is coloured, -1 otherwise.

print(size[0])
print(size[1])

#print(pixels[0,0])
u_n =[[]]*size[1]

for i in range(size[1]):
	for j in range(size[0]):
		if pixels[j,i][0] == 255:
			u_n[i] = u_n[i] + [-1]
		else:
			u_n[i] = u_n[i] + [1]

# PARAMETERS

width = len(u_n[0]) # Set this to the height of the picture. Set arbitrarily to 100.
height =  len(u_n) # Set this to the width of the picture. Set arbitratily to 100.
tf = 3000 # Number of iterations
deltat = 1
epsilon = 0.000001

# print(len(u_n[0]))
# print(width)
# print(height)
#print(u_n[1][0])
#print(u_n[1])
#print(u_n[1][width-1])
# print([u_n[i][0]] + u_n[i] + [u_n[i][width-1]])

for k in range(tf):

	# Pad u_n
	u_ntop = [u_n[0][0]] + u_n[0] + [u_n[0][width-1]]
	u_nbottom = [u_n[height-1][0]] + u_n[height-1] + [u_n[height-1][width-1]]
	# print(u_n)
	# print(u_ntop)
	# print(u_nbottom)
	u_n = [u_ntop] + u_n + [u_nbottom]
	#print(u_n[0])
	for i in range(1,height+1):
		# print(u_n[i]);
		u_n[i] = [u_n[i][0]] + u_n[i] + [u_n[i][width-1]]

	u_n1 = [[]]*height
	for i in range(1, height+1):
		for j in range(1, width+1):
			D_0x = (u_n[i+1][j]-u_n[i-1][j])/2
			D_0y = (u_n[i][j+1]-u_n[i][j-1])/2
			u_x = D_0x
			u_y = D_0y
			u_xx = (u_n[i+1][j]-2*u_n[i][j]+u_n[i-1][j])/2
			u_xy = (u_n[i+1][j+1]-u_n[i+1][j-1]-u_n[i-1][j+1]+u_n[i-1][j-1])/4
			u_yy = (u_n[i][j+1]-2*u_n[i][j]+u_n[i][j-1])/2
			K_n = (u_xx*u_y**(2)-2*u_y*u_x*u_xy+u_yy*u_x**(2))/((u_x**(2)+u_y**(2))**(3/2)+epsilon)
			u_n1[i-1] = u_n1[i-1] + [u_n[i][j] + deltat*K_n*(D_0x**(2)+D_0y**(2))**(1/2)]

	# Convert u_n1 back to a photo via the following scheme. If u_n1[i][j] >= 0, colour pixel[i][j].

	if k % 25 == 0:
		img2 = Image.new('RGBA', img.size, "white")
		#pixels2 = img2.load()
		for i in range(height):
			for j in range(width):
				if u_n1[i][j] > 0:
					img2.putpixel((j,i),(0,0,0,255))
		img2.save('Transitions5/Step_{}.png'.format(k))

	# Print photo.

	u_n = u_n1

img2 = Image.new('RGBA', img.size, "white")
#pixels2 = img2.load()
for i in range(height):
	for j in range(width):
		if u_n1[i][j] > 0:
			img2.putpixel((j,i),(0,0,0,255))
img2.show()
