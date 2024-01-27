total_sweets = int(input("Enter the total number of sweets: "))
num_pupils = int(input("Enter the number of pupils attending: "))

sweets_per_pupil = total_sweets // num_pupils
sweets_left_over = total_sweets % num_pupils

print(f"Each pupil will receive {sweets_per_pupil} sweets.")
print(f"There will be {sweets_left_over} sweets left over.")
