def wc(files):
    """print newline, word, and byte counts for each file"""
    files = files[2:]
   
    for filename in files:
        with open(filename) as doc:
            doc_duplicate = doc
            doc_words = doc.read()
            doc_list = list(doc_words.split('\n'))
            newline = len(doc_list)-1
            word = len(doc_words.rstrip('\n').split())
            byte_c = len(doc_words.encode('utf-8'))
            print(f"{newline}\t{word}\t{byte_c}\t{filename}")
   
   
