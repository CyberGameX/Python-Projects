import pyfiglet
import os


class Login:
    error = None

    def __init__(self, log_usr_data, log_usr_password):
        self.log_usr_data = 'admin'  # You can change it
        self.log_usr_password = 'root'  # You can change it
        Login.error = 'Enter a valid username and password'

    def authenticate(self):
        if self.log_usr_data == login_user and self.log_usr_password == login_pas:
            print(f'Welcome {self.log_usr_data}')
            while True:
                print("Options:")
                print("1. Google")
                print("2. Amazon")
                print("3. Ebay")
                print("4. Password manager exit")

                option = int(input("Choose a option: "))
                os.system("cls")

                if option == 1:
                    banner_google = pyfiglet.figlet_format("GOOGLE")
                    print(banner_google)
                    google_email = 'xxxx@gmail.com'  # Change it
                    google_password = 'qwertz12345'  # Change it
                    print(google_email)
                    print(google_password)
                elif option == 2:
                    banner_amazon = pyfiglet.figlet_format("AMAZON")
                    print(banner_amazon)
                    amazon_email = 'xxxx@gmail.com'  # Change it
                    amazon_password = 'qwertz12345'  # Change it
                    print(amazon_email)
                    print(amazon_password)
                elif option == 3:
                    banner_ebay = pyfiglet.figlet_format("EBAY")
                    print(banner_ebay)
                    ebay_email = 'xxxx@gmail.com'  # Change it
                    ebay_password = 'qwertz12345'  # Change it
                    print(ebay_email)
                    print(ebay_password)
                elif option == 4:
                    print("Password manager exit.")
                    break
                else:
                    print("Invalid option !")

        else:
            print(Login.error)


log = Login("", "")
banner = pyfiglet.figlet_format("LOGIN")
print(banner)
login_user = input("Username: ")
login_pas = input("Password: ")

log.authenticate()
