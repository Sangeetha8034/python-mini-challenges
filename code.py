# --------------
#Code starts here
def palindrome(num):
    l=[]
    t=num
    while t>0:
        l.append(t%10)
        t=t//10
    l.reverse()
    tlen=len(l)
    if l.count(9)==tlen:
        return num+2
    else:
        return smallPalin(l,tlen)

def smallPalin(lis,n):
    mid=n//2
    left=mid-1
    npalin=False
    right=mid+1 if(n%2) else mid
    while(left>=0 and lis[left]==lis[right]):
        left-=1
        right+=1
    if(left<0 or lis[left]<lis[right]):
        npalin=True
    while(left>=0):
        lis[right]=lis[left]
        left-=1
        right+=1
    if npalin:
        c=1
        left=mid-1
        if n%2:
            lis[mid]+=c
            c=lis[mid]//10
            lis[mid]%=10
            right=mid+1
        else:
            right=mid
        while(left>=0):
            lis[left]+=c
            c=lis[left]//10
            lis[left]%=10
            lis[right]=lis[left]
            left-=1
            right+=1
    st=''
    for i in lis:
        st=st+str(i)
    return int(st)



# --------------
#Code starts here
def a_scramble(str_1, str_2):
    str_1=str_1.strip().lower()
    str_2=str_2.strip().lower()
    dic={}
    for i in str_2:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for i in str_1:
        if i in dic:
            dic[i]-=1
    for i in dic:
        if dic[i]>0:
            return False            
    return True



# --------------
#Code starts here
def check_fib(num):
    if num==0 or num==1:
        return True
    else:
        return isPossible(1,1,num)

def isPossible(f,s,n):
    if f+s==n:
        return True
    elif f+s>n:
        return False
    else:
        return isPossible(s,f+s,n)


# --------------
#Code starts here
def compress(word):
    word=word.strip().lower()
    c=word[0]
    cnt=1
    ans=''
    for i in range(1,len(word)):
        if word[i]==c:
            cnt+=1
            continue
        else:
            ans=ans+c+str(cnt)
        c=word[i]
        cnt=1
    ans=ans+c+str(cnt)
    return ans


# --------------
#Code starts here
def k_distinct(string,k):
    string=string.strip().lower()
    l=[]
    for i in string:
        if i not in l:
            l.append(i)
    if len(l)==k:
        return True
    else:
        return False


