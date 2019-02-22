import os
import fnmatch
import shutil
from glob import glob

import model.kaiba.constants as KaibaConstants
from common.command import Command

__author__ = 'Qi.Chen@nyulangone.org'

class Kaiba(object):

    def __init__(self, input_path, prefix, output_path='./processed/kaiba', nii_only=True, keep_file=False):
        self.input_path = input_path
        self.output_path = output_path
        self.prefix = prefix
        self.nii_only = nii_only
        self.keep_file = keep_file

    def process(self, replace=True):
        file_lst = self.pre_process()

        for f_path in file_lst:

            f_name = os.path.basename(f_path)

            # process using bash
            Kaiba.process_bash(f_path)

            # extract all file using os.listdir
            output_lst = fnmatch.filter(os.listdir('.'), f_name.rstrip('.nii') + '*') + ['foo.csv']

            # generate output dictionary
            o_f_path = self.output_path +\
                       f_path[len(self.input_path):].rstrip(f_name) + '/' +\
                       f_name.rstrip('.nii') + '_kaiba'

            if not os.path.exists(o_f_path):
                os.makedirs(o_f_path)
            shutil.copy2(f_path, o_f_path)
            for output in output_lst:
                if replace:
                    shutil.move(output, '{}/{}'.format(o_f_path, output))
                else:
                    try:
                        shutil.move(output, o_f_path)
                    except:
                        print 'file {} already exist will not modify it'.format(output)
            print 'move files to' + o_f_path + '\n'

    @staticmethod
    def process_bash(input_nii, output_csv='foo', verbose=True):

        command = KaibaConstants.KAIBAOPERATION + input_nii
        if verbose:
            command += KaibaConstants.KAIBAVERBOSE
        command += KaibaConstants.KAIBAOUTPUTCSV + output_csv

        print '......kaiba command generated now processing {}.....'.format(input_nii)
        Command.command_excute(command)
        print '{} processed using kaibai'.format(input_nii)

    def pre_process(self):
        """
        generate a file list for processing
        :return: a list of file name with certain prefix
        """
        if self.nii_only:
            file_lst = [y for x in os.walk(self.input_path) for y in glob(os.path.join(x[0], self.prefix + '*.nii'))]
        else:
            # read all files if there is dicom transform to nii
            file_lst = [y for x in os.walk(self.input_path) for y in glob(os.path.join(x[0], self.prefix + '*'))]
            new_file_lst = []
            for i, file_path in enumerate(file_lst):
                if os.path.isfile(file_path) and file_path.endswith('.nii'):
                    output_name = file_path
                else:
                    output_name = file_path+ '/' + self.prefix+'_transformed.nii'
                    is_covert = Command.dicom2nii(file_path, output_name)
                    if not is_covert:
                        continue
                new_file_lst.append(output_name)
            file_lst = new_file_lst[:]
        return file_lst
