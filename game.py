import PySimpleGUI as sg
from PIL import Image, ImageDraw

# Create a new image with a white background
image = Image.new('RGB', (200, 200), 'white')

# Get a drawing context
draw = ImageDraw.Draw(image)

# Draw a circle representing the cookie
draw.ellipse((50, 50, 150, 150), fill='brown')

# Draw two eyes on the cookie
draw.rectangle((70, 70, 90, 90), fill='white')
draw.rectangle((110, 70, 130, 90), fill='white')
draw.rectangle((80, 80, 90, 90), fill='black')
draw.rectangle((120, 80, 130, 90), fill='black')

# Save the image to a file
image.save('cookie.png')

layout = [
    [sg.Text('Cookies: 0', key='cookies_text'), sg.Text('Points: 0', key='points_text'), sg.Text('Rebirths: 0', key='rebirths_text')],
    [sg.Button('Click'), sg.Button('Buy Cookie (1 point)')],
    [sg.Button('Rebirth (10 points)')],
    [sg.Image('cookie.png', key='cookie_image')]
]

window = sg.Window('Cookie Clicker').layout(layout)

cookies = 0
points = 0
rebirths = 0

while True:
    event, values = window.read()

    if event in (None, 'Exit'):
        break

    if event == 'Click':
        cookies += 1
        points += 1
        window['cookies_text'].update(f'Cookies: {cookies}')
        window['points_text'].update(f'Points: {points}')

    if event == 'Buy Cookie (1 point)':
        if points >= 1:
            cookies += 1
            points -= 1
            window['cookies_text'].update(f'Cookies: {cookies}')
            window['points_text'].update(f'Points: {points}')
        else:
            sg.popup("You don't have enough points to buy a cookie!")

    if event == 'Rebirth (10 points)':
        if points >= 10:
            points -= 10
            rebirths += 1
            cookies = 0
            window['cookies_text'].update(f'Cookies: {cookies}')
            window['points_text'].update(f'Points: {points}')
            window['rebirths_text'].update(f'Rebirths: {rebirths}')

window.close()