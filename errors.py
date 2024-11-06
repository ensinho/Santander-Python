# Here lets check some try errors checking !

try:
    # code that can have an outlier
    result = 10 / 0 # it will crash, so just ajust your code to an reasonable operation hehe
    print(result)
except ZeroDivisionError:
    print("Error: Dividing by Zero!!!")
finally:
    print("We're done! ") # A part of the code that will ALWAYS execute!

''' You can add too an new except error
Like except ValueError:
        print("error: INvalid value!!!")'''


# creating an custom error, for your code only
number = 2
def function():
    # Code that can give an especific error
    if number < 0:
        raise Exception("Error description")

try:
    function()
except Exception as e:
    print(f"Erro: {str(e)}")

    


