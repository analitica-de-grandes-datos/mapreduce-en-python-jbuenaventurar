#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

  for line in sys.stdin:

    lista= line.strip().replace('-', ' ').split(' ')

    sys.stdout.write("{}\t{}\n".format(lista[0], lista[8]))