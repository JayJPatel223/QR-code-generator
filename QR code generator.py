# QR CODE GENERATOR AND SCANNER

import pyqrcode
import pyzbar.pyzbar as pyzbar
import cv2

ans = input('Do you want to Generate new QR code or Scan an existing one?(G/S): ')

# For Generating New QR Code

if ans.upper() == 'G':
    reply = input('Would you like to Generate the QR Code for a Single Person or Multiple People?(S/M): ')

    # For Single Person

    if reply.upper() == 'S':
        name = input('Please Enter the Name: ') 
        rollno = input('Please Enter the roll number: ')
        std = input('Please Enter the Standard and Division: ')
        remark = input('Please Enter Special Remarks(if any). If not press Enter: ')
        name1 = input('Please Enter the Name you want of the File: ')

        if remark is True: 
            details = f'''Name: {name}.\nRoll number: {rollno}.\nStandard: {std}.\nSpecial Remarks: {remark}.'''

        else:
            details = f'''Name: {name}.\nRoll number: {rollno}.\nStandard: {std}.'''

        qr = pyqrcode.create(details)  # To create QR Code
        qr.png(name1 + '.png', scale=8)   # For format and size of image output

    # For Multiple People

    elif reply.upper() == 'M':
        i = 1

        num = int(input('Please Enter the Number of Students: '))

        while i <= num:
            print(f'\nPlease Enter the Details of Student No. {i}.')
            name = input(f'\nPlease Enter the Name of Student No. {i}: ')
            rollno = input(f'Please Enter the Roll Number of Student No. {i}: ')
            std = input(f'Please Enter the Standard and Division of Student No. {i}: ')
            remark = input(f'Please Enter Special Remarks of Student No. {i}(if any). If not press Enter: ')
            name1 = input(f'Please Enter the Name you want for the File of Student No. {i}: ')
            i += 1

            if remark is True:
                details = f'''Name: {name}.\nRoll number: {rollno}.\nStandard: {std}.\nSpecial Remarks: {remark}.'''

            else:
                details = f'''Name: {name}.\nRoll number: {rollno}.\nStandard: {std}.'''

            qr = pyqrcode.create(details)   # To create QR Code
            qr.png(name1 + '.png', scale=8)    # For format and size of image output

    else:
        print('Enter a Valid Response.')

# For Scanning

elif ans.upper() == 'S':
    print('\nScanning...\n')
    i = 1

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)   # To Open Camera
    while i < 2:
        _, frame = cap.read()     # To Read the Video and store the information in "frame" Variable
        decoded = pyzbar.decode(frame)      # To decode the information in "frame" and store the information in "decoded" variable
        for obj in decoded:
            print(obj.data.decode('ascii'))    # To print the data in the variable "decoded" in ASCII Format
            i += 1
        cv2.imshow('QR Code', frame)    # To Open a Window with name "QR Code" to display information stored in "frame"
        cv2.waitKey(5)
    cv2.destroyAllWindows()     # To Destroy the "QR Code" Window

else:
    print('Please Enter a Valid Option.')