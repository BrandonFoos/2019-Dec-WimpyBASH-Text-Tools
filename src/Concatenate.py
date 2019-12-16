def cat(args):
    """concatenate files and print on the standard output"""
    
    for i in range(len(args)-2):
            with open(args[i+2]) as doc:
                for line in doc:
                    print(line.rstrip('\n'))
            doc.close()

def tac(args):
    """concatenate and print files in reverse"""
 
    for i in range(len(args)-2):
            with open(args[i+2]) as doc:
                for line in reversed(list(doc)):
                    print(line.rstrip('\n'))
            doc.close()


