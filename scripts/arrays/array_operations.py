# reverse given array, no extra memory
# linear time complexity


class ArrayOperations:
    def __init__(self, data, is_string=False, is_string_list=False):
        self.arr_data = data
        self.is_string = is_string
        self.is_string_list = is_string_list

    def is_integer_duplicate(self):
        # need to add exceptions here
        for num in self.arr_data:
            # if the number at the index location has been flipped,
            # current value is duplicate
            if self.arr_data[abs(num)] >= 0:
                self.arr_data[abs(num)] = -self.arr_data[abs(num)]
                # print(self.arr_data[num])
            else:
                print("repetition is found at", str(abs(num)))

    def is_anagram(self):
        if self.is_string_list:
            self.subject = list(self.arr_data[0])
            self.anagram = list(self.arr_data[1])
        if len(self.subject) == len(self.anagram):
            self.subject = sorted(self.subject)
            self.anagram = sorted(self.anagram)
            for letter in range(len(self.subject)):
                if self.subject[letter] != self.anagram[letter]:
                    return False
                return True
        # print(self.subject,self.anagram)
        return False

    def reverse_array(self):
        if self.is_string:
            data = list(self.arr_data)
        else:
            data = self.arr_data

        start_index = 0
        end_index = len(data) - 1

        while end_index > start_index:
            data[start_index], data[end_index] = data[end_index], data[start_index]
            start_index += 1
            end_index -= 1
        # print(data)

        if not self.is_string:
            return data
        else:
            return ''.join(data)

    def reverse_integer(self):
        original_integer = self.arr_data
        reversed_integer, remainder = 0, 0
        while original_integer > 0:
            remainder = original_integer % 10
            original_integer = original_integer // 10
            reversed_integer = reversed_integer * 10 + remainder
        return reversed_integer

    def is_palindrome(self):
        if self.is_string:
            if self.arr_data == self.reverse_array():
                return True
        return False


if __name__ == "__main__":
    test_array = ArrayOperations([1, 4, 2, -41, 3, 2, 1])
    print(test_array.is_integer_duplicate())

    # test_array = ArrayOperations(["restful","fluster"],is_string_list=True)
    # print(test_array.is_anagram())

    # test_array = ArrayOperations(1235)
    # print(test_array.reverse_integer())
