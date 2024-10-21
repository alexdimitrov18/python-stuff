import tkinter as tk
from tkinter import messagebox


# Function to show the sum of the inputs
def show_sum():
    try:
        # Get the input values from the entries and convert them to floats
        inputs = [float(entry1.get()), float(entry2.get()), float(entry3.get()), float(entry4.get()),
                  float(entry5.get())]

        # Calculate the sum
        total = sum(inputs)

        # Show the sum in a message box
        messagebox.showinfo("Sum of Inputs", f"The sum is: {total:.2f}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers in all fields.")


# Create the main window
root = tk.Tk()
root.title("Input Fields")
root.geometry("400x300")  # Set the size of the window (width x height)

# Create five input fields for numbers
entry1 = tk.Entry(root, width=30)
entry1.pack(pady=5)

entry2 = tk.Entry(root, width=30)
entry2.pack(pady=5)

entry3 = tk.Entry(root, width=30)
entry3.pack(pady=5)

entry4 = tk.Entry(root, width=30)
entry4.pack(pady=5)

entry5 = tk.Entry(root, width=30)
entry5.pack(pady=5)

# Create a submit button
submit_button = tk.Button(root, text="Submit", command=show_sum)
submit_button.pack(pady=20)

# Run the application
root.mainloop()
