from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Test_WebDriverObjectMethods:

    def setup_class(cls):
        global driver
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.imdb.com/")

    def test_demo01(self):
        driver.refresh()
        imdb_title = driver.title
        if imdb_title == "IMDb: Ratings, Reviews, and Where to Watch the Best Movies & TV Shows":
            print(imdb_title)

    def test_demo02(self):
        imdb_url = driver.current_url
        if imdb_url == "https://www.imdb.com/":
            print(imdb_url)

    def teardown_class(cls):
        driver.quit()
