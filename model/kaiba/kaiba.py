import os
import fnmatch
import shutil
from glob import glob
from common.command import Command

__author__ = 'Qi.Chen@nyulangone.org'

class Kaiba(object):

    def __init__(self, input_path, prefix, output_path='./processed'):
        self.input_path = input_path
        self.output_path = output_path
        self.prefix = prefix

    def process(self):
        file_lst = [y for x in os.walk(self.input_path)
                    for y in glob(os.path.join(x[0], self.prefix + '*.nii'))]

        for f_path in file_lst:

            f_name = os.path.basename(f_path)

            # process using bash
            Command.kaibai_processing(f_path)

            # extract all file using os.listdir
            output_lst = fnmatch.filter(os.listdir('.'), f_name.rstrip('.nii') + '*')

            # generate output dictionary
            o_f_path = self.output_path +\
                       f_path.lstrip(self.input_path).rstrip(f_name) + '/' +\
                       f_name.rstrip('.nii')

            if not os.path.exists(o_f_path):
                os.makedirs(o_f_path)

            # put all file into output folder and remove current
            for output in output_lst:
                shutil.move(output, o_f_path)
            print 'move files to' + o_f_path

