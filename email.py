# An Email Simulation
# Creating a class definition
# This constructor takes in the sender's email address and initialises
class Email:

    def __init__(self, from_address):
        self.has_been_read = False  # email has  not being read
        self.email_contents = None
        self.is_spam = False  # email not a spam
        self.from_address = from_address

    # This method marks an email as read
    def mark_as_read(self):
        self.has_been_read = True

    # This function marks an email as spam
    def mark_as_spam(self):
        self.is_spam = True  # Means the email is a spam


inbox = []  # a list to store all emails


# A function that adds an email to the inbox list.
def add_email(contents, from_address):
    email = Email(from_address)
    email.email_contents = contents
    inbox.append(email)


# A function that returns the number messages in the store.
def get_count():
    return len(inbox)  # len() function to get the number of messages in the inbox


# A function that returns the contents of an email in the list and marks it as read.
def get_email(i):
    inbox[i].has_been_read = True
    return inbox[i].email_contents


# A function that returns a list of all the emails that haven’t been read.
def get_unread_emails():
    unread_emails = []
    for email in inbox:

        if not email.has_been_read:
            unread_emails.append(email)
            return unread_emails


# A function that returns a list of all the emails that have been marked as spam.
def get_spam_emails():
    spam_emails = []
    for email in inbox:
        if email.is_spam:
            spam_emails.append(email)
        return spam_emails


# A  function that  deletes an email from the inbox.
def delete(i):
    del inbox[i]


user_choice = ""

while user_choice != "quit":
    print('"')
    user_choice = input("What would you like to do - read/mark spam/send/quit?\n")
    # if user wants to read
    if user_choice == "read":
        count = get_count()  # get count of emails in the inbox
        if count == 0:  # if no message pass that to the user
            print("Sorry, No emails in inbox!\n")
        # If there are emails, show user the emails
        else:
            print(f"There are {count} emails in your inbox:\n")
            for x in range(count):
                print(f"{x}: {get_email(x)}")

    # if user wants to mark email as sperm
    elif user_choice == "mark spam":
        # Get the index of the email to be marked as spam
        count = get_count()  # get count of emails in the inbox
        if count == 0:  # if no message pass that to the user
            print("Sorry, No emails in inbox!\n")
        # If there are emails, show user the emails
        else:
            print(f"There are {count} emails in your inbox:\n")  # Display the emails to user
            for x in range(count):
                print(f"{x}: {get_email(x)}")

            index = int(input("Enter the number of the email you want to mark as spam \n"))
            if index >= len(inbox):
                print("You have selected a wrong number!!, Please Enter a number that is associated with a email as "
                      "displayed "
                      "above.")
            else:
                # Mark the email as spam
                inbox[index].mark_as_spam()
                print("The Email has been marked as spam!\n")

    # if user wants to send email
    elif user_choice == "send":
        from_address = input("Enter email address:\n ")
        contents = input("Enter email contents:\n")
        add_email(contents, from_address)  # Create email object and add it to inbox
        print("Email has been successfully sent!\n")

    # if user wants to quit
    elif user_choice == "quit":
        print("Goodbye!!\n")
    else:
        print("Oops - incorrect input\n")

# At This code I have only given the user 4 options to select from, We can still add more options by adding to the
# options and calling in a function and conditions to do what the user desires We can add options like delete emails
# option, view list of emails added to spam etc. but for the sake of this task I have limited to this options
