def windChill(V, T):
    V = V * 2.23694
    T = 1.8*(T-273) + 32.
    R =35.74 + 0.6215 * T  - 35.75 * (V**0.16) +0.4275 * T * (V**0.16)
    print("wind chill in farenheit: ", int(R))