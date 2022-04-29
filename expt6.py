import math

def minimax(l,d):
    if d==1:
        return max(l)
    else:
        i = 0
        a = []
        n = len(l)
        if d%2==0:
            while i<n:
                a.append(min(l[i],l[i+1]))
                i += 2
        else:
            while i<n:
                a.append(max(l[i],l[i+1]))
                i += 2
        l = a
        d = int(math.log(len(l),2))
        return minimax(l,d)
 
   
scores = [3,5,2,9,12,5,21,23] 

d = math.log(len(scores), 2)

print('The optimum score is -')
print(minimax(scores,int(d)))