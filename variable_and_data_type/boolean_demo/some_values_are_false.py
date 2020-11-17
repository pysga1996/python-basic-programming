# In fact, there are not many values that evaluates to False, except empty values, such as (), [], {}, "",
# the number 0, and the value None. And of course the value False evaluates to False.
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})


# One more value, or object in this case, evaluates to False,
# and that is if you have an objects that are made from a class with a __len__ function that returns 0 or False:
class MyClass:
    def __len__(self):
        return 0


myObj = MyClass()
print(bool(myObj))
