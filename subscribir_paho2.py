import paho.mqtt.client as paho

frec_cont = [0,0,0,0,0,0,0]
nuc_cont = [0,0,0,0,0,0,0]
uso_cont = [0,0,0,0,0,0,0]
mem_cont = [0,0,0,0,0,0,0]
proc_cont = ['','','','','','','']


def parse(value):
    tmp_frec = value
    data = tmp_frec.split("'")
    return data[1]

def max(frec_cont):
    max = frec_cont[0]
    for x in frec_cont:
        if x>max:
            max = x
    return max

def min(frec_cont):
    min = frec_cont[0]
    for x in frec_cont:
        if x<min:
            min = x
    return min
def on_message(client, userdata, msg):
    avg_f = 0
    avg_n = 0
    avg_u = 0
    avg_m = 0

    if (msg.topic == "dafne/frec"):
        frec_cont [0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/frec"):
        frec_cont [1] = float(parse(str(msg.payload)))
    #if (msg.topic == "dafne_badillo/frec"):
        #frec_cont [2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/frec"):
        frec_cont [3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/frec"):
        frec_cont [4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/frec"):
        frec_cont [5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/frec"):
        frec_cont [6] = float(parse(str(msg.payload)))
    for i in frec_cont:
        avg_f += i 
    total_f = "{:.2f}".format(avg_f/7)
    print ("Frecuencia Promedio: ", total_f)
    print ("Frecuencia Minima: ", min(frec_cont))
    print ("Frecuencia Maxima: ", max(frec_cont))

    if (msg.topic == "dafne/nuc"):
        nuc_cont [0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/nuc"):
        nuc_cont [1] = float(parse(str(msg.payload)))
    #if (msg.topic == "dafne_badillo/nuc"):
        #nuc_cont [2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/nuc"):
        nuc_cont [3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/nuc"):
        nuc_cont [4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/nuc"):
        nuc_cont [5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/nuc"):
        nuc_cont [6] = float(parse(str(msg.payload)))
    for i in nuc_cont:
        avg_n += i 
    total_n = "{:.2f}".format(avg_n/7)
    print ("No. de nucleos Promedio: ", total_n)
    print ("No. de nucleos Minimo: ", min(nuc_cont))
    print ("No. de nucleos Maximo: ", max(nuc_cont))

    if (msg.topic == "dafne/uso"):
        uso_cont [0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/uso"):
        uso_cont [1] = float(parse(str(msg.payload)))
    #if (msg.topic == "dafne_badillo/uso"):
        #nuc_cont [2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/uso"):
        uso_cont [3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/uso"):
        uso_cont [4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/uso"):
        uso_cont [5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/uso"):
        uso_cont [6] = float(parse(str(msg.payload)))
    for i in uso_cont:
        avg_u += i 
    total_u = "{:.2f}".format(avg_u/7)
    print ("Uso Promedio: ", total_u)
    print ("Uso Minimo: ", min(uso_cont))
    print ("Uso Maximo: ", max(uso_cont))

    if (msg.topic == "dafne/mem"):
        mem_cont [0] = float(parse(str(msg.payload)))
    if (msg.topic == "miles/mem"):
        mem_cont [1] = float(parse(str(msg.payload)))
    #if (msg.topic == "dafne_badillo/mem"):
        #mem_cont [2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/mem"):
        mem_cont [3] = float(parse(str(msg.payload)))
    if (msg.topic == "joseduardo/mem"):
        mem_cont [4] = float(parse(str(msg.payload)))
    if (msg.topic == "alonso/mem"):
        mem_cont [5] = float(parse(str(msg.payload)))
    if (msg.topic == "anthony/mem"):
        mem_cont [6] = float(parse(str(msg.payload)))
    for i in mem_cont:
        avg_m += i 
    total_m = "{:.2f}".format(avg_m/7)
    print ("Memoria Promedio: ", total_m)
    print ("Memoria Minima: ", min(mem_cont))
    print ("Memoria Maxima: ", max(mem_cont))

    if (msg.topic == "dafne/proc"):
        proc_cont [0] = parse(str(msg.payload))
    if (msg.topic == "miles/proc"):
        proc_cont [1] = parse(str(msg.payload))
    #if (msg.topic == "dafne_badillo/proc"):
        #proc_cont [2] = float(parse(str(msg.payload)))
    if (msg.topic == "victor/proc"):
        proc_cont [3] = parse(str(msg.payload))
    if (msg.topic == "joseduardo/proc"):
        proc_cont [4] = parse(str(msg.payload))
    if (msg.topic == "alonso/proc"):
        proc_cont [5] = parse(str(msg.payload))
    if (msg.topic == "anthony/proc"):
        proc_cont [6] = parse(str(msg.payload))
    print("Procesos:", proc_cont)


    




client = paho.Client()
#client.on_subscribe = on_subscribe
client.on_message = on_message
#client.username_pw_set("etorresr", "G4t0")
client.connect("broker.mqttdashboard.com", 1883)
f1 = client.subscribe("dafne/frec", qos=1)
n1 = client.subscribe("dafne/nuc", qos=1)
client.subscribe("dafne/uso", qos=1)
client.subscribe("dafne/mem", qos=1)
client.subscribe("dafne/proc", qos=1)
f2 = client.subscribe("miles/frec", qos=1)
n2 =client.subscribe("miles/nuc", qos=1)
client.subscribe("miles/uso", qos=1)
client.subscribe("miles/mem", qos=1)
client.subscribe("miles/proc", qos=1)
f3 = client.subscribe("dafne_badillo/frec", qos=1)
n3 = client.subscribe("dafne_badillo/nuc", qos=1)
client.subscribe("dafne_badillo/uso", qos=1)
client.subscribe("dafne_badillo/mem", qos=1)
client.subscribe("dafne_badillo/proc", qos=1)
f4 = client.subscribe("victor/frec", qos=1)
n4 = client.subscribe("victor/nuc", qos=1)
client.subscribe("victor/uso", qos=1)
client.subscribe("victor/mem", qos=1)
client.subscribe("victor/proc", qos=1)
f5 = client.subscribe("joseduardo/frec", qos=1)
n5 = client.subscribe("joseduardo/nuc", qos=1)
client.subscribe("joseduardo/uso", qos=1)
client.subscribe("joseduardo/mem", qos=1)
client.subscribe("joseduardo/proc", qos=1)
f6 = client.subscribe("alonso/frec", qos=1)
n6 = client.subscribe("alonso/nuc", qos=1)
client.subscribe("alonso/uso", qos=1)
client.subscribe("alonso/mem", qos=1)
client.subscribe("alonso/proc", qos=1)
f7 = client.subscribe("anthony/frec", qos=1)
n7 = client.subscribe("anthony/nuc", qos=1)
client.subscribe("anthony/uso", qos=1)
client.subscribe("anthony/mem", qos=1)
client.subscribe("anthony/proc", qos=1)
client.loop_forever()

