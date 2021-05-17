# -*- coding: utf-8 -*-
"""
Various methods of drawing scrolling plots.
"""
#import initExample  ## Add path to library (just for examples; you do not need this)
import sys
import numpy as np
import pyqtgraph as pg
#import soundfile as sf
#from playsound import playsound
from pyqtgraph.Qt import QtCore, QtGui
#from outdata import output
import pdb
#CUDA_VISIBLE_DEVICES=-1
pg.setConfigOption('background', 'w')
pg.setConfigOption('foreground', 'k')

win = pg.GraphicsLayoutWidget(show=True)
win.setWindowTitle('Red:reference Blue:separated source')


# 3) Plot in chunks, adding one new plot curve for every 100 samples
chunkSize = 10000
# Remove chunks after we have 10
maxChunks = 50
startTime = pg.ptime.time()
win.nextRow()
p5 = win.addPlot(colspan=2)
p5.setLabel('bottom', 'Time', 's')
p5.setXRange(-10, 0)
curves = []
curves_b = []
data5 = np.empty((chunkSize + 1, 2))
data6 = np.empty((chunkSize + 1, 2))
ptr5 = 0

#x=np.random.rand(10000)
mode=int(sys.argv[1])
xuhao=int(sys.argv[2])
#mode = 2
#xuhao = 0
a = np.load("source.npy")
b = np.load("separated.npy")

#pdb.set_trace
x = a[xuhao*3+mode-1,:]
y = b[xuhao*3+mode-1,:]
#samplerate=16000
#sf.write('stereo_file.wav', x, samplerate, subtype='PCM_24')
#playsound("stereo_file.wav")


def update3(x,y):
    global p5, data5, ptr5, curves,curves_b,data6
    now = pg.ptime.time()
    for c in curves:
        c.setPos(-(now - startTime), 0)
    for d in curves_b:
        d.setPos(-(now - startTime), 0)
    i = ptr5 % chunkSize
    if i == 0:
        curve = p5.plot(pen={'color': 'r', 'width': 2},antialias=True,fillLevel=0,brush=(100,0,50,100))
        curve_b = p5.plot(pen={'color': 'b', 'width': 2}, antialias=True,fillLevel=0,brush=(0,0,100,50))

        curves.append(curve)
        curves_b.append(curve_b)

        last = data6[-1]
        data6 = np.empty((chunkSize + 1, 2))
        data6[0] = last

        last_b = data5[-1]
        data5 = np.empty((chunkSize + 1, 2))
        data5[0] = last_b

        while len(curves) > maxChunks:
            c = curves.pop(0)
            p5.removeItem(c)
        while len(curves_b) > maxChunks:
            d = curves_b.pop(0)
            p5.removeItem(d)
    else:
        curve = curves[-1]
        curve_b = curves_b[-1]

    data5[i + 1, 0] = now - startTime
    data5[i + 1, 1] = x[ptr5]
    data6[i + 1, 0] = now - startTime
    data6[i + 1, 1] = y[ptr5]
    curve.setData(x=data5[:i + 2, 0], y=data5[:i + 2, 1])
    curve_b.setData(x=data5[:i + 2, 0], y=data6[:i + 2, 1])
    ptr5 += 1

def update():
    update3(x,y)
    #update4(y)
timer = pg.QtCore.QTimer()
timer.timeout.connect(update)
timer.start(50)


if __name__ == '__main__':
    pg.mkQApp().exec_()
