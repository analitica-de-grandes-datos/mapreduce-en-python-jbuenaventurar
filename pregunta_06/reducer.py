#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys

if __name__ == '__main__':

    curkey=None
    max_val=0
    min_val=0

    for line in sys.stdin:

        row=line.split("\t")
        key=row[0]
        val=float(row[1])
        
        
        if key == curkey:

            if val > max_val:
                max_val = val
            else:
                val=max_val
            
            if val < min_val:
                min_val=val
            else:
                val=min_val
            
        else:
            if curkey is not None:
                sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_val, min_val))
            
            curkey = key
            max_val = val
            min_val = val
    
    sys.stdout.write("{}\t{}\t{}\n".format(curkey, max_val, min_val))