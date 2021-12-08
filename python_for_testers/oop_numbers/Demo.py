class Demo:

    def __init__(self, my_list):
        self.my_list = my_list

    def handle_numbers(self):
        print(self.the_min_num_in_list())
        print(self.the_max_num_in_list())
        print(self.the_avg_in_list())

    def the_min_num_in_list(self):
        minimum = self.my_list[0]
        for x in self.my_list:
            if minimum > x:
                minimum = x
        return minimum

    def the_max_num_in_list(self):
        maximum = self.my_list[0]
        for x in self.my_list:
            if maximum < x:
                maximum = x
        return maximum

    # return also NONE why???
    def the_avg_in_list(self):
        summarize = 0
        for x in self.my_list:
            summarize += x
        avg = summarize / len(self.my_list)
        return avg
