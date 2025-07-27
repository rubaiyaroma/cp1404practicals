# Read and display subject data
with open("subject_data.txt") as file:
    for line in file:
        parts = line.strip().split(',')
        print(f"{parts[0]} is taught by {parts[1]} and has {parts[2]} students")