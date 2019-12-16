def cut(args):
    """remove sections from each line of files"""
    try:
        col = [0]
        csv_filenames = args[2:]
        has_col = False  
        if args[2] == "-f":
            col = args[3].split(',')
            csv_filenames = args[4:]
            has_col = True
            
        for filename in csv_filenames:
            temp_csv = readCSV(filename)
            for row in temp_csv:
                if has_col:
                    for i in col:
                        try:
                            print(row[int(i)-1],end='')
                        except:
                            pass
                        if i != col[len(col)-1]:
                            print(',', end = '')
                    print()
                else:
                    print(row[int(col[0])])
    except:
        exit(0)

def paste(args):
    """merge lines of files"""
    files = args[2:]
    text_list = []
    for filename in files:
        file_text = []
        with open(filename) as doc:
            for line in doc:
                file_text += line.rstrip('\n').split('\n')
        text_list.append(file_text)
    width = len(text_list)            
    height = 0
    for line in text_list:
        if len(line) > height:
            height = len(line)
    for i in range(height):
        for j in range(width):
            try:
                print(text_list[j][i],end='')
            except:
                pass
            if j < width-1:
                print(',',end='')
        print()

def getLength(doc):
    size = 0
    for line in doc:
        print(size)
        size += 1
    return size

def readCSV(filename):
    csvList = []
    with open(filename) as doc:
        for line in doc:
            csvList.append(line.rstrip('\n').split(","));
    doc.close()

    return csvList
