FROM python:3.11.0

COPY . /test-project
WORKDIR test-project

# env setup
RUN pip install pipenv
RUN pipenv install

# install google chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list'
RUN apt-get -y update
RUN apt-get install -y google-chrome-stable
#CMD ["pipenv", "run", "nose2", "ui_tests.tests.login_test"]
CMD ["pipenv", "run", "behave", "-f", "allure_behave.formatter:AllureFormatter", "-o", "result-folder-docker"]
