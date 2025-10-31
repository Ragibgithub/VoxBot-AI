import os
import librosa
from sklearn import svm
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import numpy as np

# Function to extract features from audio files
def extract_features(audio_files):
    features = []
    for file in audio_files:
        y, sr = librosa.load(file, sr=None)
        mfccs = librosa.feature.mfcc(y=y, sr=sr)
        features.append(np.mean(mfccs, axis=1))
    return features

# Path to enrollment audio files - Replace this with the actual path
path_to_enrollment_audio_files = "D:/jarves_backend/features/recorded_audio.wav"

# Get list of audio files
audio_files = [os.path.join(path_to_enrollment_audio_files, f) for f in os.listdir(path_to_enrollment_audio_files) if f.endswith(".wav")]

# Extract features from audio files
X = extract_features(audio_files)

# Labels for training data (assuming each file belongs to the same speaker)
y = ['speaker'] * len(X)

# Train SVM model
clf = make_pipeline(StandardScaler(), svm.SVC(kernel='linear', probability=True))
clf.fit(X, y)

# Save the trained model
import joblib
joblib.dump(clf, 'svm_model.joblib')
