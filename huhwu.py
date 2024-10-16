import turtle as t  
  
def get_color(num):  
   colors=["black","white","red","yellow","orange","green","yellowgreen","sienna","tan","gray","darkgray"]  
   if num=="A":  
      colorchoice="darkgray"  
   elif num in ["0","1","2","3","4","5","6","7","8","9"]:  
      colorchoice=colors[int(num)]  
   return colorchoice  
    
def draw_color_pixel(color_string,turta):  
    
   t.fillcolor(color_string)  
   t.begin_fill()  
   t.forward(turta)  
   t.left(90)  
   t.forward(turta)  
   t.left(90)  
   t.forward(turta)  
   t.left(90)  
   t.forward(turta)  
   t.left(90)  
   t.end_fill()  
   t.penup()  
   t.forward(turta)  
   t.pendown()  
  
  
def draw_pixel(color_string,turta):  
   color=get_color(color_string)  
   draw_color_pixel(color,turta)  
  
def draw_line_from_string(color_string,turta):  
   for i in color_string:  
      draw_pixel(i,turta)  
    
def draw_shape_from_string(turta):  
   y=turta  
   while True:  
      color_string=input("Enter a string prompt:")  
      detector=0  
      for i in color_string:  
        if i not in ["0","1","2","3","4","5","6","7","8","9","A"]:  
           detector=1  
      if color_string=="":  
        detector=1  
      if detector>0:  
        print("Enter Valid Color String!")  
        break  
      draw_line_from_string(color_string,turta)  
      t.penup()  
      t.goto(0,-y)  
      t.pendown()  
      y*=2  
  
def draw_grid(turta):  
   row1="20202020202020202020"
   row2="02020202020202020202"
   
   for i in range(20):
      if i%2==0:
         ypos= t.ycor() - 20
         t.penup()
         t.goto(0,ypos)
         t.pendown()
         draw_line_from_string(row1,turta)
      else:
         ypos= t.ycor() - 20
         t.penup()
         t.goto(0,ypos)
         t.pendown()
         draw_line_from_string(row2,turta)


   
  
  

    
draw_grid(20)  
    
t.done()



