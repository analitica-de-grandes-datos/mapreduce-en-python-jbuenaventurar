#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator

if __name__ == '__main__':
    
    num_lista=[]
    primera=False
    for line in sys.stdin:
        str_aux=line.replace('\n','')
        num=int(str_aux.split(' ')[1])
        if not primera:
            lis=[num,str_aux]
            num_lista.append(lis)
            primera=True
        else:
            agregado=False
            lis=[num,str_aux]
            for i in range(len(num_lista)):
                if num_lista[i][0]>num:
                    num_lista.insert(i,lis)
                    agregado=True
                    break
            if not agregado:
                num_lista.append(lis)
                
    for l in range(len(num_lista)):
        if l<6:
            aux_str=num_lista[l][1].split(' ')[0]+"   "+num_lista[l][1].split(' ')[2]+"   "+str(num_lista[l][0])
            sys.stdout.write(aux_str+"\n")
        else:
            break
    
    
            
        
        #lista = line.split(" ")
        
    #sorted_data = sorted(lista, key=lambda x: int(x[1]))
    #sorted_data[-1, -5]
    #sys.stdout.write("{}   {}   {}\n".format(lista[0], lista[2].strip(), int(lista[1])))
        
