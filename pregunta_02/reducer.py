#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

from pyrsistent import s 

if __name__ == '__main__':

    last_key=None
    max_val=0

    for line in sys.stdin:

        key , val = line.strip().split("\t")
        
        if last_key and last_key != key:
            print("%s\t%s" % (last_key, max_val))
            (last_key, max_val) = (key, int(val))
        else:
            (last_key, max_val) = (key, max(max_val, int(val)))
    
    sys.stdout.write("{}\t{}\n".format(last_key, max_val))

        