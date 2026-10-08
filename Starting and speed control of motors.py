# Starting-and-speed-control-of-motors
print("DC Motor Starting and Speed Control")

V = float(input("Enter supply voltage (V): "))
Ia = float(input("Enter armature current (A): "))
Ra = float(input("Enter armature resistance (ohm): "))
flux = float(input("Enter flux (Wb): "))
K = float(input("Enter motor constant K: "))

# Back EMF
Eb = V - (Ia * Ra)

# Calculate speed
N = Eb / (K * flux)

print("\n--- Motor Results ---")
print("Back EMF =", Eb, "V")
print("Motor Speed =", N, "RPM")

print("\nSpeed Control Methods:")
print("1. Armature Voltage Control")
print("2. Field Flux Control")
print("3. Armature Resistance Control")

choice = int(input("Select speed control method (1/2/3): "))

if choice == 1:
    new_V = float(input("Enter new armature voltage (V): "))
    new_Eb = new_V - (Ia * Ra)
    new_N = new_Eb / (K * flux)
    print("New Motor Speed =", new_N, "RPM")

elif choice == 2:
    new_flux = float(input("Enter new flux (Wb): "))
    new_N = Eb / (K * new_flux)
    print("New Motor Speed =", new_N, "RPM")

elif choice == 3:
    new_Ra = float(input("Enter new armature resistance (ohm): "))
    new_Eb = V - (Ia * new_Ra)
    new_N = new_Eb / (K * flux)
    print("New Motor Speed =", new_N, "RPM")

else:
    print("Invalid choice")
