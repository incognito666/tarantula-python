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
#import src.*


#===============================================================================
# TestCard Class
#===============================================================================

##class TestCard(unittest.TestCase):

def setUp():
    """"""
    card = pydealer.Card("Ace", "Spades")
    return 0

def test_card_abbrev():
    """"""
    abbrev = card.card_abbrev("Ace", "Spades")
    try:
        assert abbrev=="AS"
        return 0
    except AssertionError:
        return 1
    #assertEqual(abbrev, "AS")

##def test_card_name(self):
##    """"""
##    name = pydealer.card.card_name("Ace", "Spades")
##
##    self.assertEqual(name, "Ace of Spades")
##
##def test_value(self):
##    """"""
##    self.assertEqual(self.card.value, "Ace")
##
##def test_suit(self):
##    """"""
##    self.assertEqual(self.card.suit, "Spades")
##
##def test_abbrev(self):
##    """"""
##    self.assertEqual(self.card.abbrev, "AS")
##
##def test_name(self):
##    """"""
##    self.assertEqual(self.card.name, "Ace of Spades")
##
##def test_eq(self):
##    """"""
##    ace_spades = pydealer.Card("Ace", "Spades")
##
##    self.assertEqual(self.card, ace_spades)
##
##def test_eq_func(self):
##    """"""
##    ace_spades = pydealer.Card("Ace", "Spades")
##
##    result = self.card.eq(ace_spades)
##
##    self.assertTrue(result)
##
##def test_ge(self):
##    """"""
##    ace_spades = pydealer.Card("Ace", "Spades")
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    self.assertGreaterEqual(self.card, ace_spades)
##    self.assertGreaterEqual(self.card, two_diamonds)
##
##def test_ge_func(self):
##    """"""
##    ace_spades = pydealer.Card("Ace", "Spades")
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    result_x = self.card.ge(ace_spades)
##    result_y = self.card.ge(two_diamonds)
##
##    self.assertTrue(result_x)
##    self.assertTrue(result_y)
##
##def test_gt(self):
##    """"""
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    self.assertGreater(self.card, two_diamonds)
##
##def test_gt_func(self):
##    """"""
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    result = self.card.gt(two_diamonds)
##
##    self.assertTrue(result)
##
##def test_le(self):
##    """"""
##    ace_spades = pydealer.Card("Ace", "Spades")
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    self.assertLessEqual(self.card, ace_spades)
##    self.assertLessEqual(two_diamonds, ace_spades)
##
##def test_le_func(self):
##    """"""
##    ace_spades = pydealer.Card("Ace", "Spades")
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    result_x = self.card.le(ace_spades)
##    result_y = self.card.le(two_diamonds)
##
##    self.assertTrue(result_x)
##    self.assertFalse(result_y)
##
##def test_lt(self):
##    """"""
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    self.assertLess(two_diamonds, self.card)
##
##def test_lt_func(self):
##    """"""
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    result = self.card.lt(two_diamonds)
##
##    self.assertFalse(result)
##
##def test_ne(self):
##    """"""
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    self.assertNotEqual(self.card, two_diamonds)
##
##def test_ne_func(self):
##    """"""
##    two_diamonds = pydealer.Card("2", "Diamonds")
##
##    result = self.card.ne(two_diamonds)
##
##    self.assertTrue(result)
##
