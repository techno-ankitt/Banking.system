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
            enter_amount = int(input("Abe kitne paise mangta hai: "))
            if enter_amount <= 0:
                print("Amount positive hona chahiye!")
                continue
            return enter_amount
        except ValueError :
            print("amount must be a number")
        
     

def ankit(attempts, max_attempts, total_amount):

    while attempts < max_attempts:
        print('''"Welcome to the "Ankit Digital's Bank"''')
        user_username = str(input("Tera naam kya hai re: "))
        user_pin = int(input("Chal pin bol: "))

        if user_username == real_username and user_pin == real_pin:
            print("Login successfully...")
            print_info(total_amount)

            while True:  # ye isliye ki bar bar input le ske
                enter_amount = input_amount()

                if  enter_amount > total_amount :
                    print("tere paas paise hi nhi hai.....")
                    
                elif enter_amount < 1000:
                    print("Abe ", enter_amount, " se kya hoga fir soch le") 
                else:    
                    print("Ha ye theek hai.")
                    print(" payment successful", enter_amount)
                    total_amount = total_amount - enter_amount
                    print("Ab tere paas ",total_amount, "rupee bache hai.")
                    break
            return
        else:
            attempts += 1
            print("try again")
    print("Acount Temporary Locked!")

ankit(attempts, max_attempts, total_amount)








