isbn_number = "030640615"
isbn_number_calculation_sum = 0

for index, number in enumerate(isbn_number):
    isbn_number_calculation_sum += (index + 1) * number
print(f"Sum equeals {isbn_number_calculation_sum}")
checksum = isbn_number_calculation_sum % 11
print(f'Checksum for this ISBN number is {checksum}')
