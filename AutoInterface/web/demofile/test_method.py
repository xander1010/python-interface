#coding:utf-8
import unittest
from demo import RunMain

class TestMethod(unittest.TestCase):

    def setUp(self):
        self.run = RunMain()

    def tearDown(self):
        print('tearDown')

    def test_01(self):
        url = 'http://www.weather.com.cn/data/cityinfo/101010100.html'                
        req = self.run.run_main(url,'GET')
        print(req)
        

    # def test_02(self):
    #     print('this is 02 方法')

if __name__ == '__main__':
    unittest.main()