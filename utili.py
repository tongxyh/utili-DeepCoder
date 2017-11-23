import numpy as np
import sys
sys.path.append('/home/chentong/deepcoder/python-huffman')
import huffman

def huffman_coding(arr,begin_n,end_n,H,W):

    dis = huffman.cal_distrib(arr, begin_n, end_n)
    #print("dis1",dis)
    #print("--->",(np.sum(dis)))
    #print(np.double(np.sum(dis)))#(tjc)

    dis = dis / np.double(np.sum(dis))
    #print("dis2", dis)
    avgbits,codec = huffman.dict(dis, begin_n, end_n)
    return avgbits,codec

def huffman_head(codec):
    hbits = 8 + 16 + 16 + 2 # QUAN_LEV(A int - 8bits) + H(A int - 16bits) + W(A int - 16bits) + Res or Not(bool - 1 bits) + AVG_PREDICT or Not(bool 1 bits)
    for i in codec:
        hbits = 8 + len(codec[i]) + hbits
    return hbits
