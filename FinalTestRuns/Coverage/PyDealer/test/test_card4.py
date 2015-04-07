#===============================================================================
# PyDealer - Tests - Card
#-------------------------------------------------------------------------------
# Version: 1.4.0
# Updated: 10-01-2015
# Author: Alex Crawford
# License: GPLv3
#===============================================================================

#===============================================================================
# Imports
#===============================================================================
import os
import sys
import unittest
p = os.path.join(os.getcwd(),'src')
sys.path.insert(0,p)
import card

import pydealer
from card import *
#import src.*


#===============================================================================
# TestCard Class
#===============================================================================

##class TestCard(unittest.TestCase):
##card = pydealer.Card("Ace", "Spades")



def test_lt():
    """"""
    card = pydealer.Card("Ace", "Spades")
    two_diamonds = pydealer.Card("2", "Diamonds")
    try:
##        assert card>=ace_spades
        assert two_diamonds<card
        return 0
    except AssertionError:
        return 1
##    self.assertLess(two_diamonds, self.card)



