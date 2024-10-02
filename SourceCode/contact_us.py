from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar
import webbrowser  # Import webbrowser for opening links
import traceback
import base64

# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, StringVar

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"data\assets\contact_assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("1204x801")
window.configure(bg="#121139")
canvas = Canvas(
    window,
    bg="#121139",
    height=801,
    width=1204,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    603.0,
    400.0,
    image=image_image_1
)

canvas.create_text(
    855.0,
    42.0,
    anchor="nw",
    text="Introduction",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 15 * -1)
)

canvas.create_text(
    987.0,
    42.0,
    anchor="nw",
    text="About",
    fill="#FFFFFF",
    font=("MontserratRoman Medium", 15 * -1)
)

canvas.create_rectangle(
    825.0,
    65.0,
    1057.9999988476347,
    66.0000000094899,
    fill="#FFFFFF",
    outline=""
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    604.0,
    437.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    599.0,
    432.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    330.0,
    553.0,
    image=image_image_4
)

canvas.create_text(
    113.0,
    322.0,
    anchor="nw",
    text="For inquiries or feedback please reach out to us via: ",
    fill="#FFFFFF",
    font=("Montserrat Light", 20 * -1)
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    876.0,
    553.0,
    image=image_image_5
)

canvas.create_text(
    113.0,
    220.0,
    anchor="nw",
    text='''Thank you for using our study companion software! This version of CASCADE was crafted by Harsh 
Dayal and Saanvi Sharma with a passion for enhancing your learning experience.''',
    fill="#FFFFFF",
    font=("Montserrat Light", 20 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print(""),  # Open Saavi's link
    relief="flat"
)
button_1.place(
    x=1071.0,
    y=31.0,
    width=30.0,
    height=40.0
)




canvas.create_text(
    818.0,
    114.0,
    anchor="nw",
    text="Contact Us",
    fill="#A791CA",
    font=("MontserratRoman SemiBold", 51 * -1)
)

canvas.create_rectangle(
    792.9873046875,
    179.0,
    1107.0127868652344,
    179.0,
    fill="#FFFFFF",
    outline=""
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    42.0,
    46.0,
    image=image_image_6
)

canvas.create_rectangle(
    602.0,
    511.9999980330508,
    602.0,
    629.0,
    fill="#FFFFFF",
    outline=""
)

# Replace these with your actual link URLs
link_saanvigithub = "https://github.com/confusedjpeg"
link_harshgithub = "https://github.com/Kaos599"
link_saanvilinkedin = "https://www.linkedin.com/in/saanvi-sharma-b12a27251/"
link_harshlinkedin = "https://www.linkedin.com/in/harshdayal/"

def open_link(url):
    try:
        webbrowser.open_new_tab(url)
    except Exception as e:
        print(f"Error opening link: {url}")
        traceback.print_exc()

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_link(link_saanvigithub),  # Open Saavi's link
    relief="flat"
)

button_2.place(
    x=950.0,
    y=525.0,
    width=106.0,
    height=104.0
)

canvas.create_text(
    775.0,
    444.0,
    anchor="nw",
    text="Saanvi Sharma",
    fill="#FFFFFF",
    font=("Sen Regular", 32 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_link(link_harshgithub),  # Open Harsh's link
    relief="flat"
)
button_3.place(
    x=398.0,
    y=520.0,
    width=105.0,
    height=104.0
)

canvas.create_text(
    229.0,
    444.0,
    anchor="nw",
    text="Harsh Dayal",
    fill="#FFFFFF",
    font=("Sen Regular", 32 * -1)
)

canvas.create_rectangle(
    107.0,
    289.0,
    1093.0000022649729,
    289.0,
    fill="#FFFFFF",
    outline=""
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_link(link_saanvilinkedin),  # Open Github link
    relief="flat"
)
button_4.place(
    x=706.0,
    y=522.0,
    width=104.0,
    height=106.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: open_link(link_harshlinkedin),  # Open Linkedin link
    relief="flat"
)
button_5.place(
    x=158.0,
    y=520.0,
    width=104.0,
    height=106.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=1119.0,
    y=37.0,
    width=30.0,
    height=28.0
)

# Fix the button background issue
for button in [button_1, button_4, button_5, button_6]:
    button.config(bg="#121139") 

for button in [button_2, button_3]:
    button.config(bg="#31125D") 

window.mainloop()