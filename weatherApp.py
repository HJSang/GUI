import tkinter as tk
import requests
HEIGHT = 700
WIDTH = 800

# ab18a46bdd5075a6f4b8c2bd914f9401
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={your api key}

def get_weather(city):
  weather_key = 'ab18a46bdd5075a6f4b8c2bd914f9401'
  url = 'https://api.openweathermap.org/data/2.5/weather'
  params = {'APPID':weather_key,'q':city,'units':'imperial'}
  response = requests.get(url, params=params)
  weather = response.json()
  name = weather['name']
  desc = weather['weather'][0]['description']
  temp = weather['main']['temp']
  label['text'] = str(name) + ' ' + str(desc) + ' ' + str(temp)


def test_function(entry):
  print('This is the entry:', entry)

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='land.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

button = tk.Button(frame, text="Test Button",font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7,relwidth=0.3,relheight=1)

# label = tk.Label(frame, text='Get Weather')
# label.place(relx=0.3,rely=0,relwidth=0.45,relheight=0.25)

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65,relheight=1)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame)
label.place(relwidth=1, relheight=1)

root.mainloop()
