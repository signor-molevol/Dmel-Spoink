RM output to CONSENSUS
================

Explanation of the RepeatMasker output file:

- `SWscore` = Smith-Waterman score of the match, usually complexity
  adjusted
- `perc_div` = % substitutions in matching region compared to the
  consensus
- `perc_del` = % of bases opposite a gap in the query sequence (deleted
  bp)
- `perc_ins` = % of bases opposite a gap in the repeat consensus
  (inserted bp)
- `query_sequence` = name of query sequence
- `position_in_query_begin` = starting position of match in query
  sequence
- `position_in_query_end` = ending position of match in query sequence
- `position_in_query_left` = no. of bases in query sequence past the
  ending position of match
- `C` = match is with the Complement of the consensus sequence in the
  database
- `matching_repeat` = name of the matching interspersed repeat
- `repeat_class/family` = the class of the repeat
- `position_in_repeat_begin` = starting position of match in database
  sequence (using top-strand numbering)
- `position_in_repeat_end` = ending position of match in database
  sequence
- `position_in_repeat_left` = no. of bases in the repeat consensus
  sequence prior to beginning of the match (so 0 means that the match
  extended all the way to the end of the repeat consensus sequence)
- `ID` = estimated unique transposon (es. two segments of the same
  transposon could be separated by another insertion, thus these two
  sequences have the same ID)
- An asterisk (\*) in the final column indicates that there is a
  higher-scoring match whose domain partly (\<80%) includes the domain
  of this match.

Note that the three column indicating the **position in repeat** are
arranged differently for insertions in the two strands:

- For `+` strand: `begin`, `end`, `left`
- For `C` strand: `left`, `end`, `begin`

For simplicity, we kept the order of the `+` strand for all the RM hits
and we dealt with this difference in the next analysis calculating
`fragment length` and `segment length` differently for the two strands.

Command to remove multiple spaces from the RM output and make it
readable in R:

    less path/rm.out | sed 's/  */ /g' | cut -c2- | > output

``` r
library(tidyverse)
```

    ## ── Attaching core tidyverse packages ──────────────────────── tidyverse 2.0.0 ──
    ## ✔ dplyr     1.1.1     ✔ readr     2.1.4
    ## ✔ forcats   1.0.0     ✔ stringr   1.5.0
    ## ✔ ggplot2   3.4.2     ✔ tibble    3.2.1
    ## ✔ lubridate 1.9.2     ✔ tidyr     1.3.0
    ## ✔ purrr     1.0.1     
    ## ── Conflicts ────────────────────────────────────────── tidyverse_conflicts() ──
    ## ✖ dplyr::filter() masks stats::filter()
    ## ✖ dplyr::lag()    masks stats::lag()
    ## ℹ Use the conflicted package (<http://conflicted.r-lib.org/>) to force all conflicts to become errors

``` r
library(ggpubr)
```

``` r
strains <- c("Es_Ten","Iso1","Pi2","RAL91","RAL176","RAL732","RAL737","SE_Sto")

read_RM_out <- function(path, strain_name) {
  
  out <- read_delim(path, delim = " ", col_names = c("SWscore", "perc_div", "perc_del", "perc_ins", "query_sequence", "position_in_query_begin", "position_in_query_end", "position_in_query_left",  "strand", "matching_repeat", "repeat_class/family", "position_in_repeat_begin", "position_in_repeat_end", "position_in_repeat_left")) %>% select(-X15) %>% mutate(position_in_repeat_begin = str_replace(position_in_repeat_begin, "\\(", "")) %>% mutate(position_in_repeat_begin = str_replace(position_in_repeat_begin, "\\)", "")) %>% mutate(position_in_repeat_left = str_replace(position_in_repeat_left, "\\(", "")) %>% mutate(position_in_repeat_left = str_replace(position_in_repeat_left, "\\)", "")) %>% mutate(position_in_query_left = str_replace(position_in_query_left, "\\(", "")) %>% mutate(position_in_query_left = str_replace(position_in_query_left, "\\)", "")) %>% mutate(position_in_repeat_end = str_replace(position_in_repeat_end, "\\(", "")) %>% mutate(position_in_repeat_end = str_replace(position_in_repeat_end, "\\)", "")) %>% mutate(position_in_query_begin = str_replace(position_in_query_begin, "\\(", "")) %>% mutate(position_in_query_begin = str_replace(position_in_query_begin, "\\)", "")) %>% mutate(position_in_query_end = str_replace(position_in_query_end, "\\(", "")) %>% mutate(position_in_query_end = str_replace(position_in_query_end, "\\)", "")) %>% type_convert()
  
  out_inverted <- out %>% mutate(backup = ifelse(strand == "C", position_in_repeat_begin, "empty"), position_in_repeat_begin = ifelse(strand == "C", position_in_repeat_left, position_in_repeat_begin), position_in_repeat_left = ifelse(strand == "C", backup, position_in_repeat_left)) %>% select(-backup) %>% mutate(strain = strain_name)
  
  out_spoink <- out_inverted %>% filter(matching_repeat == "gypsy-7-sim1")
}

Es_Ten <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.Es_Ten.fa.ori.out", "Es_Ten")
```

    ## Rows: 2316 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
Iso1 <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.Iso1.fa.ori.out", "Iso1")
```

    ## Rows: 2338 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
Pi2 <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.Pi2.fa.ori.out", "Pi2")
```

    ## Rows: 2844 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
RAL91 <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.RAL91.fa.ori.out", "RAL91")
```

    ## Rows: 2638 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
RAL176 <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.RAL176.fa.ori.out", "RAL176")
```

    ## Rows: 2620 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
RAL732 <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.RAL732.fa.ori.out", "RAL732")
```

    ## Rows: 2259 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
RAL737 <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.RAL737.fa.ori.out", "RAL737")
```

    ## Rows: 2374 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
SE_Sto <- read_RM_out("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/readable/D.mel.SE_Sto.fa.ori.out", "SE_Sto")
```

    ## Rows: 2352 Columns: 15
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: " "
    ## chr (7): query_sequence, position_in_query_left, strand, matching_repeat, re...
    ## dbl (7): SWscore, perc_div, perc_del, perc_ins, position_in_query_begin, pos...
    ## lgl (1): X15
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.
    ## 
    ## ── Column specification ────────────────────────────────────────────────────────
    ## cols(
    ##   query_sequence = col_character(),
    ##   position_in_query_begin = col_double(),
    ##   position_in_query_end = col_double(),
    ##   position_in_query_left = col_double(),
    ##   strand = col_character(),
    ##   matching_repeat = col_character(),
    ##   `repeat_class/family` = col_character(),
    ##   position_in_repeat_begin = col_double(),
    ##   position_in_repeat_end = col_double(),
    ##   position_in_repeat_left = col_double()
    ## )

``` r
RM_merged <- bind_rows(Es_Ten, RAL91, RAL176, RAL732, RAL737, SE_Sto) %>% select(-"matching_repeat", -"repeat_class/family")
```

``` r
identify_fragments <- RM_merged %>% mutate(length = position_in_query_end-position_in_query_begin,
    distance_from_previous = position_in_query_begin - lag(position_in_query_end, default = first(position_in_query_end)),
    distance_from_next = lead(position_in_query_begin, default = last(position_in_query_begin)) - position_in_query_end,
    HQ_hits = ifelse(SWscore > 10000, "HQ", "fragment"))

fragments_near_fragments <- identify_fragments %>%
  filter(HQ_hits == "fragment" & 
           (lead(HQ_hits) == "fragment" & distance_from_next < 100) | 
           (lag(HQ_hits) == "fragment" & distance_from_previous < 100)) %>% filter(perc_div < 20)
    
fragments_near_HQ <- identify_fragments %>% filter(HQ_hits == "HQ" | (lead(HQ_hits) == "HQ" & distance_from_next < 100) | (lag(HQ_hits) == "HQ" & distance_from_previous < 100)) %>% filter(perc_div < 20) %>% bind_rows(fragments_near_fragments) %>% arrange(strain, query_sequence, position_in_query_begin)

(insertions <- fragments_near_HQ %>% group_by(strain) %>% mutate(insertion_number = cumsum(distance_from_previous > 100) + 1) %>% ungroup() %>% select(-position_in_query_left) %>% group_by(insertion_number, strain) %>% filter(sum(length) > 4500) %>% ungroup() %>% group_by(strain, query_sequence) %>% mutate(insertion_number = cumsum(distance_from_previous > 100) + 1) %>% ungroup() %>% distinct())
```

    ## # A tibble: 432 × 17
    ##    SWscore perc_div perc_del perc_ins query_sequence position_in_query_begin
    ##      <dbl>    <dbl>    <dbl>    <dbl> <chr>                            <dbl>
    ##  1    5010     1.39     0.69     1.21 CM034718.1                     6130345
    ##  2   42769     0.17     0.23     0.9  CM034718.1                     6130870
    ##  3    4681     1.76     0        0.18 CM034718.1                    14085675
    ##  4   40380     0.09     0.26     0.09 CM034718.1                    14086194
    ##  5   39626     0.15     1.1      0.11 CM034718.1                    20111890
    ##  6    4698     0.88     0.17     0.88 CM034718.1                    20116464
    ##  7    4642     0.89     0.88     0.88 CM034718.1                    20122293
    ##  8   39531     0.19     1.13     0.11 CM034718.1                    20122813
    ##  9   40513     0.04     0.19     0.11 CM034718.1                    20157002
    ## 10    4640     0.36     1.45     0.18 CM034718.1                    20161632
    ## # ℹ 422 more rows
    ## # ℹ 11 more variables: position_in_query_end <dbl>, strand <chr>,
    ## #   position_in_repeat_begin <dbl>, position_in_repeat_end <dbl>,
    ## #   position_in_repeat_left <chr>, strain <chr>, length <dbl>,
    ## #   distance_from_previous <dbl>, distance_from_next <dbl>, HQ_hits <chr>,
    ## #   insertion_number <dbl>

``` r
insertions_selected <- insertions %>% select(query_sequence, position_in_query_begin, position_in_query_end, strand, position_in_repeat_begin, position_in_repeat_end, strain, distance_from_previous, distance_from_next)

strains <- c("Es_Ten","RAL176","RAL732","RAL737","RAL91","SE_Sto")
for (s in strains){
  single_strain <- insertions_selected %>% filter(strain==s)
  path <- paste0("/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/bed/", "D.mel.", s, ".tsv")
  write_tsv(single_strain, path)
}
```

    find /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/bed -name '*.tsv' -type f -exec sh -c 'python /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/insertions2bed.py $0 5000 5600 29 ${0%.tsv}.bed' {} \;


    for bed_file in /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/bed/*.bed; do
        base_name=$(basename "$bed_file" .bed)
        fasta_file="/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/genomes/$base_name.fa"   
        output_fasta="/Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/fasta/$base_name.fasta"
        bedtools getfasta -s -fi "$fasta_file" -bed "$bed_file" -fo "$output_fasta"
    done

    cat /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/RM-out/fasta/*.fasta > /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/MSA/spoink-Dmel.fasta

    muscle -in /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/MSA/spoink-Dmel.fasta -out /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/MSA/spoink.MSA

    python /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/MSA2consensus.py /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/MSA/spoink.MSA /Volumes/Temp1/simulans-old-strains/Dmel-spoink/consensus/MSA/spoink-consensus-dmel.fasta
