
from generic.base_setup import BaseSetup
from generic.excel import Excel
from generic.mian import Test1
#from generic.excel import Excel
class TestScript1(BaseSetup):

    def test_script1(self):
        print("this is first test case")
        print(self.driver.title)

        Excel.get_data("../test_data/input.xlsx",'login',2,2)

class TestScrip2(Test1):
    def test_script2(self):
     print("This is main class")
     self.mian_run()
     print("Hello mian azam")




