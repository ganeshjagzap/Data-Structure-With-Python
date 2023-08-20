#!/usr/bin/env python
# coding: utf-8

# # Linked list

# In[1]:


class Node:
    def __init__(self,Data=None,Next=None):
        self.Data=Data
        self.Next=Next


# In[2]:


class Linkedlist:
    def __init__(self):
        self.head=None
    def insert_at_beg(self,Data):
        node=Node(Data,self.head)
        self.head=node
        
    def insert_at_last(self,Data):
        if self.head is None:
            self.insert_at_beg(Data)
        else:
            node=Node(Data)
            itr=self.head
            while(itr.Next!=None):
                itr=itr.Next
            itr.Next=node
    def insert_before(self,Data,Key):
        if self.head is None:
            self.insert_at_beg(Data)
        else:
            itr=self.head
            while(itr.Next.Data!=Key):
                itr=itr.Next

            itr.Next=Node(Data,itr.Next)
        
    def insert_after(self,Data,Key):
        if self.head is None:
            self.insert_at_beg(Data)
        else:
            itr=self.head
            while(itr.Data!=Key):
                itr=itr.Next

            itr.Next=Node(Data,itr.Next)  
        
    def delete_node(self,Key):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            itr=self.head
            if(itr.Data==Key):
                self.head=itr.Next
                return
            while(itr.Next.Data!=Key or itr.Next==None):
                if(itr.Next.Next==None):
                    print("this element is not present")
                    return
                
                itr=itr.Next

            itr.Next=itr.Next.Next
            
    def printlist(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr=self.head
        lists=''
        while(itr):
            lists+=str(itr.Data)+"-->"
            itr=itr.Next
        print(lists)
            


# In[3]:


l=Linkedlist()
l.insert_at_beg(5)
l.insert_at_beg(6)
l.insert_at_beg(9)
l.insert_at_last(10)
l.insert_at_last(11)
l.insert_at_last(12)
l.insert_at_beg(3)
l.insert_after(7,6)
l.insert_after(8,6)
l.insert_after(1,6)
l.insert_after(2,6)
l.insert_before(9,10)
l.insert_before(8,10)
l.insert_before(7,10)
l.printlist()


# In[4]:


l.delete_node(10)


# In[5]:


l.printlist()


# In[6]:


l.delete_node(3)
l.printlist()


# In[ ]:





# In[ ]:




