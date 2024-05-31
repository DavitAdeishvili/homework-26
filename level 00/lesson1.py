from turtle import *

# we want to paint a house

# step 1: draw a square
width (7)
color ("grey")
begin_fill ()
forward (300)
left(90)
forward(300)
left(90)
forward (300)
left(90)
forward (300)
left(90)
end_fill ()

# end of square
# drawing a door
forward (100)
color ("brown")
begin_fill ()
left (90)
forward (150)
right (90) #height of the door
forward (100)
right (90)
forward (150)
end_fill ()
#now lets draw roof of the house
penup ()
goto (300, 300)
pendown ()
color ("brown")
begin_fill ()
right (150)
forward (300)
left (120)
forward (300)
end_fill ()
#now lets start drawing windows
penup ()
goto (60, 200)
pendown ()
color ("brown")
begin_fill ()
left (210)
forward (50)
right (90)
forward (50)
right (90)
forward (50)
right (90)
forward (50)
right (90)
end_fill ()
#first one is done
penup ()
goto (180, 200)
pendown ()
color ("brown")
begin_fill ()
forward (50)
right (90)
forward (50)
right (90)
forward (50)
right (90)
forward (50)
right (90)
end_fill ()
#congratulation we have finished drawing a house!!!







exitonclick ()