# import os

# PATH = "C:/dev/DSA/Dsa"
# files = 0
# lineofcode = 0
# dirs = set()

# for dirpath, _, filenames in os.walk(PATH):
#     # Track every directory visited
#     dirs.add(dirpath)
    
#     for file in filenames:
#         if file.endswith('.py'):
#             files += 1
#             file_path = os.path.join(dirpath, file)
            
#             # Read file and count non-blank, non-comment lines
#             with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
#                 lineofcode += sum(1 for line in f if line.strip() and not line.strip().startswith('#'))

# print(f"Total Python files: {files}")
# print(f"Total lines of code (excluding comments/blanks): {lineofcode}")
# print(f"Total folders: {len(dirs)}")

import os

PATH = "C:/dev/DSA/Dsa"
files = 0
lineofcode = 0
dirs = set()

for dirpath, dirnames, filenames in os.walk(PATH):
    # Ignore hidden, cache, and virtual environment folders
    dirnames[:] = [d for d in dirnames if not d.startswith('.') and d != '__pycache__' and d != 'venv']
    
    dirs.add(dirpath)
    for file in filenames:
        if file.endswith('.py'):
            files += 1
            file_path = os.path.join(dirpath, file)
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                lineofcode += sum(1 for line in f if line.strip() and not line.strip().startswith('#'))

print(f"Total Python files: {files}")
print(f"Total lines of code (excluding comments/blanks): {lineofcode}")
print(f"Total folders: {len(dirs)}")
