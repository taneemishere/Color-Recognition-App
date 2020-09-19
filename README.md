# Color-Recognition-App
A python application that recognize a color by double clicking on it in an image

## Requirements
-	[OpenCV](https://opencv.org/)
-	[Pandas](https://pandas.pydata.org/)
-	[Numpy](https://numpy.org/)

## The Colors
The colors data is obtained from a [repo](github.com/codebrainz/color-names/blop/master/output/colors.csv). Which has a lot of colors' names, it's hex code as well as the RGB channel codes. Thanks to [codebrainz](github.com/codebrainz) for having this.

## The Code Flow
-	Import the libraries
-	Initialize the image
-	Define the column names for the dataset
-	Read the csv file according to the names
-	The function ```color_recognizer``` is called when we double click and it returns the the color name and it's RGB value
-	The function ```mouse_click``` defines the callback to the double click of the mouse over a certain area of the image
-	Show the image in a window and enabling the double click of the mouse
-	Showing the window untill not quit
	-	Create a rectangle that will show the name and RGB value of a color
	-	Create a string to display, the color name and it's value
	-	Put the string over the image
	-	If the image or display is light, show the string in black color
	-	Close the window if escape key is pressed
-	At last release all the windows. And boom!
