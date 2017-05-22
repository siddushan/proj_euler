# problem 17


def number_to_word(number):
    map_nums = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
                6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
                11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen',
                16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty',
                30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety'}
    k = 1000
    m = k * 1000

    assert(0 <= number)

    if number < 20:
        return map_nums[number]

    if number < 100:
        if number % 10 == 0:
            return map_nums[number]
        else:
            return map_nums[number // 10 * 10] + ' ' + map_nums[number % 10]
    if number < k:
        if number % 100 == 0:
            return map_nums[number // 100] + ' hundred'
        else:
            return map_nums[number // 100] + ' hundred and ' + number_to_word(number % 100)

    if number < m:
        if number % k == 0:
            return number_to_word(number // k) + ' thousand'
        else:
            return number_to_word(number // k) + ' thousand ' + number_to_word(number % k)

nums = list()
for i in range(1, 1001):
    word = number_to_word(i)
    nums.append(word)
all_nums = ''.join(nums)  # puts all the numbers together
all_nums = ''.join(all_nums.split())  # removes all the white space
print len(all_nums)

