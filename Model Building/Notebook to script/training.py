import os
import logging
from pathlib import Path
from dotenv import load_dotenv
from joblib import dump

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split,GridSearchCV,StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report,confusion_matrix


def train_model():
    try:
        print("placeholder")
        
    except Exception as e:
        pass
    
    
if __name__=="__main__":
    train_model()