# F String

#### Prob #1

```python
abbr = 'NLP'
full_text = 'Natural Language Processing'
```

##### Enter My code here


```python
print (f'{abbr} stands for {full_text}')

```

##### output

    NLP stands for Natural Language Processing



# Files

##### Prob #2

#### ※ '%%writefile ~~~' neeed to be allocated in first sentence


```python
%%writefile contacts.txt
First_name Last_Name, Title, Extension, Email
```

##### output

    Overwriting contacts.txt



##### Prob #3

##### open the contacts.txt file


```python
my_file=open('contacts.txt')
fields = my_file.read()
my_file.close()
```

# Working with PDF Files
#### Prob #4

## what if PyPDF2 has n't installed yet  then 'pip install PyPDF2'




```python
# Perform import
import PyPDF2
```




```python
# PDF File composed of binary code. so it needs 'rb or wb'
#Open the file as a binary object
f = open('Business_Proposal.pdf','rb')
```




```python
# Use PyPDF2 to read the text of the file
pdf_reader = PyPDF2.PdfFileReader(f)
```

##### ※ Need to addd extract Text at the end


```python
# Get the text from page 2 (CHALLENGE: Do this in one step!)
# I've Missied extractText Function in line..
page_two_text = pdf_reader.getPage(1).extractText()
```




```python
#close the File
f.close()
```




```python
# Print the contents of page_two_text
print(page_two_text)
```

##### output

    AUTHORS:
     
    Amy Baker, Finance Chair, x345, abaker@ourcompany.com
     
    Chris Donaldson, Accounting Dir., x621, cdonaldson@ourcompany.com
     
    Erin Freeman, Sr. VP, x879, efreeman@ourcompany.com


​    
​    


```python
#Problem #5 -1
f= open('Business_Proposal.pdf','rb')
pdf_reader = PyPDF2.PdfFileReader(f)
first_page =pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open("context.txt","wb")
pdf_writer.write(pdf_output)
pdf_output.close()
f.close()
```


```python
#Prob #5-2
  #rCHALLENGE : remove the Word "AUTHORS"
```

# Regular Expression

##### Prob #6


```python
import re
```


```python
# r string , \w 
pattern = r'\w+@\w+.\w{3}'

re.findall(pattern, page_two_text)
```

##### output


    ['abaker@ourcompany.com',
     'cdonaldson@ourcompany.com',
     'efreeman@ourcompany.com']

![image-20210829213743311](C:\Users\count\OneDrive\문서\image-20210829213743311.png)

![image-20210829213821670](C:\Users\count\OneDrive\문서\image-20210829213821670-16302407028611.png)
