import nltk
import numpy

def get_names(input):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(input)
    # Perform part-of-speech tagging on the words
    tagged_words = nltk.pos_tag(words)
    # Named entity recognition
    ner = nltk.ne_chunk(tagged_words)

    # Initialize a list to store the extracted names
    names = []
    
    # Loop through the tagged words to find proper nouns (NNP: Proper noun, singular)
    for entity in ner: 
        if isinstance(entity, nltk.tree.Tree) and entity.label()=="PERSON":
            print(entity)
            name = tuple([leaf[0] for leaf in entity])
            if name!=("Title", "Age"):
                names.append(name)
    
    return names

'''
data = "Members of the board\n\
Members of the board    Title   Age     Since\n\
Robyn Denholm\n\
        Chairman        60      14-08-10\n\
Kathleen Wilson-Thompson\n\
        Director/Board Member   66      18-12-26\n\
\n\
Elon Musk\n\
        Founder 52      03-06-30\n\
\n\
James Murdoch\n\
        Director/Board Member   50      17-07-12\n\
\n\
Ira Ehrenpreis\n\
        Director/Board Member   55      07-04-30\n\
\n\
Kimbal Musk\n\
        Director/Board Member   51      04-03-31\n\
\n\
Jeffrey Straubel\n\
        Director/Board Member   48      23-05-15\n\
\n\
Joseph Gebbia\n\
        Director/Board Member   42      22-09-24"

#nltk.download()
names = get_names(data)
print(names)
'''

