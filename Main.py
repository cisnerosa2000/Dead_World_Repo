from Tkinter import *

root = Tk()
root.title('Scrolling!')
root.geometry("1344x600+0+0")
root.config(bg="black")

canvas = Canvas(root,width=1216,height=576,scrollregion=(0,0,6016,3712))
#168x96 32x32 tiles is required for a 5376x3072 px map
canvas.config(width=1216,height=600)
canvas.pack(expand=True)
canvas.config(xscrollincrement='4',yscrollincrement='4')
#2688 is halfway horizontal, 1536 is halfway vertical


hbar=Scrollbar(root,orient=HORIZONTAL)
hbar.pack()
hbar.config(command=canvas.xview)


vbar=Scrollbar(root,orient=VERTICAL)
vbar.pack()
vbar.config(command=canvas.yview)

canvas.config(xscrollcommand=hbar.set,yscrollcommand=vbar.set)

### setting up canvas and window


class Level(object):
    def __init__(self,file):
        self.t1 = PhotoImage(file='border.gif')
        self.t2 = PhotoImage(file='dos.gif')
        self.t3 = PhotoImage(file='tres.gif')
        
        
        
        self.center = [3008,1856]
        canvas.xview_scroll(672, "units")
        canvas.yview_scroll(384, "units")
        
    
        coords = [16,16]
        tile_list = []
    
        
    
    
        with open(file,'r') as imperfect:
            imp = imperfect.read()
            imp = imp.replace(",","")
        with open(file,'w') as fixed:
            fixed.write(imp)
    
        with open(file,'r') as map_:  
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
                    tileimg = self.t1
                elif c == '2':
                    tileimg = self.t2
                    make = True
                
                
              
                  
            
                if make == True:
                    tile = canvas.create_image(*coords,image=tileimg)
                    tile_list.append(tile)
                    
                    if c == "1":
                        canvas.itemconfig(tile,tags="collide")
                    
            
                    
                    
                    
        
                    coords[0] += 32
class Player(object):
    def __init__(self,coords):
        self.right_m = False
        self.left_m = False
        self.up_m = False
        self.down_m = False
        
        self.p = PhotoImage(file='player.gif')
        self.coords = coords
        self.avatar = canvas.create_image(*self.coords,image=self.p)
        
        self.c_img = PhotoImage(file='ch.gif')
        self.mx,self.my = canvas.winfo_pointerxy()
        self.mx = canvas.canvasx(self.mx)
        self.my = canvas.canvasy(self.my)
       
        self.cursor = canvas.create_image(self.mx,self.my,image=self.c_img)        
        
        
        
        self.update()
    def update(self):
        
        #remove this later, this is ONLY for visualing/debugging bullet travel
        self.mx = canvas.canvasx(canvas.winfo_pointerx()) - 62
        self.my = canvas.canvasy(canvas.winfo_pointery()) - 50
        canvas.coords(self.cursor,self.mx,self.my)
        #remove this later, this is ONLY for visualing/debugging bullet travel
        
        
        
        
        self.coords = canvas.coords(self.avatar)
        
        self.llist = []
        self.rlist = []
        self.ulist = []
        self.dlist = []        
            
        self.l_sample = canvas.find_overlapping(self.coords[0]-48,self.coords[1]-16,self.coords[0]+16,self.coords[1]+16)
        for i in self.l_sample:
            if "collide" in canvas.gettags(i):
                self.llist.append(i)
                
        self.r_sample = canvas.find_overlapping(self.coords[0]+48,self.coords[1]-16,self.coords[0]+16,self.coords[1]+16)
        for i in self.r_sample:
            if "collide" in canvas.gettags(i):
                self.rlist.append(i)
                
        self.u_sample = canvas.find_overlapping(self.coords[0]-16,self.coords[1]-16,self.coords[0]+16,self.coords[1]-48)
        for i in self.u_sample:
            if "collide" in canvas.gettags(i):
                self.ulist.append(i)
                
        self.d_sample = canvas.find_overlapping(self.coords[0]-16,self.coords[1]+16,self.coords[0]+16,self.coords[1]+48)
        for i in self.d_sample:
            if "collide" in canvas.gettags(i):
                self.dlist.append(i)
        
        
        if self.up_m == True and len(self.ulist) < 1:
            canvas.yview_scroll(-1, "units")
            canvas.move(self.avatar,0,-4)
        if self.down_m == True and len(self.dlist) < 1:
            canvas.yview_scroll(1, "units")
            canvas.move(self.avatar,0,4)
        if self.left_m == True and len(self.llist) < 1:
            canvas.xview_scroll(-1, "units")
            canvas.move(self.avatar,-4,0)
        if self.right_m == True and len(self.rlist) < 1:
            canvas.xview_scroll(1, "units")
            canvas.move(self.avatar,4,0)
        
        
        
        
        
        
        
        
        root.after(1,self.update)
        
        
        
    def up(self,event):
        self.up_m = True
    def upoff(self,event):
        self.up_m = False
        
        
    def left(self,event):
        self.left_m = True
    def leftoff(self,event):
        self.left_m = False
        
    def down(self,event):
        self.down_m = True
    def downoff(self,event):
        self.down_m = False
        
    def right(self,event):
        self.right_m = True
    def rightoff(self,event):
        self.right_m = False
        
    def fire(self,event):
        st = canvas.coords(self.avatar)
        nd = [self.mx,self.my]


    
    
    

    
            
            
        

level = Level(file="Empty_Map.txt")
player = Player(coords=level.center)
    
    
    
    
    
root.bind("<d>",player.right)
root.bind("<KeyRelease-d>",player.rightoff)


root.bind("<a>",player.left)
root.bind("<KeyRelease-a>",player.leftoff)

root.bind("<w>",player.up)
root.bind("<KeyRelease-w>",player.upoff)

root.bind("<s>",player.down)
root.bind("<KeyRelease-s>",player.downoff)

root.bind("<Button-1>",player.fire)






root.mainloop()