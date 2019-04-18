import unittest
import torch

import gravity

dim = 2
N = 3

M = torch.tensor([1.0,2,10])

coords = torch.tensor(
    [[0.0,0],
     [0,10],
     [10,0]])

vels = torch.tensor(
    [[1.0,-1],
     [1, 1],
     [-1,-1]])

state = torch.stack([coords, vels])

state2_true = torch.tensor([[[ 1.0000, -1.0000],
         [ 1.0000,  1.0000],
         [-1.0000, -1.0000]],

        [[10.0000,  2.0000],
         [ 7.0711, -8.0711],
         [-2.4142,  1.4142]]])

class MyTestCase(unittest.TestCase):
    def test_F(self):
        F = gravity.make_F(M)
        st2 = F(state)
        dst = ((st2 - state2_true)**2).sum()
        self.assertLess(dst, 1e-6)


if __name__ == '__main__':
    unittest.main()
