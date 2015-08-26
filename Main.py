from Tkinter import *

root = Tk()
root.title('Scrolling!')
root.geometry("1344x600+0+0")

canvas = Canvas(root,width=1216,height=576,scrollregion=(0,0,5376,3072))
#168x96 32x32 tiles is required for a 5376x3072 px map
canvas.config(width=1216,height=600)
canvas.pack(expand=True)
canvas.config(xscrollincrement='32')
#set to the size of the tiles


hbar=Scrollbar(root,orient=HORIZONTAL)
hbar.pack()
hbar.config(command=canvas.xview)


vbar=Scrollbar(root,orient=VERTICAL)
vbar.pack()
vbar.config(command=canvas.yview)

canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)



def right(event):
    canvas.xview_scroll(1, "units")
def left(event):
    canvas.xview_scroll(-1, "units")
def up(event):
    canvas.yview_scroll(-1, "units")
def down(event):
    canvas.yview_scroll(1, "units")
    
    
    
def maps():
    t1 = PhotoImage(file='uno.gif')
    t2 = PhotoImage(file='dos.gif')
    t3 = PhotoImage(file='tres.gif')
    root.t1 = t1
    root.t2 = t2
    root.t3 = t3
    
    coords = [16,16]
    tile_list = []
    
    attempt = canvas.create_rectangle(0,0,32,32,fill='purple')
    attempt2 = canvas.create_image(32,32,image=t2)
    
    
    with open('first_map.txt','r') as imperfect:
        imp = imperfect.read()
        imp = imp.replace(",","")
    with open('first_map.txt','w') as fixed:
        fixed.write(imp)
    
    with open('first_map.txt','r') as map_:  
        make = False
        while True:
            c = (map_.read(1))
            if not c:
                break
                
           
            if c == """\n""":
                coords[1] += 32
                coords[0] = 16
                make = False
            
               
            elif c == '1':
                make = True
                tileimg = t1
            elif c == '7':
                tileimg = t2
                make = True
            elif c =='3':
                tileimg = t3
                make = True
            else:
                print "this should not be printed"
                print c
              
                  
            
            if make == True:
            
                    
                tile = canvas.create_image(*coords,image=tileimg)
                tile_list.append(tile)
                    
        
                coords[0] += 32
            
            
        


maps()
    
    
    
    
    
root.bind("<d>",right)
root.bind("<a>",left)
root.bind("<w>",up)
root.bind("<s>",down)

root.mainloop()