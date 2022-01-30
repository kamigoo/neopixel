color = 0
led2 = 0
strip = neopixel.create(DigitalPin.P1, 10, NeoPixelMode.RGB)
basic.show_string("LED")

def on_forever():
    global led2, color
    led2 = randint(0, 9)
    color = neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    strip.set_pixel_color(led2, color)
    strip.show()
basic.forever(on_forever)
