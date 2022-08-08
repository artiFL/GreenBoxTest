from pathlib import Path
import serial
from colorama import Fore
from serial.tools import list_ports
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing   
from matplotlib import cm
from pathlib import Path
import matplotlib


BoolReadTxt = False


path_to_save_file_source = str(Path.cwd()) + "\Data\\"
SFP_PORT = 5
TimeStamp = 0.7
Speed = 2

xsize = 26
ysize = 26

x = 10
p = -15
pre_cursor = []
post_cursor = []
buff_str_var = []
if SFP_PORT == 5:
    BERT_Value_Channel0 = np.empty((ysize, xsize))
    BERT_Value_Channel1 = np.empty((ysize, xsize))
    BERT_Value_Channel2 = np.empty((ysize, xsize))
    BERT_Value_Channel3 = np.empty((ysize, xsize))


BERT_Value = np.empty((ysize, xsize))

version_Checker = np.empty((4))

nameModule = ""

path_to_save_file_backup = path_to_save_file_source + str(version_Checker[2]) + "_Channel" + str(SFP_PORT) + nameModule

BERT_Normalize_Value = np.empty((ysize, xsize))
Build_time = ""

def getport() -> str:
    VID = 0x0483
    PID = 0x5740

    device_list = list_ports.comports()
    for device in device_list:
        if device.vid == VID and device.pid == PID:
            return device.device
    raise OSError("Device not found")

def heatmap(data, row_labels, col_labels, ax=None,
            cbar_kw={}, cbarlabel="", **kwargs):
    """
    Create a heatmap from a numpy array and two lists of labels.

    Parameters
    ----------
    data
        A 2D numpy array of shape (M, N).
    row_labels
        A list or array of length M with the labels for the rows.
    col_labels
        A list or array of length N with the labels for the columns.
    ax
        A `matplotlib.axes.Axes` instance to which the heatmap is plotted.  If
        not provided, use current axes or create a new one.  Optional.
    cbar_kw
        A dictionary with arguments to `matplotlib.Figure.colorbar`.  Optional.
    cbarlabel
        The label for the colorbar.  Optional.
    **kwargs
        All other arguments are forwarded to `imshow`.
    """

    if not ax:
        ax = plt.gca()

    # Plot the heatmap
    im = ax.imshow(data, **kwargs)

    # Create colorbar
    cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
    cbar.ax.set_ylabel(cbarlabel, rotation=-90, va="bottom")

    # Show all ticks and label them with the respective list entries.
    ax.set_xticks(np.arange(data.shape[1]), labels=col_labels)
    ax.set_yticks(np.arange(data.shape[0]), labels=row_labels)

    # Let the horizontal axes labeling appear on top.
    ax.tick_params(top=True, bottom=False,
                   labeltop=True, labelbottom=False)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=-30, ha="right",
             rotation_mode="anchor")

    # Turn spines off and create white grid.
    ax.spines[:].set_visible(False)

    ax.set_xticks(np.arange(data.shape[1]+1)-.5, minor=True)
    ax.set_yticks(np.arange(data.shape[0]+1)-.5, minor=True)
    ax.grid(which="minor", color="w", linestyle='-', linewidth=3)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar

def annotate_heatmap(im, data=None, valfmt="{x:.2f}",
                     textcolors=("black", "white"),
                     threshold=None, **textkw):
    """
    A function to annotate a heatmap.

    Parameters
    ----------
    im
        The AxesImage to be labeled.
    data
        Data used to annotate.  If None, the image's data is used.  Optional.
    valfmt
        The format of the annotations inside the heatmap.  This should either
        use the string format method, e.g. "$ {x:.2f}", or be a
        `matplotlib.ticker.Formatter`.  Optional.
    textcolors
        A pair of colors.  The first is used for values below a threshold,
        the second for those above.  Optional.
    threshold
        Value in data units according to which the colors from textcolors are
        applied.  If None (the default) uses the middle of the colormap as
        separation.  Optional.
    **kwargs
        All other arguments are forwarded to each call to `text` used to create
        the text labels.
    """

    if not isinstance(data, (list, np.ndarray)):
        data = im.get_array()

    # Normalize the threshold to the images color range.
    if threshold is not None:
        threshold = im.norm(threshold)
    else:
        threshold = im.norm(data.max())/2.

    # Set default alignment to center, but allow it to be
    # overwritten by textkw.
    kw = dict(horizontalalignment="center",
              verticalalignment="center")
    kw.update(textkw)

    # Get the formatter in case a string is supplied
    if isinstance(valfmt, str):
        valfmt = matplotlib.ticker.StrMethodFormatter(valfmt)

    # Loop over the data and create a `Text` for each "pixel".
    # Change the text's color depending on the data.
    texts = []
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            kw.update(color=textcolors[int(im.norm(data[i, j]) > threshold)])
            text = im.axes.text(j, i, valfmt(data[i, j], None), **kw)
            texts.append(text)

    return texts

def normalize(ptr):
    BERT_Normalize_Value = preprocessing.normalize(ptr)
    return BERT_Normalize_Value

def normalize2(ptr):
    BERT_Normalize_Value = ptr
    for i in range(len(ptr)):
        for j in range(len(ptr[i])):
            if(ptr[i][j]) >= 300:
                BERT_Normalize_Value[i][j] = 300
    return BERT_Normalize_Value

while x > -16:
    pre_cursor.append(str(x))
    post_cursor.append(str(p))
    p += 1
    x -= 1

def main():
    global nameModule
    global BERT_Value_Channel0
    global BERT_Value_Channel1
    global BERT_Value_Channel2
    global BERT_Value_Channel3


    buff_str_var = []


    print(path_to_save_file_source)

    if BoolReadTxt == True:
        if SFP_PORT == 5:
            BERT_Value_Channel0 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch0.txt", "rb"))
            BERT_Value_Channel1 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch1.txt", "rb"))
            BERT_Value_Channel2 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch2.txt", "rb"))
            BERT_Value_Channel3 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch3.txt", "rb"))
        else:
            # open the file in read binary mode
            file = open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/1.5805638443516308e-153_Channel5QSFP.txt", "rb")
            #file = open(path_to_save_file_backup + ".txt", "rb")
            #read the file to numpy array
            BERT_Value = np.load(file)
            #close the file
    else:

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


        #time.sleep(1)
        Checker.write(bytes(f"cmd_start_callib_FIR {SFP_PORT} {TimeStamp} {Speed}", encoding="utf-8")) 
        #time.sleep(1)

        flag = True
        ack_speed = ""
        ack_speed = str(Checker.readline(), 'UTF-8')

        while flag:
            ack_speed = str(Checker.readline(), 'UTF-8')

            if "Clock is set" in ack_speed:
                flag = False

        ack_speed = ack_speed.split(',')
        nameModule = ack_speed[2].replace('\n', '')

        for b in range(ysize):
            for n in range(xsize):
                string_reccive = str(Checker.readline(), 'UTF-8').replace('\n', '')
                string_reccive = string_reccive.split(',')

                var = string_reccive
                buff_str_var += var

                if SFP_PORT == 5:
                    BERT_Value_Channel0[b, n] = int(str(var[0]))
                    BERT_Value_Channel1[b, n] = int(str(var[1]))
                    BERT_Value_Channel2[b, n] = int(str(var[2]))
                    BERT_Value_Channel3[b, n] = int(str(var[3]))
                    print(string_reccive)

                else:
                    BERT_Value[b, n] = int(str(var[0]))
                    print(string_reccive)

        Checker.close()
        if SFP_PORT == 5:

            file = open(path_to_save_file_backup + "QSFP.txt", "wb")
            # save array to the file
            file_channel0 = open(path_to_save_file_backup + "QSFPch0.txt", "wb")
            file_channel1 = open(path_to_save_file_backup + "QSFPch1.txt", "wb")
            file_channel2 = open(path_to_save_file_backup + "QSFPch2.txt", "wb")
            file_channel3 = open(path_to_save_file_backup + "QSFPch3.txt", "wb")



            np.save(file_channel0, BERT_Value_Channel0)
            np.save(file_channel1, BERT_Value_Channel1)
            np.save(file_channel2, BERT_Value_Channel2)
            np.save(file_channel3, BERT_Value_Channel3)

            print("File save to - " + path_to_save_file_backup + ".txt")
            # close the file
            file.close
        else:
            file = open(path_to_save_file_backup + ".txt", "wb")
            # save array to the file
            np.save(file, BERT_Value)
            print("File save to - " + path_to_save_file_backup + ".txt")
            # close the file
            file.close

    if SFP_PORT == 5:
        fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(26, 26))

        # Replicate the above example with a different font size and colormap.

        y = ["{}".format(i) for i in range(10, -16, -1)]
        x = ["{}".format(i) for i in range(-15, 11, 1)]

        im, _ = heatmap(normalize2(BERT_Value_Channel0), y, x, ax=ax,
                        cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
        annotate_heatmap(im, valfmt="{x:.1f}", size=6)

        im, _ = heatmap(normalize2(BERT_Value_Channel1), y, x, ax=ax2,
                        cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
        annotate_heatmap(im, valfmt="{x:.1f}", size=6)

        im, _ = heatmap(normalize2(BERT_Value_Channel2), y, x, ax=ax3,
                        cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
        annotate_heatmap(im, valfmt="{x:.1f}", size=6)


        im, _ = heatmap(normalize2(BERT_Value_Channel3), y, x, ax=ax4,
                        cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
        annotate_heatmap(im, valfmt="{x:.1f}", size=6)


        plt.tight_layout()
        plt.show()

        fig.savefig(path_to_save_file_backup + "_Figure.png")

    else:
        fig, ax = plt.subplots()
        im = ax.imshow(normalize(BERT_Value), cmap = cm.magma)

        # Show all ticks and label them with the respective list entries
        ax.set_xticks(np.arange(len(post_cursor)), labels=post_cursor)
        ax.set_yticks(np.arange(len(pre_cursor)), labels=pre_cursor)

        # Rotate the tick labels and set their alignment.
        plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
                 rotation_mode="anchor")
        plt.xlabel("post-cursor")
        plt.ylabel("pre-cursor")


        ax.set_title(f"Fir sweep {nameModule} speed = {Speed} timestamp = {TimeStamp}")
        fig.tight_layout()
        plt.show()

        fig.savefig(path_to_save_file_backup + "_Figure")


if __name__ == "__main__":
    main()