""" ChatBot project """

bot_name = 'Ayanami Rei'
birth_year = 2045

print(f"Hello! My name is {bot_name}")
print(f"I was created in {birth_year}")
your_name = input("Please, remind me your name, kind sir\n")
print(f"What a great name you have, {your_name}")
print("Let me guess your age.")
print("Enter remainders of dividing your age by 3, 5 and 7.")
rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
your_age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print(f"Your age is {your_age}; that's a good time to start programming!")
print("Now I will prove to you that I can count to any number you want.")
num = int(input())
for i in range(num+1):
    print(str(i) +'!')

print("Let's test your programming knowledge.")
print("Who is the best anime girl?")
print("1. Shoko Nishimiya")
print("2. Robert E.O. Speedwagon")
print("3. Ayanami Rei")
print("4. Makima")
while True:
    ans = int(input())
    if ans != 3:
        print("Try again")
    else: break
print("Completed, have a nice day!")
