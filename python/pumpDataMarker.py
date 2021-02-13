import glob 
import subprocess


#Symbol,Timestamp,Date,Open,High,Low,Close,Volume,MA_High,MA_Volume,P_Anomaly,V_Anomaly
print("Starting..")
files = glob.glob(r"../data/*.csv")
print(files)
for f in files:
    cmd="tac "+f+" >temp.csv" 
    print(cmd)
    log3 = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output,error=log3.communicate()
    flag=False
    count=0	
    print('Processing ', f)
    file = open("temp.csv")
    Lines = file.readlines()
    line1 = Lines[-1]
    with open("../data/flag/"+f[8:], "a") as file_object:
        file_object.write(line1[:-1]+","+"PrePump\n")
    
    for line in Lines[:-1]:
        l = line.split(',')
        if(count==0):
            if(l[-1][:-1]==l[-2] and l[-2]=="True"):
                flag=True
                count=1
                with open("../data/flag/"+f[8:], "a") as file_object:
                    file_object.write(line[:-1]+","+str(flag)+"\n")
            else:
                flag=False
                with open("../data/flag/"+f[8:], "a") as file_object:
                    file_object.write(line[:-1]+","+str(flag)+"\n")
        else:
            if(count<13):
                with open("../data/flag/"+f[8:], "a") as file_object:
                    file_object.write(line[:-1]+","+str(flag)+"\n")
                    count+=1
            else:
                count=0
                flag=False
                with open("../data/flag/"+f[8:], "a") as file_object:
                    file_object.write(line[:-1]+","+str(flag)+"\n")

print("..Over!!!")