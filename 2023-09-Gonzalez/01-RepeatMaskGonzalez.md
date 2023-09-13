Gonzalez - analysis (MCTE)
================
roko
9/8/2023

# Prepare

## Download

``` bash
datasets download genome accession PRJNA559813
unzip ncbi_dataset.zip 
mv **/*.fna .
#-rw-------  1 rokofler  staff  139816568 Sep 11 11:42 GCA_020141485.1_ASM2014148v1_genomic.fna
#-rw-------  1 rokofler  staff  142835567 Sep 11 11:42 GCA_020141495.1_ASM2014149v1_genomic.fna
#-rw-------  1 rokofler  staff  140907722 Sep 11 11:42 GCA_020141505.1_ASM2014150v1_genomic.fna
#-rw-------  1 rokofler  staff  138375870 Sep 11 11:42 GCA_020141515.1_ASM2014151v1_genomic.fna
#-rw-------  1 rokofler  staff  144365713 Sep 11 11:42 GCA_020141575.1_ASM2014157v1_genomic.fna
#-rw-------  1 rokofler  staff  145537283 Sep 11 11:42 GCA_020141585.1_ASM2014158v1_genomic.fna
#-rw-------  1 rokofler  staff  144190481 Sep 11 11:42 GCA_020141595.1_ASM2014159v1_genomic.fna
#-rw-------  1 rokofler  staff  138723309 Sep 11 11:42 GCA_020141625.1_ASM2014162v1_genomic.fna
#-rw-------  1 rokofler  staff  143680170 Sep 11 11:42 GCA_020141655.1_ASM2014165v1_genomic.fna
#-rw-------  1 rokofler  staff  145802657 Sep 11 11:42 GCA_020141665.1_ASM2014166v1_genomic.fna
#-rw-------  1 rokofler  staff  142980044 Sep 11 11:42 GCA_020141675.1_ASM2014167v1_genomic.fna
#-rw-------  1 rokofler  staff  146569987 Sep 11 11:42 GCA_020141705.1_ASM2014170v1_genomic.fna
#-rw-------  1 rokofler  staff  138579471 Sep 11 11:42 GCA_020141735.1_ASM2014173v1_genomic.fna
#-rw-------  1 rokofler  staff  145268839 Sep 11 11:42 GCA_020141745.1_ASM2014174v1_genomic.fna
#-rw-------  1 rokofler  staff  141744246 Sep 11 11:42 GCA_020141765.1_ASM2014176v1_genomic.fna
#-rw-------  1 rokofler  staff  140435517 Sep 11 11:42 GCA_020141795.1_ASM2014179v1_genomic.fna
#-rw-------  1 rokofler  staff  140195787 Sep 11 11:42 GCA_020141815.1_ASM2014181v1_genomic.fna
#-rw-------  1 rokofler  staff  149836741 Sep 11 11:42 GCA_020141835.1_ASM2014183v1_genomic.fna
#-rw-------  1 rokofler  staff  142670860 Sep 11 11:42 GCA_020141845.1_ASM2014184v1_genomic.fna
#-rw-------  1 rokofler  staff  142883001 Sep 11 11:42 GCA_020141855.1_ASM2014185v1_genomic.fna
#-rw-------  1 rokofler  staff  139883285 Sep 11 11:42 GCA_020141875.1_ASM2014187v1_genomic.fna
#-rw-------  1 rokofler  staff  145660857 Sep 11 11:42 GCA_020141925.1_ASM2014192v1_genomic.fna
#-rw-------  1 rokofler  staff  138818887 Sep 11 11:42 GCA_020141935.1_ASM2014193v1_genomic.fna
#-rw-------  1 rokofler  staff  150309083 Sep 11 11:43 GCA_020141955.1_ASM2014195v1_genomic.fna
#-rw-------  1 rokofler  staff  140470348 Sep 11 11:43 GCA_020141985.1_ASM2014198v1_genomic.fna
#-rw-------  1 rokofler  staff  142688333 Sep 11 11:43 GCA_020142005.1_ASM2014200v1_genomic.fna
#-rw-------  1 rokofler  staff  143903305 Sep 11 11:43 GCA_020142025.1_ASM2014202v1_genomic.fna
#-rw-------  1 rokofler  staff  145301536 Sep 11 11:43 GCA_020142045.1_ASM2014204v1_genomic.fna
#-rw-------  1 rokofler  staff  140026929 Sep 11 11:43 GCA_020142055.1_ASM2014205v1_genomic.fna
#-rw-------  1 rokofler  staff  139844620 Sep 11 11:43 GCA_020142085.1_ASM2014208v1_genomic.fna
#-rw-------  1 rokofler  staff  143116365 Sep 11 11:43 GCA_020142105.1_ASM2014210v1_genomic.fna
#-rw-------  1 rokofler  staff  136961092 Sep 11 11:43 GCA_020169495.1_ASM2016949v1_genomic.fna
```

## Renaming list

here are all infos for the strains, from the Gonzalez publication.
including old and novel file names

``` remark
filename    newname Genome  Strain  Location    Latitude    Longitude   Collection date Collected by    Inbreed generations
GCA_020142105.1_ASM2014210v1_genomic.fna    D.mel.AKA017.fa AKA-017 cross FI_Aka_ I_15_17   Akka, Finland   61,1    23,52   2015-07-21  Maaria Kankare Lab  F20
GCA_020169495.1_ASM2016949v1_genomic.fna    D.mel.AKA018.fa AKA-018 FI_Aka_15_18    Akka, Finland   61,1    23,52   2015-07-21  Maaria Kankare Lab  0
GCA_020142085.1_ASM2014208v1_genomic.fna    D.mel.COR014.fa COR-014 cross ES_Cor_ I_15_1414 Cortes de Baza, Spain   37,662  -2,796  2015-08-08  González Lab    F20
GCA_020142045.1_ASM2014204v1_genomic.fna    D.mel.COR018.fa COR-018 cross ES_Cor_15_18  Cortes de Baza, Spain   37,662  -2,796  2015-08-08  González Lab    F20
GCA_020142055.1_ASM2014205v1_genomic.fna    D.mel.COR023.fa COR-023 cross ES_Cor_15_23_1    Cortes de Baza, Spain   37,662  -2,796  2015-08-08  González Lab    F20
GCA_020142025.1_ASM2014202v1_genomic.fna    D.mel.COR025.fa COR-025 cross ES_Cor_15_25_1    Cortes de Baza, Spain   37,662  -2,796  2015-08-08  González Lab    F20
GCA_020141985.1_ASM2014198v1_genomic.fna    D.mel.GIM012.fa GIM-012 cross ES_Gim_15_12  Gimenells, Spain    41,656  0,388   2015-06-28  Marta Pascual   F20
GCA_020142005.1_ASM2014200v1_genomic.fna    D.mel.GIM024.fa GIM-024 cross ES_Gim_15_24_1    Gimenells, Spain    41,656  0,388   2015-06-28  Marta Pascual   F16
GCA_020141955.1_ASM2014195v1_genomic.fna    D.mel.JUT008.fa JUT-008 cross DK_Jut_15 8   Jutland, Denmark    59,9    10,75   2015-08-06  Mads Fristrup (Loeschke Lab)    F20
GCA_020141935.1_ASM2014193v1_genomic.fna    D.mel.JUT011.fa JUT-011 cross DK_Jut_ I_15_11   Jutland, Denmark    55,56   10,12   2015-08-06  Mads Fristrup (Loeschke Lab)    F20
GCA_020141925.1_ASM2014192v1_genomic.fna    D.mel.KIE094.fa KIE-094 cross KIE 15 94 Kiev, Ucrania   50,38   30,36   2018-05-01  Elena Pasyukova F20
GCA_020141875.1_ASM2014187v1_genomic.fna    D.mel.LUN004.fa LUN-004 cross SE_Lun_15_4   Lund, Sweden    55,694  13,198  August 2015 Jessica Abbot   F20
GCA_020141855.1_ASM2014185v1_genomic.fna    D.mel.LUN007.fa LUN-007 cross SE_Lun_15_7   Lund, Sweden    55,694  13,198  August 2015 Jessica Abbot   F20
GCA_020141845.1_ASM2014184v1_genomic.fna    D.mel.MUN008.fa MUN-008 cross DE_Mun_15_8   Munich, Germany 48,18   11,61   2015-06-17  John Parsch F20
GCA_020141835.1_ASM2014183v1_genomic.fna    D.mel.MUN009.fa MUN-009 cross DE_Mun_15_9   Munich, Germany 48,18   11,61   2015-06-17  John Parsch F13
GCA_020141815.1_ASM2014181v1_genomic.fna    D.mel.MUN013.fa MUN-013 cross DE_Mun_15_13  Munich, Germany 48,18   11,61   2015-06-17  John Parsch F20
GCA_020141795.1_ASM2014179v1_genomic.fna    D.mel.MUN015.fa MUN-015 cross DE_Mun_15_15  Munich, Germany 48,18   11,61   2015-06-17  John Parsch F20
GCA_020141765.1_ASM2014176v1_genomic.fna    D.mel.MUN016.fa MUN-016 cross DE_Mun_15_16  Munich, Germany 48,18   11,61   2015-06-17  John Parsch F20
GCA_020141735.1_ASM2014173v1_genomic.fna    D.mel.MUN020.fa MUN-020 DE_Mun_15_20    Munich, Germany 48,18   11,61   2015-06-17  John Parsch 0
GCA_020141745.1_ASM2014174v1_genomic.fna    D.mel.RAL059.fa RAL-059 RAL-59  Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141705.1_ASM2014170v1_genomic.fna    D.mel.RAL091.fa RAL-091 RAL-91  Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141665.1_ASM2014166v1_genomic.fna    D.mel.RAL176.fa RAL-176 RAL-176 Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141655.1_ASM2014165v1_genomic.fna    D.mel.RAL177.fa RAL-177 RAL177  Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141675.1_ASM2014167v1_genomic.fna    D.mel.RAL375.fa RAL-375 RAL375  Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141625.1_ASM2014162v1_genomic.fna    D.mel.RAL426.fa RAL-426 RAL-426 Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141585.1_ASM2014158v1_genomic.fna    D.mel.RAL737.fa RAL-737 RAL-737 Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141575.1_ASM2014157v1_genomic.fna    D.mel.RAL855.fa RAL-855 RAL-855 Raleigh, USA    35,787  -78,644 NA  Bloomington F20
GCA_020141595.1_ASM2014159v1_genomic.fna    D.mel.SLA001.fa SLA-001 RS_Sla_16_1 Slankamen, Serbia   45,15   20,18   2016-06-18  Maria Stamenkovic   0
GCA_020141495.1_ASM2014149v1_genomic.fna    D.mel.STO022.fa STO-022 SE_Sto_11_22    Stockholm, Sweden   59,329  18,068  September 2011  González Lab    0
GCA_020141505.1_ASM2014150v1_genomic.fna    D.mel.TEN015.fa TEN-015 ES_Ten_15_15    Tenerife, Spain 28,291  -16,629 2015-09-09  González Lab    0
GCA_020141485.1_ASM2014148v1_genomic.fna    D.mel.TOM007.fa TOM-007 cross TOM I.15 (7)  Tomelloso, Spain    39,158  -3,021  2015-09-17  González Lab    F20
GCA_020141515.1_ASM2014151v1_genomic.fna    D.mel.TOM008.fa TOM-008 cross_ES_Tom_15_8   Tomelloso, Spain    39,158  -3,021  2015-09-17  González Lab    F20
```

## rename command

using renamer.py

``` python
import sys
output="/Users/rokofler/analysis/2023-Spoink/gonzalez/files"
ct="fasta-reader.py {0} | fasta-formatter.py --upper |fasta-writter.py > {1}/{2}"

for name in sys.stdin:
    ifile,ofile =name.rstrip("\n").split("\t")
    com=ct.format(ifile,output,ofile)
    print(com)
```

``` bash
cat fileinfo|python renamer.py
fasta-reader.py GCA_020142105.1_ASM2014210v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.AKA017.fa
fasta-reader.py GCA_020169495.1_ASM2016949v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.AKA018.fa
fasta-reader.py GCA_020142085.1_ASM2014208v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.COR014.fa
fasta-reader.py GCA_020142045.1_ASM2014204v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.COR018.fa
fasta-reader.py GCA_020142055.1_ASM2014205v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.COR023.fa
fasta-reader.py GCA_020142025.1_ASM2014202v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.COR025.fa
fasta-reader.py GCA_020141985.1_ASM2014198v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.GIM012.fa
fasta-reader.py GCA_020142005.1_ASM2014200v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.GIM024.fa
fasta-reader.py GCA_020141955.1_ASM2014195v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.JUT008.fa
fasta-reader.py GCA_020141935.1_ASM2014193v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.JUT011.fa
fasta-reader.py GCA_020141925.1_ASM2014192v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.KIE094.fa
fasta-reader.py GCA_020141875.1_ASM2014187v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.LUN004.fa
fasta-reader.py GCA_020141855.1_ASM2014185v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.LUN007.fa
fasta-reader.py GCA_020141845.1_ASM2014184v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.MUN008.fa
fasta-reader.py GCA_020141835.1_ASM2014183v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.MUN009.fa
fasta-reader.py GCA_020141815.1_ASM2014181v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.MUN013.fa
fasta-reader.py GCA_020141795.1_ASM2014179v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.MUN015.fa
fasta-reader.py GCA_020141765.1_ASM2014176v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.MUN016.fa
fasta-reader.py GCA_020141735.1_ASM2014173v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.MUN020.fa
fasta-reader.py GCA_020141745.1_ASM2014174v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL059.fa
fasta-reader.py GCA_020141705.1_ASM2014170v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL091.fa
fasta-reader.py GCA_020141665.1_ASM2014166v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL176.fa
fasta-reader.py GCA_020141655.1_ASM2014165v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL177.fa
fasta-reader.py GCA_020141675.1_ASM2014167v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL375.fa
fasta-reader.py GCA_020141625.1_ASM2014162v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL426.fa
fasta-reader.py GCA_020141585.1_ASM2014158v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL737.fa
fasta-reader.py GCA_020141575.1_ASM2014157v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.RAL855.fa
fasta-reader.py GCA_020141595.1_ASM2014159v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.SLA001.fa
fasta-reader.py GCA_020141495.1_ASM2014149v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.STO022.fa
fasta-reader.py GCA_020141505.1_ASM2014150v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.TEN015.fa
fasta-reader.py GCA_020141485.1_ASM2014148v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.TOM007.fa
fasta-reader.py GCA_020141515.1_ASM2014151v1_genomic.fna | fasta-formatter.py --upper |fasta-writter.py > /Users/rokofler/analysis/2023-Spoink/gonzalez/files/D.mel.TOM008.fa
```

**Run the commands by pipeing into zsh**

``` bash
cat fileinfo|python renamer.py|zsh
```

# RepeatMask

## Almos LTR

``` bash
for i in raw-dmel/D.mel.*.fa; do RepeatMasker -pa 20 -no_is -s -nolow -dir rm/Ltr-v2  -lib seqs/LTR_Almo-v2.fasta $i;done
```
