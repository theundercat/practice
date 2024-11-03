candidate1 = "Trump"
candidate2 = "Harris"

print(f"Who will win the election?")
print(f"{candidate1}? or {candidate2}?")
Choice = input(f"Pick wisely:")

if Choice == candidate1:
    print(f"MURICA")

elif Choice == candidate2:
    print(f"AMERICA")

else:
    print(f"Nice try.")
