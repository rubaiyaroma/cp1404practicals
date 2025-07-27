"""
Estimated time: 20 minutes
Actual time: 15/17minutes
"""
from programming_language import ProgrammingLanguage
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
all_languages = [python, ruby, visual_basic]
print("\nDynamic languages:")
for language in all_languages:
    if language.is_dynamic():
        print(f"- {language.name}")