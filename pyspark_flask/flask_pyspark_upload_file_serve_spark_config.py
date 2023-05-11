Sure, here's an example of a Flask application that is configured to use Apache Spark and 
where you can specify the Spark settings script:

1. Create a new Flask application:

   ```python
   from flask import Flask, request, send_from_directory
   from pyspark import SparkContext, SparkConf
   import os
   
   app = Flask(__name__)
   app.config['UPLOAD_FOLDER'] = '/path/to/uploads'
   app.config['STATIC_FOLDER'] = '/path/to/static/files'
   ```

2. Specify the location of the Spark settings script as an environment variable:

   ```python
   import os
   os.environ['SPARK_SETTINGS'] = '/path/to/spark-settings.py'
   ```

3. Load the Spark settings from the specified script:

   ```python
   if 'SPARK_SETTINGS' in os.environ:
       exec(open(os.environ['SPARK_SETTINGS']).read())
   else:
       conf = SparkConf().setAppName("MyApp")
       sc = SparkContext(conf=conf)
   ```

   This code checks if the `SPARK_SETTINGS` environment variable is set and 
   if so, loads the settings from the specified script using the `exec()` function. 
   If the variable is not set, it creates a default Spark configuration with the `SparkConf()` function and 
   creates a Spark context with the default configuration.

4. Define routes for serving static files and handling file uploads, as described in the previous examples.

5. Run the Flask application:

   ```python
   if __name__ == '__main__':
       app.run(debug=True)
   ```

   Note that in this example, the `spark-settings.py` script should contain the Spark configuration settings, 
   as described in the previous examples.

With this setup, you can specify the location of the Spark settings script as 
an environment variable when starting the Flask application, and 
the application will use the specified settings to configure Apache Spark.
