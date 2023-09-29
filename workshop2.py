p = 1
q = 1
fibo = [1,1]
fibo.append(p*fibo[0] + q*fibo[1])
fibo.append(p*fibo[1] + q*fibo[2])
print("p = {} , q = {}, the list is: {}".format(p,q,fibo))