import glob, os
file_count = 0
WorkingPath = os.path.dirname(os.path.abspath(__file__))
for file in glob.glob(os.path.join(WorkingPath, '*.py')):
    file_count += 1
print(file_count-1)