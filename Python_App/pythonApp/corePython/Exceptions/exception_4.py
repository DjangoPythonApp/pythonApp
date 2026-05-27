

while True:
    try:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Create Student")
        print("2. Read Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            create_student()

        elif choice == 2:
            read_students()

        elif choice == 3:
            update_student()

        elif choice == 4:
            delete_student()

        elif choice == 5:
            search_student()

        elif choice == 6:
            print("Program Exited")
            logging.info("Program terminated")
            break

        else:
            print("Invalid Choice")
            logging.warning("Invalid menu choice entered")

    except ValueError:
        print("Please enter numeric choice only")
        logging.error("Non-numeric menu choice entered")