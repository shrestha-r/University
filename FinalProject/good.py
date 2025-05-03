def input_account_type(choices):
    print("Choose your account type:")
    for idx, choice in enumerate(choices, 1):
        print(f"\t{idx}. {choice}")
    while True:
        choice = input(f">>>1-{len(choices)}: ").strip()
        if choice in [str(i) for i in range(1,len(choices)+1)]:
            return choices[int(choice)-1]
        print(f"Invalid choice. Please number between 1 to {len(choices)}")
print(input_account_type(["hi","hello","namaste"]))