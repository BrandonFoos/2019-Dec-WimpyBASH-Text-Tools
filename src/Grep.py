def grep(args):
    """print lines that match patterns"""
    search_for = args[2]
    files = args[3:]
    match = True 
    if args[2] == '-v':
        search_for = args[3]
        files = args[4:]
        match = False
    for filename in files:
        with open(filename) as doc:
            for line in doc:
                line = line.rstrip('\n')
                if search_for not in line and not match or search_for in line and match:
                    print(line)
