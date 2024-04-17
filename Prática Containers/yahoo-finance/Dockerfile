# set base image (host OS)
FROM python:3.7

# set the working directory in the container
WORKDIR /code

# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip install -r requirements.txt

# copy the script to the working directory
COPY web_scrapping_yahoo_balance_sheet_server.py .

# command to run on container start
CMD [ "python", "./web_scrapping_yahoo_balance_sheet_server.py" ]
