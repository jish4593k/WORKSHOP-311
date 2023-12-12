import torch
import torchvision.transforms as transforms
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import ttk
import os


transform = transforms.Compose([
    transforms.RandomRotation(40),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    transforms.RandomResizedCrop(150, scale=(0.8, 1.0)),
    transforms.ToTensor(),
])


original_image_path = 'data/test/2.jpg'
original_image = Image.open(original_image_path)

root = tk.Tk()
root.title("Augmentation Preview")


def update_image(image):
    tk_image = ImageTk.PhotoImage(image)
    label.config(image=tk_image)
    label.image = tk_image


label = ttk.Label(root)
label.pack()
update_image(original_image)


output_directory = 'preview'
os.makedirs(output_directory, exist_ok=True)

def generate_and_display_images():
    for i in range(36):
        augmented_image = transform(original_image)
        
       
        save_path = os.path.join(output_directory, f'dog_augmented_{i}.png')
        torchvision.utils.save_image(augmented_image, save_path)
        
        
        update_image(augmented_image)
        root.update()


generate_button = ttk.Button(root, text="Generate Augmented Images", command=generate_and_display_images)
generate_button.pack()

root.mainloop()
