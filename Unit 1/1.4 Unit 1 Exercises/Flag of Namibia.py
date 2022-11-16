# background
Rect(0, 0, 400, 400, fill='whiteSmoke')

# Draw the flag of Namibia.
### (HINT: The sun is drawn using one star and one circle with a border.)
### Place Your Code Here ###

Rect(5, 100, 390, 265, fill = 'white')

Label('Namibia', 200, 50, fill = 'black', font = 'arial', size = 30 ) 
Polygon(5, 100, 315, 100, 5, 310, fill = rgb(0, 60, 125))
Polygon(335, 100, 395, 100, 395, 140, 65, 365, 5, 365, 5, 325, fill = rgb(210, 15, 50))
Polygon(395, 155, 85, 365, 395, 365, fill = rgb(0, 150, 65))

Star(84, 174, 40, 12, fill = rgb(255, 215, 0))
Circle(84, 174, 25, fill = rgb(255, 215, 0), border = rgb(0, 60, 125), borderWidth = 5)
