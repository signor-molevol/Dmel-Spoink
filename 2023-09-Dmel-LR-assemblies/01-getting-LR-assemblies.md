Gonzalez - analysis (MCTE)
================
roko
9/8/2023

# Infos and download

## Canton-S

``` bash
# Canton-S
https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_015832445.1/
datasets download genome accession PRJNA618654
unzip ncbi_dataset.zip
mv ncbi_dataset/data/GCA_015832445.1/GCA_015832445.1_ASM1583244v1_genomic.fna tmp
reader-fasta.py tmp | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.CanS.fa
```

## Chakraborty DSPR

### Info about strains

``` bash
# info about the strains https://wfitch.bio.uci.edu/~dspr/RILs/index.html
Founder Vial Code   Stock Center    Stock Number    Stock Name  Details     
A1  1   Bloomington 1   Canton-S    i18+        # 1935 (Schwarz)
A2  3841    Bloomington 3841    BOG1    i18+        # Bogota 1962 (Bloomington)
A3  3844    Bloomington 3844    BS1 i18+        # Barcelona 1954 (Bloomington)
A4  3852    Bloomington 3852    KSA2    i18+        # Koriba Dam, South Africa 1963 (Bloomington)
A5  3875    Bloomington 3875    VAG1    i18+        # Athens, Greece 1965
A6  3886    Bloomington 3886    wild5B  i18+        # Georgia   1966
A7  T.7 Tucson  14021-0231.7    n/a i18+        
AB8 Sam TFC Mackay  n/a Sam; ry506  +       
B1  3839    Bloomington 3839    BER1    i18+, tetracyline treated       # Bermuda 1954
B2  3846    Bloomington 3846    CA1 i18+                              # Capetown 1954
B3  3864    Bloomington 3864    QI2 i9+, tetracyline treated        # Israel 1954
B4  3870    Bloomington 3870    RVC3    i3+                         # California, 1963
B5  T.0 Tucson  14021-0231.0    n/a i18+        
B6  T.1 Tucson  14021-0231.1    n/a i18+        
B7  T.4 Tucson  14021-0231.4    n/a i18+
# more info
A1  b.1 Canton-S    Canton, Ohio, USA
A21 b.3841  BOG 1   Bogata, Colombia, 1962
A3  b.3844  BS 1    Barcelona, Spain, 1954
A4  b.3852  KSA 2   Koriba Dam, Zimbabwe, 1963
A5  b.3875  VAG 1   Athens, Greece, 1965
A6  b.3886  Wild 5B Red Top Mountain, Georgia, USA, 1966
A7  t.14021-0231.7  –   Ken-ting, Taiwan, 1968
B1  b.3839  BER 1   Bermuda, 1954
B2  b.3846  CA 1    Capetown, South Africa, 1954
B3  b.3864  QI 2    Israel, 1954
B4  b.3870  RVC 3   Riverside, California, USA, 1963
B51 t.14021-0231.0  –   Oahu, Hawaii, 1955
B6  t.14021-0231.1  –   Ica, Peru, 1956
B7  t.14021-0231.4  –   Kuala Lumpur, Malaysia, 1962
AB8 –   Sam ry506   Gift from TFC Mackay (November 2006)
```

``` bash
# Assembly paper
# https://www.nature.com/articles/s41467-019-12884-1/figures/1
# DSPR - King
# https://pubmed.ncbi.nlm.nih.gov/22496517/
# DSPR webpage https://wfitch.bio.uci.edu/~dspr/
datasets download genome accession  PRJNA418342
#   inflating: ncbi_dataset/data/assembly_data_report.jsonl  
 
#  inflating: ncbi_dataset/data/GCA_003401685.1/GCA_003401685.1_ASM340168v1_genomic.fna  

#  inflating: ncbi_dataset/data/GCA_003397115.2/GCA_003397115.2_ASM339711v2_genomic.fna 
#  inflating: ncbi_dataset/data/GCA_003401735.1/GCA_003401735.1_ASM340173v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003401745.1/GCA_003401745.1_ASM340174v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003401795.1/GCA_003401795.1_ASM340179v1_genomic.fna  

#  inflating: ncbi_dataset/data/GCA_003401805.1/GCA_003401805.1_ASM340180v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003401855.1/GCA_003401855.1_ASM340185v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003401885.1/GCA_003401885.1_ASM340188v1_genomic.fna  

#  inflating: ncbi_dataset/data/GCA_003401915.1/GCA_003401915.1_ASM340191v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003401925.1/GCA_003401925.1_ASM340192v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003401975.1/GCA_003401975.1_ASM340197v1_genomic.fna  

#  inflating: ncbi_dataset/data/GCA_003402005.1/GCA_003402005.1_ASM340200v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003402015.1/GCA_003402015.1_ASM340201v1_genomic.fna  
#  inflating: ncbi_dataset/data/GCA_003402055.1/GCA_003402055.1_ASM340205v1_genomic.fna
# 15

reader-fasta.py ncbi_dataset/data/GCA_003401685.1/GCA_003401685.1_ASM340168v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.AB8.fa
 
reader-fasta.py ncbi_dataset/data/GCA_003397115.2/GCA_003397115.2_ASM339711v2_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.B6.fa 
reader-fasta.py ncbi_dataset/data/GCA_003401735.1/GCA_003401735.1_ASM340173v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.CanSChak.fa
reader-fasta.py ncbi_dataset/data/GCA_003401745.1/GCA_003401745.1_ASM340174v1_genomic.fna  | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.A4.fa
reader-fasta.py ncbi_dataset/data/GCA_003401795.1/GCA_003401795.1_ASM340179v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.A3.fa

reader-fasta.py ncbi_dataset/data/GCA_003401805.1/GCA_003401805.1_ASM340180v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.A2.fa
reader-fasta.py ncbi_dataset/data/GCA_003401855.1/GCA_003401855.1_ASM340185v1_genomic.fna  | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.A5.fa
reader-fasta.py ncbi_dataset/data/GCA_003401885.1/GCA_003401885.1_ASM340188v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.A6.fa 

reader-fasta.py ncbi_dataset/data/GCA_003401915.1/GCA_003401915.1_ASM340191v1_genomic.fna  | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.A7.fa
reader-fasta.py ncbi_dataset/data/GCA_003401925.1/GCA_003401925.1_ASM340192v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.B1.fa 
reader-fasta.py ncbi_dataset/data/GCA_003401975.1/GCA_003401975.1_ASM340197v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.B2.fa

reader-fasta.py ncbi_dataset/data/GCA_003402055.1/GCA_003402055.1_ASM340205v1_genomic.fna   | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.B3.fa
reader-fasta.py ncbi_dataset/data/GCA_003402015.1/GCA_003402015.1_ASM340201v1_genomic.fna | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.ORE.fa 
reader-fasta.py ncbi_dataset/data/GCA_003402005.1/GCA_003402005.1_ASM340200v1_genomic.fna  | fasta-formatter-fasta.py --upper | fasta-writter.py > D.mel.B4.fa
```

## overview of the assemblies

``` bash
-rw-r--r--   1 fschwarz  staff  144129164 Sep 25 17:31 D.mel.A2.fa
-rw-r--r--   1 fschwarz  staff  135009301 Sep 25 17:31 D.mel.A3.fa
-rw-r--r--   1 fschwarz  staff  142447183 Sep 25 17:31 D.mel.A4.fa
-rw-r--r--   1 fschwarz  staff  140670166 Sep 25 17:31 D.mel.A5.fa
-rw-r--r--   1 fschwarz  staff  134893231 Sep 25 17:31 D.mel.A6.fa
-rw-r--r--   1 fschwarz  staff  148701351 Sep 25 17:31 D.mel.A7.fa
-rw-r--r--   1 fschwarz  staff  139429369 Sep 25 17:31 D.mel.AB8.fa
-rw-r--r--   3 fschwarz  staff  143111534 Sep 12 10:51 D.mel.AKA017.fa
-rw-r--r--   3 fschwarz  staff  136960293 Sep 12 10:51 D.mel.AKA018.fa
-rw-r--r--   1 fschwarz  staff  137677086 Sep 25 17:31 D.mel.B1.fa
-rw-r--r--   1 fschwarz  staff  139205134 Sep 25 17:31 D.mel.B2.fa
-rw-r--r--   1 fschwarz  staff  137897059 Sep 25 17:31 D.mel.B3.fa
-rw-r--r--   1 fschwarz  staff  137965310 Sep 25 17:31 D.mel.B4.fa
-rw-r--r--   1 fschwarz  staff  139179045 Sep 25 17:31 D.mel.B6.fa
-rw-r--r--   3 fschwarz  staff  139842923 Sep 12 10:51 D.mel.COR014.fa
-rw-r--r--   3 fschwarz  staff  145299444 Sep 12 10:51 D.mel.COR018.fa
-rw-r--r--   3 fschwarz  staff  140024989 Sep 12 10:51 D.mel.COR023.fa
-rw-r--r--   3 fschwarz  staff  143902144 Sep 12 10:51 D.mel.COR025.fa
-rw-r--r--   1 fschwarz  staff  150968688 Sep 25 17:31 D.mel.CanS.fa
-rw-r--r--   1 fschwarz  staff  139390242 Sep 25 17:31 D.mel.CanSChak.fa
-rw-r--r--   3 fschwarz  staff  140468926 Sep 12 10:52 D.mel.GIM012.fa
-rw-r--r--   3 fschwarz  staff  142683453 Sep 12 10:52 D.mel.GIM024.fa
-rw-r--r--   7 fschwarz  staff  146520911 Apr 27 13:21 D.mel.Iso1.fa
-rw-r--r--   3 fschwarz  staff  150301503 Sep 12 10:52 D.mel.JUT008.fa
-rw-r--r--   3 fschwarz  staff  138817322 Sep 12 10:52 D.mel.JUT011.fa
-rw-r--r--   3 fschwarz  staff  145655576 Sep 12 10:52 D.mel.KIE094.fa
-rw-r--r--   3 fschwarz  staff  139881972 Sep 12 10:52 D.mel.LUN004.fa
-rw-r--r--   3 fschwarz  staff  142881688 Sep 12 10:52 D.mel.LUN007.fa
-rw-r--r--   3 fschwarz  staff  142669641 Sep 12 10:52 D.mel.MUN008.fa
-rw-r--r--   3 fschwarz  staff  149831916 Sep 12 10:52 D.mel.MUN009.fa
-rw-r--r--   3 fschwarz  staff  140194270 Sep 12 10:52 D.mel.MUN013.fa
-rw-r--r--   3 fschwarz  staff  140434475 Sep 12 10:52 D.mel.MUN015.fa
-rw-r--r--   3 fschwarz  staff  141741002 Sep 12 10:52 D.mel.MUN016.fa
-rw-r--r--   3 fschwarz  staff  138578050 Sep 12 10:52 D.mel.MUN020.fa
-rw-r--r--   1 fschwarz  staff  137962260 Sep 25 17:32 D.mel.ORE.fa
-rw-r--r--   7 fschwarz  staff  170631244 May  3 11:26 D.mel.Pi2.fa
-rw-r--r--   3 fschwarz  staff  145265667 Sep 12 10:52 D.mel.RAL059.fa
-rw-r--r--   3 fschwarz  staff  146565891 Sep 12 10:52 D.mel.RAL091.fa
-rw-r--r--   4 fschwarz  staff  145799362 Sep 12 10:52 D.mel.RAL176.fa
-rw-r--r--   3 fschwarz  staff  143675822 Sep 12 10:52 D.mel.RAL177.fa
-rw-r--r--   3 fschwarz  staff  142976704 Sep 12 10:52 D.mel.RAL375.fa
-rw-r--r--   3 fschwarz  staff  138721884 Sep 12 10:52 D.mel.RAL426.fa
-rw-r--r--   3 fschwarz  staff  145534753 Sep 12 10:52 D.mel.RAL737.fa
-rw-r--r--   3 fschwarz  staff  144362758 Sep 12 10:52 D.mel.RAL855.fa
-rw-r--r--   3 fschwarz  staff  144188721 Sep 12 10:52 D.mel.SLA001.fa
-rw-r--r--   3 fschwarz  staff  142833877 Sep 12 10:52 D.mel.STO022.fa
-rw-r--r--   3 fschwarz  staff  140906390 Sep 12 10:53 D.mel.TEN015.fa
-rw-r--r--   4 fschwarz  staff  139815051 Sep 12 10:53 D.mel.TOM007.fa
-rw-r--r--   3 fschwarz  staff  138373990 Sep 12 10:53 D.mel.TOM008.fa
```

# RepeatMasking all assemblies

``` bash
for i in assemblies/*.fa ; do RepeatMasker -pa 20 -no_is -s -nolow -dir rm -lib seq/spoink-dmel-consensus_v1.fasta  $i;done 
# cleaning all repeat masked files
for i in *.ori.out; do cat $i|reader-rm.py|rm-cleanup.py > $i.clean; done
```

# Infer contig identities

``` bash
# info Download ref-genome with proper chromosome names https://ftp.ensembl.org/pub/release-110/fasta/drosophila_melanogaster/dna/

# Nucmer
nucmer -p nuco/D.mel.RAL176.nuco refgenome/Dmel.ref.fa assemblies/D.mel.RAL176.fa
nucmer -p nuco/D.mel.Iso1.nuco refgenome/Dmel.ref.fa assemblies/D.mel.Iso1.fa
nucmer -p nuco/D.mel.AKA017.nuco refgenome/Dmel.ref.fa assemblies/D.mel.AKA017.fa
nucmer -p nuco/D.mel.RAL737.nuco.delta refgenome/Dmel.ref.fa assemblies/D.mel.RAL737.fa 
nucmer -p nuco/D.mel.RAL059.nuco.delta refgenome/Dmel.ref.fa assemblies/D.mel.RAL059.fa

# coordinates
show-coords D.mel.RAL176.nuco.delta > D.mel.RAL176.nuco.delta.coordinates
```

### which chromosomes?

**Iso1**

``` bash
(base) [0,11099]fschwarz% cat D.mel.Iso1.nuco.delta.coordinates|awk '$7>100000'|awk '{print $12 "-" $13}'|sort |uniq -c |sort -nr $1|head -20
  67 3L-JAEIGS010000103.1
  66 X-JAEIGS010000021.1
  60 2L-JAEIGS010000190.1
  58 3R-JAEIGS010000049.1
  55 2R-JAEIGS010000001.1
   8 3R-JAEIGS010000050.1
   8 3L-JAEIGS010000286.1
   8 2R-JAEIGS010000288.1
   5 X-JAEIGS010000287.1
   5 4-JAEIGS010000192.1
   4 3L-JAEIGS010000237.1
   4 2L-JAEIGS010000089.1
   3 3R-JAEIGS010000285.1
   3 3R-JAEIGS010000052.1
   3 2R-JAEIGS010000127.1
   2 3R-JAEIGS010000110.1
   2 3R-JAEIGS010000059.1
   1 [%-IDY]
   1 3R-JAEIGS010000165.1
   1 3L-JAEIGS010000104.1
```

**AKA017**

``` bash
cat D.mel.AKA017.nuco.delta.coordinates|awk '$7>100000'|awk '{print $12 "-" $13}'|sort |uniq -c |sort -nr $1|head -20 
  59 3R-CM034932.1
  44 X-CM034928.1
  43 3L-CM034931.1
  38 2R-CM034930.1
  36 2L-CM034929.1
   2 4-CM034933.1
```

# Visualize

``` r
library(tidyverse)
```

    ## ── Attaching packages ─────────────────────────────────────── tidyverse 1.3.1 ──

    ## ✔ ggplot2 3.3.6     ✔ purrr   0.3.4
    ## ✔ tibble  3.1.7     ✔ dplyr   1.0.9
    ## ✔ tidyr   1.2.0     ✔ stringr 1.4.0
    ## ✔ readr   2.1.2     ✔ forcats 0.5.1

    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()

``` r
theme_set(theme_bw())

boundary<-data.frame(crap=rep("rm",12),score=rep(1,12),similarity=rep(-1,12),
                     contig=c("X","X","2L","2L","2R","2R","3L","3L","3R","3R","4","4"),
                     start=c(1,21975285,1,22510348,1,21632781,1,24592382,1,25812719,1,1341466),end=rep(-1,12),strand=rep("+",12),te=rep("spoink",12),testart=rep(1,12),teend=rep(2,12),fraclen=rep(c(0.01,1.0),6))

hiso<-read.table("/Users/rokofler/analysis/2023-Spoink/Dmel-Spoink/2023-09-Dmel-LR-assemblies/rawori/D.mel.Iso1.fa.ori.out.clean",header=F)
# rm    281 32.98   JAECWU010000001.1   6501457 6501784 +   spoink  1967    2300    0.06    C.costata
# rm    316 34.41   JAECWU010000001.1   12897196    12897520    C   spoink  1953    2274    0.06    C.costata
# rm    316 34.73   JAECWU010000001.1   13058319    13058643    C   spoink  1953    2274    0.06    C.costata
names(hiso)<-c("crap","score","similarity","contig","start","end","strand","te","testart","teend","fraclen")
#  66 X-JAEIGS010000021.1
#  60 2L-JAEIGS010000190.1
#  55 2R-JAEIGS010000001.1
#  67 3L-JAEIGS010000103.1
#  58 3R-JAEIGS010000049.1
#   5 4-JAEIGS010000192.1

keeporder<-c("JAEIGS010000021.1","JAEIGS010000190.1","JAEIGS010000001.1", "JAEIGS010000103.1","JAEIGS010000049.1","JAEIGS010000192.1")
hiso<-subset(hiso,contig %in% keeporder)
hiso$contig<-recode_factor(hiso$contig,JAEIGS010000021.1="X",JAEIGS010000190.1="2L",JAEIGS010000001.1="2R", JAEIGS010000103.1="3L",JAEIGS010000049.1="3R",JAEIGS010000192.1="4")

hiso<-subset(hiso,similarity<25)
hiso<-subset(hiso,fraclen>0.01)
hiso<-rbind(hiso,boundary)


tiso<-ggplot()+geom_point(data=hiso,aes(x=start,y=similarity,size=fraclen))+facet_grid(.~contig, scales="free_x", space = "free_x")+ylim(0,25)+scale_x_continuous(breaks=c(0,5000000,10000000,15000000,20000000,25000000),labels=c("0","5m","10m","15m","20m","25m"))+ylab("divergence [%]")
plot(tiso)
```

    ## Warning: Removed 12 rows containing missing values (geom_point).

![](01-getting-LR-assemblies_files/figure-gfm/unnamed-chunk-9-1.png)<!-- -->

``` r
haka<-read.table("/Users/rokofler/analysis/2023-Spoink/Dmel-Spoink/2023-09-Dmel-LR-assemblies/rawori/D.mel.AKA017.fa.ori.out.clean",header=F)
names(haka)<-c("crap","score","similarity","contig","start","end","strand","te","testart","teend","fraclen")
#  59 3R-CM034932.1
#  44 X-CM034928.1
#  43 3L-CM034931.1
#  38 2R-CM034930.1
#  36 2L-CM034929.1
#   2 4-CM034933.1


keeporder<-c("CM034928.1","CM034929.1","CM034930.1", "CM034931.1","CM034932.1","CM034933.1")
haka<-subset(haka,contig %in% keeporder)
haka$contig<-recode_factor(haka$contig, CM034928.1="X",CM034929.1="2L",CM034930.1="2R", CM034931.1="3L",CM034932.1="3R",CM034933.1="4")
haka<-subset(haka,similarity<25)
haka<-subset(haka,fraclen>0.01)
haka<-rbind(haka,boundary)

taka<-ggplot()+geom_point(data=haka,aes(x=start,y=similarity,size=fraclen))+facet_grid(.~contig, scales="free_x", space = "free_x")+ylim(0,25)+scale_x_continuous(breaks=c(0,5000000,10000000,15000000,20000000,25000000),labels=c("0","5m","10m","15m","20m","25m"))+ylab("divergence [%]")
#+scale_size_manual(limits=c(0.0,1.0))
plot(taka)
```

    ## Warning: Removed 12 rows containing missing values (geom_point).

![](01-getting-LR-assemblies_files/figure-gfm/unnamed-chunk-9-2.png)<!-- -->

``` r
#pdf(file="/Users/rokofler/analysis/2023-Spoink/Dmel-Spoink/2023-09-originOfSpoink/graphs/species-histogram.pdf",width=7,height=7)
#plot(p)
#dev.off()
```
