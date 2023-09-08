import argparse

# Parse command-line arguments
parser = argparse.ArgumentParser(description="")
parser.add_argument("insertions", help="Path to insertions file")
parser.add_argument("min_len", help="Requested minimum length to include a sequence into the output")
parser.add_argument("max_len", help="Requested maximum length to include a sequence into the output")
parser.add_argument("to_add", help="Bases to add at the end of the annotation (eg. to include more bases in the end)")
parser.add_argument("output", help="Path to the output file")
args = parser.parse_args()

def filter(ins, min_len, max_len, to_add,  out):
    query_sequence=""
    strand=""
    strain=""
    sequence = [0,0]
    with open(ins, 'r') as input, open(out, 'w') as output:
        next(input).rstrip().split('\t')
        for line in input:
                cells = line.rstrip().split('\t')
                if query_sequence!=cells[0] or strand!=cells[3] or (int(cells[1])-int(sequence[1])>=100):
                    if (query_sequence!="") and (int(sequence[1])-int(sequence[0])>int(min_len)) and (int(sequence[1])-int(sequence[0])<int(max_len)):
                        sequence[1]=int(sequence[1])+int(to_add)
                        l = int(sequence[1])-int(sequence[0])
                        output.write(str(query_sequence) + "\t" + str(sequence[0]) + "\t" + str(sequence[1]) + "\t" + str(strain) + "\t" + str(0) + "\t" + str(strand) + "\n")
                        #print(str(sequence) + "\t" + str(l))
                    query_sequence = cells[0]
                    strain = cells[6]
                    if cells[3]=="+":
                         strand = cells[3]
                    else:
                         strand = "-"
                    sequence = [cells[1], cells[2]]
                    #print("New sequence: " +str(sequence))
                elif (int(cells[2])>int(sequence[1])) and (int(cells[1])-int(sequence[1])<100):
                    sequence[1]=cells[2]
                    #print(sequence)
                     
filter(args.insertions, args.min_len, args.max_len, args.to_add, args.output)