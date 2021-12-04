def ngoinha():
    import turtle
    hcn=turtle.Turtle()
    turtle.bgcolor("aqua")
    hcn.speed(5)
    hcn.penup()
    hcn.goto(-320,-100)
    hcn.pendown()
    # vẽ hình chữ nhật mặt trước ngôi nhà
    a=150;
    b=200;
    a1=a-50;
    hcn.fillcolor("blue")
    hcn.begin_fill()
    for i in range(2):
        hcn.fd(a)
        hcn.rt(90)
        hcn.fd(b)
        hcn.rt(90)
    hcn.end_fill()

    # vẽ mái nhà phía trước
    hcn.fillcolor("fuchsia")
    hcn.begin_fill()
    hcn.lt(60)
    hcn.fd(a)
    hcn.rt(120)
    hcn.fd(a)
    hcn.end_fill()

    # vẽ mái nhà phía sau
    hcn.fillcolor("orange")
    hcn.begin_fill()    
    for i in range(4):
        hcn.lt(90)
        hcn.fd(a)
    hcn.end_fill()

    # vẽ phần sau của ngôi nhà
    hcn.fillcolor("yellow")
    hcn.begin_fill()    
    hcn.rt(30)
    hcn.fd(b)
    hcn.lt(120)
    hcn.fd(a)
    hcn.lt(60)
    hcn.fd(b)
    hcn.end_fill()

    # vẽ cửa sổ của ngôi nhà
    hcn.lt(120)
    hcn.fd(a1)
    hcn.lt(60)
    hcn.penup()
    hcn.fd(50)
    hcn.pendown()
    hcn.fillcolor("red")
    hcn.begin_fill()
    for i in range(2):
        hcn.fd(50)
        hcn.lt(120)
        hcn.fd(50)
        hcn.lt(60)
    hcn.end_fill()

    # vẽ cửa chính
    hcn.penup()
    hcn.goto(-280,-300)
    hcn.pendown()
    hcn.lt(180)
    hcn.fillcolor("chartreuse")
    hcn.begin_fill()
    for i in range(2):
        hcn.fd(100)
        hcn.rt(90)
        hcn.fd(70)
        hcn.rt(90)
    hcn.end_fill()
if __name__ =="__main__":ngoinha()
def cay():
    import turtle
    import math
    cc=turtle.Turtle()
    cc.speed(5)
    cc.penup()
    cc.goto(150,-180)
    cc.pendown()
    a=40;
    b=100;
    a1=25;
    b1= math.sqrt(2)*b/2;
    # vẽ thân cây
    cc.fillcolor("red")
    cc.begin_fill()
    cc.fd(a1)
    cc.rt(90)
    cc.fd(b)
    cc.rt(90)
    cc.fd(a)
    cc.rt(90)
    cc.fd(b)
    cc.rt(90)
    cc.fd(a1)
    cc.end_fill()
    # vẽ các tầng lá
    cc.fillcolor("chartreuse")
    cc.begin_fill()
    for i in range(3):
        cc.fd(b1)
        cc.lt(135)
        cc.fd(b)
        cc.rt(135)
    cc.rt(135)
    for i in range(3):
        cc.fd(b)
        cc.lt(135)
        cc.fd(b1)
        cc.rt(135)
    cc.end_fill()
if __name__  == "__main__":cay()
def troi():
   import turtle
   mt = turtle.Turtle()
   turtle.bgcolor("aqua")
   a=40;
   b=200;
   c=100;
   mt.speed(5)
   # vẽ các đường tia mặt trời
   mt.penup()
   mt.goto(a-c,b)
   mt.pendown()
   mt.goto(a+c,b)

   mt.penup()
   mt.goto(a,b-c)
   mt.pendown()
   mt.goto(a,b+c)

   mt.penup()
   mt.goto((2*a-c)/2,(2*b+c)/2)
   mt.pendown()
   mt.goto((2*a+c)/2,(2*b-c)/2)

   mt.penup()
   mt.goto((2*a-c)/2,(2*b-c)/2)
   mt.pendown()
   mt.goto((2*a+c)/2,(2*b+c)/2)

   # vẽ mặt trời
   mt.penup()
   mt.goto(a,(2*b-c)/2)
   mt.pendown()
   mt.fillcolor("yellow")
   mt.begin_fill()
   mt.circle(c/2)
   mt.end_fill()
   turtle.done()
if __name__ =="__main__":troi()