
print("Diffie-Hellman Key Exchange")

# Public Numbers
public_int_one = input("Enter the Public Number 1 (P): ")
public_int_two = input("Enter the Public Number 2 (G): ")

# Private Numbers
print("Enter the Private Numbers for Alice and Bob")
private_int_alice = input("Enter the Private Number for Alice (a): ")
private_int_bob = input("Enter the Private Number for Bob (b): ")

# Alice and Bob's Public Numbers
public_int_alice = (int(public_int_two) ** int(private_int_alice)) % int(public_int_one)
public_int_bob = (int(public_int_two) ** int(private_int_bob)) % int(public_int_one)

# Shared Secret Key
shared_secret_key_alice = (public_int_bob ** int(private_int_alice)) % int(public_int_one)
shared_secret_key_bob = (public_int_alice ** int(private_int_bob)) % int(public_int_one)

print("Public Number 1 (P): ", public_int_one)
print("Public Number 2 (G): ", public_int_two)
print("Private Number for Alice (a): ", private_int_alice)
print("Private Number for Bob (b): ", private_int_bob)
print("Public Number for Alice (A): ", public_int_alice)
print("Public Number for Bob (B): ", public_int_bob)

print("Shared Secret Key for Alice: ", shared_secret_key_alice)
print("Shared Secret Key for Bob: ", shared_secret_key_bob)
