from flask import Flask, render_template, Response,request, jsonify, send_file, session, flash, redirect, url_for
from werkzeug.utils import secure_filename
import logging
from pathlib import Path
from flask_cors import CORS
import pyttsx3


from flask_mysqldb import MySQL
import cv2
import os
import base64
import glob
import math
from PIL import Image
from os import listdir
import json
#from PIL import Image
import numpy as np
from decimal import Decimal
from datetime import date,datetime, timedelta  

from time import sleep
import logging


# Set up logging configuration
logging.basicConfig(level=logging.INFO)  # Set logging level to INFO

app = Flask(__name__)

CORS(app)

app.secret_key = 'your_secret_key'

app.config['MYSQL_HOST'] = '89.116.228.212'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admin@hydax23'
app.config['MYSQL_DB'] = 'hydax'
mysql = MySQL(app)

@app.route('/')
def index():
   return render_template('index.html')

@app.route('/rosai',methods=['GET', 'POST'])
def rosai():

    return render_template('rosai.html')

@app.route('/teach',methods=['GET', 'POST'])
def teach():
    return render_template('teach.html')


path1 = '/var/www/basic/static/'
#path1 = 'www.hydaxdroid.com/static/'
#path1 = app.static_folder
global user_folder

global pathh
@app.route('/create',methods=['GET', 'POST'])
def create():
    global user_folder
    global pathh
    data = request.json
    name = data.get('folder_name')
    user_folder = os.path.join(path1, name)
    os.mkdir(user_folder)
    p = Path(user_folder)
    pathh = ('/'.join( p.parts[4:]))
    app.config['USER_FOLDER'] = user_folder

    #return render_template('teach.html') 
    return redirect(url_for('nextpage'))

@app.route('/nextpage')
def nextpage():
    return render_template('teach.html')

global user_folder
global folder_path
global image_path1
    
global pathh1

@app.route('/page1', methods=['POST'])
def page1():
    global user_folder
    global image_path1
    global pathh1
    global folder_path
    root_folder = app.config.get('USER_FOLDER',)
    app.config['ROOT_FOLDER'] = root_folder


    filename = 'image1.png'
    securefilename = secure_filename(filename)
    image_path1 = os.path.join(app.config['ROOT_FOLDER'], securefilename)
        
    # Decode base64 image data
    image_data = request.form.get('image_data').split(',')[1]
    image_data_decoded = base64.b64decode(image_data)
   
    with open(image_path1, 'wb') as f:
         f.write(image_data_decoded)

    return redirect(url_for('next_page'))

@app.route('/next_page')
def next_page():
    return  render_template('page2.html')

@app.route('/page2', methods=['POST'])
def page2():
    global user_folder
    global image_path1
    global pathh1
    global folder_path
    root_folder = app.config.get('USER_FOLDER',)
    app.config['ROOT_FOLDER'] = root_folder


    filename = 'image2.png'
    securefilename = secure_filename(filename)
    image_path1 = os.path.join(app.config['ROOT_FOLDER'], securefilename)
        
    # Decode base64 image data
    image_data = request.form.get('image_data').split(',')[1]
    image_data_decoded = base64.b64decode(image_data)
   
    with open(image_path1, 'wb') as f:
         f.write(image_data_decoded)

    return redirect(url_for('next_page1'))

@app.route('/next_page1')
def next_page1():
    return render_template('page3.html')

@app.route('/page3', methods=['POST'])
def page3():
    global user_folder
    global image_path1
    global pathh1
    global folder_path
    root_folder = app.config.get('USER_FOLDER',)
    app.config['ROOT_FOLDER'] = root_folder


    filename = 'image3.png'
    securefilename = secure_filename(filename)
    image_path1 = os.path.join(app.config['ROOT_FOLDER'], securefilename)
        
    # Decode base64 image data
    image_data = request.form.get('image_data').split(',')[1]
    image_data_decoded = base64.b64decode(image_data)
   
    with open(image_path1, 'wb') as f:
         f.write(image_data_decoded)

    return redirect(url_for('next_page2'))

@app.route('/next_page2')
def next_page2():
    return render_template('page4.html')


@app.route('/page4', methods=['POST'])
def page4():
    global user_folder
    global image_path1
    global pathh1
    global folder_path
    root_folder = app.config.get('USER_FOLDER',)
    app.config['ROOT_FOLDER'] = root_folder


    filename = 'image4.png'
    securefilename = secure_filename(filename)
    image_path1 = os.path.join(app.config['ROOT_FOLDER'], securefilename)
        
    # Decode base64 image data
    image_data = request.form.get('image_data').split(',')[1]
    image_data_decoded = base64.b64decode(image_data)
   
    with open(image_path1, 'wb') as f:
         f.write(image_data_decoded)

   # return redirect(url_for('submit'))
    #return jsonify({'Image saved successfully.'}), 200
    return 'Image is saved'


@app.route('/submit',methods=['GET','POST'])

def submit():
    global user_folder
    global folder_path
    global image_path1
    global pathh
    global pathh1
    list1 = []
    shapes = []
    firstimgshape = []
    NonBP=[]
    NBP=[]
    calc=[]

    path1 = (user_folder)
    
   # files = os.listdir(folder_path)
    
    images=[]

    #file_list = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files = sorted(os.listdir(app.config['ROOT_FOLDER']))

    for f in files:
       images.append(f)
    print('list of image in folder:', images)

    
    firstimage = images[0]
    print("firstimage:", firstimage)
    firstimagepath = app.config['ROOT_FOLDER']
    imagepath1 = os.path.join(firstimagepath, firstimage)
    print("firstimagepath:",imagepath1)
    
    p1 = Path(imagepath1)
    imagepath1 = ('/'.join(p1.parts[4:]))
    
    path1 = (user_folder)
    #folderpath = (folder_path)
    print('userfolder:', path1)
    #firstimage = folderpath[0]
    #print("folderpath:", folderpath)
    
    for root, dirs, files in os.walk(path1):
        for file in files:
            if file.lower().endswith(('.png')):
                list1.append(os.path.join(root, file))

    print(list1)
    print(f"Found {len(list1)} image files in the folder:")
    #i=2
    
    img1=cv2.imread(list1[0])
    img1_canny=cv2.Canny(img1,100,150)
    cv2.imwrite(f'/var/www/basic/static/cannyimages/cannyimage1.png',img1_canny)

    img2=cv2.imread(list1[1])
    img2_canny=cv2.Canny(img2,100,150)
    cv2.imwrite(f'/var/www/basic/static/cannyimages/cannyimage2.png',img2_canny)
    
    img3=cv2.imread(list1[2])
    img3_canny=cv2.Canny(img3,100,150)
    cv2.imwrite(f'/var/www/basic/static/cannyimages/cannyimage3.png',img3_canny)

    img4=cv2.imread(list1[3])
    img4_canny=cv2.Canny(img4,100,150)
    cv2.imwrite(f'/var/www/basic/static/cannyimages/cannyimage4.png',img4_canny)
    

    if img1_canny.shape == img4_canny.shape:
        non_black_before_img1=np.sum(img1_canny)
        print("non_black_pix_before_img1:",non_black_before_img1)

        non_black_before_img2=np.sum(img2_canny)
        print("non_black_pix_before_img2:",non_black_before_img2)

        non_black_before_img3=np.sum(img3_canny)
        print("non_black_pix_before_img3:",non_black_before_img3)
        

        non_black_before_img4=np.sum(img4_canny)
        print("non_black_pix_before_img4:",non_black_before_img4)

        add1=cv2.add(img1_canny,img2_canny)
        white_pixel_add1=np.sum(add1 == 255)
        print("Number of white pixel add1:",white_pixel_add1)
       # print("After subtract img1 with img2:",difff1)
        non_black_after_img1=np.sum(add1!=0)
        print("Non-black_after_img1:",non_black_after_img1)

        add2=cv2.add(img2_canny,img3_canny)
        white_pixel_add2=np.sum(add2 == 255)
        print("Number of white pixel add2:",white_pixel_add2)
        #print("After subtract img2 with img3:",difff2)
        non_black_after_img2=np.sum(add2!=0)
        print("Non-black_after_img2:",non_black_after_img2)

        add3=cv2.add(img3_canny,img4_canny)
        white_pixel_add3=np.sum(add3 == 255)
        print("Number of white pixel add3:",white_pixel_add3)
        #print("After subtract img3 with img4:",difff3)
        non_black_after_img3=np.sum(add3!=0)
        print("Non-black_after_img3:",non_black_after_img3)

        add4=cv2.add(img2_canny,img3_canny)
        white_pixel_add4=np.sum(add4 == 255)
        print("Number of white pixel add4:",white_pixel_add4)
        #print("After subtract img4 with img1:",difff4)
        non_black_after_img4=np.sum(add4!=0)
        print("Non-black_after_img4:",non_black_after_img4)


        image1=Image.open('/var/www/basic/static/cannyimages/cannyimage1.png')
        img_array=np.array(image1)
        white_pixels=np.where(img_array == 255)
        std_dev_x_1=np.std(white_pixels)
        print("Standard Dev of img1:",std_dev_x_1)

        image2=Image.open('/var/www/basic/static/cannyimages/cannyimage2.png')
        img_array_2=np.array(image2)
        white_pixels_1=np.where(img_array_2 == 255)
        std_dev_x_2=np.std(white_pixels_1)
        print("Standard Dev of img2:",std_dev_x_2)

        image3=Image.open('/var/www/basic/static/cannyimages/cannyimage3.png')
        img_array_3=np.array(image3)
        white_pixels_2=np.where(img_array_3 == 255)
        std_dev_x_3=np.std(white_pixels_2)
        print("Standard Dev of img3:",std_dev_x_3)


        image4=Image.open('/var/www/basic/static/cannyimages/cannyimage4.png')
        img_array_4=np.array(image4)
        white_pixels_3=np.where(img_array_4 == 255)
        std_dev_x_4=np.std(white_pixels_3)
        print("Standard Dev of img4:",std_dev_x_4)
    
        
        
        all_white_pixels = np.vstack([std_dev_x_1,std_dev_x_2,std_dev_x_3,std_dev_x_4])

        std_deviation = np.std(all_white_pixels, axis=0)
        
        average_std_deviation = np.mean(all_white_pixels, axis=0)

        print("Avg of Standard Deviation :", average_std_deviation)


        
        dat=[non_black_after_img1,non_black_after_img2,non_black_after_img3,non_black_after_img4]
        Mean=np.mean(dat)
        #print("Meann:",Mean)
        Std_dev=np.std(dat)
        #print("Dev:",Std_dev)
        Uthreshold=Mean+Std_dev
        #print("Uthh:",Uthreshold)
        
       #NBP = list(map(int, dat))
        NBP = int(non_black_after_img1)
        print('typecasting of list:',NBP)
        
        
        
        my_list_json = json.dumps(NBP)
   
  

    cursor=mysql.connection.cursor()
    
    # Define the SQL query to insert the data into the table
    insert_query = "INSERT INTO teach (product,image1,Uthreshold,non_black_pixels) VALUES (%s, %s, %s ,%s)"
    data = (pathh,imagepath1,Uthreshold, my_list_json )

    # Execute the SQL query with the list and string data as parameters
    cursor.execute(insert_query, data)

    # Commit the changes to the database
    mysql.connection.commit()

    # Close the cursor and connection
    cursor.close()
    message = {'message': 'Data Stored!'}
    return jsonify(message)
    #return 'data stored'

@app.route('/openn',methods=['GET', 'POST'])
def openn():
    cur=mysql.connection.cursor()
   #cur.execute("SELECT image1 FROM teach ")
    cur.execute('SELECT image1 FROM teach ORDER BY SerialNo DESC LIMIT 5')
    image_paths=[row[0] for row in cur.fetchall()]
    mysql.connection.commit()
    cur.close()
    return render_template('openn.html',image_paths=image_paths)

global non_black_pixels
global upper_threshold
   
TEST_FOLDER = '/var/www/basic/static/test'
#TEST_FOLDER = 'test'
app.config['TEST_FOLDER'] = TEST_FOLDER

global pathh2
@app.route('/handle_click',methods=['GET','POST'])
def handle_click():
    global pathh2
    href_link = request.form.get('href')
    print('imagepath:', href_link)

    p2 = Path(href_link)
    pathh2 = ('/'.join(p2.parts[2:]))
    print('extractedpath:', pathh2)
   
   #return render_template('display.html', href_value = pathh2)
    return jsonify({'success': True})

@app.route('/display',methods=['GET','POST'])
def display():
    global pathh2
    print("extracted path from handle click:",pathh2)
    return render_template('display.html', href_value = pathh2)

@app.route('/test',methods=['GET','POST'])
def test():
    global message
    global user_folder
    global user_folder1
    global image_path1
    global pathh2
    global pathh
   
    filename = 'test.png'
    securefilename = secure_filename(filename)
    image_path1 = os.path.join(app.config['TEST_FOLDER'], securefilename)
        
    # Decode base64 image data
    image_data = request.form.get('image_data').split(',')[1]
    image_data_decoded = base64.b64decode(image_data)
   
    with open(image_path1, 'wb') as f:
         f.write(image_data_decoded)

    loadpath = '/var/www/basic/'
    
    user_folder1 = os.path.join(loadpath, pathh2)
   
 
    #return render_template('openn.html')
    return redirect(url_for('openn'))
 
global message

@app.route('/verify',methods=['GET','POST'])
def verify():
    global user_folder
    global user_folder1
    global image_path1
    global pathh2
    global pathh
    global message
   
    message= None
    print("user_folder1:", user_folder1)
 
    frame1 = cv2.imread(image_path1)

    #new_dimensions = (150, 100)

    # Resize the image using cv2.resize()
   # frame1 = cv2.resize(frame1, new_dimensions)

    load1 = cv2.imread(user_folder1)
    load1_canny = cv2.Canny(load1,100,150)
    print("shapeframe1:",frame1.shape)
    print("shapeload1:",load1.shape)
    frame1_canny = cv2.Canny(frame1,100,150)

    partname = os.path.dirname(pathh2)
    

    cur=mysql.connection.cursor()

    cur.execute('SELECT Image1 FROM teach ORDER BY SerialNo DESC LIMIT 5')
    image_paths=[row[0] for row in cur.fetchall()]
    
        

    if load1_canny.shape==frame1_canny.shape:
        add5 = cv2.add(load1_canny,frame1_canny)
        cv2.imwrite(f'/var/www/basic/static/canny/testt.png',add5)
        frame2=cv2.imread(f'/var/www/basic/static/canny/testt.png')
        white_pixel_test=np.sum(frame2 == 255)
        print("Number of white pixel for test:",white_pixel_test)
        non_black_pix = np.sum(add5!=0)

        print("#########")
        print("non_black_pix",non_black_pix)
        query="SELECT SerialNo, Uthreshold from teach where Product= %s"
        cur.execute(query, (partname,))
        Uth = cur.fetchall()
        Std_dev=cur.fetchall()

        print("uthershold:",Uth)
        print("std_dev:",Std_dev)
        #print("dtype uth:",type(Uth))
        serialid = Uth[0][0]
        Uthreshold = Uth[0][1]
    
        
        reject = "Rejected"
        accept = "Accepted"
        if non_black_pix > Uthreshold:
            print("non black pixel is greater than uthreshold")
            difference = abs(non_black_pix - Uthreshold)
            quotient = difference/Uthreshold
            percentage = quotient * 100
            formatted_num = format(percentage, ".2f")
            print(str(formatted_num)+ "%" + " " + reject)
            today = datetime.now()
            d1 = today.strftime("%d/%m/%Y %H:%M:%S")
            print("Date and Time:", today)
            query1 = "INSERT into open (SerialNo,product,Result,dateandtime) values (%s, %s, %s, %s)"
            data1 = (serialid,partname, reject, today)
            cur.execute(query1, data1)
            message = True
            
            
        else:
            print("non black pixel is lesser than uthreshold")
            difference = abs(non_black_pix - Uthreshold)
            quotient = difference/Uthreshold
            percentage = quotient * 100
            formatted_num = format(percentage, ".2f")
            print(str(formatted_num)+ "%" + " " + accept)
            today = datetime.now()
            #d1 = today.strftime("%d/%m/%Y %H:%M:%S")
            print("Date and Time:", today)         
            query1 = "INSERT into open (SerialNo,product,Result,dateandtime) values (%s, %s, %s, %s)"
            data1 = (serialid,partname, accept, today)
            cur.execute(query1, data1)
            message =  False
            
        
        
        mysql.connection.commit()
        cur.close()
 
    return render_template('openn.html', image_paths=image_paths,message = message)



@app.route('/rosac', methods=['GET','POST'])
def rosac():
    
    return render_template('main_rosa_c.html')

@app.route('/setup',methods=['GET'])
def setup():
    #newuser1 = session.get('serialid')

    return render_template('setup.html')



@app.route('/Sync',methods=['GET'])
def Sync():
    return render_template('async.html')



STATIC_FOLDER = '/var/www/basic/static/images'
app.config['STATIC_FOLDER'] = STATIC_FOLDER

CASCADE_FILE_PATH = '/var/www/basic/haarcascade_frontalface_default.xml'
app.config['CASCADE_FILE_PATH'] = CASCADE_FILE_PATH

# Load the Haar cascade classifier
face_cascade = cv2.CascadeClassifier(app.config['CASCADE_FILE_PATH'])

# Function to detect faces
def detect_faces(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Check if the image was read successfully
    if img is None:
        return None

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3, minSize=(100, 100))

    # If no face detected, return None
    if len(faces) == 0:
        return None

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Save the image with detected faces
    cv2.imwrite(image_path, img)

    return faces

@app.route('/capture', methods=['POST'])
def capture():
    filename = 'live.png'
    securefilename = secure_filename(filename)
    image_path1 = os.path.join(app.config['STATIC_FOLDER'], securefilename)

    # Get the base64 encoded image data from the request
    image_data = request.form.get('image_data')

    # Check if image data exists
    if not image_data:
        # If no image data, stay on the same page
        return render_template('async.html')

    # Decode and save the image data to a file
    image_data_decoded = base64.b64decode(image_data.split(',')[1])
    with open(image_path1, 'wb') as f:
        f.write(image_data_decoded)

    # Perform face detection
    faces = detect_faces(image_path1)

    if faces is not None and len(faces) > 0:  # Check if faces are detected
        # If face detected, redirect to detected.html
        print("Faces detected:", faces)  # Print detected faces
        return redirect(url_for('face__detected'))  # Redirect using url_for
    else:
        # If no face detected, stay on the same page
        print("No faces detected...")
        return redirect(url_for('async'))

@app.route('/face__detected')
def face__detected():
    # Get current time and add 5 hours and 30 minutes
    current_time = datetime.now() + timedelta(hours=5, minutes=30)
    current_hour = current_time.hour
    
    # Determine the greeting based on the adjusted time
    if current_hour < 12:
        greeting = "Good morning, Welcome to the stall of Hydax. We are engineers who make your products better. Our range of hydraulics accessories will give you one-stop solution for your power pack. Our machines are built with technologies such as Electro Chemical radiusing and Deburring for Deburring applications, Mechanical Deburring for Gear Deburring, Vacuum technology which is used for coolant filtration of machine coolant tanks, Water-based washing machines, and Tres, which is a solvent-based part cleaning machine. I am also a product of Hydax and I am called ROSA. I come in different avatars. ROSA I, as you see in this stall, can be used for part inspection. ROSA C is what I am called. I can be your catalog droid to help out humans find information they need. ROSA G is another Avatar which holds our products. Please feel free to look into the video on my screen below"
    elif current_hour < 15:
        greeting = "Good afternoon, Welcome to the stall of Hydax. We are engineers who make your products better. Our range of hydraulics accessories will give you one-stop solution for your power pack. Our machines are built with technologies such as Electro Chemical radiusing and Deburring for Deburring applications, Mechanical Deburring for Gear Deburring, Vacuum technology which is used for coolant filtration of machine coolant tanks, Water-based washing machines, and Tres, which is a solvent-based part cleaning machine. I am also a product of Hydax and I am called ROSA. I come in different avatars. ROSA I, as you see in this stall, can be used for part inspection. ROSA C is what I am called. I can be your catalog droid to help out humans find information they need. ROSA G is another Avatar which holds our products. Please feel free to look into the video on my screen below"
    else:
        greeting = "Good evening, Welcome to the stall of Hydax. We are engineers who make your products better. Our range of hydraulics accessories will give you one-stop solution for your power pack. Our machines are built with technologies such as Electro Chemical radiusing and Deburring for Deburring applications, Mechanical Deburring for Gear Deburring, Vacuum technology which is used for coolant filtration of machine coolant tanks, Water-based washing machines, and Tres, which is used for coolant filtration of machine coolant tanks, Water-based washing machines, and Tres, which is a solvent-based part cleaning machine. I am also a product of Hydax and I am called ROSA. I come in different avatars. ROSA I, as you see in this stall, can be used for part inspection. ROSA C is what I am called. I can be your catalog droid to help out humans find information they need. ROSA G is another Avatar which holds our products. Please feel free to look into the video on my screen below"
    
    # Pass the greeting to the template
    return render_template('detected.html', greeting=greeting)
