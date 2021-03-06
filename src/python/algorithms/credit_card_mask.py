# return masked string
def maskify(cc):
    length = len(cc)
    return ((length-4)*"#") + cc[-4:]

# Example:
#maskify("4556364607935616") == "############5616"
#maskify(     "64607935616") ==      "#######5616"
#maskify(               "1") ==                "1"
#maskify(                "") ==                 ""

# "What was the name of your first pet?"
#maskify("Skippy")                                   == "##ippy"
#maskify("Nananananananananananananananana Batman!") == "####################################man!"
