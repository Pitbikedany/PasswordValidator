import getpass

def password(pw):
    pw_upper = any(rules.isupper() for  rules in pw)
    pw_lower = any(rules.isupper() for  rules in pw)
    pw_digits = any(rules.isdigit() for rules in pw)
    pw_char_set = set('!@#$%^&*()-_+=<>?/[]{}|\\:;\'",.')    
    pw_char = any(rules in pw_char_set for rules in pw)
    
    i = 0
    while i < len(pw):
        i+=1 

    if pw_upper and pw_lower and pw_digits and pw_char and i>=8:
        print('Sucesso')
    else: 
        print('Insucesso')  


pw = getpass.getpass(prompt='Password: ')

password(pw)