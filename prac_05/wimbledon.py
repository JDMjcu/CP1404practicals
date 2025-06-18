"""
Expected time: 30 Minutes initially 60 minutes after starting it
Actual time:  7 minutes for read function, 34 for process function, after editting and completing 53 minutes
JDM CP1404 
Prac 05  - Wimbledon
"""

FILENAME = "wimbledon.csv"

def main():
    """Read the file and output details for the wimbledon"""
    records = read_record(FILENAME)
    champion_to_count, countries = process_data(records)    
    display_data(champion_to_count, countries)

def read_record(FILENAME):
    """Reads wimbledon.csv and stores it as a list"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        
        for line in in_file.readlines()[1:]: # Remove CSV header 
            parts = line.strip().split(",")
            records.append(parts)  
            
        return(records)


def process_data(records):
    """Create a dictionary for champion_to_count and a set of countries"""
    champion_to_count = {} # champion, : count
    countries = set()
    for record in records:
        
        countries.add(record[1])
        
        champion = record[2]
        
        if champion in champion_to_count:
            champion_to_count[champion] += 1
            
        else:
            champion_to_count[champion] = 1
            
    return champion_to_count, countries

def display_data(champion_to_count, countries):
    """Display the champions and their countries"""
    print("Wimbledon Champions: ")    
    
    for name, count in champion_to_count.items():
        print(name, count)
    
    print(f"\nThese {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()