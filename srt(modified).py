#!/usr/bin/python

bt=[]
at=[]
rt=[]
time=0
n=0
j=0
low=0
total=0
finish=[]
checkCount=0
temp=[]
x=0

n=raw_input("Enter no. of processes: ")
def read():
	
	for i in range(int(n)):
		print "For ", i+1
		bt.append([])		
		bt[i].append(int(raw_input("Enter burst time: ")))
		at.append([])		
		at[i].append(int(raw_input("Enter arrival time: ")))

def init(total=0):
	for i in range(int(n)):
		rt.append([])
		rt[i]=bt[i][0]
		total=total+bt[i][0]
		finish.append([])
		finish[i].append(0)
	return total

def getProcess(time, low=0):
	for i in range(int(n)):
		if finish[i][0]==0:
			low=i
			break
	for i in range(int(n)):
		if finish[i][0]!=1:
			if rt[i]<rt[low]:
				if at[i][0]<=time:
					low=i
	return low	

def SRTF(time=0, next=0, old=0, i=0, total=0):
	read();
	total=init();
	for time in range(int(total)):
		old=next
		next=getProcess(time)
		if old!=next or time==0:
			print "(",time, ")==p", next+1, "==|"
		rt[next]=rt[next]-1
		if rt[next]==0:
			finish[next][0]=1
	print "(",total,")"
	for i in range(int(n)):
		if finish[i][0]==0:
			print "Scheduling error"

SRTF();

