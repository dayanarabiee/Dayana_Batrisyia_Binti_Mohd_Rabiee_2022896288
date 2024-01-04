import tkinter as tk
import mysql.connector 
from datetime import date

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bmi_calculator_health_indicator"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()


# Function
def calculate_bmi():
    global name_entry, weight_entry, height_entry, age, result_text, output_label

    # Get values from entry fields
    name = name_entry.get()
    weight = float(weight_entry.get())
    height = float(height_entry.get())
    dbirth = d_b_entry.get()
    mbirth = m_b_entry.get()
    ybirth = y_b_entry.get()

    today = date.today() 
    birthdate = date(int(y_b_entry.get()), int(m_b_entry.get()), int(d_b_entry.get()))
    age = today.year - birthdate.year #- ((today.month, today.day) < (birthdate.month, birthdate.day))

    print("Student Name:", name)
    print("Student Age:", age )
    print("Student Weight:", weight)
    print("Student Height:", height)
    print("Birth Date:", dbirth, "/", mbirth, "/", ybirth)

    # Calculate BMI
    BMI = weight / (height * height)

    # Display student information
    result_text.set(f"Student: {name}\n"
                    f"Age: {age} years\n"
                    f"BMI: {BMI:.2f}")

    #  BMI category
    if BMI < 18.5:
        bmi_category = "Underweight"
        tips = "Need to gain weight and need to eat a lot of carbohydrates and protein."
    elif 18.5 <= BMI < 24.9:
        bmi_category = "Normal Weight"
        tips = "Maintain the body! and take care of your health."
    elif 25 <= BMI < 29.9:
        bmi_category = "Overweight"
        tips = "Try to reduce your weight, more excercises and observing food portions!."
    else:
        bmi_category = "Obesity"
        tips = "Please go to consultation expert to reduce your weight and please be more excercise!."

    # Update with BMI category and tips
    output_label.config(text=f"BMI Category: {bmi_category}, \n\nTips: {tips}")

    # Insert data into the database
    sql = "INSERT INTO student_information (Stu_Name, Stu_Age, Stu_Weight, Stu_Height) VALUES (%s, %s, %s, %s)"
    val = (name, age, weight, height)
    mycursor.execute(sql, val)
    mydb.commit()

   # GUI code
root = tk.Tk()
root.title("BMI Calculator & Health Indicator")
root.geometry('800x600')
root.configure(bg="pink")

frame = tk.Frame(root)
frame.pack()

user_info_frame = tk.LabelFrame(frame, text="Student Information")
user_info_frame.grid(row=0, column=0, ipadx=28, ipady=28)
user_info_frame.configure(bg="white", fg="deep pink", font=("Arial",20, "bold"))

name_label = tk.Label(user_info_frame, text="Name")
name_label.grid(row=0, column=0)
name_label.configure(fg="dark blue", font=("Arial",12, "bold"))

name_entry = tk.Entry(user_info_frame)
name_entry.grid(row=1, column=0)

weight_label = tk.Label(user_info_frame, text="Weight (kg)")
weight_label.grid(row=2, column=0)
weight_label.configure(fg="dark blue", font=("Arial",12 , "bold"))

weight_entry = tk.Entry(user_info_frame)
weight_entry.grid(row=3, column=0)

height_label = tk.Label(user_info_frame, text="Height (m)")
height_label.grid(row=4, column=0)
height_label.configure(fg="dark blue", font=("Arial",12 , "bold"))

height_entry = tk.Entry(user_info_frame)
height_entry.grid(row=5, column=0)

birth_date = tk.Label(user_info_frame, text="Birth Date")
birth_date.grid(row=0, column=1) 
birth_date.configure(fg="dark blue", font=("Arial",12 , "bold"))

d_b_entry = tk.Entry(user_info_frame) 
d_b_entry.grid(row=1, column=1)
d_b_entry.insert(2,'00')

m_b_entry = tk.Entry(user_info_frame) 
m_b_entry.grid(row=2, column=1)
m_b_entry.insert(2,'00')

y_b_entry = tk.Entry(user_info_frame)
y_b_entry.grid(row=3, column=1)
y_b_entry.insert(4,'0000')

#age_label = tk.Label(user_info_frame, text="Age")
#age_label.grid(row=4, column=1)

calculate_button = tk.Button(frame, text="Calculate BMI", command=calculate_bmi)
calculate_button.grid(row=16, column=0)
calculate_button.configure(bg="pink", fg="dark blue", font=("Arial", 12 , "bold"))

result_text = tk.StringVar()
result_label = tk.Label(frame, textvariable=result_text)
result_label.grid(row=14, column=0)

# Output Label & result
label = tk.Label(root, text='BMI Category', font=("Times New Roman", 12))
label.pack(ipadx=10, ipady=10)
output_label = tk.Label(root, text="")
output_label.pack()

root.mainloop()