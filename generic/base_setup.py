import pytest
from pyjavaproperties import Properties
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Remote

class BaseSetup:
    @pytest.fixture(autouse=True)
    def pre_condtion(self):
        ppj=Properties()
        ppj.load(open('../config.properties'))
        usergrid=ppj['USERGRID'].lower()
        print('USERGRID',usergrid)
        browser=ppj['BROWSER'].lower()
        print('BROWSWER',browser)
        gridurl=ppj['GRIDURL']
        print('GRIDURL',gridurl)
        appurl=ppj['APPURL']
        print('APPURL',appurl)
        ito=ppj['IMPLICIT_TIME_OUT']
        print('IMPLICIT_TIME_OUT',ito)
        eto=ppj['EXPLICIT_TIME_OUT']
        print('EXPLICIT_TIME_OUT',eto)
        if usergrid=='yes':
            print("Executing in remote system")
            if browser == 'chrome':
                print("Open Chrome browser")
                self.driver=webdriver.Remote(command_executor=gridurl,options=webdriver.ChromeOptions())
            elif browser=='firefox':
                print("Open firefox browder")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.FirefoxOptions())
            else:
                print("Open edge browder")
                self.driver = webdriver.Remote(command_executor=gridurl, options=webdriver.EdgeOptions())
        else:
            print("Excecuting in local system")
            if browser=='chrome':
                self.driver=webdriver.Chrome()
                print("Open Chrome Browser")
            elif browser=='fireforx':
                self.driver=webdriver.Firefox()
                print("Open Firefox Browser")
            else:
                self.driver=webdriver.Edge()
                print("Open Chrome Browser")

        print("Enter the URL",appurl)
        self.driver.get(appurl)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.wait=WebDriverWait(self.driver,10)

    @pytest.fixture(autouse=True)
    def post_condtion(self):
        yield
        print("close the browser")
        self.driver.quit()
