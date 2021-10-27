import matplotlib .pyplot as plt
import psutil as p

appnamesdict ={}
count=0

for process in p.process_iter():
    count=count + 1
    
    if count <= 6:
        name = process.name()
        cpuusage = p.cpu_percent()
        print("Name: ", name, "-- cpu usage: ", cpuusage)
        appnamesdict.update({name: cpuusage})
        keymax=max(appnamesdict, key=appnamesdict.get)
        print(keymax)
        keymin=min(appnamesdict, key=appnamesdict.get)
        print(keymin)
        nlist=[keymax, keymin]
        print(nlist)
        app = appnamesdict.values()
        maxapp = max(app)
        print(maxapp)
        minapp = min(app)
        print(minapp)
        maxminlist=[maxapp,minapp]
        print(maxminlist)
        
        
plt.figure(figsize=(15,7))
plt.xlabel("Apps")
plt.ylabel("usage")
plt.bar(nlist,maxminlist,width=0.6,color=("purple", "green"))
plt.show()