#! /usr/bin/python
# -*- coding: utf-8 -*-
#############################################################################
# Copyright 2014 Muhammad Usman Akram. muhammadusman.akram@studenti.unitn.it
#############################################################################

from sklearn.feature_extraction.text import TfidfVectorizer
#import pdb

file = "TREC_10" #"train_5500"

f = open(file+".label.q")
train_set = []
for  line in f.readlines():
    train_set.append(str.decode(line.replace("\r\n",""), "UTF-8", "ignore"))

f.close()

tiV = TfidfVectorizer()
trMat = tiV.fit_transform(train_set) 

# load parse trees
ftree = open(file+".label.parsed")
parsetrees = ftree.readlines()
ftree.close()

# Make following trees from .senna
# BoW, BoP and PAS
senna = open(file+".senna")
bow = [] # Bag of words tree for each sentence
bop = [] # Bag of Parts of Speech for each sentence
pas = [] # pas from srl for each sentence

w = ""
pos = ""
srl = ""

## senna's output for
# what is considered the costliest disaster the insurance industry has ever faced ?
#           what	        WP	              -	   (R-A1*)	   (R-A1*)	         *	         *
#             is	       VBZ	             is	      (V*)	         *	         *	         *
#     considered	       VBN	     considered	    (C-A1*	      (V*)	         *	         *
#            the	        DT	              -	         *	      (A2*	      (A0*	      (A1*
#      costliest	       JJS	              -	         *	         *	         *	         *
#       disaster	        NN	              -	         *	         *	         *	        *)
#            the	        DT	              -	         *	         *	         *	      (A0*
#      insurance	        NN	              -	         *	         *	         *	         *
#       industry	        NN	              -	        *)	         *	        *)	        *)
#            has	       VBZ	            has	         *	         *	      (V*)	         *
#           ever	        RB	              -	         *	         *	 (AM-TMP*)	 (AM-TMP*)
#          faced	       VBN	          faced	         *	        *)	         *	      (V*)
#              ?	         .	              -	         *	         *	         *	         *
#
#(PAS (R-A1 (what *)) (V (is *)) (V (considered *)) (A1 (the costliest disaster *)) (A0 (the insurance industry *)) (V (has*)) (AM-TMP (ever)) (V (faced *)) )
pr_inc = 0 # predicate is incomplete 0/1

for line in senna.readlines():
    #pdb.set_trace()
    tmp = line.replace("\n", "").replace("\t","").replace("*","").split()
    if len(tmp) == 0:
        bow.append("(BOW " + w + ")")
        bop.append("(BOP " + pos + ")")
        pas.append("(PAS " + srl + ")")
        w = ""
        pos = ""
        srl = ""
    else:
        w += "(" + tmp[0] + " *)"
        pos += "(" + tmp[1] + " *)"
        if len(tmp) > 3:
            if tmp[-1].find("(") > -1 and tmp[-1].find(")") > -1:
                srl += " (" + tmp[-1][1:-1] + " (" + tmp[0] + " *))"
            elif tmp[-1].find("(") > -1 and tmp[-1].find(")") == -1:
                srl += " (" + tmp[-1][1:-1] + " (" + tmp[0] 
                pr_inc = 1
            elif tmp[-1].find("(") == -1 and tmp[-1].find(")") > -1:
                srl += tmp[0]  + " *))"
                pr_inc = 0                
                
        elif pr_inc == 1:
            srl += tmp[0]
            
            
fout = open(file+".feat", "w")

ind = trMat.nonzero()
curr = ind[0][0]
r = ""
for q_i in range(len(ind[0])):
    if ind[0][q_i] == curr:
        r += " " + ind[1][q_i].astype(str) + ":" + trMat[curr, ind[1][q_i]].astype(str)
    else:
        feat_w  = " |BT| " + parsetrees[curr].replace("\n","").replace("\r","")
        feat_w += " |BT| " + bow[curr]
        feat_w += " |BT| " + bop[curr]
        feat_w += " |BT| " + pas[curr]
        feat_w += " |ET| " + r
        feat_w += " |EV|\n"
        fout.write(feat_w)
        curr = ind[0][q_i]
        r = " " + ind[1][q_i].astype(str) + ":" + trMat[curr, ind[1][q_i]].astype(str)
 
fout.close()