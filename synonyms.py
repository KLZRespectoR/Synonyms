#!/usr/bin/env python
# coding: utf-8

# # Steps for getting a Lemmas, Synonyms, Antonyms from Wordnet Corpus:

# In[1]:

from nltk.corpus import wordnet
example= wordnet.synsets('cold')
print(example)


# to choose a specific word from the Synsets above:

# In[2]:


print(example[3])


# to make this specific synset as a base for further implications:

# In[3]:


woc= example[3]


# some fuctions and shortcuts:

# In[4]:


woc.pos()


# In[5]:


woc.definition()


# In[6]:


woc.lemmas()


# to remove the big brackts:

# In[7]:


woc.lemmas()[0]


# # Synonyms:

# we use for loops: firstly, we create an area

# In[8]:


synexample= []
antexample= []


# In[9]:


for syn in example:
    for lem in syn.lemmas():
        synexample.append(lem.name())


# In[10]:


synexample


# to remove any repetation use:

# In[11]:


set(synexample)


# to check the length of all synonyms use:

# In[12]:


len(synexample)


# to check the length of the synonyms without repetations, use:

# In[13]:


len(set(synexample))


# # Antonyms:

# In[14]:


woc.lemmas()


# In[15]:


woc.lemmas()[0]


# In[16]:


woc.lemmas()[0].antonyms()


# In[17]:


woc.lemmas()[0].antonyms()[0]


# In[18]:


woc.lemmas()[0].antonyms()[0].name()


# In[19]:


for syn in example:
    for lem in syn.lemmas():
        for ant in lem.antonyms():
            antexample.append(ant.name())


# In[20]:


antexample


# use the same shortcuts to delete repetations and to check the length of the antonyms and the group without repetations
