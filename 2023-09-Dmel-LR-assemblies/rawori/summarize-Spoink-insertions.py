#!/usr/bin/env python
import os
import sys
import re
import argparse
import random
import collections




parser = argparse.ArgumentParser(description="""           
Description
-----------
    This script simulates single-end reads from the population genome""",formatter_class=argparse.RawDescriptionHelpFormatter,
epilog="""
Prerequisites
-------------
    python version 3+

Authors
-------
    Robert Kofler 
""")

ages={
"A2":("1962","SoA"),
"A3":("1954","Europe"),
"A4":("1963","Africa"),
"A5":("1965","Europe"),
"A6":("1966","NoA"),
"A7":("1968","Asia"),
"AB8":("NA","NA"),
"AKA017":("2015","Europe"),
"AKA018":("2015","Europe"),
"B1":("1954","NoA"),
"B2":("1954","Africa"),
"B3":("1954","Asia"),
"B4":("1963","NoA"),
"B6":("1956","SoA"),
"COR014":("2015","Europe"),
"COR018":("2015","Europe"),
"COR023":("2015","Europe"),
"COR025":("2015","Europe"),
"CanS":("1935","NoA"),
"CanSChak":("1935","NoA"),
"GIM012":("2015","Europe"),
"GIM024":("2015","Europe"),
"Iso1":("NA","NA"),
"JUT008":("2015","Europe"),
"JUT011":("2015","Europe"),
"KIE094":("2018","Europe"),
"LUN004":("2015","Europe"),
"LUN007":("2015","Europe"),
"MUN008":("2015","Europe"),
"MUN009":("2015","Europe"),
"MUN013":("2015","Europe"),
"MUN015":("2015","Europe"),
"MUN016":("2015","Europe"),
"MUN020":("2015","Europe"),
"ORE":("1925","NoA"),
"Pi2":("1975","NA"),
"RAL059":("2003","NoA"),
"RAL091":("2003","NoA"),
"RAL176":("2003","NoA"),
"RAL177":("2003","NoA"),
"RAL375":("2003","NoA"),
"RAL426":("2003","NoA"),
"RAL737":("2003","NoA"),
"RAL855":("2003","NoA"),
"SLA001":("2016","Europe"),
"STO022":("2011","Europe"),
"TEN015":("2015","Africa"),
"TOM007":("2015","Europe"),
"TOM008":("2015","Europe"),
}



parser.add_argument("--sum", type=str, required=True, dest="sum", default=None, help="the summary file")
args = parser.parse_args()

ch=collections.defaultdict(lambda:[0,0])

for line in open(args.sum):
	line=line.rstrip().lstrip()
	a=re.split("\s+",line)
	#print(a)
	#  0	1	2		3			4		5		6		7	8		9		10			11		
	# rm	240	20.74	CM010555.1	7955735	7955880	+	spoink	2049	2194	0.03	 D.mel.A2
	# rm	278	29.69	CM010555.1	8266306	8266547	+	spoink	1967	2208	0.05	 D.mel.A2
	divergence,fam,lenfrac,assembly=float(a[2]),a[7],float(a[10]),a[11]
	if fam != "spoink":
		raise Exception("invalid family")
	
	if divergence < 5 and lenfrac >0.8:
		ch[assembly][0]+=1
	elif divergence <25 and lenfrac >0.1:
		ch[assembly][1]+=1 
	else:
		pass # total crap ignore


for assembly,count in ch.items():
	assembly=assembly[6:]
	year,area=ages[assembly]
	consc,fragc=count
	tpa=[assembly,year,area,"consensus",str(consc)]
	tpb=[assembly,year,area,"degraded",str(fragc)]
	print("\t".join(tpa))
	print("\t".join(tpb))

