#Try and Except With Loop--------------------------------
while True:
    try:
        nr = int(input("Enter one Number: "))
        s = nr * 3
        print(s)
        q = 12 / s
        print(q)
        print()

    except ValueError:
        print('Enter Valid Number!')
        print()
    except ZeroDivisionError:
        print("The Number Cannot be Zero!")
        print()
    else:
        print('Entered Else.')
        print()
        break
    finally:
        print('Entered Node Finally.')

#Try and Except-----------------------------------------
try:
    num = eval(input("Enter With One Number Whole: \n"))
    print(num)
except:
    print("Enter With The Value Numeric And Not Letter")

#01------------------------------------------------------
try:
    num = eval(input("Enter With One Number Whole: \n"))
    print(num)
except NameError:
    print("Enter With The Value Numeric And Not Letter")

#02------------------------------------------------------
try:
    num = eval(input("Enter With One Number Whole: \n"))
    print(num)

except ValueError:
    print("Message 1")
except IndexError:
    print("Message 2")
except:
    print("Message 3")