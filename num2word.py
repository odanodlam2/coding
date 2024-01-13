
ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
units = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion']

def read_three_digits(num, unit):
    hundred = ones[num // 100]
    ten = tens[num % 100 // 10]
    one = ones[num % 10]
    unit = units[unit] 

    if hundred != "": hundred += " hundred"

    word = f'{hundred} {ten} {one} {unit}'

    return word

def num2word(num):
    result = ""

    parts = [int(num[max(0, i-2):i+1]) for i in reversed(range(0, len(num), 3))] if len(num) > 3 else [int(num)] # [num] if under 999 else list with every three digits
    result = ' '.join([read_three_digits(x, idx) for idx, x in reversed(list(enumerate(parts)))])

    return result.strip()

print(num2word("1289348192394819234891238974"))


