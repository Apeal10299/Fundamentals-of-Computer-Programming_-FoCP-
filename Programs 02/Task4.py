#4.A kindly teacher wishes to distribute a tub of sweets between her pupils. 
# She will first count the sweets and then divide them according to how many pupils attend that day. 
# Write a program that will tell the teacher how many sweets to give to each pupil, and how many she will have left over.

pupils=int(input("Enter the number of pupils:"))
sweets=int(input("Enter the number of sweets:"))
left_sweets=sweets-pupils
sweets_per_pupil=sweets//pupils
print(f"Each pupil will get {sweets_per_pupil} sweets and there will be {left_sweets} sweets left over")
