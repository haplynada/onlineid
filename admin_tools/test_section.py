from test.test_OTP import menu as otp_menu

def test_menu():
    while True:

        print("\nTest section:\n"
              "1. Test OTP\n"
              "Q. Go back")
        selection = input("")

        if selection == "1":
            otp_menu()
        elif selection == "2":
            pass
        elif selection == "3":
            pass
        elif selection == "q" or selection == "Q":
            break

if __name__ == "__main__":
    while True:
        test_menu()