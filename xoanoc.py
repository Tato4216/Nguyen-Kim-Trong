def xoanoc():
    import math
    import turtle
    k=float(input("nhap gia tri"))
    t=turtle.Turtle()
    
    t.speed(20)
    t.pensize(5)
    r=10
    # i la bien lap 
    i=0
    # dist la khoang cach tu tam den diem gion han
    dist=0
    while dist<k:
        t.circle(r+i,45)
        dist=t.distance(turtle.position(),(0,0))
        i+=1
    turtle.exitonclick()
if __name__ == "__main__":
    xoanoc()