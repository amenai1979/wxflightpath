import os
import sys
current_path=os.getcwd()
parent_path = os.path.abspath(os.path.join(current_path, os.pardir))
sys.path.append(parent_path)
