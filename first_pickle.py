import pickle

py_study_data = {}
fhand = open('study_data.pickle', 'wb')
pickle.dump(py_study_data, fhand)
fhand.close()

