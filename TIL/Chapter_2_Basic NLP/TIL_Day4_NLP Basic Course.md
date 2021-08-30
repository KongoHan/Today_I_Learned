# NLP Basic Course

##### open the CMD (or Conda CMD)

1. change the directory

  → Basically current location would be System32 in Windows folder. and it might cause some permission issue on project. so we need to change the current directory.

  → write 'cd ..'  and enter (system 32 to Windows)

  → write 'cd ..' and enter (Windows to C:/)

2. install spacy
   write 'conda install -c conda-forge spacy' & hit enter then complete the install.

3. download language library
   write 'python -m spacy download en' enter then download english library in same director

   

# Spacy basics

- Key steps
  1) Loading the language library
  2) Building a pipeline object
  3) Using Tokens
  4) Parts-of-speech Tagging
  5) Understanding Token Attributes

![image-20210831000403031](C:\Users\count\OneDrive\문서\image-20210831000403031.png)

- nlp() function takes automatically raw text data and performs a series of operations to tag, parse, and describe the text data





```python
import spacy
```


```python
nlp = spacy.load('en_core_web_sm')
#libary name is en core web small
```


```python
doc = nlp(u'tesla is looking at buying U.S. startup for $6 million')
```


```python
for token in doc :
    print(token.text, token.pos)  # it describes position information in number
    print(token.text, token.pos_) # it describes poisition informatino in parts of speech
```

    tesla 92
    tesla NOUN
    is 87
    is AUX
    looking 100
    looking VERB
    at 85
    at ADP
    buying 100
    buying VERB
    U.S. 96
    U.S. PROPN
    startup 92
    startup NOUN
    for 85
    for ADP
    46 93
    46 NUM
    million 93
    million NUM



```python
for token in doc :
    print(token.text, token.pos_,token.dep_) # it describes syntatic dependency
#Syntactic dependencies : relation between two words in a sentence with one word being the governor and the other being the dependent of the relation.
```

    tesla NOUN nsubj
    is AUX aux
    looking VERB ROOT
    at ADP prep
    buying VERB pcomp
    U.S. PROPN compound
    startup NOUN dobj
    for ADP prep
    46 NUM compound
    million NUM pobj



```python
nlp.pipeline
```




    [('tok2vec', <spacy.pipeline.tok2vec.Tok2Vec at 0x258d3934cc0>),
     ('tagger', <spacy.pipeline.tagger.Tagger at 0x258d1a7fc20>),
     ('parser', <spacy.pipeline.dep_parser.DependencyParser at 0x258d23cabe0>),
     ('ner', <spacy.pipeline.ner.EntityRecognizer at 0x258d23b9460>),
     ('attribute_ruler',
      <spacy.pipeline.attributeruler.AttributeRuler at 0x258d37b9e40>),
     ('lemmatizer', <spacy.lang.en.lemmatizer.EnglishLemmatizer at 0x258d39a9e00>)]




```python
nlp.pipe_names
```




    ['tok2vec', 'tagger', 'parser', 'ner', 'attribute_ruler', 'lemmatizer']


