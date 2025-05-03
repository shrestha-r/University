def write_anime_file():
    data = [
        "1, Naruto, 8.4, Masashi Kishimoto, 2002, 23, Action Adventure Comedy Martial Arts Shounen Superpower, 220, Oct 3 2002 to Feb 8 2007, False, Studio Pierrot\n",
        "2, One Piece, 9.0, Eichiro Oda, 1999, 23, Action Adventure Comedy Drama Fantasy Shounen Superpower, 1125, Oct 20 1999 to ?, True, Toei Animation\n",
        "3, Black Clover, 8.2, Yuki Tabata, 2017, 23, Action Adventure Comedy Drama Fantasy Shounen Superpower, 170, Oct 3 2017 to Mar 30 2021, False, Studio Pierrot\n",
        "4, Death Note, 8.9, Tsugumi Ohba / Takeshi Obata, 2006, 23, Mystery Shounen Supernatural Police Psychological Thriller, 37, Oct 4 2006 to Jun 27 2007, False, Mad House\n"
    ]
    with open("anime_1.txt", "w") as file:
        file.writelines(data)

try:
    open("anime_1.txt")
except FileNotFoundError:
    write_anime_file()


def load_anime_data():
    anime_list = []
    with open("anime_1.txt", "r") as file:
        for line in file:
            parts = [p.strip() for p in line.strip().split(',')]
            genres = parts[6].split()
            status = parts[9].strip().lower() == "true"  # True = Currently Airing
            anime = {
                "ID": int(parts[0]),
                "Title": parts[1],
                "Rating": float(parts[2]),
                "Author": parts[3],
                "Start Year": int(parts[4]),
                "Duration (mins)": int(parts[5]),
                "Genres": genres,
                "Episodes": int(parts[7]),
                "Air Dates": parts[8],
                "Status": status,
                "Studio": parts[10]
            }
            anime_list.append(anime)
    return anime_list

def save_anime_data(anime_list):
    with open("anime_1.txt", "w") as file:
        for anime in anime_list:
            line = f'{anime["ID"]}, {anime["Title"]}, {anime["Rating"]}, {anime["Author"]}, {anime["Start Year"]}, {anime["Duration (mins)"]}, {" ".join(anime["Genres"])}, {anime["Episodes"]}, {anime["Air Dates"]}, {str(anime["Status"])}, {anime["Studio"]}\n'
            file.write(line)
def add_anime(anime_list):
    print("\nAdd a new anime:")
    try:
        status_input = input("Status (Currently Airing/Finished Airing): ").strip().lower()
        new_anime = {
            "ID": int(input("ID: ")),
            "Title": input("Title: "),
            "Rating": float(input("Rating: ")),
            "Author": input("Author: "),
            "Start Year": int(input("Start Year: ")),
            "Duration (mins)": int(input("Duration (mins): ")),
            "Genres": input("Genres (separated by space): ").split(),
            "Episodes": int(input("Episodes: ")),
            "Air Dates": input("Air Dates: "),
            "Status": int(input("0 or 1: ")),
            "Studio": input("Studio: ")
        }
        return anime_list.append(new_anime)
        save_anime_data(anime_list)
        print("Anime added successfully!")
    except ValueError:
        print("Invalid input. Please try again.")

def show_all_anime(anime_list):
    print("\nAll Anime Entries:")
    print("{:<3} {:<20} {:<5} {:<25} {:<6} {:<5} {:<30} {:<5} {:<25} {:<18} {:<20}".format(
        "ID", "Title", "Rate", "Author", "Year", "Dur", "Genres", "Ep", "Air Dates", "Status", "Studio"))
    print("-" * 170)
    for anime in anime_list:
        print("{:<3} {:<20} {:<5} {:<25} {:<6} {:<5} {:<30} {:<5} {:<25} {:<18} {:<20}".format(
            anime["ID"], anime["Title"], anime["Rating"], anime["Author"],
            anime["Start Year"], anime["Duration (Years)"],
            ' '.join(anime["Genres"]),
            anime["Episodes"], anime["Air Dates"],
            "Currently Airing" if anime["Status"] else "Finished Airing",
            anime["Studio"]))

def is_currently_airing(anime):
    return anime.get("Status", False)  # True means currently airing

def remove_anime(anime_list):
    search_input = input("Enter anime Title or ID to remove: ").strip()
    found = None
    if search_input.isdigit():
        found = next((anime for anime in anime_list if anime["ID"] == int(search_input)), None)
    else:
        found = next((anime for anime in anime_list if anime["Title"].lower() == search_input.lower()), None)

    if found:
        confirm = input(f"Are you sure you want to delete '{found['Title']}'? (y/n): ").strip().lower()
        if confirm == 'y':
            anime_list.remove(found)
            save_anime_data(anime_list)
            print("Anime removed successfully.")
        else:
            print("Deletion canceled.")
    else:
        print("Anime not found.")

def search_anime(anime_list):
    while True:
        print("\n1. Search anime")
        print("2. Add anime")
        print("3. Remove anime")
        print("4. Show currently airing anime")
        print("5. Show all anime")
        print("6. Exit")
        try:
            choice = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Enter a number.")
            continue

        if choice == 1:
            search_input = input("Enter anime title or ID to search: ").strip()
            found = None
            if search_input.isdigit():
                found = next((anime for anime in anime_list if anime["ID"] == int(search_input)), None)
            else:
                found = next((anime for anime in anime_list if anime["Title"].lower() == search_input.lower()), None)

            if found:
                print("\n{:<20} {:<50}".format("Field", "Value"))
                print("-" * 70)
                for key, value in found.items():
                    print("{:<20} {:<50}".format(key, str(value)))
            else:
                print("Anime not found.")

        elif choice == 2:
            add_anime(anime_list)
        elif choice == 3:
            remove_anime(anime_list)
        elif choice == 4:
            print("\nCurrently Airing Anime:")
            found_any = False
            for anime in anime_list:
                if is_currently_airing(anime):
                    print(f"- {anime['Title']} ({anime['Episodes']} episodes)")
                    found_any = True
            if not found_any:
                print("No currently airing anime found.")
        elif choice == 5:
            show_all_anime(anime_list)
        elif choice == 6:
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

def main():
    anime_list = load_anime_data()
    search_anime(anime_list)

# Run the program
main()