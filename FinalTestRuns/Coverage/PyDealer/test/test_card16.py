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




def test_card_name():
    """"""
    name = pydealer.card.card_name("Ace", "Spades")
    try:
        assert name=="Ace of Spades"
        return 0
    except AssertionError:
        return 1
##    self.assertEqual(name, "Ace of Spades")
##card = pydealer.Card("Ace", "Spades")
