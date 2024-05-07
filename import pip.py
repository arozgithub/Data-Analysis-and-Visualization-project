import pip
# run pip install -U nltk
pip.main(['install', '-U', 'nltk'])
# run nltk.download()
import nltk
nltk.download('all')
# “pip install beautifulsoup4”
pip.main(['install', '-U', 'beautifulsoup4'])

pip.main(['install', '-U', 'selenium'])