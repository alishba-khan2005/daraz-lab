

print("--------------DARAZ-------------")
name=str(input("enter your name"))
email=str(input("enter your email: "))
contact=int(input("enter your phone number: "))
country=str(input("enter your country: "))
city=str(input("enter your city: "))

print("category1:  foundation suncreen feminine products category2 men shoe face wash vase category3 straightner computer phone")
print ("select your category")
category1=["foundation", "sunscreen", "feminine products"]
category2=["men shoe", "face wash", "vase"]
category3=["straightner", "computer", "phone"]

choice=str(input("enter 1 till 3: "))

if choice==1:
   print(category1)
elif choice==2:
   print(category2)
elif choice==3:
   print(category3 )

category1=str(input("enter this category product or skip : "))
category2=str(input("enter this category product or skip: "))
category3=str(input("enter this category product or skip: "))

if(category1=="foundation"or"sunscreen"or"feminine product"or category2=="men shoes"or"face wash"or"vase"or category3=="styraightner"or"computer"or"phone"):
    print("your item is purchased")
    paymentmethod=str(input("enter payment mehtod: "))
    print("thankyou for shopping")
    