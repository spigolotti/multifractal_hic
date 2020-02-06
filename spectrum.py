#!/usr/bin/env python3

import sys
import os


def main():

    qvals=[0.25*float(i) for i in range(21)]
    qlen=len(qvals)

    norm=0.0
    matrc={}

    with open(sys.argv[1],'r') as fin:
        for line in fin:
            aa=line.split()
            bin_x=int(aa[1])
            bin_y=int(aa[2])
            count=float(aa[3])
            if (bin_x,bin_y) in matrc:
                matrc[(bin_x,bin_y)]+=count
            else:
                matrc[(bin_x,bin_y)]=count
            norm+=count


    resol_range=[int(1.2**i) for i in range(32)]

    resol_range = list(dict.fromkeys(resol_range))  # remove duplicates
#    print(resol_range)

    fname=os.path.basename(sys.argv[1])+'.scaling'

    with open(fname,'w') as fout:
        for resol in resol_range:
            partition=[0.0 for i in range(qlen)]
            matr={}
            for bin_x, bin_y in matrc:
                if (bin_x//resol,bin_y//resol) in matr:
                    matr[(bin_x//resol,bin_y//resol)]+=matrc[(bin_x,bin_y)]
                else:
                    matr[(bin_x//resol,bin_y//resol)]=matrc[(bin_x,bin_y)]

            for bl in matr:
                for i in range(qlen):
                    partition[i]+=matr[bl]**qvals[i]

            for i in range(qlen):
                partition[i]=partition[i]/norm
                print(resol,partition[i],qvals[i],file=fout)


if __name__ == '__main__':
    main()
