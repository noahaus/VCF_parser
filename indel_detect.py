#indel_detect.py
#author: Noah A. Legall
#date created: September  2019
#date finished: July 3rd 2019
#dates edited:
#purpose: extract number of insertions and deletions in VCF files.

import os # use in order to call commands from the terminal script is called in
import glob

list_of_files = glob.glob('*.vcf')

snp_count = 0
del_count = 0
ins_count = 0
print("ISOLATE NAME,No. SNP,No. DEL,No. INS")
for file in list_of_files:
    name = file.replace(".vcf","")
    vcf = open(file,'r')
    vcf_list = []
    for line in vcf:
        vcf_list.append(line.strip())
    for i in range(len(vcf_list)):
        if vcf_list[i].startswith('#'):
            continue
        else:
            if "TYPE=snp" in vcf_list[i]:
                snp_count = snp_count + 1
            elif "TYPE=del" in vcf_list[i]:
                del_count = del_count + 1
            elif "TYPE=ins" in vcf_list[i]:
                ins_count = ins_count + 1
    print("{},{},{},{}".format(name,snp_count,del_count,ins_count))
    snp_count = 0
    del_count = 0
    ins_count = 0
