#Libraries
import nltk
import re
import time

#Explanations
"""
RegEx:
? : 0 or 1 repetitions
* : 0 or more repetitions
+ : 1 ore more repetitions
. : any character except for new line
\w: any letter
| : or
Chunk:
A regex that groups by part of speech.

<RB\w?>*<VB\w?>*<NNP>
Here, I am saying I want an adverb, the RB.
However, I also accept adverb subtypes (RBR,RBS), hence RB\w?.
The regex RB\w? means RB followed by none or one letter.
The same for VB ( verb ) and NNP (singular proper noun)

{<.*>}
}<RB|NNS>{
This will chunk everything (.*), then remove
every adverb and plural noun.

namedEnt = nltk.ne_chunk(tagged,binary=True)
In recognizing named entities, the parameter "binary=True" means:
The binary flag is set to True to indicate only whether a subtree is NE or not.
When set to False it will give more information
like whether the NE is an Organization, Person etc.
See: http://stackoverflow.com/questions/26862970/nltk-ner-word-extraction
"""

#Assets
exampleArray = ["The incredibly intimidating NLP scares people away who are sissies."]
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

#Methods
def processLanguage():
    try:
         for item in exampleArray:
             tokenized = nltk.word_tokenize(item)
             tagged = nltk.pos_tag(tokenized)

             namedEnt = nltk.ne_chunk(tagged,binary=True)
             namedEnt.draw()

    except Exception as e:
        print(str(e))

#Main
def main():
    processLanguage()

if __name__=="__main__":
    main()
