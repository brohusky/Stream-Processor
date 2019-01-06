# Stream-Processor

POC | a simple processor for video feed in order to detect face and create classifier to recognise the familiar faces and produce appearance stats

## Notebook

```
jupyter notebook --notebook-dir opencv-presentation
```

## Install

```
brew install pipenv opencv

pip install --upgrade autopep8 --isolated
pipenv install
```

## Run

```
pipenv --python 3.6
pipenv shell
ENV=${development|staging|pre-prod|production} python3 main.py
```
