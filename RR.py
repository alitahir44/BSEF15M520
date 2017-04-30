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

def RR(time=0, a=0, dec=0):
	readData();
	total=init();
	a=raw_input("Enter the time quantum:")
	for time in range(int(total)):
		for i in range(int(n)):
			if at[i][0]<=time and finish[i][0]==0:
				print time, "p=>",(i+1)
				x=rt[i][0]
				if x<a:
					dec=rt[i][0]
				else:
					dec=a
				rt[i][0]=rt[i][0]-dec
				if rt[i][0]==0:
					finish[i][0]=1
				for j in range(int(n)):
					if j!=i and finish[j][0]==0 and at[j][0]<=time:
						wt[j][0]=wt[j][0]+dec
				time=time+dec
	print total
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
RR();
