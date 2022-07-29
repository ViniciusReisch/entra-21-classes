from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
from selenium import webdriver

username = "user_name"
access_key = "access_key"
class blogScraper:
    # Generate capabilities from here: https://www.lambdatest.com/capabilities-generator/
    def setUp(self):
        capabilities = {
            "build": "your build name",
            "name": "your test name",
            "platform": "Windows 10",
            "browserName": "Chrome",
            "version": "91.0",
            "selenium_version": "3.11.0",
            "geoLocation": "IN",
            "chrome.driver": "91.0",
            "headless": True
        }
        self.driver = webdriver.Remote(
            command_executor="https://{}:{}@hub.lambdatest.com/wd/hub".format(username, access_key),
            desired_capabilities=capabilities)

    def tearDown(self):
        self.driver.quit()

    def scrapTopic(self, topic):
        driver = self.driver

        # Url
        driver.get("https://www.lambdatest.com/blog/")

        searchBarXpath = "/html[1]/body[1]/section[1]/div[1]/form[1]/label[1]/input[1]"

        # searching topic
        textbox = driver.find_element_by_xpath(searchBarXpath)
        textbox.send_keys(topic)
        textbox.send_keys(Keys.ENTER)

        source = driver.page_source
        # scraping title
        title_list = []
        soup = bs(source, "html.parser")
        for h2 in soup.findAll("h2", class_="blog-titel"):
            for a in h2.findAll("a", href=True):
                title_list.append(a.text)

        return title_list


if __name__ == "__main__":
    obj = blogScraper()
    obj.setUp()
    print(obj.scrapTopic("scrap"))
    obj.tearDown()