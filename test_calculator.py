import re
import unittest
from appium import webdriver
from appium.options.ios import XCUITestOptions
from appium.webdriver.common.appiumby import AppiumBy

capabilities = dict(
    platformName='ios',
    automationName='xcuitest',
    udid='00008120-000602813472201E',
    bundleId='com.apple.calculator',
    usePrebuiltWDA=True,
    derivedDataPath='~/PycharmProjects/TestIosDemo/appium_wda_ios'
)

appium_server_url = 'http://localhost:4723'

class TestAppium(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Remote(appium_server_url, options=XCUITestOptions().load_capabilities(capabilities))

    def tearDown(self) -> None:
        if self.driver:
            self.driver.quit()

    def test_add(self) -> None:
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='One').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Add').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Three').click()
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Equals').click()
        el = self.driver.find_element(by=AppiumBy.XPATH, value='//XCUIElementTypeScrollView[@name="StandardInputView"]/XCUIElementTypeOther/XCUIElementTypeStaticText')
        result = el.text
        actual_value = float(re.sub(r'[^\d.-]', '', result))
        assert actual_value == 4, f'加法计算错误，预期结果为4，当前结果为:{actual_value}'
        self.driver.save_screenshot('screenshot.png')


if __name__ == '__main__':
    unittest.main()
