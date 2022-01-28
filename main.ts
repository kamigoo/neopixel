let color = 0
let led2 = 0
let strip = neopixel.create(DigitalPin.P1, 10, NeoPixelMode.RGB)
basic.showString("LED")
basic.forever(function () {
    led2 = randint(0, 9)
    color = neopixel.rgb(randint(0, 255), randint(0, 255), randint(0, 255))
    strip.setPixelColor(led2, color)
    strip.show()
})
