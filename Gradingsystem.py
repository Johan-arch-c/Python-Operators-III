print("enter marks obtained in 5 subjects:")
markOne=int(input("enter marks obtained in math"))
markTwo=int(input("enter marks obtained in english"))
markThree=int(input("enter marks obtained in art"))
markFour=int(input("enter marks obtained in english"))
markFive=int(input("enter marks obtained in geography"))
tot=markOne+markTwo+markThree+markFour+markFive
avg=tot/5

if avg>=91 and avg<=100:
    print("your grade is A1")
elif avg>=81 and avg<=91:
    print("your grade is A2")
elif avg>=71 and avg<=81:
    print("your grade is B1")
elif avg>=61 and avg<=71:
    print("your grade is B2")
elif avg>=51 and avg<=61:
    print("your grade is C1")
elif avg>=41 and avg<=51:
    print("your grade is C2")
elif avg>=33 and avg<=41:
    print("your grade is D")
elif avg>=21 and avg<=33:
    print("your grade is E1")
elif avg>=0 and avg<=21:
    print("your grade is E2")
else:print("invalid Input!")