#! /usr/bin/python
# -*- coding: utf-8 -*-
#############################################################################
# Copyright 2014 Muhammad Usman Akram. muhammadusman.akram@studenti.unitn.it
#############################################################################

import sys
import math
import getopt
import random
import time
#import numpy as np
import itertools as IT
#from threading import Lock
#mport threading
#rom Queue import Queue
import pdb

#############################################################################
#                PRE PROCESSING
#############################################################################
def stripLabels(pathname):   
    fin = open(pathname)
    
    flbl = open(pathname+".lbl", "w")
    fq = open(pathname+".q", "w")
    
    for line in fin.readlines():
        line = line.strip()
        if len(line) == 0:
            continue
            
        #colon = line.find(":")
        #lbl = -1
        #if lbl[0:colon] == "DESC":
        #    lbl = "1"
            
        start = line.find(" ")
        q = line[start+1:].lower()
        
        if line[-1] != "." and line[-1] != "?" :
            q += " ."
        
        #flbl.write("%s\n" % lbl)
        fq.write("%s\n" % q)
    
    fq.close()
    #flbl.close()
    fin.close()


def usage():
    print("--striplbls")
    
def main(argv):
    try:               
#        print argv    
#        pdb.set_trace()
        opts, args = getopt.getopt(argv, "l:", ["striplbls"])
    except getopt.GetoptError:
#        print e
        usage()
        sys.exit(2)
        
    for opt, arg in opts:                
        if opt in ("-l", "--striplbls"):
            stripLabels(arg)
            
        
#####################################################################
if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))