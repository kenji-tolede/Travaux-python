mot=input("entrez votre mot:")


def est_palindrome (s):
    return s == s [::-1]

s=mot
a=est_palindrome (s)

if a == True:
    print("est un mot palindrome")
else:
    print("n est pas palindrome, car a l envers il donne",s[::-1])
