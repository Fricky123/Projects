import linecache

logged_account = None
position = -1
# ------------------------------------------------------------------------
'''Main Functions'''

def intro():
    separate()
    print('[INTRO]\n\n'
          'Login or Create/Register Account?')

    x = input('Input: ').lower()
    if 'login' in x:
        login()
    elif 'create' in x or 'register' in x:
        register()
    else:
        invalid('invalid')
        intro()

def login():
    global logged_account, position

    username_found = False

    separate()
    print('[LOGIN]\n')

    with open('accounts_for_password_manager.txt', 'r') as a_r:
        accounts = a_r.readlines()

        username = input('Input username: ').lower()

        try:
            position = -1
            for account in accounts:
                position += 1
                if username == account.split(' ')[0]:
                    username_found = True
                    break

        except IndexError:
            invalid('username_not_found')
            intro()

        if username_found:
            with open('accounts_for_password_manager.txt', 'r') as a_r2:
                accounts = a_r2.readlines()
                x = accounts[position].split()[-1]

                password = input('Input password: ').lower()

                if password == x:
                    logged_account = username
                    print('Login Successful...')
                    main()

                else:
                    invalid('wrong_password')
                    intro()

        else:
            invalid('username_not_found')
            intro()

def register():
    proceed = False
    separate()
    print('[REGISTER]\n')

    new_username = input('Create username: ').lower()

    with open('accounts_for_password_manager.txt', 'r') as a_r:
        accounts = a_r.readlines()

        if accounts:
            for account in accounts:
                if new_username == account.split(' ')[0]:
                    invalid('username_taken')
                    intro()
                else:
                    proceed = True
                    break
        else:
            proceed = True

    if proceed is True:

        new_password = input('Create password: ').lower()
        confirm_password = input('Confirm password: ').lower()

        if new_password != confirm_password:
            invalid('wrong_confirm_password')
            intro()

        else:
            with open('accounts_for_password_manager.txt', 'a') as a:
                a.write(f'{new_username} | {new_password} \n')

            with open('accounts_for_password_manager.txt', 'r') as a_r:
                accounts = a_r.readlines()

                username_found = False
                for account in accounts:
                    if new_username == account.split(' ')[0]:
                        username_found = True

                if username_found:
                    input('[Registration Success] Press any key to continue> ')
                    intro()
                else:
                    input('[Registration Error, Something went wrong] Press any key to continue> ')

def main():
    separate()
    print(f'Welcome, {logged_account}!\n\n'
          f'[1] Reset Password\n')

    x = input('Choice> ').lower()

    if x == ' ':
        invalid('empty')
        main()
    elif '1' in x or 'reset' in x:
        reset_pass()
    else:
        invalid('invalid')

def reset_pass():
    separate()
    print('[RESET PASSWORD]\n')

    x = input('Enter current password: ')

    with open('accounts_for_password_manager.txt', 'r') as a:
        if x != a.readlines()[position].split()[-1]:
            invalid('wrong_password')
            main()
        else:
            y = input('Enter new password: ').lower()
            z = input('Confirm new password: ').lower()

            if y != z:
                invalid('wrong_confirm_password')
                main()
            else:
                with open('accounts_for_password_manager.txt', 'r') as a_r:
                    pass

# ------------------------------------------------------------------------
'''Utility Functions'''
def separate(): print('---------------------------------------------------------')

def invalid(error):
    if error == 'empty':
        input('[Empty Input] Press any key to continue> ')

    elif error == 'username_not_found':
        input('[Username Not Found] Press any key to continue> ')

    elif error == 'wrong_password':
        input('[Wrong Password] Press any key to continue> ')

    elif error == 'username_taken':
        input('[Username Taken] Press any key to continue> ')

    elif error == 'wrong_confirm_password':
        input('[Wrong Confirmation Password] Press any key to continue> ')

    elif error == 'invalid':
        input('[Invalid Input] Press any key to continue> ')
# ------------------------------------------------------------------------
'''sequence'''
intro()

# make invalid func to method
#  fix index error finding password in file