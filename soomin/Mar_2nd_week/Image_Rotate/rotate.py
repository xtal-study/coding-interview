import cv2

image = cv2.imread('./pic.jpg')
image = cv2.resize(image, (int(image.shape[1] / 4), int(image.shape[0] / 4)))
c = image.shape[1] - image.shape[0]
image = image[:, int(c/2):image.shape[1]-int(c/2), :]
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
length = image.shape[0]

cv2.imshow('image-before', image)

for otg in range(length):
    for cur in range(otg, length):
        image[otg, length-cur-1], image[cur, length-otg-1] = image[cur, length-otg-1], image[otg, length-cur-1]

for y in range(int(length/2)):
    for x in range(length):
        image[y, x], image[length-y-1, x] = image[length-y-1, x], image[y, x]

cv2.imshow('image', image)
cv2.waitKey()