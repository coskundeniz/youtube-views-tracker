FROM python:3.9-alpine

# Set the working directory in the container to /src
WORKDIR /src

# Copy the project directory into /src
COPY . /src

# upgrade pip
RUN python -m pip install --no-cache-dir --upgrade pip

# install requirements
RUN python -m pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# Run the script when the container launches
ENTRYPOINT ["python", "yt_views_tracker.py"]
CMD ["--help"]
