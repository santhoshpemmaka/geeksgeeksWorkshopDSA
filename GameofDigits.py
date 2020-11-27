find the smallest number K, such that product of digits of K is equal to N.
Testcase 1: 26 is the smallest number, and product of 2 and 6 is 12.
Testcase 2: 5 is the smallest number which is itself equal to 5.

Answer:-
def smallestK(n):
    # code here
    # retured value will be printed by driver code
    if n>=0 and n<=9:
        return n
    digits = list()
    for i in range(9,1,-1):
        while n% i ==0:
            digits.append(i)
            n = n//i
    if n != 1:
        return -1
    else:
        k = 0
        while len(digits) != 0:
            k = k*10+digits[-1]
            digits.pop()
        return k
