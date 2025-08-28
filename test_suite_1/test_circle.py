from circle import Circle
import unittest

class testCircle(unittest.TestCase):

    def setUp(self):
        self.circle = Circle(10)

    def test_get_radius(self):
        self.assertEqual(self.circle.getRadius(), 10)

    def test_set_radius(self):
        self.assertEqual(self.circle.setRadius(30), True)

    def test_set_bad_radius(self):
        self.assertEqual(self.circle.setRadius(-50), False)

    def test_get_area(self):
        self.assertEqual(self.circle.getArea(), 314.1592653589793)

    def test_get_area_2(self):
        self.circle.setRadius(2)
        self.assertEqual(self.circle.getArea(), 0)

    def test_get_circumference(self):
        self.assertEqual(self.circle.getCircumference(), 62.83185307179586)

    def test_all_functions(self):
        self.circle.setRadius(5)
        self.assertEqual(self.circle.getRadius(), 5)
        self.assertEqual(self.circle.getArea(), 78.53981633974483)
        self.assertEqual(self.circle.getCircumference(), 31.41592653589793)


