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

    def range_sum(self, range_start, range_end):
        return self.prefix_sum_array[range_end] - self.prefix_sum_array[range_start - 1]

    def range_minimum(self, range_start, range_end):
        if not range_end - range_start:
            return self.array[range_start]
        else:
            length = range_end - range_start + 1
            if (length != 0 ) and (length & (length - 1) == 0):
                length = int(length / 2)
                return min(self.range_minimum(range_start, range_start + length - 1), self.range_minimum(range_start + length, range_end))
            else:
                closest_power_two = 2
                while closest_power_two**2 <= length:
                    closest_power_two = closest_power_two**2
                return min(self.range_minimum(range_start, range_start + closest_power_two - 1), self.range_minimum(range_end - closest_power_two + 1, range_end))

def main():
    query = Query([1, 3, 4, 8, 6, 1, 4, 2])
    print("This is the array being worked on:")
    query.show_array()

    query.generate_prefix_sum_array()
    print("This is its prefix array sum:")
    query.show_prefix_sum_array()
    print("This is the sum of the elements from index 3 to index 6 of the array:")
    print(query.range_sum(3, 6))
    print("This is the minimum of the elements from index 1 to index 6 of the array:")
    print(query.range_minimum(1, 6))



if __name__ == "__main__":
    main()