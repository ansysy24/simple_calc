from django.views import View
from django.shortcuts import render

import re

class CalcView(View):

    def post(self, request):
        first_number = int(request.POST.get('first_number', 0))
        second_number = int(request.POST.get('second_number', 0))
        operator = request.POST.get('operator', 'add')
        result = 'please use form correctly'
        print(operator)
        if operator == 'add':
            result = first_number + second_number
        if operator == 'sub':
            result = first_number - second_number
        if operator == 'mul':
            result = first_number * second_number
        if operator == 'div':
            result = first_number / second_number
        return render(request, 'calc.html', {'result': str(result)})

    def get(self, request):
        return render(request, 'calc.html')


class CalcLineView(View):

    @staticmethod
    def return_list_of_integers(numbers: str):
        nums = re.findall('\d+', numbers)
        nums_neg = re.findall('-\d+', numbers)
        for num in nums_neg:
            if num[1:] in nums:
                nums.remove(num[1:])

        nums = nums + nums_neg
        return nums

    def post(self, request):
        numbers = request.POST.get('numbers', '0')

        nums = self.return_list_of_integers(numbers)

        operator = request.POST.get('operator', 'add')
        result = int(nums[0])

        if operator == 'add':
            for num in nums[1:]:
                result += int(num)
        if operator == 'sub':
            for num in nums[1:]:
                result -= int(num)
        if operator == 'mul':
            for num in nums[1:]:
                result *= int(num)
        if operator == 'div':
            for num in nums[1:]:
                result /= int(num)
        return render(request, 'line.html', {'result': str(result)})

    def get(self, request):
        return render(request, 'line.html')
