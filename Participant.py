#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 12:56:28 2018

@author: kristianeschenburg
"""

class Participant(object):
    
    """
    Class to generate a participant in a set of transactions.
    
    Parameters:
    - - - - -
        name : who is this person
        paid : how much this person paid
        owes : how much this person owes
    """
    
    def __init__(self,name,paid=0,owes=0):
        
        self.name = name
        self.paid = paid
        self.owes = owes
        
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def paid(self):
        return self.__paid
    
    @paid.setter
    def paid(self,paid):
        self.__paid = paid
        
    @property
    def owes(self):
        return self.__owes
    
    @owes.setter
    def owes(self,owes):
        self.__owes = owes
        
    def update(self,amount):
        
        """
        Method to update the amount Participant owes and has paid.
        """
        
        self.owes -= amount
        self.paid += amount
        
    def pay(self,recipient,amount):
        
        """
        Method to pay money to another Participant.
        """
        
        recipient.update(-amount)
        self.update(amount)