import sys

def analyze_log(file_path):
    try:
        with open(file_path, 'r') as file:
            cat_visits = 0
            other_cats = 0
            total_time_in_house = 0
            durations = []

            for line in file:
                if line.strip() == 'END':
                    break
                
                parts = line.strip().split(',')
                cat_name, entry_time, departure_time = parts

                entry_time = int(entry_time)
                departure_time = int(departure_time)

                duration = departure_time - entry_time
                total_time_in_house += duration

                if cat_name == 'OURS':
                    cat_visits += 1
                    durations.append(duration)
                else:
                    other_cats += 1

            if cat_visits == 0:
                print("No data for the correct cat.")
            else:
                avg_duration = sum(durations) // len(durations)
                longest_duration = max(durations)
                shortest_duration = min(durations)

                print("Log File Analysis")
                print("==================\n")
                print(f"Cat Visits: {cat_visits}")
                print(f"Other Cats: {other_cats}\n")
                print(f"Total Time in House: {total_time_in_house // 60} Hours, {total_time_in_house % 60} Minutes\n")
                print(f"Average Visit Length: {avg_duration} Minutes")
                print(f"Longest Visit: {longest_duration} Minutes")
                print(f"Shortest Visit: {shortest_duration} Minutes")

    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        file_path = sys.argv[1]
        analyze_log(file_path)

        

