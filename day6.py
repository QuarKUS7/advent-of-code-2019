from collections import defaultdict

if  __name__== '__main__':
    with open('./input/day6', 'r') as f:
        orbit_input = [l.strip().split(")") for l in f.readlines()]
    planets = [planet[0] for planet in orbit_input]
    planets1 = [planet[1] for planet in orbit_input]
    planets = set(planets+planets1)
    system = {}
    print(orbit_input)

    for inp in orbit_input:
        system[inp[1]] = inp[0]

    def compute_orbits(planet, system):
        if planet == 'COM':
            return 0
        next_p = system[planet]
        return 1 + compute_orbits(next_p, system)

    num_orb = 0
    for planet in planets:
        num_orb =  num_orb + compute_orbits(planet, system)
    print(num_orb)


