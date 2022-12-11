
#!/usr/bin/env python3

# Psudo code
# 
# open files to copy
# Make new directory
# make new files with replaces strings
# add model to world file

import os
import errno
import sys
import fileinput
import shutil

numCopies = 3

templateDir = '/home/matt/Workspace/GazeboDev/quad_model_dev/modelDev/quad_2292_template'
copyDir = '/home/matt/Workspace/GazeboDev/quad_model_dev/Gen_Models'
#newpath = r'C:\Program Files\arbitrary' 
templateVar = '{$modelName}'
modelName = 'quad_2292' # append _1 to each model

runName = 'test1'
worldFile = '/home/matt/Workspace/GazeboDev/quad_model_dev/modelDev/quad_2292_template.world'
