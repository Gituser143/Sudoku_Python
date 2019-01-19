#SYNOPSIS

#Members - Aditi Ahuja, Ishitha Agarwal, Bhargav SNV
#Title - Sudoku Game with GUI
#Description - This code develops a GUI for a sudoku, with a Start Screen, Game Window and Instructions Screen, all referenced from the Start Screen

#Concepts Used - 
#1.For the grid:
#  a.Nested lists
#  b.shuffling and slicing of list

#2.For the GUI:
#  a.Used Tkinter module to design screens.
#  b.Used Toplevel to create window hierarchy for Game Window and Instructions Screen.
#  c.Used frames and canvas to align buttons on the start and game windows.
#  d.Used Entry boxes and Labels for the grid. 


from random import *
import copy
from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox

def create_solution_grid():#function to create complete sudoku grid
    global l,solution
    
    a=randrange(1,10) #Here b,c,i,j,i1,j1,i2,j2 are variables used later and their values are based on the random value of variable 'a'
    if(a%2==0):
        i=3; j=6; j1=1; j2=8; 
    else:
        i=6; j=3; j1=2;j2=7;
    i1 = 0;i2 = 6
    
    a=randrange(1,10)
    if(a%2==0):
        b=4; c=7;
    else:
        c=7; b=4;
    
    l1=[x for x in range(1,10)] #l1 through l9 are rows, l1 is first assigned and values within it are shuffled 
    shuffle(l1)
    for temp in range(0,len(l1)):
        l1[temp]=str(l1[temp])
    #lists l2 to l9 initially have the same values as l1 but are serially shifted 
    #i,b,c,j are the variables used for shifting these variables.
 
    l2=[]
    l2.extend(l1[i::]); l2.extend(l1[0:i:]) 
    l3=[]
    l3.extend(l2[i::]); l3.extend(l2[0:i:]) 
    l4=[]
    l4.extend(l3[b::]); l4.extend(l3[0:b:]) 
    l5 = []
    l5.extend(l4[j::]); l5.extend(l4[0:j:]) 
    l6=[]
    l6.extend(l5[j::]); l6.extend(l5[0:j:]) 
    l7=[]
    l7.extend(l6[c::]); l7.extend(l6[0:c:]) 
    l8=[]
    l8.extend(l7[j::]); l8.extend(l7[0:j:]) 
    l9=[]
    l9.extend(l8[j::]); l9.extend(l8[0:j:]) 
    l=[l1,l2,l3,l4,l5,l6,l7,l8,l9]
    for i in range(0,len(l)):
        l[i][i1],l[i][j1]=l[i][j1],l[i][i1] 
        l[i][i2],l[i][j2]=l[i][j2],l[i][i2] #These two lines swap coloumns based on the earlier random values. 
    solution=copy.deepcopy(l)
 
def create_grid():#function to create unsolved sudoku grid from solution grid
    for i in range(0,len(l)):
        for j in range(0,5):
            l[i][randrange(0,9)]=0
            
def validate_func():#function to check user's grid against correct solution grid.
    global l,input_grid
    
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            if(l[i][j]==0):
                input_value=input_grid[i][j].get()
                l[i][j]=input_value
                
    if(l==solution):
        messagebox.showinfo("SUDOKU","You have solved the puzzle !!")
        exit()
        
    else:
        messagebox.showinfo("SUDOKU","Your solution is not right, try again...")
        
def sol():#function to print the solution grid on the user's choice
    global x,y 
    
    temp=copy.deepcopy(solution)
    for i in range(0,len(l)):
        for j in range(len(l[i])):
             if (i in x and j in x) or (i in y and j in y):#if a cell has indices as [x,x] or [y,y], it will be blue
                     temp[i][j]=Label(main_frame,font="Verdana",relief='sunken',bg='#85C1E9',fg='black',width=4,text=solution[i][j],bd=3)
             else:#cells not in these indices will be gray
                    temp[i][j]=Label(main_frame,font="Verdana",relief='sunken',bg='#D5DBDB',fg='black',width=4,text=solution[i][j],bd=3)
             temp[i][j].grid(row=i,column=j)
            
def exit_func():#function to exit game window
    global rootg
    rootg.destroy()
    exit()

def Start_screen():#function to display Start screen
    global root,rooti
    
    root.configure(background='#E0FFFF')
    root.title('Start Screen')
    
    img1 = Image.open('start_button.jpg')#opening image of start button
    photo1 = ImageTk.PhotoImage(img1)
     
    img2 = Image.open('instructions.png')
    photo2 = ImageTk.PhotoImage(img2)
    
    #canvas used to align sudoku image on start screen
    canvas = Canvas(root, width=501, height=153,bg='#E0FFFF')
    canvas.grid(row=0,column=5)
    img = Image.open('text-sudoku.png')
    Photoimg= ImageTk.PhotoImage(img)
    canvas.create_image(0,0,image=Photoimg,anchor='nw')

    sb=Button(root,image=photo1,width=132,height=69,command=Game_window,bd=1).grid(row=3,column=5)#Play button
    ib = Button(root,image=photo2,width=330,height=50,command=Instruct_screen,bd=1).grid(row=6,column=5)#Instructions button
    root.mainloop()

def Instruct_screen():#function to display instructions screen
    str=""" WELCOME TO THE SUDOKU!
        This is a grid to be filled with the digits 1-9 as per the following rules:
        1.No digit can be repeated in each row,column or 3x3 box.
        2.Each row,column and 3x3 box should contain all the digits.
        HAPPY SOLVING!
        """
    rooti = Toplevel()#to create window hierarchy using Toplevel
    rooti.title('Instructions Screen')
    l = Label(rooti,font='Verdana',bg='#E0FFFF',fg='black',width=80,text=str,bd=3)#creating a label with the instructions
    l.grid(row=3,column=3)

def Game_window():#function to display interactive sudoku game window
    global l,solution,input_grid,rootg,x,y,main_frame
    create_solution_grid()
    create_grid()
    
    rootg = Toplevel() #to create a window hierarchy, wherein the Gamewindow opens upon clicking start button
    rootg.title("Sudoku")
    rootg.configure(background='#E0FFFF')
    
    #packing into frames for separation of widgets.
    title_frame=Frame(rootg)
    main_frame=Frame(rootg)
    button_frame=Frame(rootg)
    input_grid=copy.deepcopy(l)
        
    for i in range(0,len(l)):
        for j in range(0,len(l[i])):
            if(l[i][j]==0):#to accept user inputs for the sudoku
                if (i in x and j in x) or (i in y and j in y):#cells with indices as [x,x] or [y,y] will be blue
                    input_grid[i][j]=Entry(main_frame,font="Verdana",relief='sunken',bg='#85C1E9',fg='#7D3C98',width=4,bd=3);
                else:#cells not in these indices will be gray
                    input_grid[i][j]=Entry(main_frame,font="Verdana",relief='sunken',bg='#D5DBDB',fg='#7D3C98',width=4,bd=3);
                input_grid[i][j].grid(row=i,column=j);
            
            else:#to print labels with digits already given to user
               if (i in x and j in x) or (i in y and j in y):
                    input_grid[i][j]=Label(main_frame,font="Verdana",relief='sunken',bg='#85C1E9',fg='black',width=4,text=l[i][j],bd=3)
               else:     
                    input_grid[i][j]=Label(main_frame,font="Verdana",relief='sunken',bg='#D5DBDB',fg='black',width=4,text=l[i][j],bd=3)
               input_grid[i][j].grid(row=i,column=j)

    #creating function buttons for the Game Window
    B1=Button(button_frame,width=20,height=3,bg = '#85C1E9',fg='black',text="Validate sudoku",command=validate_func,bd=4).grid(row=0,column=3)
    B2=Button(button_frame,width=20,height=3,bg = '#E74C3C',fg='black',text="Exit sudoku",command=exit_func,bd=4).grid(row=2,column=3)
    B3=Button(button_frame,width=20,height=3,bg = '#2ECC71',fg='black',text="Show solution",command=sol,bd=4).grid(row=1,column=3)
    main_frame.grid(row=0,column=0)
    button_frame.grid(row=1,column=0)

x = [0,1,2,6,7,8]#indices for blue cells  
y = [3,4,5]  

l=[] #l is the grid
solution=[]

root = Tk()

for i in range(0,len(l)):
    for j in range(0,len(l[i])):
        solution[i][j]=str(solution[i][j])


Start_screen()
