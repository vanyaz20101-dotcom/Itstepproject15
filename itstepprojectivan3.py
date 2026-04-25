#try:
#    num = int(input("Enter number: "))
#    print(8/num)
#except:
#    print("Invalid input")
#try:
#    count = int(input("Enter a number: "))
#    type_box = input("Enter a number: ")
#    print(f"We got {type_box} in {count}")
#    avg_count = count // int(input("enter amount of parts: ")
#except ZeroDivisionError:
#    print("You can't divide by zero")
#except ValueError:
#    print("Invalid input, try again, first count then type")
#except Exception as e:
#    print("Something went wrong", e)
#finally:
#    print("Goodbye")
#try:
#    num = int(input("Enter number: "))
#    print("You entered: ", num)
#except ValueError:
#        print("Invalid input, enter a number")
#while True:
#    try:
#       num = int(input("Enter a number: "))
#        print(f"You entered: {num}")
#        break
#    except ValueError:
#        print("Error, try again.")
#my_list = ["apple", "banana", "cherry"]

#try:
#    index = int(input("Enter index: "))
#    print(f"Element: {my_list[index]}")
#except ValueError:
#    print("You need to enter a number!")
#except IndexError:
#    print("This index doesn't exist")
#except Exception as e:
#    print("Something went wrong:", e)
