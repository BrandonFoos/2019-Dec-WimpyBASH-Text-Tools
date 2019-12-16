def sort(args):
    """sort lines of text files"""
    files = args[2:]
    cat_files = []
    for filename in files:
        with open(filename) as doc:
            doc_list = list(doc)
            cat_files += [item.strip() for item in doc_list]
    cat_files.sort()
    print('\n'.join(map(str, cat_files)))

def uniq(args):
    """Report or omit repeated lines"""
    files = args[2:]
    cat_files = []
    uniq_words = []
    for filename in files:
        with open(filename) as doc:
            doc_list = list(doc)
            cat_files += [item.strip() for item in doc_list]
    for word in cat_files:
        if word not in uniq_words:
            uniq_words.append(word)
    print('\n'.join(map(str,uniq_words)))


