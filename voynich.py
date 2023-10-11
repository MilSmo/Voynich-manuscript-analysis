#!/usr/bin/env python
# coding: utf-8

# In[1]:


from matplotlib import pyplot as plt


# In[2]:


import pandas as pd


# In[3]:


def frequency(f):
    frequency_dict = {}

    for word in f:
        if word in frequency_dict:
            count = frequency_dict[word]  
            count += 1
            frequency_dict[word] = count
        else:
            frequency_dict[word] = 1
    most_frequent = dict(sorted(frequency_dict.items(), key=lambda elem: elem[1], reverse=True))
    return most_frequent


# In[4]:


def sherlock_preprocessing(file):
    characters = ['.',',','-','?','«','»',';','–',':']
    file = file.replace('\n', ' ').lower()
    for i in characters:
        file = file.replace(i,'')
    
    return file.split(' ')


# In[5]:


with open('sherlock_holmes.txt', 'r',encoding='utf-8') as content:
    sherlock_string = content.read()


# In[6]:


sherlock_words=sherlock_preprocessing(sherlock_string)


# In[7]:


sherlock_most_frequent=frequency(sherlock_words)


# In[8]:


total =len(sherlock_words)


# In[9]:


headers = ['RANK','ACTUAL FREQUENCY','ZIPF FRAC','ZIPF FREQUENCY']
df_sherlock = pd.DataFrame(columns=headers)
rank = 1
for word, freq in sherlock_most_frequent.items():
    df_sherlock.loc[word] = [rank, freq, freq/total,rank*freq]
    rank+=1


# In[11]:


df_sherlock


# In[13]:


plt.figure(figsize=(10, 5))
plt.plot(df_sherlock['RANK'], df_sherlock['ACTUAL FREQUENCY'])
plt.xlabel('RANK')
plt.ylabel('ACTUAL FREQUENCY')
plt.title('ACTUAL FREQUENCY vs. RANK')
plt.xlim(0, 30) 
plt.show()


# In[14]:


top_30 = dict(list(sherlock_most_frequent.items())[:30])

words = list(top_30.keys())
frequencies = list(top_30.values())

plt.figure(figsize=(20, 20))
plt.ylabel("Frequency")
plt.xlabel("Words")
plt.xticks(rotation=90)

plt.bar(words, frequencies)
plt.show()


# In[15]:


#voynich


# In[16]:


def voynich_preprocessing(txt):
    lines = txt.split("\n")
    lines = [line for line in lines if not line.startswith("#")]
    lines = [line.strip("-=") for line in lines]
    lines = [line for line in lines if line]
    words = []
    for line in lines:
        words.extend(line.split(","))
    words = [word.strip() for word in words]
    words = [word for word in words if word]
    return words


# In[17]:


with open('voynich.txt', 'r',encoding='utf-8') as content:
    voynich_string = content.read()


# In[18]:


voynich_words = voynich_preprocessing(voynich_string)


# In[19]:


print(voynich_words)


# In[20]:


voynich_most_frequent = frequency(voynich_words)


# In[21]:


voynich_most_frequent


# In[22]:


top_30_voynich = dict(list(voynich_most_frequent.items())[:30])

words = list(top_30_voynich.keys())
frequencies = list(top_30_voynich.values())

plt.figure(figsize=(20, 20))
plt.ylabel("Frequency")
plt.xlabel("Words")
plt.xticks(rotation=90)

plt.bar(words, frequencies)
plt.show()


# In[23]:


df_voynich = pd.DataFrame(columns=headers)
rank = 1
for word, freq in voynich_most_frequent.items():
    df_voynich.loc[word] = [rank, freq, freq/total,rank*freq]
    rank+=1


# In[24]:


df_voynich


# In[ ]:




