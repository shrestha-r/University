print("Nritya International Dance Academy")
print("Welcome to Nritya International Dance Academy.")

valid_dance_styles = [
    "Kathak dance",
    "Bharatnatyam dance",
    "Belly dance",
    "Hip hop dance",
    "Locking and popping",
    "Break dance",
    "Jazz",
    "Contemporary"
]

def save_admission_to_file(admission):
    # Save admission as comma-separated values in data.txt
    # Replace commas in user input to avoid CSV issues, or use another separator if you wish
    values = [
        str(admission["Id"]),
        admission["Name"].replace(",", " "),
        str(admission["Age"]),
        str(admission["Height"]),
        admission["Gender"],
        admission["Experience"].replace(",", " "),
        admission["Dance_Style"],
        admission["Father_Name"].replace(",", " "),
        admission["Mother_Name"].replace(",", " "),
        admission["Mobile_Number"],
        admission["Email_Address"].replace(",", " "),
        admission["Dance_Group"].replace(",", " "),
        str(admission["Is_Enrolled"])
    ]
    line = "|".join(values) + "\n"
    with open("data.txt", "a") as f:
        f.write(line)

def load_admissions_from_file():
    admissions = []
    try:
        with open("data.txt", "r") as f:
            for line in f:
                fields = line.strip().split("|")
                if len(fields) == 13:
                    admissions.append(fields)
    except FileNotFoundError:
        pass
    return admissions

while True:
    print("\nEnter 1 for new admission info")
    print("Enter 2 for admission of student")
    print("Enter 3 for student records")
    print("Enter 4 see types of dance styles with price")
    print("Enter 5 for dance teacher names")
    print("Enter 6 view for time details")
    print("Enter 7 for class section")
    print("Enter 8 for dance group")
    print("Enter 9 for discount information")
    print("Enter 10 for additional academy information")
    print("Enter 0 to Exit")

    try:
        num = int(input("enter number: "))
    except ValueError:
        print("Invalid input. Please enter a number between 0 and 10.")
        continue

    if num == 1:
        admission_info = {
            "required information",
            "student name",
            "age",
            "height",
            "experience",
            "father name",
            "mother name",
            "address",
            "mobile number",
            "email address",
            "date",
            "dance group",
        }
        print("\nRequired Admission Information:")
        for item in admission_info:
            print("-", item)

    elif num == 2:
        # Get and validate numeric ID
        while True:
            id_input = input("Enter ID (numbers only): ")
            if id_input.isdigit():
                id = int(id_input)
                break
            else:
                print("Invalid input. ID must be a number.")

        # Get and validate student name
        while True:
            name = input("Enter student name: ")
            if name.replace(" ", "").isalpha():
                break
            else:
                print("Invalid name. Only letters and spaces are allowed.")

        # Get and validate age
        while True:
            age_input = input("Enter student age: ")
            if age_input.isdigit():
                age = int(age_input)
                break
            else:
                print("Invalid input. Age must be a number.")

        # Get and validate height
        while True:
            height_input = input("Enter student height (e.g., 5.6): ")
            try:
                height = float(height_input)
                break
            except ValueError:
                print("Height must be a decimal number like 5.6")

        # Gender (simple input without restriction)
        gender = input("Enter student gender (M/F): ")

        # Experience
        experience = input("Enter experience (e.g., 2 years): ")

        # Show valid dance styles
        print("\nAvailable Dance Styles:")
        for style in valid_dance_styles:
            print(" -", style)

        # Dance style
        while True:
            dance_style_prices = input("Enter dance style (match exactly): ").strip()
            if dance_style_prices in valid_dance_styles:
                break
            else:
                print("Please enter a valid dance style from the list above.")

        # Guardian, father, mother names
        guardian_name = input("Enter guardian name: ")
        father_name = input("Enter father name: ")
        mother_name = input("Enter mother name: ")

        # Validate mobile number
        while True:
            mobile_number = input("Enter mobile number (digits only): ")
            if mobile_number.isdigit() and len(mobile_number) >= 7:
                break
            else:
                print("Invalid mobile number. Please enter at least 7 digits.")

        # Validate email address (basic)
        while True:
            email_address = input("Enter email address: ")
            if "@" in email_address and "." in email_address:
                break
            else:
                print("Invalid email address format.")

        # Date and group
        date_of_enrollment = input("Enter date of enrollment (e.g., 2024-05-01): ")
        dance_group = input("Enter dance group: ")

        # Enrollment flag
        is_enrolled = True

        # Display confirmation
        print(f"\nCongratulations to {name} for joining us!")
        print(f"Enrollment status for {name}: {'Enrolled' if is_enrolled else 'Not Enrolled'}")

        # Save data
        admission = {
            "Id": id,
            "Name": name,
            "Age": age,
            "Height": height,
            "Gender": gender,
            "Experience": experience,
            "Dance_Style": dance_style_prices,
            "Father_Name": father_name,
            "Mother_Name": mother_name,
            "Mobile_Number": mobile_number,
            "Email_Address": email_address,
            "Dance_Group": dance_group,
            "Is_Enrolled": is_enrolled
        }

        save_admission_to_file(admission)
        print(f"\nAdmission of {name} successfully recorded and saved to file.")

    elif num == 3:
        admissions = load_admissions_from_file()
        print("\n" + "=" * 120)
        print("STUDENT RECORDS FROM FILE")
        print("=" * 120)
        print("{:<5} {:<20} {:<5} {:<6} {:<6} {:<12} {:<15} {:<12} {:<12} {:<12} {:<25} {:<12} {:<10}".format(
            "ID", "Name", "Age", "Ht", "Gen", "Exp", "Dance Style", "Father", "Mother", "Mobile", "Email", "Group", "Enrolled"))
        print("-" * 120)
        if not admissions:
            print("No admissions found yet. Please add a student first.")
        else:
            for fields in admissions:
                print("{:<5} {:<20} {:<5} {:<6} {:<6} {:<12} {:<15} {:<12} {:<12} {:<12} {:<25} {:<12} {:<10}".format(*fields))
        print("=" * 120)

    elif num == 4:
        dance_style_prices = {
            "Kathak dance": 200.0,
            "Bharatnatyam dance": 250.0,
            "Belly dance": 300.0,
            "hip hop dance": 280.0,
            "locking and poping": 350.0,
            "break dance": 220.0,
            "jazz": 230.0,
            "contemporary": 210.0,
        }
        print("\nDance Styles and Prices:")
        for style, price in dance_style_prices.items():
            print(f"Dance Style: {style}, Price: ${price:.2f}")

    elif num == 5:
        Teachers_name = {
            "Saumya Maa": "kathak dance teacher",
            "Naresh Tharu": "Bharatnatyam",
            "Umesh dai": "Belly dance",
            "Manish Sah": "Hip hop",
            "Kushum Rai": "Locking and popping",
            "Jatin B": "Break dance",
            "Jasmine Rose": "Jazz",
            "Asmita Ch": "Contemporary",
        }
        for teacher, dance_form in Teachers_name.items():
            print(f"{teacher} teaches {dance_form}")

    elif num == 6:
        view_for_details = {
            "Kathak dance": "5am to 8am and 6pm to 9pm",
            "Bharatnatyam dance": "12pm to 3pm",
            "Belly dance": "4pm to 7pm",
            "hip hop dance": "10am to 1pm",
            "locking and popping": "8am to 2pm",
            "break dance": "2pm to 5pm",
            "jazz": "5pm to 9pm",
            "contemporary": "3pm to 9pm",
        }
        print("\nDance Class Timings:")
        for style, time in view_for_details.items():
            print(f"{style}: {time}")

    elif num == 7:
        class_section = {
            "Kathak dance": "Sec A",
            "Bharatnatyam dance": "Sec B",
            "Belly dance": "Sec C",
            "hip hop dance": "Sec D",
            "locking and poping": "Sec E",
            "break dance": "Sec F",
            "jazz": "Sec G",
            "contemporary": "Sec H",
        }
        print("\nDance Class Sections:")
        for style, section in class_section.items():
            print(f"{style}: {section}")

    elif num == 8:
        dance_group = {
            "Kathak dance": "group 31A and 32B",
            "Bharatnatyam dance": "41A and 42B",
            "Belly dance": "20A and 21B",
            "hip hop dance": "10a and 10B",
            "locking and poping": "1A and 2B",
            "break dance": "50A and 51B",
            "jazz": "60A and 61B",
            "contemporary": "70A and 71B",
        }
        print("\nDance Groups:")
        for style, group in dance_group.items():
            print(f"{style}: {group}")

    elif num == 9:
        print("\nDiscount Information:")
        print("10% discount for students under 10 years old.")
        print("15% discount for students who enroll in 2 or more dance styles.")
        print("20% family discount for siblings enrolled together.")
        print("5% discount for paying 3 months fee altogether.")
        print("12% discount for paying 6 months fee altogether.")
        print("25% discount for paying 1 year fee altogether.")

    elif num == 10:
        print("\nAcademy Information:")
        print("Opening Hours:")
        print("Monday to Saturday: 5:00 AM to 10:00 PM")
        print("Sunday: Closed")
        print("\nContact Information:")
        print("Phone: +44 7385811259")
        print("Email: asmita@nrityainternationaldanceacademy.com")
        print("Website: www.nrityainternationaldanceacademy.com")
        print("\nSpecial Announcements:")
        print("We are closed on major public holidays.")
        print("Please check our website or social media for holiday updates.")
        print("\nAdditional Information:")
        print("We offer online classes for international students.")
        print("New batches start every month.")
        print("Join us for our annual recital held in November!")

    elif num == 0:
        print("\nThank you for visiting Nritya International Dance Academy!")
        break

    else:
        print("Invalid input. Please enter a number between 0 and 10.")
