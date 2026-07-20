import unittest
from aegisdet.crop_refine import CropPlanner, CropPlannerConfig
from aegisdet.types import Detection

class CropPlannerTests(unittest.TestCase):
    def test_cap_and_priority(self):
        ds=[Detection((1,1,6,6),0.3,0),Detection((20,20,30,30),0.4,1),Detection((50,50,90,90),0.9,2)]
        crops=CropPlanner(CropPlannerConfig(max_crops=1,minimum_crop_pixels=1)).plan(ds,100,100)
        self.assertEqual(len(crops),1); self.assertEqual(crops[0].trigger_class_id,0)
    def test_ignores_easy(self):
        crops=CropPlanner().plan([Detection((10,10,80,80),0.9,0)],100,100)
        self.assertEqual(crops,[])
if __name__ == "__main__": unittest.main()
