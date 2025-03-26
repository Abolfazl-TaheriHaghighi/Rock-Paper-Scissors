from random import randint
import os

def Menu():
    while True:
             y = input(f"\nType your choice or select it with the appropriate number in the menu\n 1_Rock\n 2_Paper\n 3_Scissors\n 4_Help\n 0_Exit(Close Game)\n >>")
             x = y.lower()
             if x in ['1' , '2' , '3'  , '4']:
                 return x
             elif x in ["rock" , "paper" , "scissors" , "help"]:
                 return x
             elif x in ["exit" , "0"]:
                  input("Press 'Enter' to exit.")
                  exit()
             else:
                  os.system("cls" if os.name == "nt" else "clear")
                  print(f"\nYou entered something unrelated.")



def Help():
    os.system("cls" if os.name == "nt" else "clear")
    print("""
 Welcome to Rock, Paper, Scissors Game! 🎮

🔹 **How to Play:**  
- Choose an option by typing the number or its name.  
  1️⃣ Rock  
  2️⃣ Paper  
  3️⃣ Scissors  

🔹 **Rules:**  
- Rock beats Scissors (Rock wins 🏆)  
- Scissors beats Paper (Scissors wins ✂️)  
- Paper beats Rock (Paper wins 📜)  
- If both players choose the same option, it's a draw!  

🔹 **Scoring System:**  
- Win: +3 points  
- Draw: +1 point  
- Lose: 0 points  

🔹 **Winning the Game:**  
- The first to reach **50 points** wins the game!  

🔹 **Other Commands:**  
- Type **"Exit"** or **"0"** to quit the game.  
- Type **"Return"** or **"1"** to return to the main menu. 


Good luck! 🚀  
        """)
    x = input(f"Select or type the desired option\n>>")
    d = x.lower()
    if d in ['exit' , '0']:
        input("Press 'Enter' to exit.")
        exit()
    elif d in ['back' , '1']:
        main()
    
        
        

def ai():
    z = ["rock" , "paper" , "scissors"]
    s = (z[randint(0,2)])
    return s



def main():
    Your_rating = 0
    Computer_rating = 0

    while True:
        Choice_User = Menu()
        Choice_ai = ai()

        if Choice_User in ['rock' , '1'] and Choice_ai == 'paper':
              os.system("cls" if os.name == "nt" else "clear")
              Computer_rating = Computer_rating + 3
              print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
              print("You lost ! ")
              print(f"Your Choice : Rock\nChoosing computer: Paper")


        elif Choice_User in ['rock' , '1'] and Choice_ai == 'scissors':
             os.system("cls" if os.name == "nt" else "clear")
             Your_rating = Your_rating + 3
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("You won !")
             print(f"Your Choice : Rock\nChoosing computer: Scissors")


        elif Choice_User in ['rock' , '1'] and Choice_ai == 'rock':
             os.system("cls" if os.name == "nt" else "clear")
             Your_rating = Your_rating + 1
             Computer_rating = Computer_rating + 1
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("The choices were the same, the game is even.")
             print(f"Your Choice : Rock\nChoosing computer: Rock")
             




        elif Choice_User in ['paper' , '2'] and Choice_ai == 'rock':
             os.system("cls" if os.name == "nt" else "clear")
             Your_rating = Your_rating + 3
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("You won !")
             print(f"Your Choice : Paper\nChoosing computer: Rock")


        elif Choice_User in ['paper' , '2'] and Choice_ai == 'scissors':
             os.system("cls" if os.name == "nt" else "clear")
             Computer_rating = Computer_rating + 3
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("You lost ! ")
             print(f"Your Choice : Paper\nChoosing computer: Scissors")


        elif Choice_User in ['paper' , '2'] and Choice_ai == 'paper':
             os.system("cls" if os.name == "nt" else "clear")
             Your_rating = Your_rating + 1
             Computer_rating = Computer_rating + 1
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("The choices were the same, the game is even.")
             print(f"Your Choice : Paper\nChoosing computer: Paper")




        elif Choice_User in ['scissors' , '3'] and Choice_ai == 'paper':
             os.system("cls" if os.name == "nt" else "clear")
             Your_rating = Your_rating + 3
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("You won !")
             print(f"Your Choice : Scissors\nChoosing computer: Paper")


        elif Choice_User in ['scissors' , '3'] and Choice_ai == 'rock':
             os.system("cls" if os.name == "nt" else "clear")
             Computer_rating = Computer_rating + 3
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("You lost ! ")
             print(f"Your Choice : Scissors\nChoosing computer: Rock")


        elif Choice_User in ['scissors' , '3'] and Choice_ai == 'scissors':
             os.system("cls" if os.name == "nt" else "clear")
             Your_rating = Your_rating + 1
             Computer_rating = Computer_rating + 1
             print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
             print("The choices were the same, the game is even.")
             print(f"Your Choice : Scissors\nChoosing computer: Scissors")
        

        elif Choice_User in ['4' , 'help']:
             Help()
             continue





        if Computer_rating >= 50 or Your_rating >= 50 :

            if Computer_rating >=50 and Computer_rating > Your_rating:
                 os.system("cls" if os.name == "nt" else "clear")
                 print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
                 print (f"The computer won the game by {Computer_rating} points and the game was over.")
                 break
            
            elif Your_rating >= 50 and Your_rating > Computer_rating:
                 os.system("cls" if os.name == "nt" else "clear")
                 print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
                 print(f"You won the game by {Your_rating} points and the game is over.")
                 break
            
            elif Your_rating == Computer_rating and Your_rating >= 50 and Computer_rating >= 50:
                 os.system("cls" if os.name == "nt" else "clear")
                 print(f"Computer rating:{Computer_rating}          Your rating:{Your_rating}")
                 print("The game is over, but since the points are tied, the game continues until one person wins.")
                 continue
                 
            
    
    while True:
         e = input(f"Do you want to try again?\n1_Yes\n2_No \n(Type or select the desired option.)\n>>")
         ee = e.lower()
         if ee in ['yes' , 'y' , '1']:
              os.system("cls" if os.name == "nt" else "clear")
              main()
         else:
              os.system("cls" if os.name == "nt" else "clear")
              input("Press 'Enter' to exit.")
              exit()
               
main()


#Abolfazl Taheri Haghighi
#Bachelor's student of statistics at Fasa University
# v1.0.0