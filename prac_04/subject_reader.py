"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()
    display_data(data)

# def load_data():
#     """Read data from file formatted like: subject,lecturer,number of students."""
#     input_file = open(FILENAME)
#     for line in input_file:
#         print(line)  # See what a line looks like
#         print(repr(line))  # See what a line really looks like
#         line = line.strip()  # Remove the \n
#         parts = line.split(',')  # Separate the data into its parts
#         print(parts)  # See what the parts look like (notice the integer is a string)
#         parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
#         print(parts)  # See if that worked
#         print("----------")
#     input_file.close()

def load_data():
    subject_data = []
    infile = open(FILENAME)
    for line in infile:
        line = line.strip()
        parts = line.split(",") # Split into [subject, lecturer, number]
        parts[2] = int(parts[2])
        subject_data.append(parts)
    infile.close()
    return subject_data

def display_data(subject_data):
    for subject in subject_data:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")

main()