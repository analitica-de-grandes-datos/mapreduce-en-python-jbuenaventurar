#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':
    def write(letra, lista):
    str_aux=""
    for i in range(len(lista)):
        if i==0:
            str_aux+="\t"+(str(lista[i]))
        else:
            str_aux+=(","+str(lista[i]))
    sys.stdout.write(letra+"\t"+str_aux+"\n")

    curkey=None
    valores=None
    
    a=[]
    b=[]
    c=[]
    d=[]
    f=[]
    g=[]
    h=[]
    i=[]
    for line in sys.stdin:
        row=line.split("\t")
        key=row[0]
        val=int(row[1])
        
        if key!=None and val != None:
            if key=='A':
                a.append(val)
            if key=='B':
                b.append(val)
            if key=='C':
                c.append(val)
            if key=='D':
                d.append(val)
            if key=='F':
                f.append(val)
            if key=='G':
                g.append(val)
            if key=='H':
                h.append(val)
            if key=='I':
                i.append(val)
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    f.sort()
    g.sort()
    h.sort()
    i.sort()
    write("A",a)
    write("B",b)
    write("C",c)
    write("D",d)
    write("F",f)
    write("G",g)
    write("H",h)
    write("I",i)
    
