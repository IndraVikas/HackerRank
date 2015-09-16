for i in range(1,input()): #More than 2 lines will result in 0 score. Do not leave a blank line also
     print sum(list(map((lambda x: pow(10,x)), range(0, i))))*i
     # print sum([pow(10,j) for j in range(0,i)])*i