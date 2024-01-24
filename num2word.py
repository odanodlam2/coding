ones = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
units = ['', 'thousand', 'million', 'billion', 'trillion', 'quadrillion']

def read_three_digits(num, unit):
    hundred = ones[num // 100] + " hundred" if int(num) >= 100 else ""
    ten = tens[num % 100 // 10]
    one = ones[num % 10 ]
    unit = units[unit]
    teen = ""

    if ten == "ten" and one != "":
        teen = teens[num % 10]
        ten, one = "", ""

    return " ".join(el for el in [hundred, ten, one, teen, unit] if el).strip()

def num2word(num):
    if int(num) >= (10**(int((len(units)) * 3))): return "Number Too High"

    parts = [int(num[max(0, i-3):i]) for i in range(len(num), 0, -3)] if len(num) > 3 else [int(num)] # [num] if under 999 else list with every three digits
    result = ' '.join([read_three_digits(x, idx) for idx, x in reversed(list(enumerate(parts))) if parts[idx] != 0])
    
    return result


print(num2word("210"))
