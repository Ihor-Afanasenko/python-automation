print("Application launching ...")
user = input("Enter username")
# set breakpoint here to get "user" variable value. Just print it in Console
print(f'Hello {user}! Please choose a number:')
number = input("0-100")
if int(number) < 0 & int(number) > 100:
    pass
"""Add "pass" instruction on the last line of the script
to get "number" variable value in debug mode.
Set breakpoint on line with pass."""
