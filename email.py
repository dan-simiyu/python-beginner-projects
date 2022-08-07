email = input("Enter your email: ").strip()
username = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
print(f"Your username is {username} and your domain is {domain_name}")
