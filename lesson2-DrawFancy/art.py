import turtle
def draw_square(some_turtle):
	for i in range(1,5):
		some_turtle.forward(100)
		some_turtle.right(90)

def draw_art():
	window = turtle.Screen()
	window.bgcolor("black")
	luca = turtle.Turtle()
	luca.shape("turtle")
	luca.color("white")
	luca.speed(15)
	#draw the circle using turtle
	counter = 0
	while(counter < 25):
		draw_square(luca)
		luca.right(15)
		counter = counter+1
	luca.forward(250)
	counter = 0
	while(counter < 25):
		draw_square(luca)
		luca.right(15)
		counter = counter+1
	window.exitonclick()

draw_art()