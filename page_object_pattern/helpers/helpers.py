import os


class ScreenshotMaker:
    def __init__(self, driver):
        self.driver = driver
        self._create_screenshot_folder_if_does_not_exist()

    def save_screenshot(self, screenshot_name):
        screenshot_path = os.path.join("screenshots", screenshot_name)
        if self.driver.get_screenshot_as_file(screenshot_path):
            print("Screenshot saved successfully")
        else:
            print("Error during saving screenshot")

    def _create_screenshot_folder_if_does_not_exist(self):
        screenshot_folder = "screenshots"
        if not os.path.exists(screenshot_folder):
            os.makedirs(screenshot_folder)

