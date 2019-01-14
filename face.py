import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk

import face_recognition

Images = ['empty.png', '', '']
size = 250, 250


def Select_Known(event=None):
    file = filedialog.askopenfilename()
    im = Image.open(file)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save('resized_known.png', "PNG")
    Images[1] = 'resized_known.png'
    imageknown.config(file=Images[1])
    print(Images)
    return file


def Select_Unknown(event=None):
    file = filedialog.askopenfilename()
    im = Image.open(file)
    im_resized = im.resize(size, Image.ANTIALIAS)
    im_resized.save('resized_unknown.png', "PNG")

    Images[2] = 'resized_unknown.png'
    imageunknown.config(file=Images[2])
    print(Images)
    return file


def Recognise_face(n, un):
    known_image = face_recognition.load_image_file(n)
    unknown_image = face_recognition.load_image_file(un)

    biden_encoding = face_recognition.face_encodings(known_image)[0]
    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]

    results = face_recognition.compare_faces(
        [biden_encoding], unknown_encoding)
    if results == [True]:
        res = 'The images Match.'
    else:
        res = 'The images dont match.'
    return res


def Compare():
    if Images[1] == '' or Images[2] == '':
        label1.config(text='Choose both pictures please')
    else:
        result = Recognise_face(Images[1], Images[2])
        label1.config(text=result)


root = tk.Tk()
root.title('Face Reacognition')
root.geometry('900x620')
buttonkn = tk.Button(root, text='Select your known image.',
                     command=Select_Known, fg="blue")
buttonunkn = tk.Button(root, text='Select the unknown image.',
                       command=Select_Unknown, fg="blue")
buttoncompare = tk.Button(root, text='Compare', command=Compare)

mainlabel = tk.Label(root, text='Use .PNG Images for better results.', font=(
    "Helvetica", 17, "bold"), fg="red")
label1 = tk.Label(root, text='No results yet', font=(
    "Helvetica", 16, "bold italic"), fg="blue",)

imageknown = tk.PhotoImage(file=Images[0])
labelknown = tk.Label(image=imageknown, height=230, width=230)
labelkn = tk.Label(text='This is the known image', fg="red", font=(12))

imageunknown = tk.PhotoImage(file=Images[0])
labelunknown = tk.Label(image=imageunknown, height=230, width=230)
labelun = tk.Label(text='This is the unknown image', fg="red", font=(12))

mainlabel.grid(column=2, row=0)

buttonkn.grid(column=1, row=3)
buttonunkn.grid(column=1, row=5)
buttoncompare.grid(column=2, row=7)

labelkn.grid(column=1, row=4)
labelknown.grid(column=3, row=4)

labelun.grid(column=1, row=6)
labelunknown.grid(column=3, row=6)

label1.grid(column=2, row=8)


root.mainloop()
