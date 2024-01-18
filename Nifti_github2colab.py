import pandas as pd
from pathlib import Path
import numpy as np
import nibabel as nib
from skimage import io

def OpenNiftiGitHubFile (PathAndFileName,UserName= "jricardoct15",GithubRepo="sep23_cds_int_medical_data"):
  ''' Open nifti files from git hub when executed from colab
  User - github user name
  PathAndFileName - includs path/filename.nii.gz
  GithubRepo - Github Repository
  '''
  url = f"https://github.com/{UserName}/{GithubRepo}/raw/main/{PathAndFileName}"
  wget --no-cache --backups=1 {url}

  data = nib.load(PathAndFileName).get_fdata()

  !rm {PathAndFileName}
  return data