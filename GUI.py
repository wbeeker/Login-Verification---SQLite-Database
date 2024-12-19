import tkinter as tk
from main import *
from tkinter import messagebox


def create_login_window():
    # Login window
    login_window = tk.Tk()
    login_window.title("Login")

    # Username field
    tk.Label(login_window, text="Username").grid(row=0, column=0)
    username_entry = tk.Entry(login_window)
    username_entry.grid(row=0, column=1)

    # Password field
    tk.Label(login_window, text="Password").grid(row=1, column=0)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if login_verification(username, password):
            messagebox.showinfo("Login Successful", f"Login successful, {username}!")
        else:
            messagebox.showinfo("Login Failure", "Login failed. Either username or password incorrect")

    def create_account_window():
        # Open a new window for account creation
        account_window = tk.Toplevel(login_window)
        account_window.title("Create new account")

        account_window.geometry("400x300")

        # Fields for account creation
        fields = ["First_Name", "Last_Name", "Age", "Email", "Username", "Password"]
        entries = {}
        for i, field in enumerate(fields):
            label = tk.Label(account_window, text=f"{field}:")
            label.grid(row=i, column=0, sticky="w")
            entry = tk.Entry(account_window)
            entry.grid(row=i, column=1)
            entries[field] = entry

        def submit_account():
            filled_entries = {field: entries[field].get() for field in fields}
            if create_user_account(filled_entries):
                username = filled_entries["Username"]
                messagebox.showinfo(f"Account Created", f"Account successfully created, {username}")
                account_window.destroy()
            else:
                messagebox.showinfo("Username taken", "Account username is already in use!\n\n\n")

        tk.Button(account_window, text="Create Account", command=submit_account).grid(row=len(fields), columnspan=2)

    tk.Button(login_window, text="Login", command=login).grid(row=2, columnspan=2)
    tk.Button(login_window, text="Create Account", command=create_account_window).grid(row=3, column=2)

    login_window.mainloop()



