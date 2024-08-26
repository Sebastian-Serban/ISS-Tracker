import turtle, json, urllib.request, time

screen = turtle.Screen()
screen.setup(720,360)
screen.setworldcoordinates(-180,-90, 180,90)
screen.bgpic("ISS\map.gif")

screen.register_shape("ISS\iss.gif")
iss = turtle.Turtle()
iss.shape("ISS\iss.gif")
iss.setheading(45)
iss.color("red")
iss.penup()

def setup():
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    latitude = location['latitude']
    longitude = location['longitude']
    iss.goto(float(longitude), float(latitude))


url = "http://api.open-notify.org/iss-now.json"

setup()
while True:
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())
    location = result['iss_position']
    latitude = location['latitude']
    longitude = location['longitude']
    print("Latitude: {}, Longitude: {}".format(latitude, longitude))
    iss.pendown()
    iss.goto(float(longitude), float(latitude))
    iss.showturtle()
    iss.penup()

    time.sleep(1)

turtle.done()

