"""
Expected time: 30 Minutes initially 60 minutes after starting it
Actual time:  7 minutes for read function,
JDM CP1404 
Prac 05  - Wimbledon
"""


# Planning
# create 4 fucntions
# main
# read_data
    # Data is recorded as Year,Country,Champion,Country,Runner-up,Score in the final 
    
# process_data
    # score in the final shows how many games they have won by the amount of scores
# display results
    # the display should print the champions and the amount of times they have won
    # the countries of the champions in alphabeticlal order
FILENAME = "wimbledon.csv"



def main():
    """Read the file and output details for the wimbledon"""
    records = read_record(FILENAME)
    winner_to_number_of_wins = process_data(records)    


def read_record(FILENAME):
    """Reads wimbledon.csv and stores it as a list"""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        for line in in_file.readlines()[1:]: # resolve error with champion being included in the process data
            parts = line.strip().split(",")
            records.append(parts)  
            
        return(records)


def process_data(records):
    winner_to_victories = {} # Winner, : count
    for record in records:
        winner = record[2]
        if winner in winner_to_victories:
            winner_to_victories[winner] += 1
        else:
            winner_to_victories[winner] = 1
    print(winner_to_victories)
    
    
    
        

main()