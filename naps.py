import numpy as np

print("Enter the number of items")
n=input()
w=[]
v=[]
a1={}
wv=[]
a2={}
in1={}

for i in range(0,n):
	print("Enter the weight of item number "+str(i+1))
	w1=input()	
	w.append(w1)
	print("Enter the value of item number "+str(i+1))
	v1=input()
	v.append(v1)
	v1=float(v1)
	w1=float(w1)
	in1[w1]=i
	a1[v1/w1]=int(v1)
	a2[v1/w1]=int(w1)
	wv.append(v1/w1)
wv11=wv
wv.sort()
#print wv
print("Enter the weigth that knapsack can bear:")
kw=input()
t1=kw
nn=len(wv)
vm=0
it=[]
it1=[]
for i in range(nn-1,-1,-1):
	v2=a1[wv[i]]
	#print v2
	w2=a2[wv[i]]
	#print w2
	an=in1[w2]
	if(t1>0):
		if(t1>=w2):
			vm=vm+v2
			t1=t1-w2
			it.append(an+1)
			it1.append(1)
		else:
			it1.append(w2/(wv[i]*t1))
			it.append(an+1)
			vm=vm+(wv[i]*t1)
			t1=0
	if(t1==0):
		break
print("Weight of items\t"+str(w))
print("Value of items\t"+str(v))
print("Value/weight of items\t"+str(wv11))
print("Capacity of knapsack\t"+str(n))
print("\n\n\nTotal value of knapsack(greedy) is: "+str(vm))
#print("Items taken are:")
#print(it)	
#print(it1)

www=kw
nn=len(wv)
km=np.zeros((nn+1,www+1))
for i in range(0,nn+1):
	for j in range(0,www+1):
		if i==0 or j==0:
			km[i][j]=0
		elif j>=w[i-1]:
			km[i][j]=max(km[i-1][j],km[i-1][j-w[i-1]]+v[i-1])
			
		else:
			km[i][j]=max(km[i][j-1],km[i-1][j])

print ("\n\n\nTotal value of knapsack(dynamic) is: "+str(km[nn][www]))