
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



confFileName = 'model.config'
sdfFileName = 'model.sdf'

confFile = open(os.path.join(templateDir,confFileName),'r')
sdfFile = open(os.path.join(templateDir,sdfFileName),'r')


for i in range(1,numCopies+1):
	newModelName = modelName+'_'+str(i)
	newDir = os.path.join(copyDir,newModelName)
	os.makedirs(newDir)
	 
	newConfFile = open(os.path.join(newDir,confFileName),'w')
	for line in confFile:
		newConfFile.write(line.replace(templateVar,newModelName))
	newConfFile.close()
	confFile.seek(0,0)
	
	newSdfFile = open(os.path.join(newDir,sdfFileName),'w')
	for line in sdfFile:
		newSdfFile.write(line.replace(templateVar,newModelName))