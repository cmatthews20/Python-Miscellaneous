
def slice(a,i,j,k):
    s=''
    if i<j:
        s=a[i:j:k]
    elif i>j:
        s=a[j:i:k]
    return s

#t=slice('abcdefghijklmnopqrstuvwxyz',2,20,3)
t = slice('cfilor',4,2,1)
print(t)