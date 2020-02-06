import requests
import face_recognition
import cv2
import main_using_csv
import time
import pyttsx3
engine = pyttsx3.init()
import numpy as np

##################################
def main(identity):
    start=time.time()
    period = 100
    
#########################################
        
    ##############    ###########333
    def email_alert(first,second):
        report = {}
        report["value1"] = first+" was absent in "+identity+" class"
        #requests.post("https://maker.ifttt.com/trigger/attendance/with/key/k8H_gZtgd2zBf_TEplDRrKKMRaD0OId-0gSNhWEUDvj", data=report) 
        if (first=="ashwin"):
            requests.post("https://maker.ifttt.com/trigger/attendance/with/key/k8H_gZtgd2zBf_TEplDRrKKMRaD0OId-0gSNhWEUDvj", data=report)
        elif(first=="aparna") :  
            requests.post("https://maker.ifttt.com/trigger/attendance/with/key/bdrm5u6QnaHdC188wU4M9HirXfRMD45BWuWd2zfyyAk", data=report)
         
#######################################
   
    
    
    
    ###############FACE_RECOGNITION WORK###############
    # Get a reference to webcam #0 (the default one)
    
    video_capture = cv2.VideoCapture(0)
    
    
    # Load a sample picture and learn how to recognize it.
    ashwin = face_recognition.load_image_file("ashwin.jpg")
    face_encoding = face_recognition.face_encodings(ashwin,num_jitters = 30)[0]
    
    aparna = face_recognition.load_image_file("appu.jpeg")
    face_encoding1 = face_recognition.face_encodings(aparna,num_jitters = 30)[0]
    
    
    known_face_encodings = [
            face_encoding, face_encoding1
        
    ]
    known_face_names = [
        "ashwin", "aparna"
        
        
    ]
    
    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    #process_this_frame = True
    kids = ['ashwin', 'aparna','ankit']
    
    
    process_this_frame = True
    #count = 0
    url = "http://172.16.3.0:8080/shot.jpg"
    while True:
        '''img_resp = requests.get(url)
        img_arr = np.array(bytearray(img_resp.content), dtype=np.uint8)
        frame = cv2.imdecode(img_arr, -1)'''
        # Grab a single frame of video
        ret, frame = video_capture.read()
    
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    
        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]
    
        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
    
            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding,tolerance=0.5)
                name = "Unknown"
    
                # If a match was found in known_face_encodings, just use the first one.
                if True in matches:
                    first_match_index = matches.index(True)
                    name = known_face_names[first_match_index]
    
                face_names.append(name)
    
        process_this_frame = not process_this_frame
    
    
        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
    
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
    
            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)
            
     ################FACE_RECOG WORK#############################       
            print(name+ " : PRESENT")
            #students.add(name)
           
            #email_alert(name)
            
            if name in kids :
                print("yes")
                #email_alert('Present :' +str(name))
                #data_entry(name)
                
                main_using_csv.call(name,identity)
                kids.remove(name)
            else:
                print("this is pass")
                pass
          
        cv2.imshow('Video', frame)
        '''count = count+1
        if(count>1000):
            break'''
            
        if time.time()>start+period:
            break
        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
           
    print("Absent students")
    engine.say("Absent students are")
    '''print(kids)
    email_alert('Absent members :' +str(kids))'''
    for i in kids :
        email_alert(i,identity)
        print(i+" present")
        engine.say(i)
        engine.runAndWait()
       
    video_capture.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    main()