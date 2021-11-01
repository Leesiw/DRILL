class Star:

    type = 'Star'
    x = 100

    def change():
        x = 200
        print('x is ', x)

print('x IS ', Star.x)  # OK
Star.change()
print('x IS ', Star.x)

star = Star()
print('x IS ', star.x)
star.change()
