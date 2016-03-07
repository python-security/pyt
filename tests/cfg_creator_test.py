import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
from ast import parse

from pyt.cfg import Listener

class CFG_if_test(unittest.TestCase):

    def setUp(self):
        self.cfg = Listener()
        obj = parse('if x > 0:\n\tx += 1\n\ty+=2\nelif x==0:\n\tx+=3\nelse:\n\tx+=4\nx+=5')

        cfg.visit(obj)

    def test_if_stmts(self):
        test = self.cfg[0]
        
        self.assertEqual(1,0)
