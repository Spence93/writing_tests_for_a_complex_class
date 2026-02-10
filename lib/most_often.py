# File: lib/most_often.py

class MostOften:
    def __init__(self, starting_list):
        self.starting_list = starting_list

    def add_new(self, new_item):
        self.starting_list.append(new_item)

    def get_most_often(self):
        # use set() to create a list of unique items
        unique_items = set(self.starting_list)

        # set up our highest recorded variables
        highest_count = 0
        highest_items = []

        for item in unique_items:
            # count the number of instances of that item in the list
            count = self.starting_list.count(item)
            # if we've found a new highest count...
            if count > highest_count:
                highest_count = count
                highest_items = [item]
            # but if we've found an equally high count...
            elif count == highest_count:
                highest_items.append(item)

        # if we have a clear winner, return it
        if len(highest_items) == 1:
            return highest_items[0]
        # otherwise we'll say there's "no clear winner"
        else:
            return "no clear winner"
