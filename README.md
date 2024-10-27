This project consists of 4 Python files and 3 folders (images, models, data_sets).
The Python files are as follows:
1. img_clf_builder.py: This python code is used to build and train the AI modules that will have the capacity to classify images
   into to categories as desired. We used it to build modules that can classify if the image has fire or not, and if it has guns or not.
2. img_clf_tester: This python code is used to test existing models. After running the code you need to input an image path for the module to classify, and the result will be printed.
3. send_warning.py: This python code is used to sent an email to a specific email address. The email is a warning that consists of the state the module found and a photo.
4. main_project.py: Is the main code where everything is tied together. You use the file by inputing the images paths, which are usually located in the "images" folder
   then the existing modules will check the images, and if they show any type of danger the modules can detect, it will send a warning using the send_warning.py code.

The other two folders:
  1. models: contains the saved trained modules.
  2. data_sets: contains the data sets of images that were used to build and train the modules.

You do not need to run any file other than the main_project.py because the modules and test images already exist.
You may need to set a sender and receiver emails in the send_warning.py file.
For the password of the sender, you have to use the apppassword feature of the senders google account. For information on using it, 
watch only the first section of this video: https://www.youtube.com/watch?v=g_j6ILT-X0k

This is just a quick documentation of the project written by Salem.                                                                                                     27th Oct, 2024
