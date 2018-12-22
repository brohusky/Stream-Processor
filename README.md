# Stream-Processor
POC | a simple processor for video feed in order to detect face and create classifier to recognise the familiar faces and produce appearance stats


## Install
```
brew install pipenv opencv

pipenv install
```

## Run
```
pipenv shell
ENV=${development|staging|pre-prod|production} python3 main.py
```
