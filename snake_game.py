# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 23:58:42 2018

Snake Mini project Starter Code
Name:
Date:
"""


import turtle
import random #We'll need this later in the lab

colorList=['red','orange','yellow','green','blue','purple','pink']
count=0

turtle.tracer(1,0) #This helps the turtle move more smoothly

textTurtle=turtle.clone()
textTurtle.hideturtle()
textTurtle.penup()
textTurtle.goto(0,350)
textTurtle.write("Snake Game !!!",align="center",font=("times",33,"bold"))

scoreTurtle=turtle.clone()
scoreTurtle.hideturtle()
scoreTurtle.penup()
scoreTurtle.goto(0,-350)


SIZE_X=1000
SIZE_Y=1000
turtle.setup(SIZE_X, SIZE_Y) #Curious? It's the turtle window  
                             #size. 
turtle.penup()

SQUARE_SIZE = 20
START_LENGTH = 10

#Initialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []
scoreTurtle.write(int(len(stamp_list)),align="center",font=("times",33,"bold"))
#Set up positions (x,y) of boxes that make up the snake

border = turtle.clone()
border.hideturtle()
border.penup()
border.goto(300,300)
border.pendown()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)
snake = turtle.clone()
snake.shape("square")
snake.color('purple')

turtle.register_shape("trash.gif")
turtle.register_shape("stars.gif")
turtle.register_shape("rock.gif")
screen = turtle.Screen()
screen.setup()
screen.bgpic('stars.gif')


food = turtle.clone()
food.shape("trash.gif")

food.hideturtle()

#Hide the turtle object (it's an arrow - we don't need to see it)
turtle.hideturtle()

#Draw a snake at the start of the game with a for loop
#for loop should use range() and count up to the number of pieces
#in the snake (i.e. START_LENGTH)
for i in range(START_LENGTH) :
    x_pos=snake.pos()[0] #Get x-position with snake.pos()[0]
    y_pos=snake.pos()[1] 

    #Add SQUARE_SIZE to x_pos. Where does x_pos point to now?    
    # You're RIGHT!
    x_pos+=SQUARE_SIZE 

    my_pos=(x_pos,y_pos) #Store position variables in a tuple
    snake.goto(my_pos) #Move snake to new (x,y)
   
    #Append the new position tuple to pos_list
    pos_list.append(my_pos) 

    #Save the stamp ID! You'll need to erase it later. Then append
    # it to stamp_list.             
    snake_stamp= snake.stamp()
    stamp_list.append(snake_stamp)


###############################################################
#                    PART 2 -- READ INSTRUCTIONS!!
###############################################################
UP_ARROW = "Up" #Make sure you pay attention to upper and lower 
                #case
LEFT_ARROW = "Left" #Pay attention to upper and lower case
DOWN_ARROW = "Down" #Pay attention to upper and lower case
RIGHT_ARROW = "Right" #Pay attention to upper and lower case
TIME_STEP = 100 #Update snake position after this many 
                #milliseconds
SPACEBAR = "space" # Careful, it's not supposed to be capitalized!

UP = 0
#1. Make variables LEFT, DOWN, and RIGHT with values 1, 2, and 3
####WRITE YOUR CODE HERE!!
LEFT=1
DOWN=2
RIGHT=3
direction = UP
UP_EDGE = 300
DOWN_EDGE = -300
RIGHT_EDGE = 300
LEFT_EDGE = -300

def up():
    global direction #snake direction is global (same everywhere)
    direction=UP #Change direction to up
    print("You pressed the up key!")

def down():
    global direction #snake direction is global (same everywhere)
    direction=DOWN #Change direction to up
    print("You pressed the down key!")

def left():
    global direction #snake direction is global (same everywhere)
    direction=LEFT #Change direction to up
    print("You pressed the left key!")
def right():
    global direction #snake direction is global (same everywhere)
    direction=RIGHT #Change direction to up
    print("You pressed the right key!")    
#2. Make functions down(), left(), and right() that change direction
####WRITE YOUR CODE HERE!!
turtle.onkeypress(right,RIGHT_ARROW) # Create listener for up key
turtle.onkeypress(left, LEFT_ARROW) # Create listener for up key
turtle.onkeypress(up, UP_ARROW) # Create listener for up key
turtle.onkeypress(down, DOWN_ARROW) # Create listener for up key
#3. Do the same for the other arrow keys
####WRITE YOUR CODE HERE!!

turtle.listen()
def make_food():
    #The screen positions go from -SIZE/2 to +SIZE/2
    #But we need to make food pieces only appear on game squares
    #So we cut up the game board into multiples of SQUARE_SIZE.
    
    min_x=(LEFT_EDGE/SQUARE_SIZE)+1
    max_x=(RIGHT_EDGE/SQUARE_SIZE)-1
    min_y=(DOWN_EDGE/SQUARE_SIZE)+1
    max_y=(UP_EDGE/SQUARE_SIZE)-1

    
    
    #Pick a position that is a random multiple of SQUARE_SIZE
    food_x = random.randint(min_x,max_x)*SQUARE_SIZE
    food_y = random.randint(min_y,max_y)*SQUARE_SIZE
    food.goto(food_x,food_y)
    food_pos.append(food.pos())
    food_stamps.append(food.stamp())

    
        ##1.WRITE YOUR CODE HERE: Make the food turtle go to the randomly-generated
        ##                        position 
        ##2.WRITE YOUR CODE HERE: Add the food turtle's position to the food positions list
        ##3.WRITE YOUR CODE HERE: Add the food turtle's stamp to the food stamps list

def move_snake():
    global count
    count+=1
    snake.color(colorList[count%7])
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]
    
    if direction==RIGHT:
        snake.goto(x_pos + SQUARE_SIZE, y_pos)
        print("You moved right!")
    elif direction==LEFT:
        snake.goto(x_pos - SQUARE_SIZE, y_pos)
        print("You moved left!")
    elif direction==UP:
        snake.goto(x_pos, y_pos + SQUARE_SIZE)
        print("You moved up!")
    elif direction==DOWN:
        snake.goto(x_pos, y_pos - SQUARE_SIZE)
        print("You moved down!")    

        #Grab position of snake
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print('You hit the right edge! Game over!')
        quit()
    elif new_x_pos <= LEFT_EDGE:
        print('You hit the right edge! Game over!')
        quit()
        
    if new_y_pos >= UP_EDGE:
        print('You hit the right edge! Game over!') 
        quit()    
    elif new_y_pos<= DOWN_EDGE:
    
        print('You hit the right edge! Game over!')
        quit()
    #4. Write the conditions for UP and DOWN on your own
    ##### YOUR CODE HERE

    #Stamp new element and append new stamp in list
    #Remember: The snake position changed - update my_pos()
    for j in pos_list:
        if snake.pos() == j:
            quit()
    
    my_pos=snake.pos() 
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    global food_stamps, food_pos
    #If snake is on top of food item
    
    if snake.pos() in food_pos:
        food_ind=food_pos.index(snake.pos()) #What does this do?
        food.clearstamp(food_stamps[food_ind]) #Remove eaten food                 
                                               #stamp
        food_pos.pop(food_ind) #Remove eaten food position
        food_stamps.pop(food_ind) #Remove eaten food stamp
        print('You have eaten the food!')
        global START_LENGTH
        START_LENGTH +=1
        stamp_list.append(snake.stamp())
        pos_list.append(snake.pos())
        scoreTurtle.clear()
        scoreTurtle.write(int(len(stamp_list)-11),align="center",font=("times",33,"bold"))
        global TIME_STEP
        if TIME_STEP >80:
            TIME_STEP=TIME_STEP-5    
        elif TIME_STEP > 60:
            TIME_STEP=TIME_STEP - 4
        elif TIME_STEP > 40:
            TIME_STEP=TIME_STEP-3
        elif TIME_STEP > 20:
            TIME_STEP=TIME_STEP -2
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    
    if len(food_stamps) <= 6 :
        make_food()
    turtle.ontimer(move_snake,TIME_STEP)
move_snake()

    
 #Add trash picture
                      # Make sure you have downloaded this shape 
                      # from the Google Drive folder and saved it
                      # in the same folder as this Python script






#Locations of food


