import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions


capabilities = dict(
    platformName='ios',
    automationName='xcuitest',
    # udid='xxx',
    deviceName='iPhone 16 Pro',
    bundleId='com.example.ss.RGBDemo',
    # app='app/iphoneos/RGBDemo.app',
    app='app/iphonesimulator/RGBDemo.app',
    # usePrebuiltWDA=True,
    # derivedDataPath='~/PycharmProjects/TestIosDemo/appium_wda_ios',
    enforceAppInstall=True,
    # language='en',
    language='zh-Hans',
    locale='zh_CN',
    calendarFormat='chinese',
    appTimeZone='America/Los_Angeles'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))
        self.driver.implicitly_wait(30)

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_xxx(self):
        self.driver.save_screenshot('screen.png')


if __name__ == '__main__':
    unittest.main()
