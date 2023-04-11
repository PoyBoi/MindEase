import numpy as np
import pandas as pd
from transformers import pipeline, BlenderbotTokenizer, TFBlenderbotForConditionalGeneration, AutoModel
from wordcloud import WordCloud
from wordcloud import STOPWORDS
from matplotlib import pyplot as plt