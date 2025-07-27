"""
CP1404 Practical
File and class example - opens/reads a file, stores in objects of custom class
Modified to support pointer arithmetic field.
"""

from programming_language import ProgrammingLanguage

def main():
    languages = []
    # Open the file for reading
    with open('languages.csv', 'r', encoding='utf-8-sig') as in_file:
        # Skip the header
        in_file.readline()
        # All other lines are language data
        for line in in_file:
            parts = line.strip().split(',')
            # Reflection and PointerArithmetic are Yes/No, convert to Boolean
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[4] == "Yes"
            # year should be int
            language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]), pointer_arithmetic)
            languages.append(language)

    # Loop through and display all languages (using their str method)
    for language in languages:
        print(language)

main()
