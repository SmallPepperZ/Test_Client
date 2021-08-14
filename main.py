import tkinter as tk

import requests

main = tk.Tk()
main.title("FerrisChat")
main.geometry("1440x1080")

username_input = tk.StringVar()
password_input = tk.StringVar()
email_input = tk.StringVar()


def create_account():
    username = username_input.get()
    email = email_input.get()
    password = password_input.get()
    account_creation_post = requests.post("https://api.ferris.chat/api/v0/users", json={
        "username": username,
        "password": password,
        "email": email
    }
                                          )
    print(account_creation_post.json())


username_label = tk.Label(main, text="Username:")
email_label = tk.Label(main, text="Email:")
password_label = tk.Label(main, text="Password:")

username_entry = tk.Entry(main, textvariable=username_input, justify=tk.CENTER)
email_entry = tk.Entry(main, textvariable=email_input, justify=tk.CENTER)
password_entry = tk.Entry(main, textvariable=password_input, show="*", justify=tk.CENTER)

button = tk.Button(main, text="Create account", command=create_account)

email_label.grid(row=1, column=1)
username_label.grid(row=2, column=1)
password_label.grid(row=3, column=1)

email_entry.grid(row=1, column=2)
username_entry.grid(row=2, column=2)
password_entry.grid(row=3, column=2)
button.grid(row=4, column=2)

main.mainloop()
