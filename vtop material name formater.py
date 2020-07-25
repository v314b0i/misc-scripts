import os
import sys

PUT_MONTH_FIRST=True

path=os.getcwd()
try:
	path=sys.argv[1]
except:
	pass

x=os.listdir(path)
path=path+"/"
exc=0
for i in x:
	print("1-\t"+i)
	try:
		if len(i.split("Material_",1))==2:
			os.rename(path+i,path+i.split("Material_",1)[1].split("_",1)[1])
		if (i[0]=="I"):
			os.rename(path+i,path+i.split("_",1)[1])
		if (len(i.split("VL20",2))==2):
			os.rename(path+i,path+i.split("VL20",2)[1].split("_",2)[1])
	except:
		exc+=1
		continue
print("\n\t"+str(exc)+" exceptions occoured and ignored.")
exc=0
if PUT_MONTH_FIRST:
	x=os.listdir(path)
	for i in x:
		print("2-\t"+i)
		try:
			i2=i.split("-",2)
			if (not len(i2)==3) or i2[0][0] not in "0987654321":
				continue
			i2=i2[1]+"-"+i2[0]+"-"+i2[2]	
			os.rename(path+i, path+i2)
		except:
			exc+=1
			continue
	print("\n\t"+str(exc)+" exceptions occoured and ignored.")
