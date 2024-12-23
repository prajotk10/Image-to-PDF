import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image
import os
from tkinter import filedialog #it is used to take input from our files

# GUI application window
win = tk.Tk() #it only popup the screen. Tk() is class of tkinter
win.title('Img to Pdf converter application')
win.geometry('700x600')
win.iconphoto(False, tk.PhotoImage(file = 'logo.png')) # it is used to set logo of App.
win.resizable(0,0) #it does not change the size of application.eg minimize or maximize

def disable(btn):
    btn['state']='disabled'
                                #this is used to disabel and enabel buttons at runtime automatically.
def enable(btn):
    btn['state']='active'

files = {}    #this is used to take the names or location of images from files in this dictionary
def upload_imgs():
    global files
    files['filename']=filedialog.askopenfilenames(filetypes=[('JPG','*.jpg'),('PNG','*.png'),('JPEG','*.jpeg')],#filename is key of dictionary to store 
    initialdir = os.getcwd(), title='Select File/Files') #It is used to open file in curent directory.
    if len(files['filename'])!=0: #this is used to check if there is no any image is selected from file if empty then download button will be disabled.
        enable(download_button)
    
def saveas():
    try:
        img_list = []
        for file in files['filename']:
            img_list.append(Image.open(file).convert('RGB'))#to convert file into pixel for converting it into PDF
        save_file_name = filedialog.asksaveasfilename(filetypes = [('PDF','*.pdf')], initialdir=os.getcwd(), title='Save File') #covert image to PDF
        img_list[0].save(f'{save_file_name}.pdf', save_all=True, append_images = img_list[1:])
        disable(download_button)
    except:
        return


# main img of application
canvas = Canvas(win, bg='white',width = 250, height=250)
canvas.grid(row =0,column=0, sticky=tk.N, padx=220, pady =25)#sticky is used to select position of image i.e. east west north south

main_img = ImageTk.PhotoImage(Image.open('main_app_img.jpg')) #ImageTk is used take image in pixel form
canvas.create_image(125,120, image=main_img)

# info img of application
canvas_info = Canvas(win, bg='white', width = 600, height=120)
canvas_info.grid(row=1, column =0, padx =5)#grid is used to place the position of image over application.

info_img = ImageTk.PhotoImage(Image.open('welcome.jpg'))
canvas_info.create_image(302,62, image =info_img)

# upload button
upload_button = tk.Button(win, text='UPLOAD IMAGES', width = 20, height =1,font=('arial',14,'bold'), bg='white',fg='green', command=upload_imgs)
upload_button.grid(row =2, column = 0, padx=200, pady =20)

# Download button
download_button = tk.Button(win, text='Download PDF', width = 20, height =1,font=('arial',14,'bold'), bg='white',fg='red', command=saveas)
download_button.grid(row=3, column=0)
disable(download_button)


win.mainloop() #it is used to hold the screen of GUI.




















# Canvas : The canvas widget is used to add the structured graphics on window to the python application. It is used to draw the graph and plots to the python application.
# tkinter : It is used to create GUI i.e.Graphical User Interface.
''' Use of tkinter:
Displaying Text and Images With Label Widgets.
Displaying Clickable Buttons With Button Widgets.
Getting User Input With Entry Widgets.
Getting Multiline User Input With Text Widgets.
Assigning Widgets to Frames With Frame Widgets.
Adjusting Frame Appearance With Reliefs '''
#getcwd = open current working directory
#asksaveasfilename this is used to ask the saving name of file.