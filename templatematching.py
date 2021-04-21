
import cv2

#loading the images in grayscale
img = cv2.imread('images/Test/ball.jpeg', 0)
template = cv2.imread('images/Test/testcric.jpeg', 0)



#height and width of the template. It will be a tuple.
h, w = template.shape

#methods. Multiple algorithms to see which gives the best results.
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF_NORMED, cv2.TM_SQDIFF]

#looping through all available methods
for method in methods:
    # to have new copy of the image for every method
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    #returns min and max value and min and max location in the array
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)
    cv2.imshow('Match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


