import streamlit as st
from streamlit.proto.RootContainer_pb2 import MAIN

st.title("IP Block Allocation")

#taking input
ip = st.text_input('Insert IP')
ip = str(ip)

#if considering prefix value instead of mask
prefix = st.number_input('Insert Network Mask')
prefix = int(prefix)

#decimaltobinary
def decimalToBinary(n):
    return bin(n).replace("0b","")

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

"""IP Validation"""
#validation function

def validIPv4(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        st.write("IP address {} is not valid".format(ip))
        return False

    for part in parts:
        if not isinstance(int(part), int):
            st.write("IP address {} is not valid".format(ip))
            return False

        if int(part) < 0 or int(part) > 255:
            st.write("IP address {} is not valid".format(ip))
            return False
 
    st.write("IP address {} is valid".format(ip))
    return True 

"""First Adress"""

parts = ip.split('.')
map_parts = map(int,parts)
#integer list of ip
ip_list=list(map_parts)

mask = 1
for i in range (1,32):
    if(i<prefix):
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

"""Last Address"""
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

# Driver's code
if __name__ == "__main__":
    validIPv4(ip)
    st.write(firadd)

    noofaddr = int(pow(2,32-prefix))
    st.write(noofaddr)

    st.write(lar)
 