def read_wimbledon_data(filename):
    champions_data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip the header line
        for line in in_file:
            parts = line.strip().split(",")
            champion = parts[1]
            country = parts[2]
            champions_data.append([champion, country])
    return champions_data

def count_champions(champions_data):
    champion_to_count = {}
    for entry in champions_data:
        champion = entry[0]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
    return champion_to_count

def get_countries(champions_data):
    countries = set()
    for entry in champions_data:
        country = entry[1]
        countries.add(country)
    return countries

def main():
    filename = "wimbledon.csv"
    champions_data = read_wimbledon_data(filename)

    champion_to_count = count_champions(champions_data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champion_to_count.items()):
        print(f"{champion} {wins}")

    countries = get_countries(champions_data)
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

main()