from tkinter import *
from tkinter import messagebox
from datetime import datetime
import pandas
import csv
import json

check_box = []
labels = []
user_nam = ''


class User:
    def __init__(self, window, canvas, c1, c2, c3):

        self.window6 = None
        self.canvas = canvas
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.user_log = Button(window, text="Login", width=15, fg="White", bg="black", highlightthickness=0,
                               command=self.user_login)
        self.button2 = Button(window, text="Register", width=15, fg="White", bg="black", highlightthickness=0,
                              command=self.register)

        self.place_order = Button(window, text="Place new order", width=15, fg="White", bg="black",
                                  highlightthickness=0, command=self.place_order)
        self.order_history = Button(window, text="Order History", width=15, fg="White", bg="black",
                                    highlightthickness=0, command=self.history_order)
        self.update_profile = Button(window, text="Update Profile", width=15, fg="White", bg="black",
                                     highlightthickness=0, command=self.update_prof)

        self.user_name = Label(window, text="User Name :", fg="black", bg="#F5F5F5", font=("Italic", 15, 'normal'))
        self.entry = Entry(width=50)
        self.entry.focus()
        self.password = Label(window, text="Password :", fg="black", bg="#F5F5F5", font=("Italic", 15, 'normal'))
        self.pass_entry = Entry(width=50)

    def user_login(self):
        global user_nam
        user_nam = self.entry.get()
        user_pass = self.pass_entry.get()
        try:
            with open("data_user.json", "r+") as fp:
                data = json.load(fp)
        except FileNotFoundError:
            messagebox.showinfo("OOPS!!", "There were no user, please register")
        else:

            if user_nam in data:
                if user_pass == data[user_nam]['Password']:
                    self.user_log.destroy()
                    self.button2.destroy()
                    try:
                        self.user_name.destroy()
                        self.entry.destroy()
                        self.password.destroy()
                        self.pass_entry.destroy()
                        self.display_user()
                    except TclError:
                        self.user_name.destroy()
                        self.entry.destroy()
                        self.password.destroy()
                        self.pass_entry.destroy()
                        self.display_user()
                    else:
                        pass
                else:
                    messagebox.showerror("OOPS!!", "Entered password is Incorrect")
            else:
                messagebox.showerror("OOPS!!", "User name doesn't exist. Please register")

    def user_save_details(self, user_n):
        full_n = self.full_entry.get()
        phone_number = self.phone_entry.get()
        email_1 = self.email_entry.get()
        address_1 = self.address_entry.get("1.0", END)
        password_1 = self.password_entry.get()

        new_data = {user_n: {
            "Full Name": full_n,
            "Phone Number": phone_number,
            "Email": email_1,
            "Address": address_1,
            "Password": password_1
        }
        }
        if user_n != '' and full_n != '' and phone_number != '' and email_1 != '' \
                and address_1 != '' and password_1 != "":
            is_ok = messagebox.askokcancel("User Details", f"Are you sure entered details are correct ?")
            if is_ok:
                try:
                    with open('data_user.json', 'r+') as fp:
                        data = json.load(fp)
                        data.update(new_data)
                except json.decoder.JSONDecodeError:
                    with open('data_user.json', 'w') as fp:
                        json.dump(new_data, fp, indent=4)
                except FileNotFoundError:
                    with open('data_user.json', 'w') as fp:
                        json.dump(new_data, fp, indent=4)
                else:
                    with open('data_user.json', 'w') as fp:
                        json.dump(data, fp, indent=4)
                self.window6.destroy()
                messagebox.showinfo('information', "Saved successfully")

        else:
            self.window6.destroy()
            messagebox.showerror("Error", "Please don't leave any of fields empty")

    def save_details(self):
        try:
            with open("data_user.json", "r+") as fp1:
                data2 = json.load(fp1)
        except FileNotFoundError:
            user_n = self.user_entry1.get()
            self.user_save_details(user_n)
        else:
            try:
                user_n = self.user_entry1.get()
                if user_n in data2:
                    messagebox.showerror("OOPS!!", "Entered user name already exists")
                else:
                    self.user_save_details(user_n)
            except TclError:
                user_n = user_nam
                self.user_save_details(user_n)

    def register(self):

        self.window6 = Tk()
        self.window6.title("User Details")
        self.window6.config(padx=50, pady=50)
        self.user_name = Label(self.window6, text="User name :")
        self.save = Button(self.window6, text="Save User", width=20, command=self.save_details)
        self.password_entry = Entry(self.window6, width=30)
        self.address_entry = Text(self.window6, height=4, width=22)
        self.address = Label(self.window6, text="Address :")
        self.email_entry = Entry(self.window6, width=30)
        self.email = Label(self.window6, text="Email :")
        self.phone_entry = Entry(self.window6, width=30)
        self.phone_num = Label(self.window6, text="Phone Number :")
        self.full_entry = Entry(self.window6, width=30)
        self.full_name = Label(self.window6, text="Full name :")
        self.user_entry1 = Entry(self.window6, width=30)
        self.user_label = Label(self.window6, text=user_nam)
        self.back = Button(self.window6, text='Back', width=20, command=self.window6.destroy)

        self.user_name.grid(column=0, row=0)
        self.user_entry1.grid(column=1, row=0)
        self.user_entry1.focus()
        self.full_name.grid(column=0, row=1)
        self.full_entry.grid(column=1, row=1)
        self.phone_num.grid(column=0, row=2)
        self.phone_entry.grid(column=1, row=2)
        self.email.grid(column=0, row=3)
        self.email_entry.grid(column=1, row=3)
        self.address.grid(column=0, row=4)
        self.address_entry.grid(column=1, row=4)
        self.password = Label(self.window6, text="Password :")
        self.password.grid(column=0, row=5)
        self.password_entry.grid(column=1, row=5)
        self.save.grid(column=1, row=6)
        self.back.grid(column=1, row=7)

    def display_user(self):
        self.canvas.delete(self.c1)
        self.canvas.delete(self.c2)
        self.canvas.moveto(self.c3, x=300, y=30)
        self.canvas.create_text(720, 100, text=f"Logged in as {user_nam}")
        self.place_order.place(x=400, y=250)
        self.order_history.place(x=600, y=250)
        self.update_profile.place(x=500, y=300)

    def update_prof(self):
        global user_nam
        with open("data_user.json", "r+") as fp:
            data1 = json.load(fp)
        full_nam = data1[user_nam]["Full Name"]
        phone_n = data1[user_nam]["Phone Number"]
        email_us = data1[user_nam]["Email"]
        address = data1[user_nam]["Address"]
        pass_use = data1[user_nam]["Password"]
        self.register()
        self.user_entry1.destroy()
        self.user_label.grid(column=1, row=0)
        self.full_entry.insert(END, full_nam)
        self.phone_entry.insert(END, phone_n)
        self.email_entry.insert(END, email_us)
        self.address_entry.insert(END, address)
        self.password_entry.insert(END, pass_use)

    @staticmethod
    def place_order():
        global labels
        item_details = []
        current_time = datetime.now()

        def order_placed():
            def save_order():
                order_name = []
                order_quantity = []
                order_price = []
                for i in range(len(item_details)):
                    order_name.append(item_details[i]['Name'])
                    order_quantity.append(item_details[i]["Quantity"])
                    order_price.append(item_details[i]["FinalPrice"])
                data_dict = {"User": user_nam,
                             "Name": order_name,
                             "Quantity": order_quantity,
                             "Price": order_price,
                             "Date and Time": current_time
                             }
                db = pandas.DataFrame(data_dict)
                try:
                    with open("order_history.csv", 'r') as fp2:
                        csv.reader(fp2)
                except FileNotFoundError:
                    db.to_csv("order_history.csv", mode='a', index=False)
                    messagebox.showinfo("Thank you", "Your order was placed successfully")
                else:
                    db.to_csv("order_history.csv", mode='a', index=False, header=False)
                    messagebox.showinfo("Thank you", "Your order was placed successfully")
                window3.destroy()

            if user_entry.get() == '':
                window2.destroy()
                messagebox.showinfo("OOps!!", "Please provide food id")
            else:
                user_choice = (user_entry.get()).split(',')
                with open("data.json", "r+") as fp1:
                    data3 = json.load(fp1)
                try:
                    for i in user_choice:
                        item_details.append(data3[i])
                except KeyError:
                    window2.destroy()
                    messagebox.showerror("OOPS!!", "You entered a wrong id. \n "
                                                   "Please enter correct food id's separated by comma.")
                else:
                    window2.destroy()
                    window3 = Tk()
                    window3.title("Order Details")
                    window3.config(padx=50, pady=50)
                    l2 = Label(window3, text="Item Name")
                    l3 = Label(window3, text="Quantity")
                    l6 = Label(window3, text="Price in Rs")
                    total = Label(window3, text="Total Price", font=("Italic", 10, "bold"))
                    back = Button(window3, text='Confirm Order', width=20, command=save_order)

                    l2.grid(column=0, row=0)
                    l3.grid(column=1, row=0)
                    l6.grid(column=2, row=0)

                    total_price = []
                    for i in range(len(item_details)):
                        total_price.append(item_details[i]["FinalPrice"])
                        food_nme = Label(window3, text=item_details[i]["Name"])
                        food_nme.grid(column=0, row=i + 1, sticky='W')

                        food_qa = Label(window3, text=item_details[i]["Quantity"])
                        food_qa.grid(column=1, row=i + 1)

                        food_pice = Label(window3, text=item_details[i]["FinalPrice"])
                        food_pice.grid(column=2, row=i + 1)
                    total.grid(column=1, row=len(item_details) + 2)
                    total_prie = Label(window3, text=f"{sum(total_price)}", font=("Italic", 10, "bold"))
                    total_prie.grid(column=2, row=len(item_details) + 2)
                    back.grid(column=4, row=len(item_details) + 2)

        window2 = Tk()
        window2.title("List of items")
        window2.config(padx=50, pady=50)
        l1 = Label(window2, text="Food ID")
        l2 = Label(window2, text="Name")
        l3 = Label(window2, text="Quantity")
        l4 = Label(window2, text="Price")
        l5 = Label(window2, text="Discount in %")
        l6 = Label(window2, text="Final Price")
        l7 = Label(window2, text="Stock Left")
        label8 = Label(window2, text="Enter the item(ex: I1,I2,I3)")
        user_entry = Entry(window2, width=30)
        user_entry.focus()
        order_place = Button(window2, text="Place Order", width=20, command=order_placed)
        back = Button(window2, text='Back', width=20, command=window2.destroy)
        with open("data.json", 'r') as fp:
            data = json.load(fp)
        l1.grid(column=1, row=0)
        l2.grid(column=2, row=0)
        l3.grid(column=3, row=0)
        l4.grid(column=4, row=0)
        l5.grid(column=5, row=0)
        l6.grid(column=6, row=0)
        l7.grid(column=7, row=0)

        item_id = []
        item_name = []
        item_qua = []
        item_price = []
        item_discount = []
        item_final_price = []
        item_stock = []

        for i in range(len(data)):
            data_1 = data.keys()
            data_2 = list(data_1)
            item_1 = data_2[i]
            item_id.append(item_1)
            item_name.append(data[item_1]["Name"])
            item_qua.append(data[item_1]["Quantity"])
            item_price.append(data[item_1]["Price"])
            item_discount.append(data[item_1]["Discount"])
            item_final_price.append(data[item_1]["FinalPrice"])
            item_stock.append(data[item_1]["stockLeft"])

            food_num = Label(window2, text=item_id[i])
            food_num.grid(column=1, row=i + 1)

            food_name = Label(window2, text=item_name[i])
            food_name.grid(column=2, row=i + 1, sticky='W')

            food_qua = Label(window2, text=item_qua[i])
            food_qua.grid(column=3, row=i + 1)

            food_price = Label(window2, text=item_price[i])
            food_price.grid(column=4, row=i + 1)

            food_discount = Label(window2, text=item_discount[i])
            food_discount.grid(column=5, row=i + 1)

            food_final_price = Label(window2, text=item_final_price[i])
            food_final_price.grid(column=6, row=i + 1)

            food_stock = Label(window2, text=item_stock[i])
            food_stock.grid(column=7, row=i + 1)

            labels.append([food_num, food_name, food_qua, food_price, food_discount,
                           food_final_price, food_stock])
        label8.grid(column=8, row=len(data) + 2)
        user_entry.grid(column=8, row=len(data) + 3)
        order_place.grid(column=8, row=len(data) + 4)
        back.grid(column=8, row=len(data) + 5)
        window2.mainloop()

    @staticmethod
    def history_order():
        try:
            df = pandas.read_csv("order_history.csv")
            data = df.loc[df["User"] == user_nam]
        except FileNotFoundError:
            messagebox.showinfo("OOPS!!", "You didn't ordered anything yet")
        else:
            if data.empty:
                messagebox.showinfo("OOPS!!", "You didn't ordered anything yet")
            else:
                date_time = data['Date and Time'].tolist()
                time_date = []
                for i in date_time:
                    if i not in time_date:
                        time_date.append(i)

                name = []
                quantity = []
                price = []

                for i in time_date:
                    name.append(data.loc[data["Date and Time"] == i]["Name"].tolist())
                    quantity.append(data.loc[data["Date and Time"] == i]["Quantity"].tolist())
                    price.append(data.loc[data["Date and Time"] == i]["Price"].tolist())

                window2 = Tk()
                window2.title("Order History")
                window2.config(padx=50, pady=50)

                count = 0
                count_1 = 1
                for i in range(len(time_date)):
                    amount = price[i]
                    total_price = sum(amount)
                    time = time_date[i]
                    l1 = Label(window2, text="Ordered on : ", font=("Italic", 10, "bold"))
                    l5 = Label(window2, text=time)
                    l2 = Label(window2, text="Name", font=("Italic", 10, "bold"))
                    l3 = Label(window2, text="Quantity", font=("Italic", 10, "bold"))
                    l4 = Label(window2, text="Price", font=("Italic", 10, "bold"))
                    total = Label(window2, text="Total Price :", font=("Italic", 10, "bold"))
                    final_price = Label(window2, text=total_price, font=("Italic", 10, "bold"))
                    l1.grid(column=0, row=count)
                    l5.grid(column=1, row=count)
                    count += 1
                    l2.grid(column=1, row=count)
                    l3.grid(column=2, row=count)
                    l4.grid(column=3, row=count)
                    for item in range(len(name[i])):
                        count_1 += 1
                        food_num = Label(window2, text=name[i][item])
                        food_num.grid(column=1, row=count_1)

                        food_name = Label(window2, text=quantity[i][item])
                        food_name.grid(column=2, row=count_1)

                        food_qua = Label(window2, text=price[i][item])
                        food_qua.grid(column=3, row=count_1)
                        count += 1
                    count += 1
                    total.grid(column=2, row=count)
                    final_price.grid(column=3, row=count)
                    count += 1
                    count_1 = count + 1

                back = Button(window2, text='Back', command=window2.destroy)
                back.grid(column=4, row=count_1 + 2)
                window2.mainloop()