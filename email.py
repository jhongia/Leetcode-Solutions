'''
Jhon Garcia
CS435 Recitation - 09/15/2021

Unique Email Addresses:

Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each email[i], return the number of different addresses that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

Constraints:

1 <= emails.length <= 100
1 <= emails[i].length <= 100
email[i] consist of lowercase English letters, '+', '.' and '@'.
Each emails[i] contains exactly one '@' character.
All local and domain names are non-empty.
Local names do not start with a '+' character.
'''

import re

def check_constraints(emails):
    '''Function checks for all constraints.'''
    if(len(emails) >= 1 and len(emails) <= 100):
        print("array length >= 1 or <= 100.")

        # Flag to keep track whether to return true or false
        flag = True

        for email in emails:
            if(len(email) >= 1 and len(email) <= 100):
                print(email + " length is >=1 or <= 100")

            else:
                flag = False
                break

            if(("+" in email or "." in email) and "@" in email):
                print("email contains +, . and @.")

            else:
                flag = False
                break

            if(email.islower()):
                print("email only contains lowercase letters.")

            else:
                flag = False
                break
            
            if(email.count("@") == 1):
                print("email contains only 1 @.")

            else:
                flag = False
                break

            if(email.count(" ") == 0):
                print("email does not have a space.")

            else:
                flag = False
                break
            
            if(email[0] != "+"):
                print("email does not start with a +.")
            
            else:
                flag = False
                break

            localname = email.split("@")[0]
            domain = email.split("@")[1]

            if(localname != "" and domain != ""):
                print("local name and domain are not empty.")

            else:
                flag = False
                break

        if(flag):
            return True

def email_checker(email):
    reg = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    if(re.fullmatch(reg, email)):
        return True
 
    else:
        return False
    
def correct_format(emails):
    '''Function that corrects the email format.'''
    result = check_constraints(emails)
    if(result):
        print("Array passed all constraints")
        receive_emails = []
        for email in emails:
            localname = email.split('@')[0]
            domain = email.split('@')[1]

            # This string ignore dots
            nodot_localname = localname.replace('.',"")
            # This string ignore everything after the first +
            nochar_afterplus = nodot_localname.split("+", 1)[0]

            correct_email = nochar_afterplus + '@' + domain

            if(email_checker(correct_email)):
                if(correct_email not in receive_emails):
                    receive_emails.append(correct_email)

        print(' and '.join(map(str, receive_emails)) + " actually receive mails.")
        print(str(len(receive_emails)) + " emails.")


        
emails = ["cfd.cf@fj", "test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com",
          "kkk.fff+grio@ccc", "ienf1+39.e@lk.koc"]
correct_format(emails)
