from tkinter import *
from tkinter import filedialog, colorchooser

from PIL import Image, ImageTk, ImageDraw, ImageFont


class ImageWatermarker:
    def __init__(self, master):
        self.master = master
        master.title("Image Watermarker")
        self.image_path = None
        self.watermark_color = "white"
        self.watermark_text = "Your watermark text"

        self.canvas = Canvas(self.master, width=500, height=500)
        self.canvas.pack()

        self.image_item = self.canvas.create_image(0, 0, anchor="nw")

        self.open_button = Button(self.master, text="Open Image", command=self.open_image)
        self.open_button.pack(side=LEFT)

        self.add_button = Button(self.master, text="Add Watermark", command=self.add_watermark)
        self.add_button.pack(side=LEFT)

        self.text_field = Entry(self.master, width=30)
        self.text_field.pack(side=LEFT)

        self.change_text_button = Button(self.master, text="Change Text", command=self.change_text)
        self.change_text_button.pack(side=LEFT)

        self.color_button = Button(self.master, text="Change Color", command=self.change_color)
        self.color_button.pack(side=LEFT)

    def open_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            image = Image.open(self.image_path)
            photo = ImageTk.PhotoImage(image)
            self.canvas.itemconfigure(self.image_item, image=photo)
            self.canvas.image = photo

    def add_watermark(self):
        if not self.image_path:
            return
        image = Image.open(self.image_path)
        width, height = image.size
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("arial.ttf", 36)
        textbbox = draw.textbbox((0, 0), self.watermark_text, font=font)
        x = width - textbbox[2] - 10
        y = height - textbbox[3] - 10
        draw.text((x, y), self.watermark_text, font=font, fill=self.watermark_color)
        save_path = filedialog.asksaveasfilename(defaultextension='.png', filetypes=[("PNG", ".png")])
        if save_path:
            image.save(save_path)

    def change_color(self):
        color = colorchooser.askcolor()[1]
        if color:
            self.watermark_color = color

    def change_text(self):
        self.watermark_text = self.text_field.get()


root = Tk()
app = ImageWatermarker(root)
root.mainloop()
