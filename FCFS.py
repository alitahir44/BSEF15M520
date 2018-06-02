#!/usr/bin/python
process=[]
total=0
t_time=0
total=input("Enter total number of processes:")
for i in range(int(total)):
	process.append([])
	process[i].append(raw_input("Enter processes name:"))
	process[i].append(int(raw_input("Enter arrival time:")))
	process[i].append(int(input("Enter burst time:")))
	t_time=t_time+process[i][2]

process.sort(key=lambda process:process[1])

for i in range(int(total)):
	print(process[i][0],'\t',process[i][1],'\t',process[i][2])
	
print ("Total: ", t_time)

