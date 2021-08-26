``` python
text = "The agent's phone number is 408-555-1234. Call soon!"

'phone' in text

import re
pattern = 'phone'
re.search(pattern,text) #it is looking for 'pattern(phone)'' in 'text'
#but we got only error messe
pattern = "NOT IN TEXT"
re.search(pattern,text)
#now this function takes pattern and scan the text, and the returns a Match object...
#If no pattern is found, a **None**
#In Jupyter Notebook, it doenst return.

pattern = 'phone'
match = re.search(pattern,text)
match
#then we can find where the 'text' is in 'pattern' sentence.
#if it had shown more than twice in sentence, then use 'findall'

matches = re.findall("phone", text)

```

