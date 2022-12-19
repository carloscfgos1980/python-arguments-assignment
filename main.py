# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line


def greet(name='Doc', greeting="Hello"):
    message = f'{greeting}, {name}'
    return message


print(greet('Bob', "What's up!"))


def force(mass=1, body='earth'):
    gravity = {
        'earth': 9.8,
        'sun': 274.1,
        'jupiter': 24.9,
        'neptune': 11.2,
        'saturne': 10.4,
        'uranus': 8.9,
        'venus': 8.9,
        'mars': 3.7,
        'mercury': 3.7,
        'moon': 1.6,
        'pluto': 0.6
    }
    force = gravity[body] * mass
    return f'The force of {body} is {force}'


print(force())


def pull(m1, m2, d):
    G = (6.674) * (10 ** -10)
    pull = G * (((m1) * m2)/d**2)

    return pull


print(pull(800, 1500, 3))
