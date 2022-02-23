# nhập chiều cao tầng 1 ngôi nhà
a = float(input("nhập chiều cao của 1 tầng trong ngôi nhà: "))
# nhập chiều rộng ngôi nhà
b = float(input("nhập chiều rong ngôi nhà: "))
def tanghai():
    import turtle
    hai=turtle.Turtle()
    mainha={2:{'x':-b/10,'y':-300+5/3*a+1/2*a},1:{'x':-b/10,'y':-300+5/3*a+a/12+1/2*a}}
    mau={1:"green",2:'yellowgreen'}
    hai.speed(10)
    hai.penup()
    hai.goto(-3*b/5+b/15,-300+a)
    hai.pendown()
    hai.fillcolor('chocolate')
    hai.begin_fill()
    for i in range(2):
        hai.fd(b-2*b/15)
        hai.lt(90)
        hai.fd(2/3*a)
        hai.lt(90)
    hai.end_fill()
    for i in (1,2):
        hai.penup()
        hai.goto(mainha[i]['x'],mainha[i]['y'])
        hai.pendown()
        hai.fillcolor(mau[i])
        hai.begin_fill()
        hai.goto(2*b/5,mainha[2]['y']-1/2*a)
        hai.goto(-3*b/5,mainha[2]['y']-1/2*a)
        hai.goto(mainha[i]['x'],mainha[i]['y'])
        hai.end_fill()
    
    hai.penup()
    hai.goto(-3*b/5,-300+a+a/12)
    hai.pendown()
    hai.fillcolor("lime")
    hai.begin_fill()  
    hai.goto(-3*b/5+b/15,-300+a+a/8+a/12)
    hai.goto(-b/15,-300+a+a/8+a/12)
    hai.goto(0,-300+a+a/12)
    hai.end_fill()
if __name__=="__main__":
    tanghai()

def gara():
    import turtle
    import math
    ga=turtle.Turtle()
    b1 =2*b/5;
    ga.speed(20)
    toado={1:{'x':0,'y':-300},2:{'x':b1/6,'y':-300},3:{'x':5*b1/24,'y':-300},4:{'x':-3*b/5-b/60,'y':-300+a},5:{'x':-3/5*b+b/15,'y':-300}}
    rongdai={1:{'x':b1,'y':a},2:{'x':2*b1/3,'y':5*a/6},3:{'x':7*b1/12,'y':19*a/24},4:{'x':b+b/30,'y':a/12},5:{'x':3*b/5-b/15,'y':a}}
    mau={1:'orange',2:'olive',3:'yellow',4:'gray',5:'darkorange'}
    for i in (1,2,3,4,5):
        ga.penup()
        ga.goto(toado[i]['x'],toado[i]['y'])
        ga.pendown()
        ga.fillcolor(mau[i])
        ga.begin_fill()
        for i2 in range(2):
            ga.fd(rongdai[i]['x'])
            ga.lt(90)
            ga.fd(rongdai[i]['y'])
            ga.lt(90)
        ga.end_fill()
    # vẽ xọc kẻ của cửa
    i=1;
    while i<=10 :
        ga.penup()
        ga.goto(b1/6+b1/24,-320+i*19*a/240)
        ga.pendown()
        ga.goto(b1-b1/6-b1/24,-320+i*19*a/240)
        i= i+1
    # vẽ tay nắm cửa
    ga.penup()
    ga.goto(b1/2,-300+19*a/240)
    ga.pendown()
    ga.fillcolor("red")
    ga.begin_fill()
    ga.circle(19*a/360)
    ga.end_fill()
if __name__ == "__main__":
     gara()

def cottru():
    import turtle
    cot=turtle.Turtle()
    cot.speed(20)
    # a la chieu cao tang 1
    # b la chieu rong ngoi nha                            
    # c la chieu cao tang 2
    # gara cao a, rong 2b/5
    # tang mot cao a, rong 3b/5 trong do
    # co 3 cot tru chiem b/5
    # ve cot tru tu toa do cua b
    # ve cot thu nhat
    bienchay={1:{'y':-300+a,"x":-b/15},2:{'y':a-300,'x':-3*b/10},3:{'y':a-300,'x':-3*b/5}}
    for i in (1,2,3):
        toado={1:{'x':bienchay[i]['x'],'y':bienchay[i]['y']+a/12},2:{'x':bienchay[i]['x']+b/120,'y':bienchay[i]['y']},3:{'x':bienchay[i]['x']+b/60,'y':bienchay[i]['y']-a/36},4:{'x':bienchay[i]['x']+b/120,'y':bienchay[i]['y']-14*a/36},5:{'x':bienchay[i]['x'],'y':bienchay[i]['y']-15*a/36}}
        rongdai={1:{'x':b/15,'y':a/12},2:{'x':b/20,'y':a/36},3:{'x':b/30,'y':13*a/36},4:{'x':b/20,'y':a/36},5:{'x':b/15,'y':21*a/36}}
        cot.penup()
        cot.goto(bienchay[i]['x'],bienchay[i]['y'])
        cot.pendown()
        for i2 in (1,2,3,4,5):
            cot.penup()
            cot.goto(toado[i2]['x'],toado[i2]['y'])
            cot.pendown()
            cot.fillcolor("silver")
            cot.begin_fill()
            for i3 in range(2):
                cot.fd(rongdai[i2]['x'])
                cot.rt(90)
                cot.fd(rongdai[i2]['y'])
                cot.rt(90)
            cot.end_fill()
if __name__ =="__main__":
    cottru()
def tangmot():
    import turtle
    mot=turtle.Turtle()
    mot.speed(20)
    biendem={1:{'x':-3*b/5-b/60,'y':-300+a/2},2:{'x':-3*b/5-b/60,'y':-300+a/4},3:{'x':-3*b/5+b/15+b/60,'y':-300+a/2+a/12+a/36+a/24}}
    hcn={1:{'x':6*b/15,'y':a/24},2:{'x':6*b/15,'y':a/4},3:{'x':7*b/30-b/30,'y':a/24}}
    for i in (1,2,3):
        mot.penup()
        mot.goto(biendem[i]['x'],biendem[i]['y'])
        mot.pendown()
        mot.fillcolor('dimgrey')
        mot.begin_fill()
        for i2 in range(2):
            mot.fd(hcn[i]['x'])
            mot.rt(90)
            mot.fd(hcn[i]['y'])
            mot.rt(90)
        mot.end_fill()
    # ve hang rao
    i=1;
    while i<9 :
        mot.penup()
        mot.goto(-3*b/5+b/15+i*7*b/270,-300+a/4)
        mot.pendown()
        mot.pensize(5)
        mot.pencolor('yellow')
        mot.begin_fill()
        mot.goto(-3*b/5+b/15+i*7*b/270,-300+a/2-a/24)
        mot.end_fill()
        i= i+1
if __name__ =="__main__":
    tangmot()
def cauthang():
    import turtle
    cau=turtle.Turtle()
    cau.speed(20)
    x=-7*b/30;
    y=-300+a/4;
    x2=b/60
    y2=a/20
   
    for i in range(5):
        cau.penup()
        cau.goto(x,y)
        cau.pendown()
        cau.fillcolor("maroon")
        cau.begin_fill()
        for i2 in range(2):
            cau.fd(b/6+2*i*x2)
            cau.rt(90)
            cau.fd(y2)
            cau.rt(90)
        x=x-x2
        y=y-y2
        cau.end_fill()
if __name__ =="__main__":
    cauthang()
def cuaso1():
    import turtle
    cua=turtle.Turtle()
    cua.speed(20)
    # tang mot
    toado={1:{'x':-3*b/5+b/15+b/30,'y':-300+a},2:{'x':-3*b/5+b/15+b/30+b/60,'y':-300+a},3:{'x':-3*b/5+b/15+b/30+b/60+b/60+7*b/120,'y':-300+a}}
    rongdai={1:{'x':7*b/30-b/15,'y':13*a/36+a/36-a/24},2:{'x':7*b/120,'y':13*a/36-a/24},3:{'x':7*b/120,'y':13*a/36-a/24}}
    mau={1:'forestgreen',2:'white',3:'white'}
    for i in (1,2,3):
        cua.penup()
        cua.goto(toado[i]['x'],toado[i]['y'])
        cua.pendown()
        cua.fillcolor(mau[i])
        cua.begin_fill()
        for i2 in range(2):
            cua.fd(rongdai[i]['x'])
            cua.rt(90)
            cua.fd(rongdai[i]['y'])
            cua.rt(90)
        cua.end_fill()
    # tang hai
    toado2={1:{'x':-3*b/5+b/15+b/30,'y':-300+a+2/3*a-a/12},2:{'x':-3*b/5+b/15+b/30+b/60,'y':-300+a+2/3*a-a/12},3:{'x':-3*b/5+b/15+b/30+b/60+b/60+7*b/120,'y':-300+a+2/3*a-a/12}}
    rongdai2={1:{'x':7*b/30-b/15,'y':13*a/36+a/36-a/24},2:{'x':7*b/120,'y':13*a/36-a/24},3:{'x':7*b/120,'y':13*a/36-a/24}}
    for i in (1,2,3):
        cua.penup()
        cua.goto(toado2[i]['x'],toado2[i]['y'])
        cua.pendown()
        cua.fillcolor(mau[i])
        cua.begin_fill()
        for i2 in range(2):
            cua.fd(rongdai2[i]['x'])
            cua.rt(90)
            cua.fd(rongdai2[i]['y'])
            cua.rt(90)
        cua.end_fill()
    # tang 2 ben phai
    toado3={1:{'x':2*b/5-b/15-b/30-2*b/10,'y':-300+a+2/3*a-a/12},2:{'x':2*b/5-b/15-b/30+b/60-2*b/10,'y':-300+a+2/3*a-a/12},3:{'x':2*b/5-b/15-b/30+b/60+b/60+7*b/120-2*b/10,'y':-300+a+2/3*a-a/12}}
    rongdai3={1:{'x':7*b/30-b/15,'y':13*a/36+a/36-a/24},2:{'x':7*b/120,'y':13*a/36-a/24},3:{'x':7*b/120,'y':13*a/36-a/24}}
    for i in (1,2,3):
        cua.penup()
        cua.goto(toado3[i]['x'],toado3[i]['y'])
        cua.pendown()
        cua.fillcolor(mau[i])
        cua.begin_fill()
        for i2 in range(2):
            cua.fd(rongdai3[i]['x'])
            cua.rt(90)
            cua.fd(rongdai3[i]['y'])
            cua.rt(90)
        cua.end_fill()
if __name__ == "__main__":
    cuaso1()
def cuachinh():
    import turtle
    cua=turtle.Turtle()
    cua.speed(20)
    toado={1:{'x':-3*b/10+b/15+b/120,'y':-300+a},2:{'x':-3*b/10+b/15+b/120+b/120,'y':-300+a}}
    rongdai={1:{'x':3*b/10-2*b/15-2*b/120,'y':3*a/4},2:{'x':3*b/10-2*b/15-2*b/120-b/120,'y':3*a/4}}
    for i in (1,2):
        cua.penup()
        cua.goto(toado[i]['x'],toado[i]['y'])
        cua.pendown()
        for i2 in range(2):
            cua.fd(rongdai[i]['x'])
            cua.rt(90)
            cua.fd(rongdai[i]['y'])
            cua.rt(90)
    taynam={1:{'x':-b/15-b/120-b/60-b/120,'y':-300+a/2},2:{'x':-3*b/20,'y':-300+2*a/3}}
    bankinh={1:b/60,2:(3*b/10-2*b/15-4*b/60)/2}
    mausac={1:'red',2:'white'}
    for i in (2,1):
        cua.penup()
        cua.goto(taynam[i]['x'],taynam[i]['y'])
        cua.pendown()
        cua.fillcolor(mausac[i])
        cua.begin_fill()
        cua.circle(bankinh[i])
        cua.end_fill()
    turtle.exitonclick()
if __name__ == "__main__":
    cuachinh()


