def interp(shapes,texts,arrowsin):
    result=""
    defin=0
    cond=0
    iforelse=-1
    i=0
    while (i<len(shapes)):
        interp1(shapes[i],texts[i],arrowsin[i])
        i+=1
    exec(result)
    def interp1(shape,text,arrowsin):
        if (cond==0):
            if (shape=="rectangle"):
                result+=text+'\n'
            if (shape=="diamond"):
                cond+=1
                result+="if ("+text+"):\n"
        elif cond>0:
            if (text[0]=="y"):
                iforelse=1
                text=text[2:]
            elif(text[0]=="n"):
                iforelse=0
                text=text[2:]
                result+=(cond-1)*"    "+"else:\n"
            if (iforelse==0):
                if (arrowsin==2):
                     cond-=1
            if (shape=="rectangle"):    
                result+=(cond)*"    "+text+'\n'
            if (shape=="diamond"):
                result+=(cond)*"    "+"if ("+text+"):\n"
                cond+=1
                iforelse=-1

#example run:            
a=("rectangle","diamond","rectangle","diamond","rectangle","rectangle","rectangle","rectangle")#list of shapes
b=("a=30","a<50","y.b=0","n.a>75","y.b=90","n.b=75","print(100)","print(b)")#list of text in shapes
c=(1,1,1,1,1,1,2,2,1)#list of arrows, pointing in
interp(a,b,c)
