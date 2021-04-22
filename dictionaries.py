#!/usr/bin/env python
# coding: utf-8

# In[1]:


num_list = [1, 2, 3, 4]
new_dict = current = {}
for name in num_list:
    current[name] = {}
    current = current[name]
print(new_dict)


# In[2]:


d1 = {'a': 100, 'b': 200}
d2 = {'v': 200, 'w': 300}
d = d1.copy()
d.update(d2)
print(d)


# In[ ]:




