# A dictionary of colour names and their hex codes
COLOURS = {
    "aliceblue": "#f0f8ff",
    "antiquewhite": "#faebd7",
    "aqua": "#00ffff",
    "aquamarine": "#7fffd4",
    "azure": "#f0ffff",
    "beige": "#f5f5dc",
    "bisque": "#ffe4c4",
    "black": "#000000",
    "blanchedalmond": "#ffebcd",
    "blue": "#0000ff"
}
colour_name = input("Enter a colour name (or press Enter to stop): ").lower()

while colour_name != "":
    if colour_name in COLOURS:
        print("Hex code:", COLOURS[colour_name])
    else:
        print("Sorry, that colour is not in the list.")
    colour_name = input("Enter another colour name (or press Enter to stop): ").lower()

print("Goodbye!")
