import unittest
import sys
from fairpy import *
from fairpy.fairpy.agentlist import AgentList
from main import Double_RoundRobin_Algorithm, Generalized_Adjusted_Winner_Algorithm, Generalized_Moving_knife_Algorithm


class Mytes(unittest.TestCase):
        # ---------------------------------------------------Tests for algo 1-----------------------------------------
    def test1(self):
        #only good chores
        exm = AgentList({"Agent1": {"1": 1, "2": 8, "3": 1, "4": 2}, "Agent2": {"1": 2, "2": 6, "3": 7, "4": 6},
                          "Agent3": {"1": 4, "2": 2, "3": 2, "4": 2}})
        res = Double_RoundRobin_Algorithm(exm)
        self.assertEqual(res, {"Agent1": ["2","4"], "Agent2": ["3"], "Agent3": ["1"]})

    def test2(self):
        # only bad chores
        exm = AgentList({"Agent1": {"1": -1, "2": -5, "3": -1, "4": 0}, "Agent2": {"1": -5, "2": -4, "3": -7, "4": -6},
                          "Agent3": {"1": -4, "2": 0, "3": -2, "4": 0}})
        res = Double_RoundRobin_Algorithm(exm)
        self.assertEqual(res, {"Agent1": ["3", "4"], "Agent2": ["1"], "Agent3": ["2"]})


    def test3(self):
        exm = AgentList({"Agent1": {"1": 1, "2": 0, "3": -1, "4": 2}, "Agent2": {"1": 2, "2": 6, "3": 0, "4": 0},
                          "Agent3": {"1": 0, "2": 2, "3": -2, "4": 2}})
        res = Double_RoundRobin_Algorithm(exm)
        self.assertEqual(res, {"Agent1": ["1","3"], "Agent2": ["2"], "Agent3": ["4"]})

    # ---------------------------------------------------Tests for algo 2 -----------------------------------------


    def test4(self):
        exm = AgentList({"Agent1": {"1": 1, "2": 0, "3": -1, "4": 2}, "Agent2": {"1": 2, "2": 6, "3": 0, "4": 0}})
        res = Generalized_Adjusted_Winner_Algorithm(exm)
        self.assertEqual(res, {"Agent1": ["4", "1"], "Agent2": ["3", "2"]})


    def test5(self):
        exm = AgentList({"Agent1":{"1":1,"2":-1,"3":-2,"4":3,"5":5,"6":0,"7":0,"8":-1,"9":2,"10":3},"Agent2":{"1":-3,"2":4,"3":-6,"4":2,"5":4,"6":-3,"7":2,"8":-2,"9":4,"10":5}})
        res = Generalized_Adjusted_Winner_Algorithm(exm)
        self.assertEqual(res, {"Agent1": ["6","1","4","10","5"], "Agent2": ["2","7","8","3","9"]})

        # --------------------------------------------------- Tests for algo 3 -----------------------------------------


    def test6(self):
        exm = AgentList({"Agent1": {"1": 1, "2": 0, "3": -1, "4": 2}, "Agent2": {"1": 2, "2": 6, "3": 0, "4": 0},
                          "Agent3": {"1": 0, "2": 2, "3": -2, "4": 2}})
        res = Generalized_Moving_knife_Algorithm(exm)
        self.assertEqual(res, {"Agent1": [], "Agent2": [], "Agent3": []})


    def test7(self):
        exm = AgentList({"Agent1": {"1": 1, "2": 0, "3": -1, "4": 2}, "Agent2": {"1": 2, "2": 6, "3": 0, "4": 0},
                          "Agent3": {"1": 0, "2": 2, "3": -2, "4": 2}})
        res = Generalized_Moving_knife_Algorithm(exm)
        self.assertEqual(res, {"Agent1": [], "Agent2": [], "Agent3": []})


if __name__ == '__main__':
    unittest.main()