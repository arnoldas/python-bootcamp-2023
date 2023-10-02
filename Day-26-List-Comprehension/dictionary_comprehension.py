import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# Create a dictionary with random scores
students_scores = {name: random.randint(1, 100) for name in names}
print(students_scores)

# Create a dictionary with passed students (score >= 60)
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# Create a dictionary with words and letter count from the sentence
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word: len(word) for word in sentence.split()}
print(result)

# Create a dictionary to convert from Celsius to Fahrenheit
weather_c = {
    "Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24
}
weather_f = {day: temp_c * 9/5 + 32 for (day, temp_c) in weather_c.items()}
print(weather_f)

