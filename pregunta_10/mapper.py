#
# >>> Escriba el codigo del mapper a partir de este punto <<<
#
import sys

if __name__ == '__main__':

  for line in sys.stdin:

    data= line.split()
    letters= data[1].split(',')
    for letter in letters:
      sys.stdout.write("{}\t{}\n".format(letter, data[0]))