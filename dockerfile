# FROM --platform=linux/amd64 python:3.10-buster

# RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
# RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

# RUN apt-get -y update
# RUN apt-get install -y google-chrome-stable
# RUN apt-get install -y xvfb
# RUN apt update
# RUN apt install python3-distutils -y

# RUN useradd -m chrome && \
#     mkdir -p /home/chrome/.config/google-chrome && \
#     chown -R chrome:chrome /home/chrome/

# USER chrome
# WORKDIR /home/chrome/

# ENV DISPLAY=:99

# COPY . .

# RUN pip install -r requirements.txt

# EXPOSE 7777

# CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]

FROM --platform=linux/amd64 python:3.10-buster

# Add Google Chrome repo and install dependencies
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - && \
    sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'

RUN apt-get -y update && \
    apt-get install -y google-chrome-stable xvfb python3-distutils redis-server && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Create a non-root user and set permissions
RUN useradd -m chrome && \
    mkdir -p /home/chrome/.config/google-chrome && \
    chown -R chrome:chrome /home/chrome/

USER chrome
WORKDIR /home/chrome/

# Set environment variables
ENV DISPLAY=:99

# Copy application files
COPY . .

# Install Python dependencies
RUN pip install -r requirements.txt

# Expose application port
EXPOSE 7777

# Start Redis server in the background & Run FastAPI
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7777"]