# Clasify a person age group: child(<13), teenager(13-19), Adult(20-59),Senior(60+)

# your_age = 
your_age_int = int(input("enter your age : "))


if your_age_int < 13 : 
    print("child")
elif your_age_int < 20 : 
    print("teenager")
elif your_age_int < 60 :
    print("adult")
else : 
    print("senior")            