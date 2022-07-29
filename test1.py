import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import sys
import glob
from numpy import byte
import serial



x_size = 26
y_size = 26

x = 10
p = -15
pre_cursor = []
post_cursor = []

#for x in range(-15):
while x > -10:

    pre_cursor.append(str(x))
    post_cursor.append(str(p))

    p += 1
    x -= 1
'''
pres = 5
flag_inv_pres = False

for v in range(21):

    if flag_inv_pres == True:
        if pres == 0:
            flag_inv_pres = False
        pres -= 1

    if flag_inv_pres == False:
        if pres == 0:
            flag_inv_pres = False
        pres += 1


    print(pres, flag_inv_pres)


for v in range(40):

    if pres == 15 and flag_inv_pres == True:
        pres = 5
        flag_inv_pres = False

    if pres == 0:
        if pres == True:
            flag_inv_pres = False
        else:
            flag_inv_pres = True

    if flag_inv_pres == True:
        pres += 1

    if flag_inv_pres == False:
        pres -= 1

    print(pres, flag_inv_pres)

'''

#BERT = np.array(None,None)
'''
BERT = np.empty((x_size, y_size))

for y in range(x_size):
    for t in range(y_size):
        BERT[t,y] = random.randint(20, 350)
'''
BERT = np.array([ 
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#4
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#3
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#2
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],#1
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 2, 2, 2],#0
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 2, 2, 2],#-1
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 1, 1, 2, 2],#-2
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 2],#-3
      [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 2],#-4
      [2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 2],#-5
      [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-6
      [2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-7
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-8
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2],#-9
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 1, 2],#-10
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 1, 2],#-11
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 1, 2, 2],#-12
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 1, 2, 2, 2],#-13
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2],#-14
      [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2]#-15
 ])



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


BERT_Value = np.empty((26, 26))


while True:
    for b in range(26):
        for n in range(26):
            string_reccive = str(Checker.readline(), 'UTF-8').replace('\n', '')
            string_reccive = string_reccive.split(',')

            var = float(str(string_reccive[0]))
            BERT_Value[b, n] = var
            print( BERT_Value[b, n], string_reccive)

    fig, ax = plt.subplots()
    im = ax.imshow(BERT_Value, cmap = cm.magma)

    # Show all ticks and label them with the respective list entries
    ax.set_xticks(np.arange(len(post_cursor)), labels=post_cursor)
    ax.set_yticks(np.arange(len(pre_cursor)), labels=pre_cursor)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
             rotation_mode="anchor")

    ax.set_title("Fir sweep space")
    fig.tight_layout()
    plt.show()


'''
    fre = str(Checker.readline(), 'UTF-8').replace('\n', '')
    fre = fre.split(',')
    #ter = int(fre)
    #fre = fre.replace("\n", '')

    print(fre)
'''





fig, ax = plt.subplots()
im = ax.imshow(BERT, cmap=cm.bwr)

# Show all ticks and label them with the respective list entries
ax.set_xticks(np.arange(len(post_cursor)), labels=post_cursor)
ax.set_yticks(np.arange(len(pre_cursor)), labels=pre_cursor)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
'''
for i in range(len(pre_cursor)):
    for j in range(len(post_cursor)):
        text = ax.text(j, i, BERT[i, j],
                       ha="center", va="center", color="w")
'''



ax.set_title("Fir sweep space")
fig.tight_layout()
plt.show()