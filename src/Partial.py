def head(args):
    """output the first part of files"""
    num_to_print = 10
    files = args[2:]
    if args[2] == '-n':
        num_to_print = int(args[3])
        files = args[4:]
    for filename in files:
        with open(filename) as doc:
            for i in range(num_to_print):
                print(doc.readline().rstrip())
        doc.close()

def tail(args):
    """output the last part of files"""
    num_to_print = 10
    files = args[2:]
    if args[2] == '-n':
        num_to_print = int(args[3])
        files = args[4:]
    for filename in files:
        with open(filename) as doc:
            doc_list = list(doc)
            if len(doc_list) < num_to_print:
                for line in doc_list:
                    print(line.rstrip())
            else:
                for i in range(num_to_print):
                    print(doc_list[(num_to_print-i)*-1].rstrip())
        doc.close()
