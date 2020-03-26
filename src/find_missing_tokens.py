
FILE_NAME = "lexer.py"

def isAllCaps(text):
    return text.isupper()

def main():
    terminals = []
    with open(FILE_NAME, 'r') as f :
        in_tokens = False
        for line in f:
            tokens = line.split()
            terminals = terminals + list(filter(isAllCaps, tokens))

    terminals = list(map(lambda t: "'" + t.replace("'", "").replace(",", "") + "'", terminals))
    terminals = set(terminals)
    print("# All terminals: ")
    print("tokens = (")
    print('    ' + (',\n    '.join(list(map(lambda t: "'" + t.replace("'", "") + "'", terminals)))))
    print(")")

if __name__ == '__main__':
    main()