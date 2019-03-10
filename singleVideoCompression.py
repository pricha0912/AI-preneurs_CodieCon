# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 09:22:38 2019

@author: Richa Patel
"""

import ffmpy
input_name = input("Enter name of input file: ")
crf = int(input("Enter constant rate factor between 18 and 24: "))
output_name = input("Enter output file name: ")
inp={input_name:None}
outp = {output_name:'-vcodec libx264 -crf %d'%crf}
ff=ffmpy.FFmpeg(inputs=inp,outputs=outp)
print(ff.cmd) # just to verify that it produces the correct ffmpeg command
ff.run()
print("done!")

