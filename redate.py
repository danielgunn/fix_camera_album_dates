import glob, os, sys
path = sys.arg[1]
fl=glob.glob(path + 'CIMG1???.???')
i=0
pvalid = 0
pcurrent = 0
pnew = 0
pbad = 0
while 1 == 1:
	filepat = path + "CIMG%0.4d.*" % (i)
	if [] == glob.glob(filepat):
		break
	for f in glob.glob(filepat):
		pcurrent = os.path.getmtime(f)
		if (pcurrent > pvalid):
			pbad = 0
			pnew = 0
			pvalid = pcurrent
		else:
			if pbad == 0:
				pbad = pcurrent-1
			pnew = (pcurrent - pbad) + pvalid
		if (pnew > 0):
			os.utime(f, (pnew, pnew))
			print "set time for %s to %d" % (f,pnew)
	i = i+1
