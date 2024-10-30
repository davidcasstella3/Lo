import turtle

ventana = turtle.Screen()
ventana.bgcolor("black")

tortuga = turtle.Turtle()
tortuga.speed(0)
tortuga.color('green')

numero_estrella = 75

for i in range(numero_estrella*5):
    tortuga.forward(i*3)
    tortuga.right(145)

ventana.exitonclick()





