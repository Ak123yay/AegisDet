import unittest
from aegisdet.router import RuleBasedRouter, RouterConfig
from aegisdet.types import Detection

class RouterTests(unittest.TestCase):
    def test_easy(self):
        result=RuleBasedRouter().route([Detection((10,10,80,80),0.9,0)],100,100)
        self.assertFalse(result.refine); self.assertEqual(result.reasons,("fast",))
    def test_small(self):
        result=RuleBasedRouter().route([Detection((1,1,5,5),0.9,0)],100,100)
        self.assertTrue(result.refine); self.assertIn("small-object",result.reasons)
    def test_uncertain_count(self):
        ds=[Detection((0,0,40,40),0.3,0),Detection((50,50,90,90),0.4,1)]
        self.assertTrue(RuleBasedRouter().route(ds,100,100).refine)
if __name__ == "__main__": unittest.main()
