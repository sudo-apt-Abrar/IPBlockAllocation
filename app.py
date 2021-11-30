from tkinter import *
import tkinter as tk

"""GUI using tkinter"""

screen = tk.Tk()
screen.geometry("500x500")
screen.title("IP Block Allocation")
heading = Label(text = "IP Block Allocation", bg = "grey", fg = "black", width = "500", height = "3")
heading.pack()

##command
def save_info():
    ip_info = ip.get()
    prefix_info = prefix.get()
    ipval = validIPv4(ip_info)
    maskval = validmask(prefix_info)
    if(ipval and maskval):
        parts = ip_info.split(".")
        map_parts = map(int,parts)
        #integer list of ip
        ip_list=list(map_parts)
        
        mask = 1
        for i in range (1,32):
            if(i<prefix_info):
                mask = mask*10 + 1
            else:
                mask = mask*10 + 0

        mask = str(mask)

        #converting the mask to numeric split int-array
        res = []
        for idx in range(0, len(mask), 8):
            res.append(mask[idx : idx + 8])

        fa=[]
        firadd=""
        for i in range (0,4):
            fa.append(binaryToDecimal(res[i]) & ip_list[i])
            if(i<3):
                firadd += str(fa[i])+"."
            else:
                firadd+= str(fa[i])

        ##Last Address
        #Not of mask
        def rev(str):
            rev=''
            for i in str:
                if i == '1':
                    rev += '0'
                elif i == '0':
                    rev += '1'
            return rev

        la=[]
        lar=""
        for i in range(0,4):
            la.append(binaryToDecimal(rev((res[i]))) | ip_list[i])  
            if(i<3):
                lar += str(la[i])+"."
            else:
                lar+= str(la[i])

        ##Block size and Display
        noofaddr = int(pow(2,32-prefix_info))

        # print("First Address: "+firadd)
        label = Label(screen, text= "First Address: {}".format(firadd))
        label.pack() 
        label.place(x = 15, y = 320)
        label = Label(screen, text= "Last Address: {}".format(lar))
        label.pack() 
        label.place(x = 15, y = 340)
        # print("Last Address: "+lar)
        
        label = Label(screen, text= "No. of addresses: {}".format(noofaddr))
        label.pack() 
        label.place(x = 15, y = 360)
        # print("No. of addresses: {}".format(noofaddr))
        label = Label(screen, text= "Block Allocation:")
        label.pack() 
        label.place(x = 15, y = 380)

        ##Block allocation(any 3)
        for i in range(0,3):
            bloc1=""
            blocf1 = cloning(la)
            blocf1[3] += noofaddr*i + 1
            if(blocf1[3]>255):
                blocf1[2] += 1
                blocf1[3] = 0 
            blocl1 = cloning(blocf1)
            blocl1[3] += noofaddr-1
            if(blocl1[3]>255):
                blocl1[2] += 1
                blocl1[3] = 0 
            label = Label(screen, text= "Block {}: {}.{}.{}.{}/{} - {}.{}.{}.{}/{}".format(i+1,blocf1[0],blocf1[1],blocf1[2],blocf1[3],prefix_info,blocl1[0],blocl1[1],blocl1[2],blocl1[3],prefix_info))
            label.pack() 
            label.place(x = 15, y = 400+i*20)
            # print("Block {}: {}.{}.{}.{}/{} - {}.{}.{}.{}/{}".format(i+1,blocf1[0],blocf1[1],blocf1[2],blocf1[3],prefix_info,blocl1[0],blocl1[1],blocl1[2],blocl1[3],prefix_info))

        
    

##Labelling GUI
ip_text = Label(text = "IP Address * ",)
prefix_text = Label(text = "MASK * ",)
ip_text.place(x = 15, y = 70)
prefix_text.place(x = 15, y = 140)



ip = StringVar()
prefix = IntVar()

ip_entry = Entry(textvariable = ip, width = "30")
prefix_entry = Entry(textvariable = prefix, width = "30")

ip_entry.place(x = 15, y = 100)
prefix_entry.place(x = 15, y = 170)

submit = Button(screen,text = "Check Now", width = "30", height = "2", command = save_info, bg = "grey")
submit.place(x = 15, y = 220)

#binarytodecimal
def binaryToDecimal(n):
    num = n
    dec_value = 0
     
    # Initializing base
    # value to 1, i.e 2 ^ 0
    base1 = 1
     
    len1 = len(num)
    for i in range(len1 - 1, -1, -1):
        if (num[i] == '1'):    
            dec_value += base1
        base1 = base1 * 2
     
    return dec_value

#copying ip
def cloning(li1):
    li_copy = li1[:]
    return li_copy

## IP Validation
#validation functions

def validIPv4(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        label = Label(screen, text= "IP address {} is not valid".format(ip))
        label.pack() 
        label.place(x = 15, y = 280) 
        # print("IP address {} is not valid".format(ip))
        return False

    for part in parts:
        if not isinstance(int(part), int):
            label = Label(screen, text= "IP address {} is not valid".format(ip))
            label.pack()
            label.place(x = 15, y = 280) 
            return False

        if int(part) < 0 or int(part) > 255:
            label = Label(screen, text= "IP address {} is not valid".format(ip))
            label.pack() 
            label.place(x = 15, y = 280) 
            return False
 
    label = Label(screen, text= "IP address {} is valid".format(ip))
    label.pack() 
    label.place(x = 15, y = 280) 
    return True 

def validmask(msk):
    if(msk<1 or msk>32):
        label = Label(screen, text= "Mask {} is not valid".format(msk))
        label.pack() 
        label.place(x = 15, y = 300)
        return False
    else:
        label = Label(screen, text= "Mask {} is valid".format(msk))
        label.pack() 
        label.place(x = 15, y = 300)
        return True

screen.mainloop()