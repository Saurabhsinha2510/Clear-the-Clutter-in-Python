import os
temp_list = os.listdir()
for i in range(len(os.listdir())):
    if temp_list[i].endswith('.png'):
        os.rename(temp_list[i], f"{i+1}.png")