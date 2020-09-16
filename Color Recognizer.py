import cv2
import pandas as pd
import numpy as np

# Our image to detect colors from
img = cv2.imread('color_image.png')

# Define the names for the columns
index = ["color", "color_name", "hex", "R", "G", "B"]

# Read the csv according to the names given above
df = pd.read_csv('colors.csv', names=index, header=None)

# print(df.head())
# print(df.tail())

# Some global variables
clicked = False
r = g = b = xpos = ypos = 0


# Color recognition function
def color_recognizer(R, G, B):
    """
    This function will be called when we double click over a certain area in an image
    :param R: Red color
    :param G: Green Color
    :param B: Blue Color
    :return: Color name and it's RGB value
    """

    minimum = 10000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, "R"])) + \
            abs(G - int(df.loc[i, "G"])) + \
            abs(B - int(df.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, "color_name"]
    return cname


# print(recognize_color(234, 33, 217))

# Mouse click function
# This is to define our double click process on an image
def mouse_click(event, x, y, flags, param):
    """
    Defines the callback to the double click of the mouse
    :param event: what should be done
    :param x: position of cursor on x-axis
    :param y: position of cursor on y-axis
    :param flags: default
    :param param: default
    :return: none
    """
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b, g, r = img[y, x]
        b = int(b)
        g = int(g)
        r = int(r)


'''
Our application, that will return the color name and the color's hex value when
we double click over a certain area of an image.
'''

# Our Application Window
cv2.namedWindow('Color Recognizer', flags=cv2.WINDOW_AUTOSIZE)

# Application window with mouse click enabled
cv2.setMouseCallback('Color Recognizer', mouse_click)


while 1:
    cv2.imshow('Color Recognizer', img)
    if clicked:

        # The rectangle that'll show the name and hex value of the color
        # cv2.rectangle(image, startpoint, endpoint, color, thickness)
        # -1 fills entire rectangle
        cv2.rectangle(img, (20, 20), (600, 60), (b, g, r), -1)

        # creating text string to display, the color name and it's value
        text = color_recognizer(R=r, G=g, B=b) + ' R=' + str(r) + ' G=' + str(g) + ' B=' + str(b)

        # Put the string over the image
        # cv2.putText(img, text, font(0-7),fontScale, color, thickness, lineType)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)

        # if the image or display is light, show the string in black color
        if r + g + b >= 600:
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)

        clicked = False

    # Close the window 'esc' key is pressed
    if cv2.waitKey(20) & 0xFF == 27:
        break

# Release all the windows
cv2.destroyAllWindows()
