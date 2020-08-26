#1-2-6
# import os
# cwd = os.getcwd()
# print(cwd)

#1-2-7-1
# import shutil
# source_file_path = "C:\\Users\\sketd\\PycharmProjects\\pythonProject\\DSC01129.ARW.jpg"
# target_file_path = "C:\\Users\\sketd\\PycharmProjects\\image folder\\my_image.jpg"
# shutil.copy(source_file_path, target_file_path)


#1-2-7-1
# from PIL import Image
# source_file_path = "C:\\Users\\sketd\\PycharmProjects\\pythonProject\\DSC01129.ARW.jpg"
# im = Image.open(source_file_path)
# img_resize = im.resize((100, 100))
# target_file_path = "C:\\Users\\sketd\\PycharmProjects\\image_folder\\resizedImg.jpg"
# img_resize.save(target_file_path)


#1-2-7-2
# import os
# file_extension = os.path.splitext('C:\\Users\\sketd\\PycharmProjects\\image_folder\\resizedImg.jpg')[1]
# print(file_extension)

#Rock-paper-scirss
import random

count = 0
while True:
    con_ch = random.randint(1,3)
    print(con_ch)

    count += 1

    if (count == 1):
        print("Now please enter your choice no. \n 1. Rock \n 2. paper \n 3. scissor \n")
        print("Now Your turn: ", end="")
        pl_ch = int(input())
    else:
        print("Now Your turn: ", end="")
        pl_ch = int(input())

    if (pl_ch == 1 and con_ch == 3):
        print("You Win!")
        print("it takes %i times!" %count)
        break
    elif (pl_ch == 3 and con_ch == 1):
        print("You Lose!")
    elif (pl_ch > con_ch):
        print("You Win!")
        print("it takes %i times!" %count)
        break
    elif (pl_ch == con_ch):
        print("Rock-paper-scissor...")
    else:
        print("You Lose!")