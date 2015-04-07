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


def test_card_abbrev():
    """"""
    abbrev = card.card_abbrev("Ace", "Spades")
    try:
        assert abbrev=="AS"
        return 0
    except AssertionError:
        return 1
    #assertEqual(abbrev, "AS")

