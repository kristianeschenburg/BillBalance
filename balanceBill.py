#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 13:53:44 2018

@author: kristianeschenburg
"""

import numpy as np

def settle(paid):
    
    """
    Greedy algorithm to balance a bill between a set of people.
    
    Parameters:
    - - - - -
        paid : dictionary containing how much each person paid as part of a 
                set of transactions
                
        paid dictionary is in form of:
            {'P 1' : $p1,
            'P 2': $p2,
            'P 3': $p3}
            
        where p1, p2, and p3 must be greater than or equal to 0, and paid must
        have at least 2 participants.
        
    """
    
    try:
        assert np.all(np.asarray(paid.values()) >= 0)
    except:
        err = 'All payments must be at least $0.00.'
        raise ValueError(err)
        
    try:
        assert len(paid)>1
    except:
        err = 'Cannot balance single transaction.'
        raise NotImplementedError(err)

    print 'In total, {} was spent.'.format(np.sum(paid.values()))
    print 'Everyone should have paid {}'.format(np.mean(paid.values()))
    
    # how much each person is owed, such that all owed sum to 0
    owed = dict(zip(paid.keys(),np.mean(paid.values)-paid.values))
    
    # initialize nested dictionary keeping track of who pays what to whom
    transfers = {k: {j: 0 for j in paid.keys()} for k in paid.keys()}

    while np.any(np.asarray(np.round(owed.values())) < 0):
        
        # current set of those who are owed money
        thoseOwed = {k: np.abs(owed[k]) for k in owed.keys() if owed[k] < 0}
        # current set of those who owe money
        thoseOwe = {k: owed[k] for k in owed.keys() if owed[k] > 0}
        
        # person with minimum amount owed
        receiver = min(thoseOwed,key=thoseOwed.get)
        # person who has paid minimum amount
        payer = min(thoseOwe,key=thoseOwe.get)

        # payer either pays all of what it owes, or all of what payee is owed
        transfer = min(thoseOwe[payer],thoseOwed[receiver])
        
        # irrelevant, but reports how much each person paid at the end
        # more for QC than anything
        paid[receiver] -= transfer
        paid[payer] += transfer
        
        # keep update owed
        owed[receiver] += transfer
        owed[payer] -= transfer
        
        transfers[payer][receiver] += transfer

    return [paid,owed,transfers]