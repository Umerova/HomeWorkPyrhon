def taxi_fare(distance_km):

    distance_m = distance_km * 1000
    blocks = distance_m / 140
    blocks_rounded = int(blocks) + (1 if blocks % 1 > 0 else 0)
    fare = 4 + (blocks_rounded * 0.25)
    print(fare)

    return fare
