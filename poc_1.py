from pynput import keyboard
from pynput.keyboard import Key
import matplotlib.pyplot as plt
from matplotlib.patches import Arc


def fill_axes(size, start_val):
    x = []
    for i in range(0, size):
        x.append(start_val)
    return x

#def draw_four_line(y_axix_start):

y1 = fill_axes(51,50)
y2 = fill_axes(51,49)
y3 = fill_axes(51,48)

y4 = fill_axes(51,46)
y5 = fill_axes(51,45)
y6 = fill_axes(51,44)

y7 = fill_axes(51,42)
y8 = fill_axes(51,41)
y9 = fill_axes(51,40)

y10 = fill_axes(51,38)
y11 = fill_axes(51,37)
y12 = fill_axes(51,36)

y13 = fill_axes(51,34)
y14 = fill_axes(51,33)
y15 = fill_axes(51,32)

fig,ax= plt.subplots()

#static plots

ax.plot(y1)
ax.plot(y2)
ax.plot(y3)
ax.plot(y4)
ax.plot(y5)
ax.plot(y6)
ax.plot(y7)
ax.plot(y8)
ax.plot(y9)
ax.plot(y10)
ax.plot(y11)
ax.plot(y12)
ax.plot(y13)
ax.plot(y14)
ax.plot(y15)

#dynamic plots

Stick_x = [0,0] 
Stick_y = [48,50]
var = 32
keys_pressed = set()

#setting x limit to navigate to new line automatically
def x_limit():
    global Stick_x,Stick_y
    Stick_x[0] = 0
    Stick_x[1] = 0
    Stick_y[0] -= 4
    Stick_y[1] -= 4

def new_3line():
    yl1 = fill_axes(51,Stick_y[0]-2)
    yl2 = fill_axes(51,Stick_y[0]-3)
    yl3 = fill_axes(51,Stick_y[0]-4)
    ax.plot(yl1)
    ax.plot(yl2)
    ax.plot(yl3)
    plt.draw()
   
# Function to start plotting lines when a key is pressed
def on_key(event):
    global Stick_x, Stick_y,var
    
    #add a new 4 lines automatically 
    if Stick_y[0] == var:
        new_3line()
        var -=4

    #close figure
    if event.key == 'escape':
        plt.close(fig) 

    # Add the pressed key to the keys_pressed set
    keys_pressed.add(event.key)

# 1/2 down /
    if '/' in keys_pressed and '1' in keys_pressed:
        #to navigate to the next line automatically
       
        Stick_x[1]+=0.5
        Stick_y[1]-=1
        if Stick_x[1] > 50:
            x_limit()
            Stick_x[1]+=0.5
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 2
        Stick_x[1] += 1.5
        Stick_y[1] += 1

# 1/2 up /
    if '/' in keys_pressed and '2' in keys_pressed:
        #to navigate to the next line automatically
        Stick_x[0]+=0.5
        Stick_x[1]+=1
        Stick_y[0]+=1

        if Stick_x[1] > 50:
            x_limit()
            Stick_x[0]+=0.5
            Stick_x[1]+=1
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 1.5
        Stick_x[1] += 1
        Stick_y[0] -= 1

# 2 lines /
    if '/' in keys_pressed and '0' in keys_pressed:
        #to navigate to the next line automatically
        Stick_x[1]+=1
        if Stick_x[1] > 50:
            x_limit()
            Stick_x[1]+=1
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 2
        Stick_x[1] += 1
        
# 1 1/2 down /
    if '/' in keys_pressed and '3' in keys_pressed:
        #to navigate to the next line automatically

        Stick_y[0]-=0.5
        Stick_y[1]-=1
        Stick_x[0]-=0.25
        Stick_x[1]+=0.5

        
        if Stick_x[1] > 50:
            x_limit()
            
            Stick_x[0]-=0.25
            Stick_x[1]+=0.5
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 2.25
        Stick_x[1] += 1.5
        Stick_y[0] += 0.5
        Stick_y[1] += 1

# 1 1/2 up /
    if '/' in keys_pressed and '4' in keys_pressed:
        #to navigate to the next line automatically
        Stick_x[0]+=0.5
        Stick_x[1]+= 1.25
        Stick_y[0]+= 1
        Stick_y[1]+= 0.5
        if Stick_x[1] > 50:
            x_limit()
            Stick_x[0]+=0.5
            Stick_x[1]+=1.25
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 1.5
        Stick_x[1] += 0.75
        Stick_y[1] -= 0.5
        Stick_y[0] -= 1

# 2 1/2 down /
    if '/' in keys_pressed and '5' in keys_pressed:
        Stick_x[1]+= 1.25
        Stick_y[0]-= 0.5

        if Stick_x[1] > 50:
            x_limit()
            Stick_x[1]+=1.25
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 2.25
        Stick_x[1] += 1
        Stick_y[0] += 0.5

# 2 1/2 up /
    if '/' in keys_pressed and '6' in keys_pressed:
        #to navigate to the next line automatically
        #Stick_x[0]+=0.25
        Stick_x[1]+= 1.25
        Stick_y[1]+= 0.5
        if Stick_x[1] > 50:
            x_limit()
            #Stick_x[0]+=0.25
            Stick_x[1]+=1.25
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 2
        Stick_x[1] += 0.75
        Stick_y[1] -= 0.5

# 3 /
    if '/' in keys_pressed and '7' in keys_pressed:
        #to navigate to the next line automatically
        
        Stick_y[0]-=0.5
        Stick_y[1]+= 0.5
        Stick_x[0]-=0.25
        Stick_x[1]+=1.25 

        if Stick_x[1] > 50:
            x_limit()
            Stick_x[0]-=0.25
            Stick_x[1]+=1.25
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            

        else:     
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 2.25
        Stick_x[1] += 0.75
        Stick_y[0] += 0.5
        Stick_y[1] -= 0.5

#2 lines \
    if '\\' in keys_pressed and '0' in keys_pressed:

        Stick_x[0]+=1
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()

            Stick_x[0]+=1
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
     
        else:     
            
            print(Stick_x,Stick_y)  
            ax.plot(Stick_x,Stick_y)
         
        plt.draw()
        Stick_x[0] += 1
        Stick_x[1] += 2

#1/2 down \
    if '\\' in keys_pressed and '1' in keys_pressed:
        Stick_y[1]-=1
        Stick_x[1]+=0.5
        Stick_x[0]+=1
        
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()
            Stick_x[1]+=0.5
            Stick_x[0]+=1
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            
        else:     
            
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 1
        Stick_x[1] += 1.5
        Stick_y[1] += 1

#1/2 up \
    if '\\' in keys_pressed and '2' in keys_pressed:
        Stick_x[0]+=0.5
        Stick_y[0]+=1
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()
            Stick_x[0]+=0.5
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            
        else:     
            
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 1.5
        Stick_x[1] += 2
        Stick_y[0] -= 1

#1 1/2 down \
    if '\\' in keys_pressed and '3' in keys_pressed:
        
        Stick_y[0]-=0.5
        Stick_y[1]-=1
        Stick_x[1] +=0.5
        Stick_x[0]+=1.25
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()
            Stick_x[1] +=0.5
            Stick_x[0]+=1.25
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            
        else:     
            
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 0.75
        Stick_x[1] += 1.5
        Stick_y[0] += 0.5
        Stick_y[1]+=1

# 1 1/2 up \
    if '\\' in keys_pressed and '4' in keys_pressed:
        
        Stick_y[0]+=1
        Stick_y[1]+=0.5
        Stick_x[1]-=0.25
        Stick_x[0]+=0.5
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()
            Stick_x[1]-=0.25
            Stick_x[0]+=0.5
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            
        else:     
            
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 1.25
        Stick_x[1] += 2
        Stick_y[0] -= 1
        Stick_y[1]-=0.5

# 2 1/2 down \
    if '\\' in keys_pressed and '5' in keys_pressed:
        
       
        Stick_y[0]-=0.5
        
        #Stick_x[1]+=0.25
        Stick_x[0]+=1.25
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()
            
            Stick_x[0]+=1.25
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            
        else:     
            
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 0.75
        Stick_x[1] += 2
        Stick_y[0] += 0.5
       
# 2 1/2 up \
    if '\\' in keys_pressed and '6' in keys_pressed:
        
        Stick_y[1]+=0.5
        Stick_x[1]-=0.25
        Stick_x[0]+=1
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()
            Stick_x[1]-=0.25
            Stick_x[0]+=1
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
            
        else:     
            
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)

        plt.draw()
        Stick_x[0] += 1
        Stick_x[1] += 2.25
        Stick_y[1] -= 0.5

# 3 \
    if '\\' in keys_pressed and '7' in keys_pressed:
        Stick_y[0]-=0.5
        Stick_y[1]+=0.5
        Stick_x[1]-=0.25
        Stick_x[0]+=1.25
        #to navigate to the next line automatically
        if Stick_x[0] >50:
            x_limit()
            Stick_x[1]-=0.25
            Stick_x[0]+=1.25
            print(Stick_x,Stick_y)
            ax.plot(Stick_x,Stick_y)
     
        else:     
            
            print(Stick_x,Stick_y)  
            ax.plot(Stick_x,Stick_y)
         
        plt.draw()
        Stick_x[0] += 0.75
        Stick_x[1] += 2.25
        Stick_y[1]-=0.5
        Stick_y[0]+=0.5


    #to navigate to the next line automatically
    if event.key == ' ': #space 
        if Stick_x[0] and Stick_x[1] > 50:
            x_limit()

        Stick_x[0] += 1
        Stick_x[1] += 1
   
    #to navigate to the next line manually
    if event.key == 'enter':
        Stick_x[0] = 0
        Stick_x[1] = 0
        Stick_y[0] -= 4
        Stick_y[1] -= 4

# Function to handle key release events
def on_key_release(event):
    # Remove the released key from the keys_pressed set
    keys_pressed.discard(event.key)

# Connect key press event to the figure
fig.canvas.mpl_connect('key_press_event', on_key)
fig.canvas.mpl_connect('key_release_event', on_key_release)
# Show the plot
plt.show()

