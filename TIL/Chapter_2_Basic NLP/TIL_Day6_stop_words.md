# Stop words

'a', 'the' which appear so frequently are not required as much as they were in sentence.

we call these stop words, and we are going to filter from the text.

SpaCy holds a built in list of some 305 English stop words.



```python
import spacy nlp = spacy.load('en_core_web_sm')</div>
Perform standard imports:import spacynlp = spacy.load('en_core_web_sm')
# Print the set of spaCy's default stop words (remember that sets are unordered):
print(nlp.Defaults.stop_words)
```

### Output

## how many stop words were holding in SpaCy.

```python
{'hers', 'show', 'though', 'various', 'sixty', 'say', 'quite', 'ten', 'anything', 'although', 'hereby', 'in', 'ours', 'herself', 'among', 'unless', 'and', 'whole', 'anywhere', 'latter', 'therein', 'whereafter', 'that', 'one', 'whose', 'either', 'within', 'eight', 'three', 'latterly', 'anyone', 'a', 'less', 'former', 'been', 'same', 'anyway', 'else', 'cannot', 'five', 'i', 'until', 'last', 'thus', 'give', 'move', 'thereafter', 'via', 'than', 'empty', 'off', 'neither', 'too', 'please', 'over', 'just', 'otherwise', 'has', 'her', 'put', 'its', 'whether', 'herein', 'myself', 'me', 'nevertheless', 'whatever', 'someone', 'towards', 'whereby', 'onto', 'sometimes', 'thence', 'them', 'done', 'at', 'back', 'nor', 'another', 'behind', 'together', 'take', 'amongst', 'being', 'seemed', 'seeming', 'fifteen', 'do', 'further', 'something', 'again', 'this', 'were', 'wherein', 'how', 'up', 'must', 'get', 'whereas', 'much', 'upon', 'yet', 'both', 'many', 'very', 'may', 'after', 'regarding', 'full', 'through', 'below', 'his', 'well', 'everything', 'so', 'our', 'should', 'seem', 'while', 'for', 'might', 'mine', 'when', 'with', 'you', 'few', 'never', 'because', 'own', 'also', 'due', 'hence', 'it', 'more', 'their', 'such', 'becomes', 'first', 'hereupon', 'since', 'third', 'twenty', 'who', 'she', 'nobody', 'name', 'really', 'enough', 'least', 'two', 'whoever', 'which', 'yours', 'moreover', 'seems', 'before', 'therefore', 'then', 'used', 'even', 'nowhere', 'without', 'other', 'around', 'made', 'hundred', 'no', 'twelve', 'several', 'your', 'meanwhile', 'per', 'except', 'yourselves', 'why', 'some', 'not', 'yourself', 'sometime', 'somehow', 'become', 'beyond', 'almost', 'will', 'somewhere', 'the', 'everyone', 'about', 'everywhere', 'anyhow', 'side', 'next', 'fifty', 'they', 'most', 'perhaps', 'across', 'themselves', 'besides', 'against', 'can', 'him', 'there', 'noone', 'under', 'formerly', 'already', 'all', 'if', 'my', 'or', 'serious', 'four', 'thereupon', 'whence', 'here', 'whither', 'beside', 'wherever', 'to', 'himself', 'between', 'ourselves', 'none', 'on', 'became', 'an', 'have', 'part', 'did', 'had', 'each', 'six', 'those', 'from', 'whenever', 'any', 'am', 'would', 'make', 'could', 'does', 'go', 'call', 'indeed', 'these', 'often', 'above', 'during', 'by', 'nine', 'thereby', 'others', 'afterwards', 'throughout', 'whom', 'amount', 'as', 'hereafter', 'top', 'mostly', 'us', 'whereupon', 'once', 'only', 'still', 'namely', 'forty', 'ca', 'along', 'be', 'itself', 'where', 'see', 'into', 'toward', 'but', 'is', 'keep', 'bottom', 'ever', 'becoming', 'every', 'always', 'front', 'nothing', 'we', 'of', 'out', 'eleven', 'alone', 'he', 'however', 'rather', 'down', 'thru', 'now', 'using', 'are', 'doing', 'what', 'beforehand', 're', 'was', 'elsewhere'}
```

### To see if a word is in 'Stop word List'

there are so many words in 'stop word list'.

so, need to see (or check) whether what i choose is in list or not.

```python
nlp.vocab['myself'].is_stop #then it shows 'True'
nlp.vocab['mystery'].is_stop #then it shows 'False'
```

### To add a word in 'Stop word List'

```python
nlp.Defaults.stop_words.add('btw') #add the word 'btw' in stop word list. and care of  and lower case. always lowercase. Lexemes are converrted to lowercase before being added to vocab.

nlp.vocab['btw'].is_stop = True #Set the stop word tag on the lexeme, 'btw'
```

### To remove a word in 'Stop word List'

```python
nlp.Default.stop_words.remove('beyond')

nlp.vocab['beyond'].is_stop = False # set the word as a False case.

```

