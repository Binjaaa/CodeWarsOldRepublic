# return masked string
def maskify(cc):
    length = len(cc)
    if length < 4:
        return cc
    else:
        return ((length-4)*"#") + cc[(length-4):]



# Example:
#maskify("4556364607935616") == "############5616"
#maskify(     "64607935616") ==      "#######5616"
#maskify(               "1") ==                "1"
#maskify(                "") ==                 ""

# "What was the name of your first pet?"
#maskify("Skippy")                                   == "##ippy"
#maskify("Nananananananananananananananana Batman!") == "####################################man!"
