from flask import Flask, request, render_template
import os
import base64

app = Flask(__name__)

# Define route to upload image
@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # Check if the post request has the file part
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            # Save the uploaded file to a folder
            filename = file.filename
            file.save(os.path.join(os.getcwd(), filename))
            # Read the uploaded image data
            with open(filename, 'rb') as f:
                image_data = f.read()
            # Convert the image data to base64 for rendering in the template
            encoded_image = base64.b64encode(image_data).decode('utf-8')
            # Render the template with the filename and image data        
            # Run the Python script on the uploaded image
            os.system('python process.py ' + filename)


            with open("process_output.jpg", 'rb') as f:
                image_data = f.read()
            # Convert the image data to base64 for rendering in the template
            encoded_image = base64.b64encode(image_data).decode('utf-8')

            return render_template('final.html', filename=filename, encoded_image=encoded_image)
    return render_template('final.html')

if __name__ == '__main__':
    app.run(debug=True)
