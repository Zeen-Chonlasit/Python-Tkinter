from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Learn To Code at Codemy.com')
root.iconbitmap('c:/Users/chonl/Downloads/icons8-go-back-64.png')
root.geometry("400x400")
root.configure(background='green')

# http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B

try:
    api_request = requests.get("http://www.airnowapi.org/aq/observation/zipCode/current/?format=application/json&zipCode=" + zip.get() + "&distance=5&API_KEY=96A38DFD-5C56-4740-AD99-E38C0C855A1B")
    api = json.loads(api_request.content)
except Exception as e:
    api = "Error..."

myLabel = Label(root, text=api)
myLabel.pack()

root.mainloop()