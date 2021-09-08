# -*- coding: utf-8 -*-
"""
paddleDetectron训练结果可视化
"""
import json
import re
from pylab import *
fig = figure(figsize=(8,6), dpi=300)
y1 = fig.add_subplot(211)
y1.set_xlabel('Iterations')
y2 = fig.add_subplot(212)
y2.set_xlabel('Iterations')
parsed = []
with open('./0904_1600.log') as f:
    for line in f:
        parsed.append(line)

    _iter = []
    _loss = []
    _lr = []
    for x in parsed:
        if 'INFO: iter: ' in x:
            index1 = x.find('iter: ')
            index2 = x.find(", lr:")
            _iter.append(int(x[index1+6:index2]))
        if 'lr: ' in x:
            index1 = x.find('lr: ')
            index2 = x.find(", 'loss_xy': ")
            _lr.append(float(x[index1+4:index2]))
        if "'loss': " in x:
            index1 = x.find("'loss': ")
            index2 = x.find("', eta")
            _loss.append(float(x[index1+9:index2]))

    y1.set_ylim(0, 50)
    y1.plot(_iter, _loss, color="blue", linewidth=0.3, linestyle="-",label='total_loss')

    y2.set_ylim(0,max(_lr)/0.8)
    y2.plot(_iter, _lr, color="purple", linewidth=1.0, linestyle="-",label='lr')

    # 图例
    y1.legend()
    y2.legend()
    savefig('./fig.png')
    show()
