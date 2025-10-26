# 1️⃣ Positional (Required) Arguments
def add(a, b):
    print("Sum:", a + b)

add(5, 10)  # both arguments are required


# 2️⃣ Default Arguments
def greet(name="Kiyo"):
    print("Hello,", name)

greet()          # uses default value
greet("Arun")    # overrides default value


# 3️⃣ Keyword Arguments
def student(name, age):
    print("Name:", name, "| Age:", age)

student(age=20, name="Kiyo")  # order doesn't matter


# 4️⃣ Variable-Length Positional Arguments (*args)
def total_marks(*marks):
    print("Marks:", marks)
    print("Total:", sum(marks))

total_marks(80, 90, 85, 75)


# 5️⃣ Variable-Length Keyword Arguments (**kwargs)
def display_info(**info):
    print("Student Info:")
    for key, value in info.items():
        print(f"{key}: {value}")

display_info(name="Kiyo", age=20, course="CSE")


# 6️⃣ Combination of all parameter types
def mix_func(a, b=10, *args, **kwargs):
    print("a:", a)
    print("b (default or passed):", b)
    print("args:", args)
    print("kwargs:", kwargs)

mix_func(5, 15, 20, 25, x=100, y=200)
 