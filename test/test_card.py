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
def test_value():
    """"""
    card = pydealer.Card("Ace", "Spades")
    try:
        
        assert card.value=="Ace"
        return 0
    except AssertionError:
        return 1
##    self.assertEqual(self.card.value, "Ace")

def test_suit():
    """"""
    card = pydealer.Card("Ace", "Spades")
    try:
        assert card.suit=="Spades"
        return 0
    except AssertionError:
        return 1
##    self.assertEqual(self.card.suit, "Spades")

def test_abbrev():
    """"""
    card = pydealer.Card("Ace", "Spades")
    try:
        
        assert card.abbrev=="AS"
        return 0
    except AssertionError:
        return 1
##    self.assertEqual(card.abbrev, "AS")

def test_name():
    """"""
    try:
        card = pydealer.Card("Ace", "Spades")
        assert card.name=="Ace of Spades"
        return 0
    except AssertionError:
        return 1
##    self.assertEqual(self.card.name, "Ace of Spades")

def test_eq():
    """"""
    ace_spades = pydealer.Card("Ace", "Spades")
    try:
        assert card==ace_spades
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
def test_ge():
    """"""
    ace_spades = pydealer.Card("Ace", "Spades")
    two_diamonds = pydealer.Card("2", "Diamonds")

    try:
        assert card>=ace_spades
        assert card>=two_diamonds
        return 0
    except AssertionError:
        return 1
##    self.assertGreaterEqual(self.card, ace_spades)
##    self.assertGreaterEqual(self.card, two_diamonds)

def test_ge_func():
    """"""
    ace_spades = pydealer.Card("Ace", "Spades")
    two_diamonds = pydealer.Card("2", "Diamonds")

    result_x = card.Card.ge(ace_spades)
    result_y = card.Card.ge(two_diamonds)
    try:
        assert result_x==True
        assert result_y==True
        return 0
    except AssertionError:
        return 1
##    assertTrue(result_x)
##    assertTrue(result_y)

def test_gt():
    """"""
    two_diamonds = pydealer.Card("2", "Diamonds")
    try:
        assert card>two_diamonds
        return 0
    except AssertionError:
        return 1
##    self.assertGreater(self.card, two_diamonds)

def test_gt_func():
    """"""
    two_diamonds = pydealer.Card("2", "Diamonds")

    result = card.gt(two_diamonds)
    try:
        assert result==True
        return 0
    except AssertionError:
        return 1
##    self.assertTrue(result)

def test_le():
    """"""
    ace_spades = pydealer.Card("Ace", "Spades")
    two_diamonds = pydealer.Card("2", "Diamonds")
    try:
        assert card<=ace_spades
        assert card<=two_diamonds
        return 0
    except AssertionError:
        return 1
##    self.assertLessEqual(self.card, ace_spades)
##    self.assertLessEqual(two_diamonds, ace_spades)

def test_le_func():
    """"""
    ace_spades = pydealer.Card("Ace", "Spades")
    two_diamonds = pydealer.Card("2", "Diamonds")

    result_x = card.le(ace_spades)
    result_y = card.le(two_diamonds)
    try:
        assert result_x==True
        assert result_y==False
        return 0
    except AssertionError:
        return 1
##    self.assertTrue(result_x)
##    self.assertFalse(result_y)

def test_lt():
    """"""
    two_diamonds = pydealer.Card("2", "Diamonds")
    try:
##        assert card>=ace_spades
        assert two_diamonds<card
        return 0
    except AssertionError:
        return 1
##    self.assertLess(two_diamonds, self.card)

def test_lt_func():
    """"""
    two_diamonds = pydealer.Card("2", "Diamonds")

    result = card.lt(two_diamonds)
    try:
        assert result==False
        return 0
    except AssertionError:
        return 1
##    self.assertFalse(result)

def test_ne():
    """"""
    two_diamonds = pydealer.Card("2", "Diamonds")
    try:
##        assert card=ace_spades
        assert card!=two_diamonds
        return 0
    except AssertionError:
        return 1
##    self.assertNotEqual(self.card, two_diamonds)

def test_ne_func(self):
    """"""
    two_diamonds = pydealer.Card("2", "Diamonds")

    result = card.ne(two_diamonds)
    try:
        assert result==True
        return 0
    except AssertionError:
        return 1
##    self.assertTrue(result)

