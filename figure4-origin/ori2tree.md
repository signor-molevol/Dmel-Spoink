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

I switched the order of the `C` strand for all the RM hits and we dealt
with this difference in the next analysis to keep it consistent.

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

List of strains used for the consensus sequence generation (long-reads).

``` r
strains <- c("D.mel.Es_Ten","D.mel.RAL91","D.mel.RAL176","D.mel.RAL732","D.mel.RAL737","D.mel.SE_Sto", "D.paulistorum.06", "D.paulistorum.12", "D.tropicalis", "D.willistoni.00", "D.willistoni.17", "D.insularis", "D.mel.Es_Ten", "D.equinoxialis")
```

Function to use to clean the RM output from parenthesis, invert position
in repeat in C strand and add a column with the strain name. Then it
selects only the `gypsy-7-sim1` insertions (spoink).

``` r
read_RM_out <- function(path, strain_name) {
  
  out <- read_delim(path, delim = " ", col_names = c("SWscore", "perc_div", "perc_del", "perc_ins", "query_sequence", "position_in_query_begin", "position_in_query_end", "position_in_query_left",  "strand", "matching_repeat", "repeat_class/family", "position_in_repeat_begin", "position_in_repeat_end", "position_in_repeat_left")) %>% select(-X15) %>% mutate(position_in_repeat_begin = str_replace(position_in_repeat_begin, "\\(", "")) %>% mutate(position_in_repeat_begin = str_replace(position_in_repeat_begin, "\\)", "")) %>% mutate(position_in_repeat_left = str_replace(position_in_repeat_left, "\\(", "")) %>% mutate(position_in_repeat_left = str_replace(position_in_repeat_left, "\\)", "")) %>% mutate(position_in_query_left = str_replace(position_in_query_left, "\\(", "")) %>% mutate(position_in_query_left = str_replace(position_in_query_left, "\\)", "")) %>% mutate(position_in_repeat_end = str_replace(position_in_repeat_end, "\\(", "")) %>% mutate(position_in_repeat_end = str_replace(position_in_repeat_end, "\\)", "")) %>% mutate(position_in_query_begin = str_replace(position_in_query_begin, "\\(", "")) %>% mutate(position_in_query_begin = str_replace(position_in_query_begin, "\\)", "")) %>% mutate(position_in_query_end = str_replace(position_in_query_end, "\\(", "")) %>% mutate(position_in_query_end = str_replace(position_in_query_end, "\\)", "")) %>% type_convert()
  
  out_inverted <- out %>% mutate(backup = ifelse(strand == "C", position_in_repeat_begin, "empty"), position_in_repeat_begin = ifelse(strand == "C", position_in_repeat_left, position_in_repeat_begin), position_in_repeat_left = ifelse(strand == "C", backup, position_in_repeat_left)) %>% select(-backup) %>% mutate(strain = strain_name)
  
  #out_spoink <- out_inverted %>% filter(matching_repeat == "gypsy-7-sim1")
}
```

Apply the function to all the RM output (after removing multiple spaces
with the command above). Then, merge the files in a single tibble.

``` r
# Define the path to the folder containing the files
folder_path <- "/Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/readable"

# Get a list of all files in the folder
file_list <- list.files(path = folder_path, pattern = "*.fa.ori.out", full.names = TRUE)

# Define a function to extract the file name without the extension
get_file_name <- function(file_path) {
  basename <- basename(file_path)
  gsub("\\.fa\\.ori\\.out$", "", basename)
}

RM_list <- c()

for (file_path in file_list) {
  file_name <- get_file_name(file_path)
  RM_data <- read_RM_out(file_path, file_name)
  RM_list[[file_name]] <- RM_data
}
```

    ## Rows: 1171 Columns: 15
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
    ## 
    ## Rows: 1066 Columns: 15
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
    ## 
    ## Rows: 769 Columns: 15
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
    ## 
    ## Rows: 730 Columns: 15
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
    ## 
    ## Rows: 922 Columns: 15
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
    ## 
    ## Rows: 914 Columns: 15
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
    ## 
    ## Rows: 770 Columns: 15
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
    ## 
    ## Rows: 787 Columns: 15
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
    ## 
    ## Rows: 952 Columns: 15
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
    ## 
    ## Rows: 796 Columns: 15
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
    ## 
    ## Rows: 3129 Columns: 15
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
    ## 
    ## Rows: 3020 Columns: 15
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
    ## 
    ## Rows: 1197 Columns: 15
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
    ## 
    ## Rows: 447 Columns: 15
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
    ## 
    ## Rows: 1287 Columns: 15
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
# Combine all data frames into one
RM_merged <- bind_rows(RM_list) %>% 
  select(-"matching_repeat", -"repeat_class/family")
```

This code is cleaning the RM tibble from hits with divergence \> 20%
(following the 80-80-80 rule), selecting high quality hits (SWscore \>
10.000) and the neighboring fragments, then is writing a new tsv file
for each strain with the selected hits.

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

    ## # A tibble: 541 × 17
    ##    SWscore perc_div perc_del perc_ins query_sequence    position_in_query_begin
    ##      <dbl>    <dbl>    <dbl>    <dbl> <chr>                               <dbl>
    ##  1    1243     3.92     3.92     0    JAECWI010000225.1                  148566
    ##  2    5151     4.73     1.66     0.75 JAECWI010000225.1                  148717
    ##  3    8413     2.57     0.4      1.53 JAECWI010000225.1                  149352
    ##  4     645     7.32     0        0    JAECWI010000225.1                  150340
    ##  5    8469     4.79     1.83     0.72 JAECWI010000225.1                  150418
    ##  6    2092     6.71     3.87     0.34 JAECWI010000225.1                  151465
    ##  7     865     2.88     0        0    JAECWI010000243.1                    8290
    ##  8   42048     0.39     0.26     0.04 JAECWI010000243.1                    8346
    ##  9    2734     0.96     0        0    JAECWI010000243.1                   13048
    ## 10    3048     0.87     1.16     0    JAECWI010000243.1                   13314
    ## # ℹ 531 more rows
    ## # ℹ 11 more variables: position_in_query_end <dbl>, strand <chr>,
    ## #   position_in_repeat_begin <dbl>, position_in_repeat_end <dbl>,
    ## #   position_in_repeat_left <chr>, strain <chr>, length <dbl>,
    ## #   distance_from_previous <dbl>, distance_from_next <dbl>, HQ_hits <chr>,
    ## #   insertion_number <dbl>

``` r
insertions_selected <- insertions %>% select(query_sequence, position_in_query_begin, position_in_query_end, strand, position_in_repeat_begin, position_in_repeat_end, strain)

for (s in strains){
  single_strain <- insertions_selected %>% filter(strain==s)
  path <- paste0("/Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/bed/", s, ".tsv")
  write_tsv(single_strain, path)
}
```

Use the python script `insertions2bed.py` on the generated `tsv` files
to ged the defragmented bed files. Arguments of the script:

- input file
- minimum length for an insertion to be included
- maximum length for an insertion to be included
- positions to add at the end of the sequence (if the RM is missing some
  part, usually just use 0)
- output file

<!-- -->

    find /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/bed -name '*.tsv' -type f -exec sh -c 'python /Volumes/EXT-RICCARDO/scripts/insertions2bed.py $0 4500 6000 0 ${0%.tsv}.bed' {} \;

For each bed file, extract the fasta sequence using `bedtools getfasta`
with the `-s` option to get the reverse complement of the insertions on
the **-** strand (the strand info is included in the bed file in the 6th
column).

    for bed_file in /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/bed/*.bed; do
        base_name=$(basename "$bed_file" .bed)
        fasta_file="/Volumes/EXT-RICCARDO/assemblies-Droso/$base_name.fa"    
        output_fasta="/Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/fasta/$base_name.fasta" 
        bedtools getfasta -s -fi "$fasta_file" -bed "$bed_file" -fo "$output_fasta"
    done

    find /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/fasta -name '*.fasta' -type f -exec sh -c 'python /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/rename-insertions.py "$0" "/Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/fasta-renamed/$(basename "$0")"' {} \;

Concatenate the fasta files together.

    cat /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/RM-out/fasta-renamed/*fasta > /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/spoink-insertions-dmel-dwil.fasta

    blastn -query /Volumes/EXT-RICCARDO/Dmel-spoink/consensus/spoink-dmel-consensus.fasta -subject /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/spoink-insertions-dmel-dwil.fasta -outfmt "6 qseqid sseqid pident qlen length mismatch gapopen qstart qend sstart send evalue bitscore" > /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/insertions-blasted.tsv

``` r
(blast <- read_tsv("/Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/insertions-blasted.tsv", col_names = c("consensus","insertion","pid","q_len","ali_len","mismatches","gap_opens","q_start","q_end","s_start","s_end","evalue","bitscore")))
```

    ## Rows: 1204 Columns: 13
    ## ── Column specification ────────────────────────────────────────────────────────
    ## Delimiter: "\t"
    ## chr  (2): consensus, insertion
    ## dbl (11): pid, q_len, ali_len, mismatches, gap_opens, q_start, q_end, s_star...
    ## 
    ## ℹ Use `spec()` to retrieve the full column specification for this data.
    ## ℹ Specify the column types or set `show_col_types = FALSE` to quiet this message.

    ## # A tibble: 1,204 × 13
    ##    consensus insertion   pid q_len ali_len mismatches gap_opens q_start q_end
    ##    <chr>     <chr>     <dbl> <dbl>   <dbl>      <dbl>     <dbl>   <dbl> <dbl>
    ##  1 spoink    DmelSo-10  99.9  5217    5216          2         2       1  5216
    ##  2 spoink    DmelSo-10 100    5217     350          0         0    4868  5217
    ##  3 spoink    DmelSo-10 100    5217     349          0         0       1   349
    ##  4 spoink    DmelSo-10  96.0  5217     151          6         0    4365  4515
    ##  5 spoink    DmelSo-10  96.0  5217     151          6         0    4326  4476
    ##  6 spoink    DmelSo-10  93.8  5217     112          7         0    4404  4515
    ##  7 spoink    DmelSo-10  93.8  5217     112          7         0    4326  4437
    ##  8 spoink    DmelR1-18  99.9  5217    5219          0         4       2  5217
    ##  9 spoink    DmelR1-18 100    5217     349          0         0    4869  5217
    ## 10 spoink    DmelR1-18  99.7  5217     351          0         1       1   350
    ## # ℹ 1,194 more rows
    ## # ℹ 4 more variables: s_start <dbl>, s_end <dbl>, evalue <dbl>, bitscore <dbl>

``` r
(max_hits <- blast %>% group_by(insertion) %>% filter(ali_len==max(ali_len), ali_len>4173, pid>80)) # 4173 is the 80% of the Spoink length
```

    ## # A tibble: 144 × 13
    ## # Groups:   insertion [144]
    ##    consensus insertion   pid q_len ali_len mismatches gap_opens q_start q_end
    ##    <chr>     <chr>     <dbl> <dbl>   <dbl>      <dbl>     <dbl>   <dbl> <dbl>
    ##  1 spoink    DmelSo-10  99.9  5217    5216          2         2       1  5216
    ##  2 spoink    DmelR1-18  99.9  5217    5219          0         4       2  5217
    ##  3 spoink    DmelR7-12  99.9  5217    5217          1         4       2  5217
    ##  4 spoink    DmelSo-2   99.9  5217    5217          4         3       2  5217
    ##  5 spoink    DmelR1-25  99.8  5217    5223          1         4       1  5216
    ##  6 spoink    DmelSo-3   99.8  5217    5218          0         4       2  5217
    ##  7 spoink    DmelSo-1   99.8  5217    5222          3         3       1  5216
    ##  8 spoink    DmelR1-2   99.8  5217    5217          1         6       2  5216
    ##  9 spoink    DmelR7-16  99.8  5217    5220          4         6       2  5217
    ## 10 spoink    DmelR1-19  99.7  5217    5228          0         8       2  5217
    ## # ℹ 134 more rows
    ## # ℹ 4 more variables: s_start <dbl>, s_end <dbl>, evalue <dbl>, bitscore <dbl>

``` r
#selected_insertions <- max_hits %>% select(insertion) %>% write_tsv("/Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/insertions-selected.tsv")

(dmelR2_18 <- max_hits %>% filter(insertion %in% c("DmelR2-18","DmelR7-14","DmelR1-6","DmelR2-15","DmelR1-6")))
```

    ## # A tibble: 4 × 13
    ## # Groups:   insertion [4]
    ##   consensus insertion   pid q_len ali_len mismatches gap_opens q_start q_end
    ##   <chr>     <chr>     <dbl> <dbl>   <dbl>      <dbl>     <dbl>   <dbl> <dbl>
    ## 1 spoink    DmelR2-18  99.4  5217    5238          4        22       2  5217
    ## 2 spoink    DmelR1-6   99.7  5217    4519          4         6       2  4515
    ## 3 spoink    DmelR2-15  99.3  5217    4530          7        15       1  4515
    ## 4 spoink    DmelR7-14  92.6  5217    5303        125       184       1  5216
    ## # ℹ 4 more variables: s_start <dbl>, s_end <dbl>, evalue <dbl>, bitscore <dbl>

Perform multiple sequence alignment using MUSCLE.

    muscle -in /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/spoink-insertions-dmel-dwil.fasta -out /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/spoink-insertions-dmel-dwil.MSA

    muscle -in /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/spoink-insertions-dmel-dwil.MSA -out /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/spoink-insertions-dmel-dwil.phylip -refine -phyi

    http://sequenceconversion.bugaco.com/converter/biology/sequences/fasta_to_nexus.php

    phyml -i /Volumes/EXT-RICCARDO/Dmel-spoink/phylogeny-species/spoink-insertions-dmel-dwil.phylip -d nt -m GTR
