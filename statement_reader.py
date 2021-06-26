# Importing Pandas to read CSV file
import pandas

# Assigning CSV File into Python and Assigning Column Names
df = pandas.read_csv('Apr27_May26.csv', 
            parse_dates=['Date'], 
            header=0, 
            names=['Date', 'Reference', 'Amount', 'Place', 'Foreign'])

# Category sums to append with the amounts after labeling:
sum_dictionary = {"groceries_sum" : 0, "eating_out_sum" : 0, "treats_or_snacks_sum" : 0, "alcohol_and_weed_sum" : 0, "electronics_sum" : 0, "home_sum" : 0, "dates_sum" : 0, "transportation_sum" : 0, "travel_sum" : 0, "miscellaneous_sum" : 0, "subscriptions_sum" : 0, "total" : 0}
label_dictionary = {"g":"groceries", "o":"eating_out", "k":"treats_or_snacks", "a":"alcohol_and_weed", "e":"electronics", "h":"home", "d":"dates", "t":"transportation", "l":"travel", "m":"miscellaneous", "s":"subscriptions"}

# Confirming data inputs to the user:
print("Let's start labelling your purchases :)!")
print("Reminder, the inputs are: ")
print("---------------")
print("g = Groceries")
print("o = Eating Out")
print("k = Treats / Snacks")
print("a = Alcohol & Weed")
print("e = Electronics")
print("h = Home")
print("d = Dates")
print("t = Transportation")
print("l = Travel")
print("m = Miscellaneous")
print("s = Subscriptions")
print("---------------")

# Looping through each line in the CSV file to enter category
for col, item in df.iterrows():
    labeled = False
    if (item[2] > 0): # This is to ignore all payments made to CC
        while labeled == False:
            print("Purchased from " + item[3] + " for $" + str(item[2]) + " on " + str(item[0]) + ".")
            print("Please categorize the following purchase: ")

            # User places their input through the following catch statement:
            category_signifier = input()

            if category_signifier in label_dictionary:
                    sum_label = label_dictionary[category_signifier]
                    sum_dictionary[sum_label+"_sum"] = sum_dictionary[sum_label+"_sum"] + item[2]
                    df.append({sum_label: item[3]}, ignore_index=True)
                    print("-------------------")
                    print("\n")
                    labeled = True
            elif category_signifier == 'i': # The user is able to disregard a purchase they do not want to label.
                    print("Purchase ignored.")
                    labeled = True
            else: # If the user has not entered 'i' or a valid option, the tool prompts them to play an input again.
                    print("!!! You entered an invalid label. Try again !!!")
                    # Confirming data inputs to the user:
                    print("---------------")
                    print("Reminder, the inputs are: ")
                    print("---------------")
                    print("g = Groceries")
                    print("o = Eating Out")
                    print("k = Treats / Snacks")
                    print("a = Alcohol & Weed")
                    print("e = Electronics")
                    print("h = Home")
                    print("d = Dates")
                    print("t = Transportation")
                    print("l = Travel")
                    print("m = Miscellaneous")
                    print("s = Subscriptions")
                    print("---------------")    

# The final sums that have been calculacted 
print("********************************************")
for item in sum_dictionary:
    if item == "Total":
        print("TOTAL: " + sum_dictionary["total"])
    else:
        print("* " + item + ": \t" + "$" + str(sum_dictionary[item]))
        sum_dictionary["total"] = sum_dictionary["total"] + sum_dictionary[item]


df.to_csv('bank_statement_python.csv')