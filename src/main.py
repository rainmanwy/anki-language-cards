import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate language learning apkg for anki')
    parser.add_argument('-f', '--word-list-file', dest='wordFile', help='word list file')
    parser.add_argument('-t', '--translator', dest='translator', help='Online dict, support "iciba"')
    args = parser.parse_args()
    if not args.wordFile:
        raise RuntimeError('Please input the file of word list')
    if not args.translator:
        raise RuntimeError('Please input translator name')

if __name__ == '__main__':
    main()