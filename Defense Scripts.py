# The user is warned if common phishing phrases are found in an email
# (Only a warning due to legitimate emails sometimes containing these words/phrases)
def phishing_warning(emailSubject):
    try:
        flag = False; #Flag to track if the email is suspected of phishing or not
        subject= emailSubject.lower().strip()
        # Common themes in phishing emails:
        # Making it seem like the msg need to be addressed quickly
        # A "Request" or "Follow up" to make it seem like the user missed or forgot something important/useful
        if (subject == "urgent" or subject == "important" or subject == "request" or subject == "follow up"):
            flag= True
            print("Warning: Potential phishing Email")
        return flag
    except Exception as e:
        print("Error: {e}")
        return False # If email subject is unreadable or invalid

# Input validation is important for many reasons
# This function primarily focuses on input validation relating to prevnetion of SQL Injection attacks
def input_validation(input):
    try:
        flag = False; #Flag to track if the input is valid or not
        if(input.find("*")!=-1): #Stars are not allowed as input as they could be used for SQL injection attack
            flag= False
        if(input.find("DROP")!=-1 or input.find("SELECT")!=-1 or input.find("FROM")!=-1): #Key words in SQL are not allowed as input
            flag= False
            print("Warning: Potential SQL Injection attack attempt")
        
        return flag

    except Exception as e:
        print("Error: {e}")
        return False #Unreadable or invalid input