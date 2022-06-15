#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import sys if __name__ == '__main__':

    curkey=None
    maximo=0

    for line in sys.stdin:

        key=line[0].split('\t')
        val=line[1].split('\t')
        val=int(val)

        if key == curkey and val > maximo:

            maximo=val

        else:
            if curkey is not None:
                
                sys.stdout.write("{}\t{}\n".format(curkey, maximo))

            curkey=key
            maximo=maximo
    
    sys.stdout.write("{}\t{}\n".format(curkey, maximo))