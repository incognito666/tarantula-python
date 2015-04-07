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




def test_eq():
    """"""
    ace_spades = pydealer.Card("Ace", "Spades")
    try:
        assert card==ace_spades
##        unittest.TestCase.assertEqual(card,ace_spades,None)
        return 0
    except AssertionError:
        return 1
##    self.assertEqual(self.card, ace_spades)

##def test_eq_func():
##    """"""
##    ace_spades = pydealer.Card("Ace", "Spades")
##
##    result = card.eq(ace_spades)
##    try:
##        assert result==True
##        return 0
##    except AssertionError:
##        return 1
##    self.assertTrue(result)
##
