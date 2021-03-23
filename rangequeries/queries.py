class Query:
    def __init__(self, array):
        self.array = array
        self.prefix_sum_array = []

    def show_array(self):
        print(self.array)

    def show_prefix_sum_array(self):
        print(self.prefix_sum_array)

    def generate_prefix_sum_array(self):
        for ind, el in enumerate(self.array):
            if not self.prefix_sum_array:
                self.prefix_sum_array.append(el)
            else:
                self.prefix_sum_array.append(el + self.prefix_sum_array[ind - 1])

    def sum_query(self, range_start, range_end):
        return self.prefix_sum_array[range_end] - self.prefix_sum_array[range_start - 1]

def main():
    query = Query([1, 3, 4, 8, 6, 1, 4, 2])
    query.show_array()
    query.generate_prefix_sum_array()
    query.show_prefix_sum_array()

    print(query.sum_query(3, 6))


if __name__ == "__main__":
    main()