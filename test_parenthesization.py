# Copyright 2015 Jason Owen <jason.a.owen@gmail.com>
#
# This file is part of matrix-chain-multiplication.
#
# matrix-chain-multiplication is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# matrix-chain-multiplication is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with matrix-chain-multiplication.  If not, see
# <http://www.gnu.org/licenses/>.

import unittest
import parenthesization

class MatrixChainMultiplicationTests(unittest.TestCase):
  def test_single_element_chain(self):
    multiplier = parenthesization.MatrixChainMultiplier([1, 2])
    self.assertEqual(multiplier.parenthesize(), '1')

  def test_double_element_chain(self):
    multiplier = parenthesization.MatrixChainMultiplier([1, 2, 3])
    self.assertEqual(multiplier.parenthesize(), '(1, 2)')

  def test_single_element_chain_calculates_costs(self):
    multiplier = parenthesization.MatrixChainMultiplier([1, 2])
    multiplier.calculate_costs()
    self.assertEqual(multiplier.costs[(0,0)], 0)

  def test_double_element_chain_calculates_costs(self):
    multiplier = parenthesization.MatrixChainMultiplier([1, 2, 3])
    multiplier.calculate_costs()
    self.assertEqual(multiplier.costs[(0,1)], 6)

  def test_triple_element_chain_calculates_costs(self):
    multiplier = parenthesization.MatrixChainMultiplier([1, 2, 3, 4])
    multiplier.calculate_costs()
    self.assertEqual(multiplier.costs[(0,1)], 6)
    self.assertEqual(multiplier.costs[(1,2)], 24)
    self.assertEqual(multiplier.costs[(0,2)], 18)

  def test_wikipedia_sample_chain_cost(self):
    multiplier = parenthesization.MatrixChainMultiplier([10, 30, 5, 60])
    multiplier.calculate_costs()
    self.assertEqual(multiplier.costs[(0,2)], 4500)

if __name__ == '__main__':
  unittest.main()
