import turtle as t
t_=t.Turtle()
t_.penup()
t_.goto(-250,250)
t_.pendown()
t_.color("white")
t_.write("RULES\n 1.RIGHT CLICK FOR CROSS\n 2.LEFT CLICK FOR ZERO\n 3.WINNER HAS TO BE CHOOSEN MANUALLY\n" )
t_.hideturtle()
#defining function fo mouse click
def right_click1(x,y):
    t1.pensize(10)
    t1.circle(20)
    t1.hideturtle()
def right_click2(x,y):
    t2.pensize(10)
    t2.circle(20)
    t2.hideturtle()
def right_click3(x,y):
    t3.pensize(10)
    t3.circle(20)
    t3.hideturtle()
def right_click4(x,y):
    t4.pensize(10)
    t4.circle(20)
    t4.hideturtle()
def right_click5(x,y):
    t5.pensize(10)
    t5.circle(20)
    t5.hideturtle()
def right_click6(x,y):
    t6.pensize(10)
    t6.circle(20)
    t6.hideturtle()
def right_click7(x,y):
    t7.pensize(10)
    t7.circle(20)
    t7.hideturtle()
def right_click8(x,y):
    t8.pensize(10)
    t8.circle(20)
    t8.hideturtle()
def right_click9(x,y):
    t9.pensize(10)
    t9.circle(20)
    t9.hideturtle()
#def left click function
def left_click1(x,y):
    t1.pensize(10)
    t1.right(45)
    t1.fd(30)
    t1.bk(60)
    t1.penup()
    t1.right(45)
    t1.fd(45)
    t1.pendown()
    t1.left(135)
    t1.fd(60)
    t1.hideturtle()
def left_click2(x,y):
    t2.pensize(10)
    t2.right(45)
    t2.fd(30)
    t2.bk(60)
    t2.penup()
    t2.right(45)
    t2.fd(45)
    t2.pendown()
    t2.left(135)
    t2.fd(60)
    t2.hideturtle()
def left_click3(x,y):
    t3.pensize(10)
    t3.right(45)
    t3.fd(30)
    t3.bk(60)
    t3.penup()
    t3.right(45)
    t3.fd(45)
    t3.pendown()
    t3.left(135)
    t3.fd(60)
    t3.hideturtle()
def left_click4(x,y):
    t4.pensize(10)
    t4.right(45)
    t4.fd(30)
    t4.bk(60)
    t4.penup()
    t4.right(45)
    t4.fd(45)
    t4.pendown()
    t4.left(135)
    t4.fd(60)
    t4.hideturtle()
def left_click5(x,y):
    t5.pensize(10)
    t5.right(45)
    t5.fd(30)
    t5.bk(60)
    t5.penup()
    t5.right(45)
    t5.fd(45)
    t5.pendown()
    t5.left(135)
    t5.fd(60)
    t5.hideturtle()
def left_click6(x,y):
    t6.pensize(10)
    t6.right(45)
    t6.fd(30)
    t6.bk(60)
    t6.penup()
    t6.right(45)
    t6.fd(45)
    t6.pendown()
    t6.left(135)
    t6.fd(60)
    t6.hideturtle()
def left_click7(x,y):
    t7.pensize(10)
    t7.right(45)
    t7.fd(30)
    t7.bk(60)
    t7.penup()
    t7.right(45)
    t7.fd(45)
    t7.pendown()
    t7.left(135)
    t7.fd(60)
    t7.hideturtle()
def left_click8(x,y):
    t8.pensize(10)
    t8.right(45)
    t8.fd(30)
    t8.bk(60)
    t8.penup()
    t8.right(45)
    t8.fd(45)
    t8.pendown()
    t8.left(135)
    t8.fd(60)
    t8.hideturtle()
def left_click9(x,y):
    t9.pensize(10)
    t9.right(45)
    t9.fd(30)
    t9.bk(60)
    t9.penup()
    t9.right(45)
    t9.fd(45)
    t9.pendown()
    t9.left(135)
    t9.fd(60)
    t9.hideturtle()

tu=t.Turtle()
tu.speed(0)
tu.pensize(10)
t.bgcolor("black")
tu.penup()
tu.color("red")
tu.goto(-150,-150)
tu.left(90)
tu.pendown()
#making square
for i in range(4):
    tu.forward(300)
    tu.right(90)
#making boxs
tu.penup()
tu.right(90)
tu.forward(100)
tu.pendown()
tu.left(90)
tu.forward(300)
tu.penup()
tu.right(90)
tu.forward(100)
tu.pendown()
tu.right(90)
tu.forward(300)
tu.penup()
tu.left(90)
tu.forward(100)
tu.left(90)
tu.forward(100)
tu.pendown()
tu.left(90)
tu.forward(300)
tu.right(90)
tu.penup()
tu.forward(100)
tu.pendown()
tu.right(90)
tu.forward(300)

#placing turtles
#first turtle
t1=t.Turtle()
t1.shape("turtle")
t1.color("white")

#second turtle
t2=t.Turtle()
t2.shape("turtle")
t2.color("white")
t2.penup()
t2.goto(90,90)
t2.pendown()
#third turtle
t3=t.Turtle()
t3.shape("turtle")
t3.color("white")
t3.penup()
t3.goto(0,100)
t3.pendown()
#forth turtle
t4=t.Turtle()
t4.shape("turtle")
t4.color("white")
t4.penup()
t4.goto(90,0)
t4.pendown()
#fifth turtle
t5=t.Turtle()
t5.shape("turtle")
t5.color("white")
t5.penup()
t5.goto(-90,0)
t5.pendown()
#sixth turtle
t6=t.Turtle()
t6.shape("turtle")
t6.color("white")
t6.penup()
t6.goto(0,-90)
t6.pendown()
#seventh turtle
t7=t.Turtle()
t7.shape("turtle")
t7.color("white")
t7.penup()
t7.goto(90,-90)
t7.pendown()
#eigth turtle
t8=t.Turtle()
t8.shape("turtle")
t8.color("white")
t8.penup()
t8.goto(-90,-90)
t8.pendown()
#nineth turtle
t9=t.Turtle()
t9.shape("turtle")
t9.color("white")
t9.penup()
t9.goto(-90,90)
t9.pendown()

t.listen()
t1.onclick(right_click1,1)
t2.onclick(right_click2,1)
t3.onclick(right_click3,1)
t4.onclick(right_click4,1)
t5.onclick(right_click5,1)
t6.onclick(right_click6,1)
t7.onclick(right_click7,1)
t8.onclick(right_click8,1)
t9.onclick(right_click9,1)

#right click

t1.onclick(left_click1,3)
t2.onclick(left_click2,3)
t3.onclick(left_click3,3)
t4.onclick(left_click4,3)
t5.onclick(left_click5,3)
t6.onclick(left_click6,3)
t7.onclick(left_click7,3)
t8.onclick(left_click8,3)
t9.onclick(left_click9,3)

t.done()




























