#
# >>> Escriba el codigo del reducer a partir de este punto <<<
#
import sys
import operator 

if __name__ == '__main__':
    
    my_list={}

    for line in sys.stdin:
       line = line.strip()
       letter, value = line.split('\t')
       
       if letter in my_list:
           my_list[letter].append(float(value))
       else: 
           my_list[letter] = []
           my_list[letter].append(float(value))
           
    for letter in my_list.keys():
        sum_letter = sum(my_list[letter])
        aver_letter = sum(my_list[letter])/ len(my_list[letter])
        print('%s\t%s\t%s'% (letter, sum_letter, aver_letter))
           
    