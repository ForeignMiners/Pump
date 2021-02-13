import glob 
import subprocess


print("Starting..")
files = glob.glob(r"../data/*.csv")
print(files)
for f in files: 
    print('Processing ', f)
    cmd="grep 'True,True' "+f+ " >>PumpList.csv"
    print(cmd)
    log3 = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output,error=log3.communicate()
    

cmd="cut -d ',' -f0 PumpList.csv | awk '!visited[$0]++' >>PumpSymbols.csv"
print(cmd)
log3 = subprocess.Popen([cmd], stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
output,error=log3.communicate()

print("..Over!!!")