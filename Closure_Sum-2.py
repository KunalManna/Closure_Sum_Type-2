#input-1:  1039           Explanation:  1+9=19  0+3=3
#Output:   22                     Ans:  19+3=22


#input-2:  2224555        Explanation:  2+5=25  2+5=25  2+5=25   4
#output:   79                     Ans:  25+25+125=4 79



s=input("Enter the numbers:\n")
n=len(s)
l=[]
for i in range(0,n//2):
    p=s[i]+s[-1-i]
    l.append(int(p))
add=sum(l)
if n%2==0:
    print(add)
else:
    print(add+int(s[n//2]))