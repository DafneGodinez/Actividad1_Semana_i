import paho.mqtt.client as paho
import time
import psutil

def getListOfProcessSortedByMemory():
    '''
    Get list of running process sorted by Memory Usage
    '''
    listOfProcObjects = []
    # Iterate over the list
    for proc in psutil.process_iter():
       try:
           # Fetch process details as dict
           pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
           pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
           # Append dict to list
           listOfProcObjects.append(pinfo);
       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
           pass
    # Sort list of dict by key vms i.e. memory usage
    listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['vms'], reverse=True)
    return listOfProcObjects

def parseFrec():
    tmp_frec = str(psutil.cpu_freq())
    i = tmp_frec.find("current=") + 8
    f = tmp_frec.index(",")
    tmp_frec = tmp_frec[i:f].strip()
    return tmp_frec

def parseMem():
    tmp_mem = str(psutil.virtual_memory())
    i = tmp_mem.find("percent=") + 8
    f = tmp_mem.index(",", i)
    tmp_mem = tmp_mem[i:f].strip()
    return tmp_mem

def parseProc():
    tmp_proc = str(proc[0])
    i = tmp_proc.find("'name':") + 9
    f = tmp_proc.index("'", i)
    tmp_proc = tmp_proc[i:f].strip()
    return tmp_proc 

client = paho.Client()
#client.username_pw_set("etorresr", "G4t0")
#client.on_publish = on_publish
client.connect("broker.mqttdashboard.com", 1883)
client.loop_start()

proc = getListOfProcessSortedByMemory()

while True:
    frec = psutil.cpu_freq()
    (rc, mid) = client.publish("dafne/frec", str(parseFrec()), qos=1)

    cpu = psutil.cpu_count()
    (rc, mid) = client.publish("dafne/nuc", str(cpu), qos=1)

    use = psutil.cpu_percent(4)
    (rc, mid) = client.publish("dafne/uso", str(use), qos=1)

    mem = psutil.virtual_memory()
    (rc, mid) = client.publish("dafne/mem", str(parseMem()), qos=1)
    
    proc = getListOfProcessSortedByMemory()
    (rc, mid) = client.publish("dafne/proc", str(parseProc()), qos=1)


    """print('The CPU usage is: ', psutil.cpu_percent(4))
    print("Number of cores in system", psutil.cpu_count())
    print("CPU Statistics", psutil.cpu_stats())
    print("CPU frequency", str(parseFrec()))
    print("CPU load average 1, 5, 15 minutes", psutil.getloadavg())
    print(psutil.virtual_memory())
    print(psutil.sensors_battery())"""
    print("Mem: ", parseMem())
    print("Frec :", parseFrec())
    print("Proceso: ", parseProc())

    time.sleep(30)
