# -*- coding: utf-8 -*-
"""
Detectron2训练结果可视化
"""
import json
import re
from pylab import *
fig = figure(figsize=(8,6), dpi=300)
y1 = fig.add_subplot(211)
y1.set_xlabel('Iterations')
# y2 = y1.twinx()
y2 = fig.add_subplot(212)
y2.set_xlabel('Iterations')
parsed = []
with open('./metrics.json') as f:
    try:
        for line in f:
            parsed.append(json.loads(line))
    except:
        print("json format is not corrrect")
        exit(1)

    _iter = [j['iteration'] for j in parsed]
    _loss = [j['total_loss'] for j in parsed]
    _loss_bbox = [j['loss_box_reg'] for j in parsed]
    _loss_cls = [j['loss_cls'] for j in parsed]
    try:
         _accuracy_cls = [j['fast_rcnn/cls_accuracy'] for j in parsed]
    except:
        _accuracy_cls = None
    _lr = [j['lr'] for j in parsed]
    try:
        _mask_loss = [j['mask_loss'] for j in parsed]
    except:
        _mask_loss = None

    y1.set_ylim(0, 1.0)
    # y1.plot(_iter, _loss_bbox, color="green", linewidth=0.3,linestyle="-",label='loss_box_reg')
    y1.plot(_iter, _loss, color="blue", linewidth=0.3, linestyle="-",label='total_loss')
    # y1.plot(_iter, _loss_cls, color="black", linewidth=0.3, linestyle="-",label='loss_cls')
    # y1.plot(_iter, _accuracy_cls, color="red", linewidth=0.3, linestyle="-",label='cls_accuracy')
    # if _mask_loss is not None:
    #      y1.plot(_iter, _mask_loss, color="grey", linewidth=0.3, linestyle="-",label='mask_loss')

    y2.set_ylim(0,max(_lr)/0.8)
    y2.plot(_iter, _lr, color="purple", linewidth=1.0, linestyle="-",label='lr')
    # y2.set_ylabel('lr')

    # 图例
    y1.legend()
    y2.legend()
    savefig('./fig.png')
    show()
