import turtle

def drawCakeLayer(x,y,fill_color):
    t=turtle
    t.speed(1)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.left(90)
    t.forward(150)
    t.left(90)
    t.forward(50)
    t.end_fill()

def drawCakeCream(x,y,fill_color):
    t=turtle
    t.speed(1)
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.left(180)
    t.forward(20)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(20)

def drawCakeLayer2(x,y,fill_color):
     t=turtle
     t.speed(1)
     t.penup()
     t.goto(x,y)
     t.pendown()
     t.fillcolor(fill_color)
     t.begin_fill()
     t.forward(50)
     t.left(90)
     t.forward(150)
     t.left(90)
     t.forward(50)
     t.left(90)
     t.forward(150)
     t.end_fill()

def drawCakeCream2(x,y,fill_color):
     t=turtle
     t.speed(1)
     t.penup()
     t.goto(x,y)
     t.pendown()
     t.fillcolor(fill_color)
     t.begin_fill()
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(150)
     t.left(90)
     t.forward(20)
     t.left(90)
     t.forward(150)
     t.end_fill()

def circleDecoration(x,y,radius,fill_color):
    t=turtle
    t.penup()
    t.goto(x,y)
    t.pendown()
    t.fillcolor(fill_color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


def Pineapple():
    drawCakeLayer(-80,-50,"Yellow")
    drawCakeCream(-80,0,"white")
    drawCakeLayer2(-80,70,"Yellow")
    drawCakeCream2(-80,90,"white")
    circleDecoration(-8,98,4,"red")

def strawBerry():
    drawCakeLayer(-80,-50,"red")
    drawCakeCream(-80,0,"white")
    drawCakeLayer2(-80,70,"red")
    drawCakeCream2(-80,90,"white")
    circleDecoration(-8,98,4,"red")

def Vanilla():
    drawCakeLayer(-80,-50,"chocolate")
    drawCakeCream(-80,0,"white")
    drawCakeLayer2(-80,70,"chocolate")
    drawCakeCream2(-80,90,"white")
    circleDecoration(-8,98,4,"red")

def main():
    flavor= input("choose a cake flavor (Pineapple, strawberry and vanilla): ")
    if flavor== "Pineapple":
        return Pineapple()
    elif flavor== "strawBerry":
        return strawBerry()
    elif flavor== "Vanilla":
        return Vanilla()
    input("enter to exit")
main()







     






























