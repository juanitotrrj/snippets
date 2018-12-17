string_with_trailing_commas = 'asda,as,das,dsa,d,,,'
delimeter = ','

generated_list_of_values = ' '.join(string_with_trailing_commas.split(delimeter)).split()

print('CSV value: "' + string_with_trailing_commas + '"')
print('Result: ', generated_list_of_values)
