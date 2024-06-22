#Zac Lee wrote the code for Dog, Cat, Heart emoji filters.
#Felix wrote the rest of the code.

#Section 1: Modules imported for program
import sys
import cv2
import numpy as np
import dlib
from math import hypot
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os

#Section 2: Front-end user input so they can use program easily
print('Hello! Please indicate your identity by pressing a number corresponding to your identity and pressing Enter.')
print(" ") #spacing so that user can see it easier
print('Student/Alumni: 1 Parent: 2 Staff: 3 Industry Partner: 4') 
choice = int(input('Enter your corresponding number:'))#User input to determine what options to inform user about
print("")
print("There are 2 different screens that will be shown, one for filters and the other for backgrounds.")
print("They will only respond to the keyboard if you tap the right key and the screen is selected correctly")
print("For example, if you tap y, and the filter screen is selected, the filter will pop up.")
print("")
print("Here's some options of filters and background you can choose from.")
print("Just press the corresponding numbers and letters for the filters and backgrounds, and they will appear!")
print("please be patient as it might take a while to show up.")
print("Refer to this list at any time.")
print("")

if choice == 1: # if "student/alumni" choice is picked, keys for options for students/alumni will be printed.
    print("Filters")
    print(" ")
    print(" ")
    print("Miscellaneous Props")
    print(" ")
    print("Cat Ears: q")
    print("Dog Ears: w")
    print("Hearts pouring out: e")
    print("Sunglasses: r")
    print("Goggles: t")
    print(" ")
    print("Hats, Caps with Hashtags and SST Related Caps")
    print(" ")
    print("SST Logo : y")
    print("#I❤️SST! : u")
    print("#I❤️IDP! : i")
    print("#I❤️SSTINC! : o")
    print("#SST15Years : p")
    print(" ")
    print(" ")
    print("Backgrounds") 
    print(" ")
    print(" ")
    print("SST Front Sign beside General Office: 1")
    print("SST Pop-Up Sign near the Atrium and Grey-wall : 2")
    print("SST Campus : 3")
    print("SST Classroom : 4")
    print("SST Greywall : 5")
    print("SST Labs : 6")
    print("SSTInc : 7")

elif choice == 2: # if "parents" choice is picked, keys for options for parents will be printed.
    print("Filters")
    print(" ")
    print(" ")
    print("Miscellaneous Props")
    print(" ")
    print("Cat Ears: q")
    print("Dog Ears: w")
    print("Hearts pouring out: e")
    print("Sunglasses: r")
    print("Goggles: t")
    print(" ")
    print("Hats, Caps with Hashtags and SST Related Caps")
    print(" ")
    print("#I❤️SST! : u")
    print("#I❤️IDP! : i")
    print("#SST15Years : p")
    print(" ")
    print(" ")
    print("Backgrounds") 
    print(" ")
    print(" ")
    print("SST Front Sign beside General Office: 1")
    print("SST Pop-Up Sign near the Atrium and Grey-wall : 2")
    print("SST Campus : 3")

elif choice == 3: # if "staff" choice is picked, keys for options for staff will be printed.
    print("Filters")
    print(" ")
    print(" ")
    print("Miscellaneous Props")
    print(" ")
    print("Cat Ears: q")
    print("Dog Ears: w")
    print("Hearts pouring out: e")
    print("Sunglasses: r")
    print("Goggles: t")
    print(" ")
    print("Hats, Caps with Hashtags and SST Related Caps")
    print(" ")
    print("SST Logo : y")
    print("#I❤️SST! : u")
    print("#I❤️IDP! : i")
    print("#I❤️SSTINC! : o")
    print("#SST15Years : p")
    print(" ")
    print(" ")
    print("Backgrounds") 
    print(" ")
    print(" ")
    print("SST Front Sign beside General Office: 1")
    print("SST Pop-Up Sign near the Atrium and Grey-wall : 2")
    print("SST Campus : 3")
    print("SST Classroom : 4")
    print("SST Greywall : 5")
    print("SST Labs : 6")
    print("SSTInc : 7")
elif choice == 4: # if "Industry partners" choice is picked, keys for options for Industry partners will be printed.
    print("Filters")
    print(" ")
    print(" ")
    print("Hats, Caps with Hashtags and SST Related Caps")
    print(" ")
    print("Hat with Computer : z")
    print("Lab Glasses : t")
    print("#I❤️SST! : u")
    print("#I❤️IDP! : i")
    print("#SST15Years : p")
    print("Nurturing Innovators! : c")
    print("Funding The Future! : v")
    print("Impacting Lives! : b")
    print(" ")
    print(" ")
    print("Backgrounds") 
    print(" ")
    print(" ")
    print("SST Campus : 3")
    print("SST Labs : 6")
    print("SSTInc : 7")

#Section 3: Backend Loading of images and camera, creating of masks
# Loading camera
camera = cv2.VideoCapture(0) #captures video from camera
segmen = SelfiSegmentation() #initialises instance of segmentation model

# Loading images for filters
fimage = cv2.imread("default.png")  # this is so nothing shows up when the user has not pressed any keys (filters).
extrafimage = cv2.imread("default.png") #this is so filters using more than 1 image asset can display both images
fbgimage = cv2.imread("default.png")  # this is so nothing shows up when the user has not pressed any keys (background).
fbgimage = cv2.resize(fbgimage, (1920, 1080))

#Loading assets for "Miscellaneous Props"
left_ear = cv2.imread("leftpinkear.png")
right_ear = cv2.imread("rightpinkear.png")
left_ear1 = cv2.imread("leftdogear.png")
right_ear1 = cv2.imread("rightdogear.png")
sung_image = cv2.imread("sunglasses.png")
sung2_image = cv2.imread("goggles.jpeg")
hpr_image = cv2.imread("plsbepng.webp")

# Loading assets for "Hats, Caps with Hashtags and SST Related Caps"
cap_image = cv2.imread("sstlogo.png")
cap2_image = cv2.imread("ilovesst.png")
cap3_image = cv2.imread("idp.png")
cap4_image = cv2.imread("sstinc.png")
cap5_image = cv2.imread("sst15.png")
cap6_image = cv2.imread("comp.png")
cap7_image = cv2.imread("nurturing.png")
cap8_image = cv2.imread("funding.png")
cap9_image = cv2.imread("impacting.png")

#Loading assets for "Background Images"
bg_image = cv2.imread("sstsign.jpeg")
bg2_image = cv2.imread("bigsign.jpeg")
bg3_image = cv2.imread("campus.jpeg")
bg4_image = cv2.imread("class.jpeg")
bg5_image = cv2.imread("greywall.jpeg")
bg6_image = cv2.imread("labs.jpeg") 
bg7_image = cv2.imread("sstinc2.jpeg")

#Resizing assets for "Background Images" so it will perfectly fit the camera frame
bg_image = cv2.resize(bg_image, (1920, 1080))
bg2_image = cv2.resize(bg2_image, (1920, 1080))
bg3_image = cv2.resize(bg3_image, (1920, 1080))
bg4_image = cv2.resize(bg4_image, (1920, 1080))
bg5_image = cv2.resize(bg5_image, (1920, 1080))
bg6_image = cv2.resize(bg6_image, (1920, 1080))
bg7_image = cv2.resize(bg7_image, (1920, 1080))

#initiallising variables used for movement of hearts
x = 0
y = 1
a = 0
b = 0
c = 0
d = 0

# Creating a mask
mask = None
_ , frame = camera.read()
rows, cols, _ = frame.shape
ear_mask = np.zeros((rows, cols), np.uint8)
# Loading Face detector
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")


#Section 4: Response based on live input

# Initialized variable to store the key pressed
key_pressed = -1

while True: #while the loop is running
    check,frame=camera.read() #camera is read
    ear_mask.fill(0)
    #cv2.imshow("video",frame)
    frame = cv2.resize(frame, (1920, 1080)) #frame of camera is resized so it can be same size as background
    videoremovebg=segmen.removeBG(frame,fbgimage) #background is removed using segmentor model, "fbgimage" becomes the background

    faces = detector(frame) #face is detected using dlib detector
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # converting color space of input frame from BGR to grayscale
    
    for face in faces: #for each deteced face during the frame
        landmarks = predictor(gray_frame, face) #predicting landmarks/points on the face using shape predictor

        #Processing of where to put filter, size of filter and putting image in frame if keys pressed fall under "Dog" or "Cat" ears
        if key_pressed == ord('q') or key_pressed == ord('w'): #if key pressed is q or w

            # Adding the specific coordinates of the location of the top, center, left, and right parts of the left ear asset
            top_leftear = (landmarks.part(18).x + 20, landmarks.part(18).y - 100)
            center_leftear = (landmarks.part(19).x, landmarks.part(19).y - 80)
            left_leftear = (landmarks.part(17).x, landmarks.part(17).y - 80)
            right_leftear = (landmarks.part(20).x, landmarks.part(20).y + 20)

             # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
            ear_width1 = int(hypot(left_leftear[0] - right_leftear[0], left_leftear[1] - right_leftear[1]) * 1.7 + 30)
            ear_height1 = int(ear_width1 * 0.77 + 30)

            # New position for the left ear
            top_left1 = (int(center_leftear[0] - ear_width1 / 2), int(center_leftear[1] - ear_height1 / 2))
            bottom_right1 = (int(center_leftear[0] + ear_width1 / 2), int(center_leftear[1] + ear_height1 / 2))

            # Resizing the left ear asset to the correct size when the person moves, converting the image to grayscale, and creating a binary mask for the ear
            ear_pig1 = cv2.resize(left_ear, (ear_width1, ear_height1))
            ear_pig_gray1 = cv2.cvtColor(ear_pig1, cv2.COLOR_BGR2GRAY)
            _, ear_mask = cv2.threshold(ear_pig_gray1, 25, 255, cv2.THRESH_BINARY_INV)

            # Defining the region of interest for where the left ear is placed, applying the binary mask to the ear region, and removing the background at the area of the ear
            ear_area1 = frame[top_left1[1]: top_left1[1] + ear_height1, top_left1[0]: top_left1[0] + ear_width1]
            ear_area_no_leftear = cv2.bitwise_and(ear_area1, ear_area1, mask=ear_mask)
            final_leftear = cv2.add(ear_area_no_leftear, ear_pig1)

            # Placing the left ear in the frame at the specified location
            frame[top_left1[1]: top_left1[1] + ear_height1, top_left1[0]: top_left1[0] + ear_width1] = final_leftear

            # Adding the specific coordinates of the location of the top, center, left, and right parts of the right ear asset
            top_rightear = (landmarks.part(24).x + 20, landmarks.part(24).y - 70)
            center_rightear = (landmarks.part(25).x, landmarks.part(25).y - 70)
            left_rightear = (landmarks.part(23).x, landmarks.part(23).y)
            right_rightear = (landmarks.part(26).x, landmarks.part(26).y)

             # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
            rightear_width = int(hypot(left_rightear[0] - right_rightear[0], left_rightear[1] - right_rightear[1]) * 1.7 + 50)
            rightear_height = int(rightear_width * 0.77 + 50)

            # New position for the right ear
            top_left = (int(center_rightear[0] - rightear_width / 2), int(center_rightear[1] - rightear_height / 2))
            bottom_right = (int(center_rightear[0] + rightear_width / 2), int(center_rightear[1] + rightear_height / 2))

            # Resizing the right ear asset to the correct size when the person moves, converting the image to grayscale, and creating a binary mask for the ear
            rightear_pig = cv2.resize(extrafimage, (rightear_width, rightear_height))
            rightear_pig_gray = cv2.cvtColor(rightear_pig, cv2.COLOR_BGR2GRAY)
            _, ear_mask = cv2.threshold(rightear_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)

            # Defining the region of interest for where the right ear is placed, applying the binary mask to the ear region, and removing the background at the area of the ear
            rightear_area = frame[top_left[1]: top_left[1] + rightear_height, top_left[0]: top_left[0] + rightear_width]
            rightear_area_no_rightear = cv2.bitwise_and(rightear_area, rightear_area, mask=ear_mask)
            final_rightear = cv2.add(rightear_area_no_rightear, rightear_pig)

            # Placing the right ear in the frame at the specified location
            frame[top_left[1]: top_left[1] + rightear_height, top_left[0]: top_left[0] + rightear_width] = final_rightear

        #Processing of where to put filter, size of filter and putting image in frame if keys pressed fall under "glasses" or "goggles"
        elif key_pressed == ord('r') or key_pressed == ord('t'): #if key pressed is r or t
            # adding the specific coordinates of the location of the top, center, left and right parts of the asset
            top_glass = (landmarks.part(19).x, landmarks.part(19).y)
            left_glass = (landmarks.part(17).x, landmarks.part(17).y)
            right_glass = (landmarks.part(26).x, landmarks.part(26).y)
            center_glass = (landmarks.part(28).x, landmarks.part(21).y + int(glass_height / 4))

            # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
            glass_width = int(hypot(left_glass[0] - right_glass[0], left_glass[1] - right_glass[1])*1.2)
            glass_height = int(glass_width * 0.6)  # Adjust aspect ratio as needed

            # calculating width using hypothenuse of triangle derived from coordinates and height
            top_left = (int(center_glass[0] - glass_width / 2), int(center_glass[1] - glass_height / 2))
            bottom_right = (int(center_glass[0] + glass_width / 2), int(center_glass[1] + glass_height / 2))

            #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for glasses
            sunglasses_resized = cv2.resize(fimage, (glass_width, glass_height))
            sunglasses_gray = cv2.cvtColor(sunglasses_resized, cv2.COLOR_BGR2GRAY)
            _, glasses_mask = cv2.threshold(sunglasses_gray, 25, 255, cv2.THRESH_BINARY_INV)
            try:
                #Defining region of interest for where glasses is placed, applying binary mask to glasses region, removing background at the area of the glasses
                glasses_area = frame[top_left[1]: top_left[1] + glass_height, top_left[0]: top_left[0] + glass_width]
                glasses_area_no_glasses = cv2.bitwise_and(glasses_area, glasses_area, mask=glasses_mask)
                final_glasses = cv2.add(glasses_area_no_glasses, sunglasses_resized)
                # putting the glasses in the frame in the location
                frame[top_left[1]: top_left[1] + glass_height, top_left[0]: top_left[0] + glass_width] = final_glasses
            except:
                True
        #Processing of where to put filter, size of filter and putting image in frame if keys pressed fall under the category of "Hats"
        elif key_pressed == ord('t') or key_pressed == ord('y') or key_pressed == ord('u') or key_pressed == ord('i') or key_pressed == ord('o') or key_pressed == ord('p') or key_pressed == ord('z') or key_pressed == ord('x') or key_pressed == ord('c') or key_pressed == ord('v'): #if key pressed is t, y, u, i or o 

            # adding the specific coordinates of the location of the top, center, left and right parts of the asset
            top_hat = (landmarks.part(19).x, landmarks.part(19).y)
            left_hat = (landmarks.part(0).x, landmarks.part(0).y)
            right_hat = (landmarks.part(16).x, landmarks.part(16).y)
            hat_width = int(hypot(left_hat[0] - right_hat[0], left_hat[1] - right_hat[1]) * 1.45)
            hat_height = int(hat_width * 0.77)
            center_hat = (landmarks.part(28).x, landmarks.part(21).y - int(hat_height / 3))

            # calculating width using hypothenuse of triangle derived from coordinates and height
            top_left = (int(center_hat[0] - hat_width / 2), int(center_hat[1] - hat_height / 2))
            bottom_right = (int(center_hat[0] + hat_width / 2), int(center_hat[1] + hat_height / 2))

            #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for hats
            nose_pig = cv2.resize(fimage, (hat_width, hat_height))
            nose_pig_gray = cv2.cvtColor(nose_pig, cv2.COLOR_BGR2GRAY)
            _, nose_mask = cv2.threshold(nose_pig_gray, 25, 255, cv2.THRESH_BINARY_INV)

            #try except so program does not crash if code does not work
            try:
                #Defining region of interest for where hat is placed, applying binary mask to hat region, removing background at the area of the hat
                nose_area = frame[top_left[1]: top_left[1] + hat_height, top_left[0]: top_left[0] + hat_width]
                nose_area_no_nose = cv2.bitwise_and(nose_area, nose_area, mask=nose_mask)
                final_nose = cv2.add(nose_area_no_nose, nose_pig)
                # putting the hat in the frame in the location
                frame[top_left[1]: top_left[1] + hat_height, top_left[0]: top_left[0] + hat_width] = final_nose
            except:
                True
        elif key_pressed == ord('e'):

            # adding the specific coordinates of the location of the top, center, left and right parts of the asset at the left eye on the 1st height
            top_heart1 = (landmarks.part(38).x + 20, landmarks.part(38).y - a + 20)
            center_heart1 = (landmarks.part(40).x, landmarks.part(40).y - a)
            left_heart1 = (landmarks.part(36).x, landmarks.part(36).y - a)
            right_heart1 = (landmarks.part(39).x, landmarks.part(39).y - a)

            # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
            heart_width1 = int(hypot(left_heart1[0] - right_heart1[0], left_heart1[1] - right_heart1[1]) * 1.7 + y)
            heart_height1 = int(heart_width1 * 0.77 + y)

            # New position for the heart
            top_left1 = (int(center_heart1[0] - heart_width1 / 2), int(center_heart1[1] - heart_height1 / 2))
            bottom_right1 = (int(center_heart1[0] + heart_width1 / 2), int(center_heart1[1] + heart_height1 / 2))

            #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
            heart1 = cv2.resize(fimage, (heart_width1, heart_height1))
            heart_gray1 = cv2.cvtColor(heart1, cv2.COLOR_BGR2GRAY)
            _, heart_mask = cv2.threshold(heart_gray1, 25, 255, cv2.THRESH_BINARY_INV)

            #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
            heart_area1 = frame[top_left1[1]: top_left1[1] + heart_height1, top_left1[0]: top_left1[0] + heart_width1]
            heart_area_no_heart1 = cv2.bitwise_and(heart_area1, heart_area1, mask=heart_mask)
            final_heart1 = cv2.add(heart_area_no_heart1, heart1)
            # putting the heart in the frame in the location
            frame[top_left1[1]: top_left1[1] + heart_height1, top_left1[0]: top_left1[0] + heart_width1] = final_heart1

            # adding the specific coordinates of the location of the top, center, left and right parts of the asset at the right eye on the 1st height
            top_heart = (landmarks.part(43).x + 20, landmarks.part(43).y - a + 20)
            center_heart = (landmarks.part(47).x, landmarks.part(47).y - a)
            left_heart = (landmarks.part(42).x, landmarks.part(42).y - a)
            right_heart = (landmarks.part(45).x, landmarks.part(45).y - a)

            # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
            heart_width = int(hypot(left_heart[0] - right_heart[0], left_heart[1] - right_heart[1]) * 1.7 + y)
            heart_height = int(heart_width * 0.77 + y)

            # New position for the heart
            top_left = (int(center_heart[0] - heart_width / 2), int(center_heart[1] - heart_height / 2))
            bottom_right = (int(center_heart[0] + heart_width / 2), int(center_heart[1] + heart_height / 2))

            #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
            heart = cv2.resize(fimage, (heart_width, heart_height))
            heart_gray = cv2.cvtColor(heart, cv2.COLOR_BGR2GRAY)
            _, heart_mask = cv2.threshold(heart_gray, 25, 255, cv2.THRESH_BINARY_INV)

            #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
            heart_area = frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width]
            heart_area_no_heart = cv2.bitwise_and(heart_area, heart_area, mask=heart_mask)
            final_heart = cv2.add(heart_area_no_heart, heart)
            # putting the heart in the frame in the location
            frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width] = final_heart

            #changing the variable to make the heart move up, reset the heart when it reaches a certain height
            a += 5
            if a == 300:
                a = 0

            #to delay the heart 
            if x >= 75:

                # adding the specific coordinates of the location of the top, center, left and right parts of the asset at the 2nd height at the left eye
                top_heart2 = (landmarks.part(38).x + 20, landmarks.part(38).y - b + 20)
                center_heart2 = (landmarks.part(40).x, landmarks.part(40).y - b)
                left_heart2 = (landmarks.part(36).x, landmarks.part(36).y - b)
                right_heart2 = (landmarks.part(39).x, landmarks.part(39).y - b)

                # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
                heart_width2 = int(hypot(left_heart2[0] - right_heart2[0], left_heart2[1] - right_heart2[1]) * 1.7 + y)
                heart_height2 = int(heart_width2 * 0.77 + y)

                # New position for the heart
                top_left2 = (int(center_heart2[0] - heart_width2 / 2), int(center_heart2[1] - heart_height2 / 2))
                bottom_right2 = (int(center_heart2[0] + heart_width2 / 2), int(center_heart2[1] + heart_height2 / 2))

                #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
                heart2 = cv2.resize(fimage, (heart_width2, heart_height2))
                heart_gray2 = cv2.cvtColor(heart2, cv2.COLOR_BGR2GRAY)
                _, heart_mask = cv2.threshold(heart_gray2, 25, 255, cv2.THRESH_BINARY_INV)

                #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
                heart_area2 = frame[top_left2[1]: top_left2[1] + heart_height2, top_left2[0]: top_left2[0] + heart_width2]
                heart_area_no_heart2 = cv2.bitwise_and(heart_area2, heart_area2, mask=heart_mask)
                final_heart2 = cv2.add(heart_area_no_heart2, heart2)
                # putting the heart in the frame in the location
                frame[top_left2[1]: top_left2[1] + heart_height2, top_left2[0]: top_left2[0] + heart_width2] = final_heart2

                # adding the specific coordinates of the location of the top, center, left and right parts of the asset at the 2nd height at the right eye
                top_heart = (landmarks.part(43).x + 20, landmarks.part(43).y - b + 20)
                center_heart = (landmarks.part(47).x, landmarks.part(47).y - b)
                left_heart = (landmarks.part(42).x, landmarks.part(42).y - b)
                right_heart = (landmarks.part(45).x, landmarks.part(45).y - b)

                 # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
                heart_width = int(hypot(left_heart[0] - right_heart[0], left_heart[1] - right_heart[1]) * 1.7 + y)
                heart_height = int(heart_width * 0.77 + y)

                # New position for the heart
                top_left = (int(center_heart[0] - heart_width / 2), int(center_heart[1] - heart_height / 2))
                bottom_right = (int(center_heart[0] + heart_width / 2), int(center_heart[1] + heart_height / 2))

                #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
                heart = cv2.resize(fimage, (heart_width, heart_height))
                heart_gray = cv2.cvtColor(heart, cv2.COLOR_BGR2GRAY)
                _, heart_mask = cv2.threshold(heart_gray, 25, 255, cv2.THRESH_BINARY_INV)

                #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
                heart_area = frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width]
                heart_area_no_heart = cv2.bitwise_and(heart_area, heart_area, mask=heart_mask)
                final_heart = cv2.add(heart_area_no_heart, heart)
                # putting the heart in the frame in the location
                frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width] = final_heart


                #changing the variable to make the heart move up, reset the heart when it reaches a certain height
                b += 5
                if b == 300:
                    b = 0

            #delay the heart
            if x >= 150:

                # adding the specific coordinates of the location of the top, center, left and right parts of the asset at the 3rd height at the left eye
                top_heart2 = (landmarks.part(38).x + 20, landmarks.part(38).y - c + 20)
                center_heart2 = (landmarks.part(40).x, landmarks.part(40).y - c)
                left_heart2 = (landmarks.part(36).x, landmarks.part(36).y - c)
                right_heart2 = (landmarks.part(39).x, landmarks.part(39).y - c)

                # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
                heart_width2 = int(hypot(left_heart2[0] - right_heart2[0], left_heart2[1] - right_heart2[1]) * 1.7 + y)
                heart_height2 = int(heart_width2 * 0.77 + y)

                # New position for the heart
                top_left2 = (int(center_heart2[0] - heart_width2 / 2), int(center_heart2[1] - heart_height2 / 2))
                bottom_right2 = (int(center_heart2[0] + heart_width2 / 2), int(center_heart2[1] + heart_height2 / 2))

                #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
                heart2 = cv2.resize(fimage, (heart_width2, heart_height2))
                heart_gray2 = cv2.cvtColor(heart2, cv2.COLOR_BGR2GRAY)
                _, heart_mask = cv2.threshold(heart_gray2, 25, 255, cv2.THRESH_BINARY_INV)

                #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
                heart_area2 = frame[top_left2[1]: top_left2[1] + heart_height2, top_left2[0]: top_left2[0] + heart_width2]
                heart_area_no_heart2 = cv2.bitwise_and(heart_area2, heart_area2, mask=heart_mask)
                final_heart2 = cv2.add(heart_area_no_heart2, heart2)
                # putting the heart in the frame in the location
                frame[top_left2[1]: top_left2[1] + heart_height2, top_left2[0]: top_left2[0] + heart_width2] = final_heart2

                # adding the specific coordinates of the location of the top, center, left and right parts of the asset
                top_heart = (landmarks.part(43).x + 20, landmarks.part(43).y - c + 20)
                center_heart = (landmarks.part(47).x, landmarks.part(47).y - c)
                left_heart = (landmarks.part(42).x, landmarks.part(42).y - c)
                right_heart = (landmarks.part(45).x, landmarks.part(45).y - c)

                # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
                heart_width = int(hypot(left_heart[0] - right_heart[0], left_heart[1] - right_heart[1]) * 1.7 + y)
                heart_height = int(heart_width * 0.77 + y)

                # New position for the heart
                top_left = (int(center_heart[0] - heart_width / 2), int(center_heart[1] - heart_height / 2))
                bottom_right = (int(center_heart[0] + heart_width / 2), int(center_heart[1] + heart_height / 2))

                #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
                heart = cv2.resize(fimage, (heart_width, heart_height))
                heart_gray = cv2.cvtColor(heart, cv2.COLOR_BGR2GRAY)
                _, heart_mask = cv2.threshold(heart_gray, 25, 255, cv2.THRESH_BINARY_INV)

                #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
                heart_area = frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width]
                heart_area_no_heart = cv2.bitwise_and(heart_area, heart_area, mask=heart_mask)
                final_heart = cv2.add(heart_area_no_heart, heart)
                # putting the heart in the frame in the location
                frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width] = final_heart

                #changing the variable to make the heart move up, reset the heart when it reaches a certain height
                c += 5
                if c == 300:
                    c = 0

            #delay the heart
            if x >= 225:

                # adding the specific coordinates of the location of the top, center, left and right parts of the asset at the 4th height at the left eye
                top_heart2 = (landmarks.part(38).x + 20, landmarks.part(38).y - d + 20)
                center_heart2 = (landmarks.part(40).x, landmarks.part(40).y - d)
                left_heart2 = (landmarks.part(36).x, landmarks.part(36).y - d)
                right_heart2 = (landmarks.part(39).x, landmarks.part(39).y - d)

                # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
                heart_width2 = int(hypot(left_heart2[0] - right_heart2[0], left_heart2[1] - right_heart2[1]) * 1.7 + y)
                heart_height2 = int(heart_width2 * 0.77 + y)

                # New position for the heart
                top_left2 = (int(center_heart2[0] - heart_width2 / 2), int(center_heart2[1] - heart_height2 / 2))
                bottom_right2 = (int(center_heart2[0] + heart_width2 / 2), int(center_heart2[1] + heart_height2 / 2))

                #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
                heart2 = cv2.resize(fimage, (heart_width2, heart_height2))
                heart_gray2 = cv2.cvtColor(heart2, cv2.COLOR_BGR2GRAY)
                _, heart_mask = cv2.threshold(heart_gray2, 25, 255, cv2.THRESH_BINARY_INV)

                #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
                heart_area2 = frame[top_left2[1]: top_left2[1] + heart_height2, top_left2[0]: top_left2[0] + heart_width2]
                heart_area_no_heart2 = cv2.bitwise_and(heart_area2, heart_area2, mask=heart_mask)
                final_heart2 = cv2.add(heart_area_no_heart2, heart2)
                # putting the heart in the frame in the location
                frame[top_left2[1]: top_left2[1] + heart_height2, top_left2[0]: top_left2[0] + heart_width2] = final_heart2

                # adding the specific coordinates of the location of the top, center, left and right parts of the asset at the 4th height at the right eye
                top_heart = (landmarks.part(43).x + 20, landmarks.part(43).y - d + 20)
                center_heart = (landmarks.part(47).x, landmarks.part(47).y - d)
                left_heart = (landmarks.part(42).x, landmarks.part(42).y - d)
                right_heart = (landmarks.part(45).x, landmarks.part(45).y - d)

                # Calculating the width using the hypotenuse of the triangle derived from coordinates and calculating height
                heart_width = int(hypot(left_heart[0] - right_heart[0], left_heart[1] - right_heart[1]) * 1.7 + y)
                heart_height = int(heart_width * 0.77 + y)

                # New position for the heart
                top_left = (int(center_heart[0] - heart_width / 2), int(center_heart[1] - heart_height / 2))
                bottom_right = (int(center_heart[0] + heart_width / 2), int(center_heart[1] + heart_height / 2))

                #resizing asset to be correct size when person moves, making image grayscale and creating a binary mask for heart
                heart = cv2.resize(fimage, (heart_width, heart_height))
                heart_gray = cv2.cvtColor(heart, cv2.COLOR_BGR2GRAY)
                _, heart_mask = cv2.threshold(heart_gray, 25, 255, cv2.THRESH_BINARY_INV)

                #Defining region of interest for where heart is placed, applying binary mask to heart region, removing background at the area of the heart
                heart_area = frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width]
                heart_area_no_heart = cv2.bitwise_and(heart_area, heart_area, mask=heart_mask)
                final_heart = cv2.add(heart_area_no_heart, heart)
                # putting the heart in the frame in the location
                frame[top_left[1]: top_left[1] + heart_height, top_left[0]: top_left[0] + heart_width] = final_heart

            #changing the variable to make the heart move up, reset the heart when it reaches a certain height
                d += 5
                if d == 300:
                    d = 0

            #increment for the delaying of the hearts
            x += 5    

    # Changing filters based on key press (captured only once)

    key = cv2.waitKey(1)

    if key != -1:  # Check if any key is pressed
        key_pressed = key

    # If key pressed  = ... , final image will be changed to option user pressed.
    if key_pressed == ord('q'): 
        fimage = left_ear
        extrafimage = right_ear
    elif key_pressed == ord('w'): 
        fimage = left_ear1
        extrafimage = right_ear1
    elif key_pressed == ord('e'):
        fimage = hpr_image
    elif key_pressed == ord('r'):
        fimage = sung_image
    elif key_pressed == ord('t'):
        fimage = sung2_image
    elif key_pressed == ord('y'):
        fimage = cap_image
    elif key_pressed == ord('u'):
        fimage = cap2_image
    elif key_pressed == ord('i'):
        fimage = cap3_image
    elif key_pressed == ord('o'):
        fimage = cap4_image
    elif key_pressed == ord('p'):
        fimage = cap5_image
    elif key_pressed == ord('z'):
        fimage = cap6_image
    elif key_pressed == ord('x'):
        fimage = cap7_image
    elif key_pressed == ord('c'):
        fimage = cap8_image
    elif key_pressed == ord('v'):
        fimage = cap9_image
    elif key_pressed == ord('1'):
        fbgimage = bg_image
    elif key_pressed == ord('2'):
        fbgimage = bg2_image
    elif key_pressed == ord('3'):
        fbgimage = bg3_image
    elif key_pressed == ord('4'):
        fbgimage = bg4_image
    elif key_pressed == ord('5'):
        fbgimage = bg5_image
    elif key_pressed == ord('6'): 
        fbgimage = bg6_image
    elif key_pressed == ord('7'):
        fbgimage = bg7_image

    # Displaying the final product
    cv2.imshow("Frame for filters", frame)
    cv2.imshow("Frame for Background", videoremovebg)
    

    # code shuts down if "esc" key is pressed
    if key_pressed == 27: 
        break

camera.release()
cv2.destroyAllWindows()


