# TODO 52: For an image for 5 x 5 pixels where each pixel stores color code between 0 - 255. create a function tht takes array and the percentage increase of color increase the color of all the pixels

from random import randint
def increaseColor(pic, percent):
    inc = (percent /100) + 1
    for row in range(5):
        for col in range(5):
            new = pic[row] [col] * inc
            if new > 255:
                new = 255
            pic[row] [col] = int(new)
    return pic

pic = [[randint(0, 255) for col in range(5)] for row in range(5)]

print("Before: ")
print(pic)

print("After: ")
print(increaseColor(pic, 40))
