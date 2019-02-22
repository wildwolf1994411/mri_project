import subprocess
import shlex
import dicom2nifti
import os

__author__='Qi.Chen@nyulangone.org'

class Command(object):

    @staticmethod
    def command_excute(command):
        subprocess.call(shlex.split(command), stdout=subprocess.PIPE)

    @staticmethod
    def convert_dicom2nii(dicom_dic, output_file, reorient_nifti=True):
        if not Command.is_dicom_dic(dicom_dic):
            return False
        dicom2nifti.dicom_series_to_nifti(dicom_dic, output_file, reorient_nifti=reorient_nifti)
        return True

    @staticmethod
    def is_dicom_dic(dicom_dic):
        # check one kinds of dicom need update
        return all(i.endswith('.IMA') for i in os.listdir(dicom_dic))
