import serial
from colorama import Fore
from serial.tools import list_ports
import time
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing   
from matplotlib import cm



def getport() -> str:
    VID = 0x0483
    PID = 0x5740

    device_list = list_ports.comports()
    for device in device_list:
        if device.vid == VID and device.pid == PID:
            return device.device
    raise OSError("Device not found")

def normalize(ptr):
    BERT_Normalize_Value = preprocessing.normalize(ptr)
    return BERT_Normalize_Value


path_to_save_file_backup = "C:/Users/flegler.a/Desktop/GreenBoxPython/GreenBoxTest/"
Channel_Checker = 3
TimeStamp = 2


x = 10
p = -15
pre_cursor = []
post_cursor = []
buff_str_var = []
BERT_Value = np.empty((26, 26))
BERT_Normalize_Value = np.empty((26, 26))
Build_time = ""


while x > -16:

    pre_cursor.append(str(x))
    post_cursor.append(str(p))

    p += 1
    x -= 1


def main():
    buff_str_var = []


    Checker = serial.Serial(getport(), 115200)  # open serial port

    Checker.write(bytes("cmd_get_version", encoding="utf-8")) 
    version_Checker = str(Checker.readline(), 'UTF-8').replace('ver', '').replace('HW - ', '').replace(' SN: ', '').replace('\n', '')

    version_Checker = version_Checker.split(',')

    Build_time = str(Checker.readline(), 'UTF-8')
    print(Build_time)

    if "DEBUG" in version_Checker[0]:
        print(Fore.RED + "Сhecker firmware is not suitable for testing, flash the release version")
        return 0
    else:
        print(Fore.RED + f"Version Sowftware - {version_Checker[0]}\nVersion Hardware - {version_Checker[1]}\nSerial Number - {version_Checker[2]}")
        print(Fore.WHITE + "Succes connect")

    path_to_save_file_backup = str(version_Checker[2]) + "_Channel" + str(Channel_Checker) + ".txt"

    time.sleep(1)
    Checker.write(bytes(f"cmd_start_callib_FIR {Channel_Checker} {TimeStamp}", encoding="utf-8")) 
    time.sleep(1)


    flag = True
    ack_speed = ""
    ack_speed = str(Checker.readline(), 'UTF-8')

    while flag:
        ack_speed = str(Checker.readline(), 'UTF-8')

        if "Clock is set" in ack_speed:
            flag = False

    print(ack_speed)

    for b in range(26):
        for n in range(26):
            string_reccive = str(Checker.readline(), 'UTF-8').replace('\n', '')
            string_reccive = string_reccive.split(',')

            var = string_reccive
            buff_str_var += var

            BERT_Value[b, n] = int(str(var[0]))
            print( BERT_Value[b, n], string_reccive)

    Checker.close()

    file = open(path_to_save_file_backup, "wb")
    # save array to the file
    np.save(file, BERT_Value)
    print("File save to - " + path_to_save_file_backup)

    # close the file
    file.close


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
    fig.savefig(str(version_Checker[2]) + "_Channel" + str(Channel_Checker))






if __name__ == "__main__":
    
    main()