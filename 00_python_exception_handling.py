try:
    data = {'A':1,'B':2}
    print(data['A'])
    print(10/0)
except KeyError:
    print("Excetion in the code")
except ZeroDivisionError:
    print("ZeroDivisionError")
finally:
    print("Finally called")
    