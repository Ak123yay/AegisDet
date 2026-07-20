import unittest
from aegisdet.geometry import area_ratio, intersection_over_union, pad_box, remap_box

class GeometryTests(unittest.TestCase):
    def test_iou(self): self.assertAlmostEqual(intersection_over_union((0,0,10,10),(5,5,15,15)),25/175)
    def test_area_ratio(self): self.assertAlmostEqual(area_ratio((0,0,10,10),100,100),0.01)
    def test_padding_clamps(self): self.assertEqual(pad_box((0,0,10,10),0.5,100,100),(0.0,0.0,15.0,15.0))
    def test_remap(self): self.assertEqual(remap_box((1,2,3,4),10,20),(11,22,13,24))
if __name__ == "__main__": unittest.main()
