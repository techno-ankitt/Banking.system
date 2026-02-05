# bank system

real_username = "admin"
real_pin = 1234

max_attempts = 3
attempts = 0

total_amount = 10000

def print_info(total_amount):
      print(f'''
            acount_holder = "ankit suthar"
            total_amount = {total_amount}
            ''')
      
def input_amount():
    while True:
        try:
            enter_amount = int(input("Enter Amount: "))
            return enter_amount
        except ValueError :
            print("amount must be a number")
        
     

def ankit(attempts, max_attempts, total_amount):

    while attempts < max_attempts:
          print('''"Welcome to the "Ankit Digital's Bank"''')
        user_username = str(input("Apna name enter karein: "))
        user_pin = int(input("Pin no. dalein: "))

        if user_username == real_username and user_pin == real_pin:
            print("Login successfully...")
            print_info(total_amount)

            while True:  # ye isliye ki bar bar input le ske
                enter_amount = input_amount()

                if  enter_amount > total_amount :
                    print("insfficiend fund.....")
                    
                elif enter_amount < 1000:
                    print("Are ", enter_amount, " se kya hoga fir soch lo") 
                else:    
                    print("Ha ye theek hai.")
                    print(" payment successful", enter_amount)
                    total_amount = total_amount - enter_amount
                    print("Ab aapke paas ",total_amount, "rupee bache hai.")
                    break
            return
        else:
            attempts += 1
            print("try again")



ankit(attempts, max_attempts, total_amount)








