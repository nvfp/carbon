import unittest
from carbon.color import (
    interpolate_color,
    get_gray,
    getgray
)


class TestColor(unittest.TestCase):

    def test_interpolate_color(self):
        
        ## regular cases

        result = interpolate_color('#ff0000', '#0000ff', 0.0)
        self.assertEqual(result, '#ff0000')

        result = interpolate_color('#ff0000', '#0000ff', 0.5)
        self.assertEqual(result, '#7f007f')

        result = interpolate_color('#ff0000', '#0000ff', 1.0)
        self.assertEqual(result, '#0000ff')


        ## extreme cases

        result = interpolate_color('#000000', '#ffffff', 0.0)
        self.assertEqual(result, '#000000')

        result = interpolate_color('#000000', '#ffffff', 1.0)
        self.assertEqual(result, '#ffffff')

        result = interpolate_color('#000000', '#000000', 0.5)
        self.assertEqual(result, '#000000')

        result = interpolate_color('#ffffff', '#ffffff', 0.8)
        self.assertEqual(result, '#ffffff')
    
    def test_get_gray(self):

        ## maximum luminance and maximum opacity (white color)
        result = get_gray(255, 1.0)
        self.assertEqual(result, '#ffffff')

        ## minimum luminance and maximum opacity (black color)
        result = get_gray(0, 1.0)
        self.assertEqual(result, '#000000')

        ## mid-range luminance and maximum opacity
        result = get_gray(128, 1.0)
        self.assertEqual(result, '#808080')

        ## maximum luminance and low opacity
        result = get_gray(255, 0.25)
        self.assertEqual(result, '#404040')

        ## mid-range luminance and high opacity
        result = get_gray(128, 0.75)
        self.assertEqual(result, '#606060')

        ## minimum luminance and maximum opacity (black color)
        result = get_gray(0, 1.0)
        self.assertEqual(result, '#000000')

        ## maximum luminance and maximum opacity (white color)
        result = get_gray(255, 1.0)
        self.assertEqual(result, '#ffffff')

    def test_getgray(self):

        result = getgray(0.5)
        self.assertEqual(result, '#808080')

        result = getgray(0)
        self.assertEqual(result, '#000000')

        result = getgray(1, max_lum=200)
        self.assertEqual(result, '#c8c8c8')

        result = getgray(0.75, max_lum=100)
        self.assertEqual(result, '#4b4b4b')



if __name__ == '__main__':
    unittest.main()