# We will focus on python dictionary and the nesting
# We can also create a empty dictionary and then add elements
# Dictionary example :
programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.",
                          "Function": "A piece of code that you can easily call over and over again.",
                        }
programming_dictionary["Loop":"The action of doing something over and over again."] ## Adding data into a dictionary
# print(programming_dictionary)    ## Retrieving data from dictionary

## programming_dictionary = {}
## print (programming_dictionary)   ## this will make the dictionary empty and print the empty dictionary

programming_dictionary["Bug"] = "a moth in your computer" ## redefinition

## Loop through a dictionary
for key in programming_dictionary:
    print(key)    ## it will just print keys
    print(programming_dictionary[key])  ## this will give key with value
    
## Nesting Lists and Dictionaries
#Nesting list in dictionary
travel_log = {
    "France":["Parris","Lille"]
}

## Dictionary in dictionary