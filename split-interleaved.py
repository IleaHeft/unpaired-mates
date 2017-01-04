#! /usr/bin/env python


import sys
import pdb
from collections import defaultdict
#from collections import Counter

interleaved=sys.argv[1]
sample = sys.argv[2]
out_folder = sys.argv[3]

read1_paired = open(out_folder + "/" + sample + "-read1.fq", mode = 'w')
read2_paired = open(out_folder + "/" + sample + "-read2.fq", mode = 'w')
lone_reads = open(out_folder + "/" + sample + "-no-mate.fq",mode = 'w')

read_info=defaultdict(list)
mates=defaultdict(list)
condition = "u"
info=[]

index_of_int = 0
for index,line in enumerate(open(interleaved)):
    
    if index == 0:
        read_id_c = line.strip().split("/")[0]
        
    if line.startswith("@ST"):
        read_id_full = line.strip()
        read_id = read_id_full.split("/")[0]
        read_num = read_id_full.split("/")[1]
        

        if index > 0 and read_id == read_id_c:
            
            print >> read1_paired, read_id_c
            print >> read1_paired, info[0]
            print >> read1_paired, info[1]
            print >> read1_paired, info[2]
            print >> read2_paired, read_id
            

            condition = "p"
        

        else:
            if index == index_of_int + 4:
                print >> lone_reads, read_id_c
                print >> lone_reads, info[0]
                print >> lone_reads, info[1]
                print >> lone_reads, info[2]
            
                read_id_c = read_id
                index_of_int = index
                condition = "u"

            else:
                read_id_c = read_id
                index_of_int = index
                condition = "u"
    else:
        if condition == "p":

            print >> read2_paired, line.strip()
            info =[]
        
        
        
        else:

            info.append(line.strip())
