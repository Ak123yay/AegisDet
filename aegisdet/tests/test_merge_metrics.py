import unittest
from aegisdet.merge import class_aware_nms
from aegisdet.metrics import edge_score, percentile
from aegisdet.types import Detection

class MergeMetricsTests(unittest.TestCase):
    def test_nms_same_class(self):
        ds=[Detection((0,0,10,10),0.9,0),Detection((1,1,11,11),0.8,0)]
        self.assertEqual(len(class_aware_nms(ds,0.5)),1)
    def test_nms_keeps_different_class(self):
        ds=[Detection((0,0,10,10),0.9,0),Detection((0,0,10,10),0.8,1)]
        self.assertEqual(len(class_aware_nms(ds,0.5)),2)
    def test_edge_score(self): self.assertAlmostEqual(edge_score(0.5,10,5),0.01)
    def test_percentile(self): self.assertEqual(percentile([1,2,3,4,5],90),5)
if __name__ == "__main__": unittest.main()
