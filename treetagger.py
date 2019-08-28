import treetaggerwrapper as ttw

def main():
    tagger = ttw.TreeTagger(TAGLANG='en')
    tags = tagger.TagText('I have a pen.')
    print(tags)

if __name__ == '__main__':
    main()