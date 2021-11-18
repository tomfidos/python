#!/usr/bin/env python
# coding: utf-8

# In[28]:


"""
Code for a script that gets publications data from a source csv, drop unneeded columns,
transform data so as it can be manipulated and create a dataframe with unique authors.
"""


# In[29]:


import pandas as pd


# In[30]:


def get_list_last_elements(name_list):
    if len(name_list) == 2:
        return name_list[1]
    # If an author has got a middle name a condition == 3 would be sufficient.
    # However, in case he's got a surname consiting of two names (like happens in Spanish-speaking
    # countries) use a condition > 2 and a right-opened index.
    elif len(name_list) > 2:
        return " ".join(name_list[2:])
    # The below shouldn't happen unless there's no author provided at all or with just one name.
    # For the needs of this MVP return an empty string to avoid breaking the code later on.
    else:
        return ""


# In[31]:


# Convert to Series while import the data as we operate on one column anyway
authors_per_publication = pd.read_csv("publications_min.csv", usecols=["authors"], squeeze=True)


# In[32]:


# Make sure there're no number typed values
authors_wo_digits = authors_per_publication.astype(str)
# Convert list strings to real lists
authors_destringified = authors_wo_digits.apply(lambda x: x.strip("][").split(", "))
# Get all names from the lists
all_authors = authors_destringified.explode()


# In[33]:


# Normalize name -> all to lower case
all_authors.str.lower()
# Convert strings to lists again so as we can put middle names aside in a separate Series variable.
all_authors_names = all_authors.apply(lambda x: x[1:-1].split(" "))
# Also get a separate Series for first & last names.
# For this MVP we leave middle names out of consideration.
first_names = all_authors_names.apply(lambda x: x[0])
last_names = all_authors_names.apply(get_list_last_elements)


# In[34]:


# Convert both Series to a dataframe and deduplicate it per last names.
first_last_names_df = pd.concat([first_names, last_names], axis=1, ignore_index=True)
first_last_names_df.rename(columns={0: "firstname", 1: "lastname"}, inplace=True)
unique_authors = first_last_names_df.drop_duplicates()
unique_authors = unique_authors.reset_index(drop=True)


# In[35]:


unique_authors.to_csv("unique_people.csv", index=False)

