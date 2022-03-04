    def check_password(pw):
        num = [int(i) for i in pw if i.isdigit()]
        for i in "!@#$%*":
            if i in pw:
                if len(num) >= 3:
                    if len(pw) >= 10 and pw.lower() != pw:
                        print('Perfect password')
                        break
        else:
            print('Easy peasy')


check_password(input())
