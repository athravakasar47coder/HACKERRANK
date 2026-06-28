# def swap_case(s):
#     for i in s:
#         if i.isupper():
#             i.lower()
#         else:
#             i.upper() 
            
#     return s

# if __name__ == '__main__':
#     s = "HackerRank.com presents \"Pythonist 2\"."
#     result = swap_case(s)
#     print(result)

s = "Hello"
s1 = ""
for i in s:
    if i.isupper():
        s1 += i.lower()
    else:
        s1 += i.upper()
        
print(s1)

