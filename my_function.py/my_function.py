# Creating a function that prints all the days of the week
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday',
        'Sunday']


# Defining Function
def days_of_the_week(x):
    return x


print(days_of_the_week(days))  # Replace X with list - Days


# Creating a function that takes in a sentence and replaces every second word with the word “Hello”

def replace(sentence):  # Define function
    words = sentence.split(' ')  # Split() a sentence into a list of words
    list_odd = words[0::2]  # Every second word of the list
    final_list = []

    for word in list_odd:
        final_list.append(word)
        final_list.append('hello')

    final_string = " ".join(final_list)  # replaces

    print(final_string)


replace(input("\nPlease enter a sentence:"))
