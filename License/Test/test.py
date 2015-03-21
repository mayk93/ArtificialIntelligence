import nltk
import re
import time

exampleArray = ["The incredibly intimidating NLP scares people away who are sissies."]

"""
RegEx:
? : 0 or 1 repetitions
* : 0 or more repetitions
+ : 1 ore more repetitions
. : any character except for noow line
\w: any letter
"""

contentArray =['Starbucks is doing very well lately.',
               'Overall, while it may seem there is already a Starbucks on every corner, Starbucks still has a lot of room to grow.',
               'They just began expansion into food products, which has been going quite well so far for them.',
               'I can attest that my own expenditure when going to Starbucks has increased, in lieu of these food products.',
               'Starbucks is also indeed expanding their number of stores as well.',
               'Starbucks still sees strong sales growth here in the united states, and intends to actually continue increasing this.',
               'Starbucks also has one of the more successful loyalty programs, which accounts for 30%  of all transactions being loyalty-program-based.',
               'As if news could not get any more positive for the company, Brazilian weather has become ideal for producing coffee beans.',
               'Brazil is the world\'s #1 coffee producer, the source of about 1/3rd of the entire world\'s supply!',
               'Given the dry weather, coffee farmers have amped up production, to take as much of an advantage as possible with the dry weather.',
               'Increase in supply... well you know the rules...',]

def processLanguage():
    try:
         for item in exampleArray:
             tokenized = nltk.word_tokenize(item)
             tagged = nltk.pos_tag(tokenized) #Pos as in part of speech
             print(tagged)

             # Here, I'm telling it I want an adverb (RB)
             # but I also accept adverb subtypes,
             # RB\w? means RB followed by none or one letter
             chunkGram = r"""Chunk: {<RB\w?>*<VB\w?>*<NNP>}""" #Regex care grupeaza pe POS-uri

             chunkParser = nltk.RegexpParser(chunkGram)

             chunked = chunkParser.parse(tagged)

             print(chunked)

             chunked.draw()

    except Exception as e:
        print(str(e))

processLanguage()
