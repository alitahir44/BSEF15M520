#!/usr/bin/python
n=0
bt=[]
at=[]
tat=[]
wt=[]
rt=[]
finish=[]
twt=0
ttat=0
total=0
qt=0
x=-1
import os
os.system('clear')
n=int(raw_input("Enter n0. of processes:"))
def readData():
	
	for i in range(int(n)):
		bt.append([])
		bt[i].append(int(raw_input("Enter burst time: ")))
		at.append([])
		at[i].append(int(raw_input("Enter arrival time: ")))

def init(total=0):
	for i in range(int(n)):
		rt.append([])
		rt[i]=bt[i][0]
		finish.append([])
		finish[i].append(0)
		wt.append([])
		wt[i].append(0)
		tat.append([])
		tat[i].append(0)
		total=total+bt[i][0]
	return total
def RR(time=0, a=0, dec=0,qt=0,x=-1,count=0,min=0):
	readData();
	total=init();
	qt=int(raw_input("Enter the time quantum:"))
	import Queue
	q=Queue.Queue()
	for i in range(int(n)):	
		at.append([])
		at[i].append(int(0))
	print "OUTPUT\n---------------------------------------------------------"
	while time<total:
		for z in range(int(n)):
			if at[z][0]<=time:
				count=count+1
				if at[min][0]>at[z][0]:
					min=z
		if count==0:
			time=at[min][0]
			print "(0)==CPU Free==",
				
		for j in range(int(n)):
			
			if rt[j]>0:
				if at[j][0]<=time and finish[j][0]==0 and at[j][1]!=1 and j!=x:
					at[j][1]=1
					q.put(j)
				if x!=-1:		
					if at[x][1]==0 and finish[x][0]==0:
						q.put(x)	
				if q.empty()==False:
					i=q.get()
					x=i
					at[i][1]=0
					print "(",time,")==p",x+1,"==",
					if rt[i]<qt:
						dec=qt
						time=time+rt[i]
					else:
						time=time+qt
					rt[i]=rt[i]-qt
					if rt[i]<=0:
						finish[i][0]=1
					for k in range(int(n)):
						if k!=i and finish[k][0]==0 and at[k][0]<=time:
							wt[k][0]=wt[k][0]+dec
	print "(",total,")\n---------------------------------------------------------"


	
	displayTime();

def displayTime(twt=0, ttat=0):
	for i in range(int(n)):
		twt=twt+wt[i][0]
		tat[i][0]=wt[i][0]+bt[i][0]
		ttat=ttat+tat[i][0]
		print "Waiting time for P", (i+1), ": ", wt[i][0]
	print "Average waiting time: ", twt/n
	print "Average turn around time: ", ttat/n

#def getProcess():
RR();
