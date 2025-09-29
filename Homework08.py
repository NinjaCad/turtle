print('Reading input file "classes.txt"...')
try:
    text = open("/Users/caedmonjulian/Library/CloudStorage/GoogleDrive-caedmon.julian@gmail.com/My Drive/Caedmon/School/Master's University/CS121P Introduction to Programming/Test/classes.txt", "r")
except FileNotFoundError:
    print("Error: classes.txt does not exist or it can't be opened for input.")
    print("Program exiting now...")

students = {}
with open("/Users/caedmonjulian/Library/CloudStorage/GoogleDrive-caedmon.julian@gmail.com/My Drive/Caedmon/School/Master's University/CS121P Introduction to Programming/Test/classes.txt", "r") as infile:
    current_class = None
    for line in infile:
        line = line.strip()
        if not line:
            current_class = None
            continue
        if line.endswith(":"):
            current_class = line[:-1].strip()
        else:
            student = line.strip()
            if student not in students:
                students[student] = []
            students[student].append(current_class)
print("Input processed")

print('Writing output file "students.txt"...')
try:
    text = open("/Users/caedmonjulian/Library/CloudStorage/GoogleDrive-caedmon.julian@gmail.com/My Drive/Caedmon/School/Master's University/CS121P Introduction to Programming/Test/students.txt", "w")
except FileNotFoundError:
    print("Error: classes.txt can't be opened for output.")
    print("Program exiting now...")

with open("/Users/caedmonjulian/Library/CloudStorage/GoogleDrive-caedmon.julian@gmail.com/My Drive/Caedmon/School/Master's University/CS121P Introduction to Programming/Test/students.txt" , "w") as outfile:
    for student in sorted(students):
        classes_list = " ".join(sorted(students[student]))
        outfile.write(str(student) + ": " + classes_list + "\n")

print("Output processed.")
print("Program exiting now...")