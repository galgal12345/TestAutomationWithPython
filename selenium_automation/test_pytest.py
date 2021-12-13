class Test_PyTest:

    def setup_class(cls):
        print("im setup class")

    def setup_method(self):
        print("im setup method")

    def test_demo01(self):
        print("im test demo 01")

    def test_demo02(self):
        print("im test demo 02")

    def teardown_method(self):
        print("im a teardown method")

    def teardown_class(cls):
        print("im a teardown class")
