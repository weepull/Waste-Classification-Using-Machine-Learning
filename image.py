# import PIL
# import os
# import os.path
# from PIL import Image


# src_path = r'D:\Machine Learning\Project\DataSet'
# dst_path = f'D:\Machine Learning\Project\final dataset'

# # For image rescaling
# for count,file in enumerate(os.listdir(src_path)):
#     f_img = src_path+"/"+file
#     image = Image.open(f_img)
#     image = image.resize((512,384))
#     # f_n_img = f"{dst_path}/bio{str(count)}.jpg"
#     image.save(f_img)
#     print("File : ",f_img," is saved")


# # # For image rename
# # for count,file in enumerate(os.listdir(src_path)):
# #     src_path1 = f"{src_path}/{file}"
# #     # dst_path1 = f"D:\Machine Learning\Project\DataSet"
# #     dst_path1 = f"{src_path}/{str(count)}.jpg"

# #     os.rename(src_path1,dst_path1)


import cv2
import os
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk

def showImg():
    file_name = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select Image', filetypes=(("JPG File","*.jpg"),("PNG file","*.")))
    img =cv2.imread(file_name)
    img =cv2.cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img.thumbnail(350,350)
    img = ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image = img


root = Tk()
root.title("Machine Learning Project")
root.geometry('300x350')

frm = Frame(root)
frm.pack(side=BOTTOM, padx = 15, pady=15)

lbl = Label(root)
lbl.pack()


btn = Button(frm, text="Drag Image", command=showImg)
btn.pack(side=LEFT)

root.mainloop()
