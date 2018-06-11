import datetime
default_names = ["Justin", "john", "Emilee", "Jim", "Ron", "Sandra", "veronica", "Whitney"]
default_amounts = [123.32, 94.23, 124.32, 323.4, 23, 322.122323, 32.4, 99.99]

unf_message = """Hi {name}! 
Thank you for the purchase on {date}. 
We hope you are excited about using it. Just as a
reminder the purchase total was ${total}.
Have a great one!
Team CFE
"""

def my_purchase(names,amounts):
    messages=[]
    if len(names)==len(amounts):
        i = 0
        for name in names:
           new_msg=unf_message.format(
                name=name[0].upper()+name[1:].lower(),
                total=amounts[i],
               date=datetime.date.today()

                )
           print(new_msg)

my_purchase(default_names,default_amounts)