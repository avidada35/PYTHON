with open('currency.txt') as f:
    lines = f.readlines()

currency_dict={}
for line in lines:
    parsed = line.split("\t")
    currency_dict[parsed[0]] = parsed[1]


amount = int(input('enter the amount: '))
print('enter the name of currency you want to convert this amount to? Available option:\n')
[print(item) for item in currency_dict.keys()]
currency = input('plz enter one of these value: \n')
print(f"{amount} INR is eqaul to {amount *float(currency_dict[currency])} {currency}")


