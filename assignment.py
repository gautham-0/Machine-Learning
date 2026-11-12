#1
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
average = total / len(numbers)
print("Average =", average)

#2
numbers = (25, 10, 45, 5, 30)
smallest = min(numbers)
print("Smallest number =", smallest)

#3
marks = {
    "Maths": 80,
    "English": 75,
    "Python": 90,
    "Physics": 85
}
total = sum(marks.values())
print("Total marks =", total)

#4
text = "programming"
unique_characters = set(text)
print("Unique characters =", unique_characters)

#5
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2
print("Merged list =", merged_list)

#6
names = ["Amina", "Sara", "Anu"]
marks = [85, 90, 78]

student_marks = dict(zip(names, marks))
print(student_marks)

#7
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common = list(set(list1) & set(list2))
print("Common elements =", common)

#8
numbers = [1, 2, 2, 3, 3, 3, 4]
frequency = {}
for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1
print(frequency)

#9
students = {
    "Amina": 85,
    "Sara": 92,
    "Anu": 78,
    "Fathima": 88
}
highest_student = max(students, key=students.get)
print("Student with highest marks =", highest_student)
print("Marks =", students[highest_student])

#10
numbers = [1, 2, 3, 2, 4, 1, 5, 3]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
print("List after removing duplicates =", unique_numbers)