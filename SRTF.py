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
x=0
n=raw_input("Enter n0. of processes:")
def readData():
	
	for i in range(int(n)):
		bt.append([])
		bt[i].append(int(raw_input("Enter burst time: ")))
		at.append([])
		at[i].append(int(raw_input("Enter arrival time: ")))

def init(total=0):
	import copy
	for i in range(int(n)):
		rt=copy.copy(bt)
		finish.append([])
		finish[i].append(0)
		wt.append([])
		wt[i].append(0)
		tat.append([])
		tat[i].append(0)
		total=total+bt[i][0]
	return total

def SRTF(time=0, next=0, old=0, i=0):
	readData();
	total=init();
	print total
	for time in range(int(total)):
		old=next
		next=getProcess(time)
		print next
		if old!=next or time==0:
			print time, "==p", next+1, "==|"
		rt[next][0]=rt[next][0]-1
		if rt[next][0]==0:
			finish[next][0]=1
		for j in range(int(n)):
			if i!=next and finish[i][0]==0 and at[i][0]<=time:
				wt[i][0]=wt[i][0]+1
	print total
	for i in range(int(n)):
		if finish[i][0]==0:
			print "Scheduling error"
	displayTime();

def displayTime(twt=0, ttat=0):
	for i in range(int(n)):
		print wt[i][0]
	for i in range(int(n)):
		twt=twt+wt[i][0]
		tat[i][0]=wt[i][0]+bt[i][0]
		ttat=ttat+tat[i][0]
		print "Waiting time for P", (i+1), ": ", wt[i][0]
	print "Average waiting time: ", twt
	print "Average turn around time: ", ttat

def getProcess(time, low=0):
	for i in range(int(n)):
		if finish[i][0]==0:
			low=i
			break
	for i in range(int(n)):
		if finish[i][0]!=1:
			print i
			if rt[i][0]<rt[low][0]:
				if at[i][0]<=time:
					low=i
	return low
SRTF();
