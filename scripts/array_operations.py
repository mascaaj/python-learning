# reverse given array, no extra memory
# linear time complexity
class ArrayOperations:
    def __init__(self,data,is_string=False,is_string_list=False):
        self.arr_data = data
        self.is_string = is_string
        self.is_string_list = is_string_list

    def is_anagram(self):    
        if self.is_string_list:
            self.subject = list(self.arr_data[0])
            self.anagram = list(self.arr_data[1])
        print(self.subject,self.anagram)

    def reverse_array(self):
        if self.is_string==True:
            data = list(self.arr_data)
        else:   
            data = self.arr_data

        start_index = 0
        end_index = len(data)-1

        while end_index > start_index:
            data[start_index], data[end_index] = data[end_index], data[start_index]
            start_index+=1
            end_index-=1
        # print(data)

        if self.is_string==False:
            return data
        else :
            return ''.join(data)

    def reverse_integer(self):
        original_integer = self.arr_data
        reversed_integer, remainder = 0 , 0
        while original_integer>0:
            remainder = original_integer % 10
            original_integer = original_integer // 10
            reversed_integer = reversed_integer * 10 + remainder
        return reversed_integer

    def is_palindrome(self):
        if self.is_string==True:
            if self.arr_data == self.reverse_array():
                return True
        return False

if __name__ == "__main__":
    test_array = ArrayOperations(["restful","fluster"],is_string_list=True)
    test_array.is_anagram()

    # test_array = ArrayOperations(1235)
    # print(test_array.reverse_integer())