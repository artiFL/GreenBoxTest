import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from sklearn import preprocessing   
from matplotlib import cm

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
    ax.grid(which="minor", color="w", linestyle='-', linewidth=1)
    ax.tick_params(which="minor", bottom=False, left=False)

    return im, cbar
def annotate_heatmap(im, data=None, valfmt="{x:.1f}",
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


BERT_Value_Channel0 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch0.txt", "rb"))
BERT_Value_Channel1 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch1.txt", "rb"))
BERT_Value_Channel2 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch2.txt", "rb"))
BERT_Value_Channel3 = np.load(open("C:/Users/flegler.a/Desktop/Work_space/CubeIDE/Checker/GreenBoxPython/GreenBoxTest/Data/0.0_Channel5QSFPch3.txt", "rb"))


np.random.seed(19680801)

fig, ((ax, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(26, 26))

# Replicate the above example with a different font size and colormap.

y = ["{}".format(i) for i in range(10, -16, -1)]
x = ["{}".format(i) for i in range(-15, 11, 1)]


def normalize(ptr):

    BERT_Normalize_Value = ptr
    for i in range(len(ptr)):
        for j in range(len(ptr[i])):
            if(ptr[i][j]) >= 300:
                BERT_Normalize_Value[i][j] = 300
    return BERT_Normalize_Value


im, _ = heatmap(normalize(BERT_Value_Channel0), y, x, ax=ax,
                cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
annotate_heatmap(im, valfmt="{x:.1f}", size=6)

im, _ = heatmap(normalize(BERT_Value_Channel1), y, x, ax=ax2,
                cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
annotate_heatmap(im, valfmt="{x:.1f}", size=6)

im, _ = heatmap(normalize(BERT_Value_Channel2), y, x, ax=ax3,
                cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
annotate_heatmap(im, valfmt="{x:.1f}", size=6)


im, _ = heatmap(normalize(BERT_Value_Channel3), y, x, ax=ax4,
                cmap=cm.magma, vmin=0, vmax=300, cbarlabel="Bit Error")
annotate_heatmap(im, valfmt="{x:.1f}", size=6)





# Create some new data, give further arguments to imshow (vmin),
# use an integer format on the annotations and provide some colors.
'''
data = np.random.randint(2, 100, size=(7, 7))
y = ["Book {}".format(i) for i in range(1, 8)]
x = ["Store {}".format(i) for i in list("ABCDEFG")]
im, _ = heatmap(data, y, x, ax=ax2, vmin=0,
                cmap="magma_r", cbarlabel="weekly sold copies")
annotate_heatmap(im, valfmt="{x:d}", size=7, threshold=20,
                 textcolors=("red", "white"))

# Sometimes even the data itself is categorical. Here we use a
# `matplotlib.colors.BoundaryNorm` to get the data into classes
# and use this to colorize the plot, but also to obtain the class
# labels from an array of classes.

data = np.random.randn(6, 6)
y = ["Prod. {}".format(i) for i in range(10, 70, 10)]
x = ["Cycle {}".format(i) for i in range(1, 7)]

qrates = list("ABCDEFG")
norm = matplotlib.colors.BoundaryNorm(np.linspace(-3.5, 3.5, 8), 7)
fmt = matplotlib.ticker.FuncFormatter(lambda x, pos: qrates[::-1][norm(x)])

im, _ = heatmap(data, y, x, ax=ax3,
                cmap=plt.get_cmap("PiYG", 7), norm=norm,
                cbar_kw=dict(ticks=np.arange(-3, 4), format=fmt),
                cbarlabel="Quality Rating")

annotate_heatmap(im, valfmt=fmt, size=9, fontweight="bold", threshold=-1,
                 textcolors=("red", "black"))

# We can nicely plot a correlation matrix. Since this is bound by -1 and 1,
# we use those as vmin and vmax. We may also remove leading zeros and hide
# the diagonal elements (which are all 1) by using a
# `matplotlib.ticker.FuncFormatter`.

corr_matrix = np.corrcoef(harvest)
im, _ = heatmap(corr_matrix, vegetables, vegetables, ax=ax4,
                cmap="PuOr", vmin=-1, vmax=1,
                cbarlabel="correlation coeff.")


def func(x, pos):
    return "{:.2f}".format(x).replace("0.", ".").replace("1.00", "")

annotate_heatmap(im, valfmt=matplotlib.ticker.FuncFormatter(func), size=7)

'''
plt.tight_layout()
plt.show()