def main():
    mainMenu()


def mainMenu():
    print("""SQL Faker Populate
          1. Create Tables
          2. Populate Tables
          3. Wipe Tables
          4. Drop Tables
          """)
    option = int(input('Enter your choice: '))
    print("selected option: ", option)


# run script
main()
