# BillBalance
Balance a bill across a group of people.

Recently, my friends and I went on a ski trip where we'd all split various purchases, such as the Airbnb, food, transportation, and lift tickets, amonst everyone.  The end result was that some people had spent more than others (with some people having spent nothing).  We left the balancing of the bill to one person, who ended up using **Splitwise** to compute the various money transfers between people such that everyone ended up paying the same amount

While her result worked, the number of money transfers wasn't minimized, so I thought I'd try my hand at writing a method to compute various payments that need to be made between people.

Contains:
  - balanceBill.py
    - takes as input a dictionary mapping person names to amount paid 
      i.e. {'Kristian': 25, 'Alissa': 45}
    - returns a nested dictionary mapping person names to amounts owed to friends 
      i.e. {'Kristian: {'Alissa': 10}, 'Alissa': {'Kristian: 0}}
      

Currently, since we're using a dictionary structure, we can't have multiple people with the same name, which can be alleviated by using different identifies (i.e. integers) that then map to individuals.
