#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator

if __name__ == '__main__':
    
    for line in sys.stdin:

        lista = line.split(" ")

        sys.stdout.write("{}   {}   {}\n".format(lista[0], lista[2].strip(), int(lista[1])))
            