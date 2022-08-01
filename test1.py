import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import glob
import serial
from sklearn import preprocessing   



x = 10
p = -15
pre_cursor = []
post_cursor = []
buff_str_var = []
BERT_Value = np.empty((26, 26))
BERT_Normalize_Value = np.empty((26, 26))

while x > -16:

    pre_cursor.append(str(x))
    post_cursor.append(str(p))

    p += 1
    x -= 1

def serial_ports():
    """ Lists serial port names
        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result

list_ports = serial_ports()
print(list_ports)
Checker = serial.Serial("COM26", 115200)  # open serial port
Checker.write(bytes("cmd_start_callib_FIR", encoding="utf-8")) 

#norm = mpl.colors.Normalize(vmin=0.,vmax=1000000000.)

def normalize(ptr):
    #min_max_scaler = preprocessing.MinMaxScaler()  
    #BERT_Normalize_Value = min_max_scaler.fit_transform(ptr)  


    BERT_Normalize_Value = preprocessing.normalize(ptr)

    return BERT_Normalize_Value

    #return BERT_Normalize_Value



'''
def normalize(ptr):
    for x in range(26):
        for i in range(26):
            if BERT_Value[x,i] >= 9000000000:
                BERT_Normalize_Value[x,i] = 2
            if BERT_Value[x,i] < 9000000000 and ptr[x,i] > 200:
                BERT_Normalize_Value[x,i] = 1
            if BERT_Value[x,i] < 200:
                BERT_Normalize_Value[x,i] = 0
    return BERT_Normalize_Value
'''

for b in range(26):
    for n in range(26):
        string_reccive = str(Checker.readline(), 'UTF-8').replace('\n', '')
        string_reccive = string_reccive.split(',')

        var = string_reccive
        buff_str_var += var

        BERT_Value[b, n] = int(str(var[0])) + 1
        print( BERT_Value[b, n], string_reccive)

#np.savetxt('C:/Users/flegler.a/Desktop/GreenBoxPython/GreenBoxTest/Chaecker_data.txt', BERT_Value, fmt='%s, \n')
#BERT_Value = np.loadtxt('C:/Users/flegler.a/Desktop/GreenBoxPython/GreenBoxTest/Chaecker_data.txt', dtype=str)
#BERT_Value = str(BERT_Value).replace(', \n', '')
#np.savetxt('C:/Users/flegler.a/Desktop/GreenBoxPython/GreenBoxTest/Chaecker_data2.txt', BERT_Value, fmt='%d, \n')
#file = open("C:/Users/flegler.a/Desktop/GreenBoxPython/GreenBoxTest/Chaecker_data.txt", "wb")

file = open("C:/Users/flegler.a/Desktop/GreenBoxPython/GreenBoxTest/Chaecker_data3.txt", "wb")
# save array to the file
np.save(file, BERT_Value)
# close the file
file.close


'''
# open the file in read binary mode
file = open("C:/Users/flegler.a/Desktop/GreenBoxPython/GreenBoxTest/Chaecker_data2.txt", "rb")
#read the file to numpy array
BERT_Value = np.load(file)
#close the file
'''

fig, ax = plt.subplots()
im = ax.imshow(normalize(BERT_Value), cmap = cm.magma)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(post_cursor)), labels=post_cursor)
ax.set_yticks(np.arange(len(pre_cursor)), labels=pre_cursor)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

ax.set_title("Fir sweep space")
fig.tight_layout()
plt.show()
