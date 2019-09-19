from math import sqrt

from PIL import Image

def q1():
    img = Image.open("flower.jpg")

    size = img.size

    img.show()
    print(size)


def q2():
    img = Image.new("RGB", (500, 500), color=(0, 0, 0))

    mat = img.load()

    for i in range(500):
        for j in range(500):
            z = int(sqrt((i/2)*(j/2)))
            mat[i,j] = (z, 0, 255-z)

    img.show()


def q3():
    img1 = Image.open("a1.jpg")
    img2 = Image.open("a2.jpg")

    img = Image.new("RGB", (500, 500), color=(0, 0, 0))

    mat1 = img1.load()
    size1 = img1.size
    mat2 = img2.load()
    size2 = img2.size

    mat = img.load()

    for i in range(size1[0]):
        for j in range(size1[1]):
            mat[i,j] = mat1[i,j]

    for i in range(size2[0]):
        for j in range(size2[1]):
            mat[100+i,j] = mat2[i,j]


    img.show()


def q4():
    img = Image.new("RGB", (640, 640), color=(0,0,0))
    img1 = Image.open("one_s.jpg")
    mat = img.load()
    size1 = img1.size
    mat1 = img1.load()

    for i in range(8):
        for j in range(8):
            if (i+j)%2 == 0:
                for k in range(80):
                    for m in range(80):
                        mat[i*80+k, j*80+m] = (128,128, 0)

    x = int((80 - size1[0])/2)
    y = int((80 - size1[1])/2)

    for i in range(size1[0]):
        for j in range(size1[1]):
            if mat1[i, j][0] < 50:
                mat[i+x, j+y] = mat1[i, j]

    img.show()

#q1()
#q2()
#q3()
q4()