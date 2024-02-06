def main():
    import cv2
    image = cv2.imread("./resim.jpeg")
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    inverted_gray_image = 255 - gray_image
    blur = cv2.GaussianBlur(inverted_gray_image, (21, 21), 0)
    invertedblur = 255 - blur
    sketch = cv2.divide(gray_image, invertedblur, scale=256.0)
    cv2.imwrite("sketch.png", sketch)
    cv2.imshow("Original Image", image)
    


if __name__ == "__main__":
    main()
