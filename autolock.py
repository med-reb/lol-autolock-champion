from tkinter import *
import os
import pyautogui
from PIL import Image, ImageDraw
import time


champions = []
folder = str("images/buttons/")
cpt = 0

def btn_clicked():
    if entry0.get() != "":
        champions.append(entry0.get())
    else:
        champions.append("")
    if entry1.get() != "":
        champions.append(entry1.get())
    else:
        champions.append("")
    if entry2.get() != "":
        champions.append(entry2.get())    
    else:
        champions.append("")
    if entry3.get() != "":
        champions.append(entry3.get())
    else:
        champions.append("")
    app(selected_option.get())




def draw_outline(draw, location):
    left, top, width, height = location
    right, bottom = left + width, top + height
    outline_color = (255, 0, 0)  # Couleur du contour en rouge

    # Dessine les contours autour de la région
    draw.rectangle([left, top, right, bottom], outline=outline_color)

def left_click(x,y,z):
    global cpt
    pyautogui.moveTo(x, y)
    pyautogui.click()
    if z == 4:
        pyautogui.write(champions[3])

        pyautogui.moveTo(x-450, y+60)
        pyautogui.click()

    elif z == 7:
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.press('delete')
        if cpt > 2:
            pyautogui.write()
        pyautogui.moveTo(x-450, y+60)
        pyautogui.click()
        cpt = cpt + 1



def app(language):
    folder = (str("images/buttons/")+language+"/")
    i = 0

    while i<9:        
        toPress = (folder+os.listdir(folder)[i])
        print(toPress)
        location = pyautogui.locateOnScreen(toPress, confidence=0.7)
        if location:
            print("Image trouvée à la position :", location)
            left_click(location[0]+location[2]/2,location[1]+location[3]/2,i)
            i = i+1
            time.sleep(1)
        else:
            print(os.listdir(folder)[i])
            time.sleep(2)

    quit()


"""# Parcourt toutes les images dans le dossier
for image_to_find in os.listdir(folder):
    card = folder + image_to_find
    print(image_to_find)
    location = pyautogui.locateOnScreen(card, confidence=0.7)
    if location:
        print("Image trouvée à la position :", location)
        print("Coordonnées du coin supérieur gauche :", location[0:2])

        # Récupère la capture d'écran
        screenshot = pyautogui.screenshot()

        # Dessine un contour autour de la zone
        draw = ImageDraw.Draw(screenshot)
        draw_outline(draw, location)

        # Enregistre l'image modifiée dans le même répertoire avec un nom différent
        new_image_path = os.path.join(folder, f"outlined_{image_to_find}")
        screenshot.save(new_image_path)

        print(f"Image modifiée enregistrée à {new_image_path}")
        break
    else:
        print("Image non trouvée.")"""



root = Tk()

root.geometry("333x594")
root.configure(bg="#ffffff")
canvas = Canvas(
    root,
    bg="#ffffff",
    height=594,
    width=333,
    bd=0,
    highlightthickness=0,
    relief="ridge")
canvas.place(x=0, y=0)

background_img = PhotoImage(file="ui/background.png")
background = canvas.create_image(
    166, 297.0,
    image=background_img)

img0 = PhotoImage(file="ui/img0.png")
b0 = Button(
    image=img0,
    borderwidth=0,
    highlightthickness=0,
    command=btn_clicked,
    relief="flat")

b0.place(
    x=106, y=498,
    width=119,
    height=47)

entry0_img = PhotoImage(file="ui/img_textBox0.png")
entry0_bg = canvas.create_image(
    166.5, 177.5,
    image=entry0_img)

bold_font = ("Helvetica", 12, "bold") 

entry0 = Entry(
    bd=0,
    justify="center",
    bg="#8EFF33",
    highlightthickness=0,
    font=bold_font)

entry0.place(
    x=49, y=159,
    width=235,
    height=35)

entry1_img = PhotoImage(file="ui/img_textBox1.png")
entry1_bg = canvas.create_image(
    165.5, 230.5,
    image=entry1_img)

entry1 = Entry(
    bd=0,
    justify="center",
    bg="#d9d9d9",
    highlightthickness=0,
    font=bold_font)

entry1.place(
    x=48, y=212,
    width=235,
    height=35)

entry2_img = PhotoImage(file="ui/img_textBox2.png")
entry2_bg = canvas.create_image(
    166.5, 285.5,
    image=entry2_img)

entry2 = Entry(
    bd=0,
    justify="center",
    bg="#d9d9d9",
    highlightthickness=0,
    font=bold_font)

entry2.place(
    x=49, y=265,
    width=235,
    height=35)

entry3_img = PhotoImage(file="ui/img_textBox3.png")
entry3_bg = canvas.create_image(
    165.5, 384.5,
    image=entry3_img)

entry3 = Entry(
    bd=0,
    justify="center",
    bg="#FF3333",
    highlightthickness=0,
    font=bold_font)

entry3.place(
    x=48, y=366,
    width=235,
    height=35)

# Ajoutez deux cases à cocher
selected_option = StringVar()
selected_option.set("fr")  # Aucune option sélectionnée par défaut

radio_option1 = Radiobutton(root, variable=selected_option,background="#183342", value="fr")
radio_option1.place(x=119, y=449)

radio_option2 = Radiobutton(root, variable=selected_option,background="#183342", value="en")
radio_option2.place(x=182, y=449)

radio_option3 = Radiobutton(root, variable=selected_option,background="#183342", value="fr")
radio_option3.place(x=119, y=449)

radio_option4 = Radiobutton(root, variable=selected_option,background="#183342", value="en")
radio_option4.place(x=182, y=449)


root.resizable(False, False)
root.mainloop()

