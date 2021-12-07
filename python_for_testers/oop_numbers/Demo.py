class Demo:

    def handle_numbers(self, my_list):
        print(self.the_min_num_in_list(my_list))
        print(self.the_max_num_in_list(my_list))
        print(self.the_avg_in_list(my_list))

    def the_min_num_in_list(self, my_list):
        min = my_list[0]
        for x in my_list:
            if min > x:
                min = x
        return min

    def the_max_num_in_list(self, my_list):
        max = my_list[0]
        for x in my_list:
            if max < x:
                max = x
        return max

    # return also NONE why???
    def the_avg_in_list(self, my_list):
        summarize = 0
        for x in my_list:
            summarize += x
        avg = summarize / len(my_list)
        return avg
