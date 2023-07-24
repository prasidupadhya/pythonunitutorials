#Computer Seminar – User-Defined Functions (Week 8)

#PART 1 - Review of Functions (with/without parameters)


#a)def greet_user():"""Display a simple greeting."""
#print("Hello!")
#greet_user() # call function



#b)def greet_user(username):
    #"""Display a simple greeting."""
    #print("Hello, " + username + "!")

#user = input('Enter your name: ')
#greet_user(user) # call function



#c)def describe_pet(animal_type, pet_name):
    #"""Display information about a pet."""
    #print("My " + animal_type + "'s name is " + pet_name + ".")

#describe_pet('dog', 'Fido')
#describe_pet('cat', 'Felix')
#describe_pet('dog', 'Rex')
#describe_pet('hamster', 'Bob')



#d)def multiplication(ntimes):
    #for i in range(1,13):
        #print(f"{ntimes} x {i} = {ntimes*i}")

#multiplication(7)



#PART 2 - Returning data from functions


#a)Convert a mark to a grade:
#def convertMark(mark):
    #if mark >= 70:
        #print("First")
    #elif mark >= 60:
        #print("2:1")
    #elif mark >= 50:
        #print("2:2")
    #elif mark >= 40:
        #print("Third")
    #else:
        #print("Fail")

#convertMark(75)
#convertMark(42)
#convertMark(55)




#b)Negative, Positive, Zero – using return
result = negativePositiveZero(-25.7)
print('-25.7 is', result)
result = negativePositiveZero(0.0)
print('0.0 is', result)
result = negativePositiveZero(123.45)
print('123.45 is', result)
# Get user input and call the function.
userValue = input('Enter a number: ')
userValue = float(userValue)
userResult = negativePositiveZero(userValue)
print(userValue, 'is', userResult)









