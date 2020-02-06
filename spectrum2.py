#!/usr/bin/env python3

import sys
import os
import math

def fna(x,a):
    return -x*math.log(4.0*a)/math.log(2.0)

def fnb(x,a):
    aa=2.0*(x-1.0)
    bb=-x*(math.log(a)/math.log(2.0))-1.0
    if aa<bb: return aa
    else: return bb

def main():

    if len(sys.argv)!=4 and len(sys.argv)!=2:
        print('Error')
        print('Usage: ./spectrum.py <file_name.scaling> <xmin> <xmax>')
        print('<xmin> and <xmax> are optional arguments. Default: xmin = 3 xmax = 75')
        exit(1)

    fname=sys.argv[1]

    if len(sys.argv)==4:
        xmin=int(sys.argv[2])
        xmax=int(sys.argv[3])
    else:
        xmin=3
        xmax=75

    qvals=[0.25*float(i) for i in range(21)]
    qlen=len(qvals)

    fname2=fname[:-8]+'_'+str(xmin)+'_'+str(xmax)+'.mfct'
    fname3=fname[:-8]+'_'+str(xmin)+'_'+str(xmax)+'.fit'
    fout=open(fname2,"w")
    fout2=open(fname3,"w")

    minn_fits=10000000.0
    exps=[]
    syt=0.0
    for qq in qvals:
        x=0.0
        xx=0.0
        y=0.0
        yy=0.0
        xy=0.0
        nnn=0.0
        with open(fname,"r") as fin:
            for line in fin:
                aa=line.split()
                if float(aa[2])==qq and float(aa[0])<=xmax and float(aa[0])>=xmin and float(aa[1])==float(aa[1]):
                    ldist=math.log(float(aa[0]))
                    lp=math.log(float(aa[1]))
                    x+=ldist
                    xx+=ldist*ldist
                    y+=lp
                    yy+=lp*lp
                    xy+=lp*ldist
                    nnn+=1.
        spc=(nnn*xy-x*y)/(nnn*xx-x*x)
        expon=(nnn*xy-x*y)/(nnn*xx-x*x)
        interc=(xx*y-x*xy)/(nnn*xx-x*x)
        sy=0.0
        exps.append(expon)
        with open(fname,"r") as fin:
            for line in fin:
                aa=line.split()
                if float(aa[2])==qq and float(aa[0])<=xmax and float(aa[0])>=xmin and float(aa[1])==float(aa[1]):
                    ldist=math.log(float(aa[0]))
                    lp=math.log(float(aa[1]))
                    sy+=(ldist-lp*expon-interc)*(ldist-lp*expon-interc)
        sy=sy/(nnn-2.0) # va calcolato l'errore sull'esponente - questa formula non va bene
        syt+=sy

    for i in range(qlen):
        print(qvals[i],exps[i],file=fout)

    minn=10000000.0
    amin=10000000.0
    aa=0.25
    while aa<0.5:
        sc=0.0
        for j in range(qlen):
            com=exps[j]-fnb(qvals[j],aa)
            sc+=com*com
        if sc<minn:
            minn=sc
            amin=aa
        aa+=0.00001
    print(amin,minn,sys.argv[1],file=fout2)

    fout.close()

if __name__ == '__main__':
    main()
