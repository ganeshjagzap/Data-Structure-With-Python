#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Hash_Map:
    def __init__(self,map_len):
        self.map_len=map_len
        self.arr=[None for i in range(map_len)]
    
    def hashfunc(self,key):
        return key%10
    
    def __setitem__(self,key,val):
        hashval=self.hashfunc(key)
        self.arr[hashval]=val
    
    def __getitem__(self,key):
        hashval=self.hashfunc(key)
        return self.arr[hashval]
    def __delitem__(self,key):
        hashval=self.hashfunc(key)
        self.arr[hashval]=None
        


# In[2]:


hashmap=Hash_Map(10)
hashmap[101]='Ganesh'
hashmap[120]='Prathamesh'
hashmap[107]='mohit'
hashmap[129]='mukesh'
hashmap[120]='Patil'


# In[3]:


hashmap[101]


# In[4]:


hashmap.arr


# # linear probing in hashing

# In[5]:


class Hash_Map:
    def __init__(self,map_len):
        self.map_len=map_len
        self.arr=[None for i in range(map_len)]
    
    def hashfunc(self,key):
        return key%10
    
    def check_vaccunt_place(self,hashval):
        start=hashval
        end=len(self.arr)
        count=0
        while(True):            
            if(start>=end):
                if(count>=len(self.arr)):
                    print("all positions are fill")
                    return
                end=hashval
                start=0
            
            elif(self.arr[start]==None):
                return start
            else:
                start+=1
                count+=1
                
    def __setitem__(self,key,val):
        hashval=self.hashfunc(key)
        pos=self.check_vaccunt_place(hashval)
        if(pos==None):
            return
        self.arr[pos]=val
    
    def __getitem__(self,key):
        hashval=self.hashfunc(key)
        return self.arr[hashval]
    def __delitem__(self,key):
        hashval=self.hashfunc(key)
        self.arr[hashval]=None
        


# In[6]:


hashmap=Hash_Map(10)
hashmap[101]='Ganesh'
hashmap[120]='Prathamesh'
hashmap[107]='mohit'
hashmap[129]='mukesh'
hashmap[120]='Patil'
hashmap[111]='Mangesh'
hashmap[189]='krishna'
hashmap[119]='pratik'
hashmap[189]='krishna'
hashmap[119]='pratik'
hashmap[189]='krishna'
hashmap[119]='pratik'


# In[7]:


hashmap.arr


# # Chaning

# In[88]:


class Hash_Map:
    def __init__(self,map_len):
        self.map_len=map_len
        self.arr=[[] for i in range(map_len)]
    
    def hashfunc(self,key):
        return key%10
    
    def check_vaccunt_place(self,hashval,key):
        for ind,keyval in enumerate(self.arr[hashval]):
            if(key in keyval):
                print("This key is already there",key)
                return 1
        return 0
    def update(self,key,val):
        hashval=self.hashfunc(key)
        for ind,keyval in enumerate(self.arr[hashval]):
            if(key in keyval):
                self.arr[hashval][ind]=(key,val)
                return
        else:
            print("key is not present")
        
    
    def __setitem__(self,key,val):
        hashval=self.hashfunc(key)
        check_val=self.check_vaccunt_place(hashval,key)
        if(check_val==0):
            self.arr[hashval].append((key,val))
    
    def __getitem__(self,key):
        hashval=self.hashfunc(key)
        return self.arr[hashval]
    def __delitem__(self,key):
        hashval=self.hashfunc(key)
        self.arr[hashval]=None
        


# In[89]:


hashmap=Hash_Map(10)
hashmap[101]='Ganesh'
hashmap[120]='Prathamesh'
hashmap[107]='mohit'
hashmap[129]='mukesh'
hashmap[120]='Patil'
hashmap[111]='Mangesh'
hashmap[189]='krishna'
hashmap[119]='pratik'
hashmap[189]='krishna'
hashmap[119]='pratik'
hashmap[189]='krishna'
hashmap[119]='pratik'
hashmap[101]='Ganesh'
hashmap[120]='Prathamesh'
hashmap[101]='Ganesh'
hashmap[120]='Prathamesh'
hashmap[101]='Ganesh'
hashmap[120]='Prathamesh'
hashmap[101]='Ganesh'
hashmap[120]='Prathamesh'


# In[90]:


for i in hashmap.arr:
    print(i)


# In[93]:


hashmap.update(144,'mangesh')


# In[94]:


hashmap.arr


# In[ ]:




