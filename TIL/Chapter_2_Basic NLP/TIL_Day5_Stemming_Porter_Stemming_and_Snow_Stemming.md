

# Stemming

in case, searing for 'boat' might return 'boats' & 'boating'.

so that, "boat" would be the stem for [boat, boater, boating, boats]


# Natural Language Toolkit (NLTK)

→  more information on nltk (https://www.nltk.org/)



# Porter's algorithm



#### Porter Stem-mer



Common and effective tool

Developed by Martin Porter in 1980

five phases of word reduction, each with its own set of mapping rules.



#### simple suffix mapping rules are defined.

such as :

![image-20210906100245653](C:\Users\count\OneDrive\문서\image-20210906100245653-16308901701141.png)

![image-20210906101835604](C:\Users\count\OneDrive\문서\image-20210906101835604-16308911167832.png)

'm>0' describes the 'measurement' of the stem.







#### Snowball stem-mer

so called, "English Stemmer" or "Porter2 Stemmer".

 slight improvement over the original Porter stemmer, both in logic and speed.

```python
from nltk.stem.snowball import SnowballStemmer

## The Snowball Stemmer requires that you pass a language parameter
s_stemmer = SnowballStemmer(language='english')

words = ['run','runner','running','ran','runs','easily','fairly']
#### words = ['generous','generation','generously','generate']

for word in words:
    print(word+' --> '+s_stemmer.stem(word))
run --> run
runner --> runner
running --> run
ran --> ran
runs --> run
easily --> easili
fairly --> fair
```

#### output

```python
run --> run
runner --> runner
running --> run
ran --> ran
runs --> run
easily --> easili
fairly --> fair
# in the case the stemmer performed the same as the Porter stemmer, but it goes to more appropriately. (like farily to fair)
```



# Drawback in Snowball 

if i set word which has '-es' in original form, or it has some variety in different form like 'Saw'.

then it couldn't find original form (lemmatization)

#### 

```python
import nltk
from nltk.stem.snowball import SnowballStemmer
words = ['tasteful','tasty','tastable','tastes','tasted','tasting'] #its original form is 'taste'
s_stemmer = SnowballStemmer(language='english') # set the linguistic base as an english
for word in words :
    print(word + ' --> '+ s_stemmer.stem(word))
```



#### Output

```python
##it has shown fairly disrupped outputs in the end.
tasteful --> tast
tasty --> tasti
tastable --> tastabl
tastes --> tast
tasted --> tast
tasting --> tast
```



##### Example #2

```python
phrase = 'I am meeting him tomorrow at the meeting'
for word in phrase.split():
    print(word+' --> '+p_stemmer.stem(word))
```

word 'meeting' appears twice, once as a verb, and once as a noun. but stemmer treats both equally

