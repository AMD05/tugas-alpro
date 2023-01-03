import view
import operasi

if __name__ == "__main__":
    while True:
        view.menu()
        user_option = input("masukan opsi ")

        if user_option == "1":
            operasi.create_console()
            continue

        elif user_option == "2":
            operasi.read_console()
            continue
        
        elif user_option == "3":
            operasi.update_console()
            continue

        elif user_option == "4":
            operasi.delete_console()
            continue
        
        elif user_option == "5":
            break
        
        else :
            print("opsi tidak ditemukan")
