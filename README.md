Emitec Embossing Machine Automation System


    1. Objective :
       The objective of this project is to detect the presence of the pipes placed in the tray and find their center coordinates to pass them to the robot for picking. (Pick and Place System)
	We have two camera stations. Station-1 is for finding center coordinates and Station-2 is for checking the part 	orientation. 
	

    2. Dependencies : 
        ◦ opencv-python      --- 
        ◦ numpy		  ---
        ◦ scipy		  ---
        ◦ Tensorrt		  ---
        ◦ Pycuda		  ---
        ◦ logging		  ---



    3. Steps to Run:
        ◦ Run main_with_plc.py script.
        ◦ Adjust the camera settings and Exposure Settings if required from main_with_plc.py.


    4. Working :
        ◦ Image frame is captured from the camera after receiving PLC trigger and the distortion correction is applied on it.
        ◦ Undistorted frame is then pre-processed (converted to grayscale and resized for consistent processing.)
        ◦ Pre-processed image is then used to run inference.
        ◦ We have used Attention-Unet segmentation model for detecting the pipes(circles) in the images. It gives us output in the form of binary mask.
        ◦ The inference output mask is then passed for further post-processing steps.
          
        ◦ Post Processing Steps: 
            ▪   separate_circles() function:
            ▪ Uses distance transformation and watershed segmentation to separate overlapping circles.
            ▪  find_circle() function:
            ▪ Finds contours in the binary mask.
            ▪ Filters contours based on circularity (> 0.80) to detect circles.
            ▪ Returns the list of coordinates of circles. 
              
            ▪ sort() function:
            ▪ Sorts circles by their X and Y coordinates.
            ▪ Groups circles into lines for structured detection.
            ▪ pick_circle_pairs() function:
            ▪ Calculates distances between all detected circles.
            ▪ Pairs circles within a specified distance range.
            ▪ Modify min_dist and max_dist to change the pairing distance range.
            ▪ pick_seq() function:
            ▪ Assigns sequence numbers to the detected circles.
            ▪ Converts pixel coordinates to real-world measurements.
STATION -2

      The code is structured into three main parts:
            1. black_main_plc.py: The main script that orchestrates the camera input, model inference, and interaction with the PLC.
            2. line_func.py: A function that processes a category mask obtained from segmentation model, counts blue (part) and green (black line) pixels, and updates a dictionary (ok_dict) to validate specific regions.
            3. black_inference.py: Processes each frame, performs inference using TensorRT, and outputs segmentation masks of each captured frame.
 
      Table of Contents
            • Overview
            • Dependencies
            • File Structure
            • Functionality
                ◦ Main Script (black_main_plc.py)
                ◦ Check for Black line (line_func.py)
              
     1. Overview
        This system processes image masks that contain blue (part) and green (black line) regions (segmented by a Multiclass Attention-Unet model), analyzes the presence of these regions, and validates specific conditions to update the status of the left and right parts of the image. It interacts with a PLC (Programmable Logic Controller) to send and receive status information, while performing the following tasks:
            • Capturing images using the camera.
            • Running inference using a trained model.
            • Analyzing the regions based on blue and green pixels.
            • Logging relevant information and errors.
            • Updating PLC with results.
        The system operates continuously and responds to PLC signals, ensuring real-time interaction with the machine.


      2. Dependencies
        Before running the code, ensure that you have the following dependencies installed:
            • numpy: For numerical operations and array manipulation.
            • opencv-python: For image processing and camera interaction.
            • TensorRT: For running the model efficiently on the GPU.
            • PyCUDA: For handling GPU memory management and streaming operations.
            • logging: For logging important events and errors.
            • time: For managing time-related tasks.
            • datetime: For timestamping logs.
            • plc: For PLC integration (custom library, assumed to be provided in your setup).


      3. File Structure
        The repository consists of the following main components:
            1. black_main_plc.py: This script coordinates the camera, PLC, and image processing tasks. It captures images, performs inference, and sends/receives signals from the PLC.
            2. line_func.py: This script contains the function analyze_blue_and_green that processes a category mask, counts blue and green pixels, and validates the regions based on the count.
            3. black_inference.py: Processes each frame, performs inference using TensorRT, and outputs segmentation masks of each captured frame.


      4. Functionality

        Main Script (black_main_plc.py)
        The main script (black_main_plc.py) is the entry point for the system. It performs the following operations:
            1. Camera Setup: Initializes the camera, grabs images, and performs model inference.
            2. PLC Interaction: Reads and writes to the PLC to control and monitor the process.
            3. Model Inference: Loads a pre-trained model and processes the captured frame.
            4. Result Saving: Saves overlayed images to disk and updates the PLC with results.

        Region Analysis (line_func.py)
        The analyze_blue_and_green function is responsible for processing a category mask (2D NumPy array) and updating the status of the left and right regions based on blue and green pixel counts.
        Key steps in analyze_blue_and_green:
            1. Region Definition: Defines the region of interest (ROI) based on predefined coordinates.
            2. Blue Pixel Count: Counts the number of blue pixels (1 in the mask) in both left and right regions.
            3. Green Line Validation: Checks if a valid green line (2 in the mask) is present in the regions by counting green pixels.
            4. Validation and Updates: Updates the ok_dict based on the presence of blue and green pixels in the regions.
        If both the left and right parts are valid, it marks both regions as valid in the ok_dict. If only one part is valid, and if neither is valid, it returns the dictionary with both regions marked invalid.

      



