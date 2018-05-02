#!/usr/bin/python3
'''
This is a python Tkinter program to simulate a 16x32 LED Matrix
to enable the user to 'draw' on it and get the resulting data
in a list for displaying on a real LED matrix.
'''
__author__ = "Haoxi Tan"

#python 2/3 compatible
try:
    from tkinter import *
except:
    from Tkinter import *
import numpy as np

root=Tk()
root.title("TkMatrix")

#create the data matrix with numpy library
#change this to the layout you want (eg 8,8)
data=np.ones((16,32))


#create the output widget as a Label

display=Toplevel(root)
display.title("Display")
display.grid()


output=Text(display, font='Consolas 10',width=80,height=40)
output.grid(row=0,column=0)


#the function for toggling the values for the specific grid

def clear():
    global data
    data=np.ones((16,32))
    #out=str(data)
    #out=out.replace('.',',').replace(',]','],').replace(' ','').replace('\n',' ').replace('],','],\n').replace(' 1','1')

    output.delete(1.0,END)
    #output.insert(END,out)
    mapbuttons()

def save(data):
    '''
    Writes python styled lists into a file called matrix.txt
    Parameters:
        (np.array) data: the array to save
    '''
    with open('matrix.txt','a+') as file:

        matrix = ''
        matrix += '['

        for i in data.tolist():
            #append each row to output after reformatting
            l=len(i)
            matrix += str(i[0:l]).replace('.0','')+',\n'

        matrix += ']\n'

        file.write(matrix)
        print("Saved matrix:")
        print(matrix)


def load():
    '''
    Load data from matrix.txt
    '''
    print("work in progress")
    return

    f=open('matrix','r')
    data=[]
    for i in f:
        i=i.split(', ')
        data.append(i)
    f.close()
    print(data)
    #return data
    
def toggle(r,c):
    '''
    toggle a position and display it on the Text widget.
    Parameters:
        (str) r: row number
        (str) c: column number
    '''
    global data
    r,c=int(r),int(c)
    if data[r][c] == 1:
        data[r][c] = 0
    else:
        data[r][c] = 1
    print('position:',str(r)+','+str(c),'New status:',int(data[r][c]))
    #string curation into a python list format
    np_list_string = str(data)
    
    python_list = np_list_string.replace('.', ',').replace(',]', '],').replace(' ', '').replace('\n', ' ').replace('],', '], \n').replace(' 1', '1') 

    c_list = python_list.replace('[', '{').replace(']', '}')


    output.delete(1.0,END)
    output.insert(END,python_list)
    output.insert(END,'\n\n')
    output.insert(END,c_list)
    #string curation into a python list format
    output.insert(END, ('\n\nLit coordinates:\n'+
                        str(np.argwhere(data == 0)).replace('\n',' ').replace('[ ','[').replace(']  [','],[').replace('  ',',').replace(' ',',') ))

    #print(data.tolist())

    

#use a nested loop based on the data matrix to draw all the buttons
def mapbuttons():
    '''
    Map all buttons
    '''
    global data

    for r in range(len(data)):
        for c in range(len(data[r])):
            #text=(str(r)+','+str(c)),
            buttons=Checkbutton(font='Arial 8',command=lambda r=r,c=c :toggle(r,c))
            buttons.grid(row=r,column=c)

    clearbutton=Button(text='Clear',width=32,height=2,font='Arial 8',command=lambda:clear())
    clearbutton.grid(row=16,column=0,columnspan=30,sticky=E)

    savebutton=Button(text='Save',width=32,height=2,font='Arial 8',command=lambda:save(data))
    savebutton.grid(row=16,column=0,columnspan=30,sticky=W)

    loadbutton=Button(text='Load',width=32,height=2,font='Arial 8',command=lambda:load())
    loadbutton.grid(row=16,column=0,columnspan=30)



if __name__=='__main__':

    mapbuttons()
    root.mainloop()

    
