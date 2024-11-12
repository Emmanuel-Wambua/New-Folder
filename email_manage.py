class Email:
    has_been_read = False
    def __init__(self,email_address,subject_line,email_content):
        self.email = email_address
        self.subject = subject_line
        self.content = email_content
        self.has_been_read == False
        """
            Simple initialisation of the email and its
            parameters
        """
    def mark_as_read(self):
        self.has_been_read = True
        """
            This method is used to mark the email as read or not read
            it marks the email using booleans.If read mark TRUE and if
            not read mark false.
        """
    def get_subject(self):
        return self.subject
    """
        This is a simple method that allows the user to 
        retrieve the subject line of the email
    """
    def check_if_read(self):
        if (self.has_been_read == True):
            return f"{self.email} has been read"
        else:
            return f"{self.email} has not been read"
        """
            This method checks to see if an email has been marked as read
            by the user.It is first tried in an if/else statement
            and then returned to user
        """


class EmailManagement:
    def __init__(self):
        self.inboxes = []
        # Empty list to store all the dummy emails
    def populate_inbox(self,inbox):
        self.inboxes.append(inbox)
        """
            This block of code appends dummy emails to the 
            empty list that has been declared above.
        """
    def show_emails(self):
        for index,mail in enumerate(self.inboxes):
            sub = mail.get_subject()
            return (f"{index + 1}: {sub}")
        """
            This code block returns all the subject lines of the emails that
            have been stored in the list above.
        """
    def read_email(self,index):
        self.index = index
        return self.inboxes[index].email
        """
            This method allows the user to specify the specific
            index of the desired email 
        """

dummy1 = Email("mantelmanu31@gmail.com","Excursion","Go on a date with the homies")
dummy1.mark_as_read()
print(dummy1.check_if_read())
dummy2 = Email("charles69@gmail.com","Impossible","Go on a date with a girl")
dummy2.mark_as_read()
dummy3 = Email("cheli98@gmail.com","Reality","Stop being deluded")
print(dummy3.check_if_read())

invent = EmailManagement()
invent.populate_inbox(dummy1)
invent.populate_inbox(dummy2)
invent.populate_inbox(dummy3)

# print(invent.inboxes[1].email)
# print(invent.show_emails())
# print(invent.read_email(1))