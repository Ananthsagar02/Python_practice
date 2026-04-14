def find_total(expenses):
    total = 0
    for i in expenses:
        total += i
    return total

expense_list = [100,200,300,400,500,600,900]

expense_list2 = [1000,2000,3000,4000,5000,6000,9000]

print(find_total(expense_list))
print(find_total(expense_list2))

d = {
    "name": "John",
    "age": 30,
    "city": "New York",
}
del d["age"]

print(d["name"])

print(d)

for name, value in d.items():
    print(name, value,'j')


salaries = {
	'python': { 'junior': '100k', 'senior': '600k' },
	'php': { 'junior': '70k', 'senior': '400k' },
	'java': { 'junior': '80k', 'senior': '500k' },
	}

print(salaries['php']['senior'])

