import sys

def join(iteration,line):
	str = ""
	obj,x,y,w,h=line.split(" ")
	x,y,w,h=float(x),float(y),float(w),float(h)
	if(iteration==1):
		x,y,w,h=x/2,y/2,w/2,h/2
	elif(iteration==2):
		x,y,w,h=(x/2)+.5,y/2,w/2,h/2
	elif(iteration==3):
		x,y,w,h=x/2,(y/2)+.5,w/2,h/2
	elif(iteration==4):
		x,y,w,h=(x/2)+.5,(y/2)+.5,w/2,h/2
	else:
		print(Error)

	str=obj+" "+str(x)+" "+str(y)+" "+str(w)+" "+str(h)
	return str

finalFile = open(sys.argv[1]+".txt","w")

for i in range(1,5):
	fi = open(str(i)+sys.argv[1]+".txt","w")
	for j in range(1,5):
		f = open(str(j)+str(i)+sys.argv[1]+".txt","r")
		for line in f:
			st = join(j,line)
			fi.write(st)
		f.close()
	for ll in fi:
		st = join(i,ll)
		finalFile.write(st)
	fi.close()
		
