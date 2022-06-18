#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator 

if __name__ == '__main__':
    
    dict={}

    for line in sys.stdin:
        key, val = line.split("\t")
        val= int(val)
        dict[key]=val
        
    sorted_dict = sorted(dict.items(), key=operator.itemgetter(1))
    for linea in sorted_dict:
        sys.stdout.write("{},{}\n".format(linea[0], linea[1])) 