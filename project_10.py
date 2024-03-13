import cv2

image_path = "C:/Users/aka-pc/Downloads/hp.jpg"
image = cv2.imread(image_path) # Load the image

# Check if the image is loaded successfully
if image is None:
    print("Error: Could not load the image.")
else:
    # Load the pre-trained Haarcascades face detector
    # This line creates a cascade classifier object for detecting faces using a pre-trained Haar cascade classifier. The path to the Haar cascade file for face detection is provided.
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')  #classifier object

    # Convert to grayscale for face detection - simplify processing and reduce computational complexity.
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray_image, scaleFactor=1.3, minNeighbors=5) # returns a list of rectangles representing the detected faces.  #a larger value of scaleFactor speeds up the process but may miss smaller faces # each potential face rectangle should have at least 5 neighboring rectangles to be considered a valid face.

    if len(faces) > 0:
        print("Human face detected!")
    else:
        print("No human face detected.")

    # green rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 5)
    # Resize the image for better visibility

    resized_image = cv2.resize(image, (600, 700))
    # Display the original image with faces highlighted
    cv2.imshow('Detected Faces', resized_image)
    cv2.waitKey(0)  # program will wait indefinitely until a key is pressed
    cv2.destroyAllWindows() # release all resources
