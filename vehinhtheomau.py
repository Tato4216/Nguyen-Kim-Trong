def elip():
    import turtle
    t=turtle.Turtle()
    t.speed(20)
    t.pensize(5)
    r=100
    x=0
    t.lt(45)
    colors= ["red","yellow","blue","pink","green","orange"]
    while x<(360/20) :
        t.pencolor(colors[x%6])
        for i in range(2):
            t.circle(r,90)
            t.circle(r/2,90)
        t.rt(20)
        x+=1
    turtle.exitonclick()
if __name__ == "__main__":
    elip()
