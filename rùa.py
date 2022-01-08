import turtle as t
import random
import time

screen = t.Screen()
screen.setup(width=800, height=400)
guess = screen.textinput(prompt='Dự đoán con rùa nào chiến thắng?', title='Nhập vào màu rùa (đỏ, nâu, xanh dương, xanh lá cây , cam, hồng)')
colors = ['red', 'brown', 'blue', 'green', 'orange', 'pink']
x = -250
y_position = [0, -40, 40, -80, 80, 120]
turtle_speed = [10,15,20,25,30,5]
all_turtles = []
# vẽ cột mốc đường đua
pen=t.Turtle(visible=False)
pen.penup()
pen.speed(10)
t.speed(10)
pen.goto(-250,150)
for i in range(21):
    pen.write(i)
    pen.forward(25)
x=-250
pen.goto(-250,150)
pen.right(90)
for i in range(21):
    for j in range(10):
        pen.pendown()
        pen.forward(20)
        pen.penup()
        pen.forward(10)
    pen.penup()
    pen.forward(5)
    pen.write(i)
    pen.goto(x+(i+1)*25,150)

run = True
start = time.time()
for turtle in range(0,6):
        turtles = t.Turtle(shape='turtle')
        turtles.penup()
        turtles.goto(x=-250, y=y_position[turtle])
        turtles.color(colors[turtle])
        all_turtles.append(turtles)

def random_walk(turtles):
    global run
    for turtle in turtles:
        turtle.forward(random.choice(turtle_speed))
        if turtle.xcor() > 250:
            run = False
            timeStop = time.time() - start
            print('Con rùa màu: ' + turtle.pencolor() + ' về đích đầu tiên.Thời gian:'+ str(timeStop))
            break
while run:
    random_walk(all_turtles)

screen.exitonclick()