Sure! Here's a cheat sheet for serving static files and handling file uploads in Python using Flask and Apache Spark:

1. Import the necessary modules in your Flask application:

   ```python
   from flask import Flask, request, render_template
   from pyspark import SparkContext, SparkConf
   import os
   ```

2. Create a new Spark configuration and context:

   ```python
   conf = SparkConf().setAppName("MyApp")
   sc = SparkContext(conf=conf)
   ```

3. Create a new Flask application and set the `UPLOAD_FOLDER` and `STATIC_FOLDER`:

   ```python
   app = Flask(__name__)
   app.config['UPLOAD_FOLDER'] = '/path/to/uploads'
   app.config['STATIC_FOLDER'] = '/path/to/static/files'
   ```

4. Define a route for serving static files:

   ```python
   @app.route('/static/<path:path>')
   def serve_static(path):
       return send_from_directory(app.config['STATIC_FOLDER'], path)
   ```

5. Define a route for handling file uploads:

   ```python
   @app.route('/upload', methods=['POST'])
   def handle_upload():
       file = request.files['file']
       if file:
           filename = secure_filename(file.filename)
           file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
           return 'File uploaded successfully!'
       else:
           return 'No file specified.'
   ```

   Note: Don't forget to import the `secure_filename` function from `werkzeug.utils` and 
      add it to the import statement at the beginning of your file.

6. Run the Flask application:

   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

   Note: If you're running your Flask application on a cluster, 
      you'll need to use a different method for starting the application, such as `spark-submit`.

That's it! With this setup, 
you should be able to serve static files and handle file uploads in your Flask application using Apache Spark.
