#Task d

def ExpSeq(n):
    a = 5
    if n <= 0:
        return 1
    if n == 1:
        return (10-a)
    else:
        yn = (10-a)*ExpSeq(n-1)
        return yn

seq = [ExpSeq(i) for i in range(1,11)]
print(seq)

