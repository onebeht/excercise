# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Install any needed packages
RUN pip install --trusted-host pypi.python.org pyowm

# install my program
COPY getweather.py  .

# Run program when the container launches
CMD ["python", "getweather.py"]

