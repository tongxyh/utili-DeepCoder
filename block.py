import numpy as np

def crop(bi,crop_size=4):
    N,W,H,C = bi.shape
    arr = bi.copy()
    W = int(np.floor(W/crop_size))
    H = int(np.floor(H/crop_size))
    arr = np.int16(arr)
    avg = np.empty(shape=[N,W,H,C],dtype = np.int16)
    for i in range(W):
        for j in range(H):
            a = np.round(np.mean(arr[:,i * crop_size:(i + 1) * crop_size, j * crop_size:(j + 1) * crop_size, :], axis=(1, 2)))
            avg[:, i, j, :] = a
            #print(a,i,j)
            for m in range(crop_size):
                for n in range(crop_size):
                    arr[:,i * crop_size+m, j * crop_size+n, :] = arr[:,i * crop_size+m, j * crop_size+n, :] - a
    return avg,arr

def decrop(avg,arr,crop_size = 4):
    N, W, H, C = avg.shape
    bi = arr.copy()
    for i in range(W):
        for j in range(H):
            bi[:,i * crop_size:(i + 1) * crop_size, j * crop_size:(j + 1) * crop_size, :] = avg[:,i,j,:] + bi[:,i * crop_size:(i + 1) * crop_size, j * crop_size:(j + 1) * crop_size, :]
    return bi
