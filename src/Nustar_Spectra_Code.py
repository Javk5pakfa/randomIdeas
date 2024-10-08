import pandas as pd
import os
from glob import glob
import sys
import numpy as np

main_dir = "/home/zxh496/Documents/randomIdeas/data/obs_in_progress/"
os.chdir(main_dir)
all_directories = glob("*")  # making "all directories" a list of folder names/directories

# 1. read names of the sources and  their ra and de (from the table) load the table then read it 
df = pd.read_csv('/home/zxh496/Documents/randomIdeas/data/sources.csv')  # opens table with the names
src_name = np.array(df['name'])  # now df is a table with many columns and each column has a name
ra = np.array(df['ra'])  # naming the columns and gives you the entire column
dec = np.array(df['dec'])  # naming the columns and gives you the entire column
nustar_obs = np.array(df['obs_id'])  # naming the columns and gives you the entire column

# Loop on the entire list of directories so we can get all the files we need from each directory
print('\we are entering into the for loop')
for i in range(len(src_name)):
    list_obs = nustar_obs[i].strip('[]').split(', ')
    ra_src = ra[i]
    dec_src = dec[i]

    print('src_name', src_name[i])

    for j in range(len(list_obs)):
        print('list_obs', list_obs[j])
        try:
            os.chdir(main_dir + list_obs[j] + "/event_cl")  # go inside nustar observation directories
            img_files = glob("*cl.evt")  # read the name of the evt file from which we need to extract the spectra
            for img_file in img_files:
                print('img_file', img_file)
                src_name[i] = src_name[i].replace(" ", "_")
                # cmd1='nupipeline indir=/home/apeca/NuSTAR_data/60901015002/ steminputs=nu60901015002 outdir=./out > nupipeline_log.txt'
                print(list_obs[j], src_name[i])

                print(os.system('pwd'))
                # cmd1 = 'nupipeline indir=' + main_dir + list_obs[j] + ' steminputs=nu' + str(
                #     list_obs[j]) + ' outdir=' + main_dir + list_obs[j] + '/out clobber=yes chatter=5 cleanup=yes'
                cmd2 = 'nuproducts srcregionfile=' + main_dir + 'src_region_files/' + src_name[
                    i] + '_src.reg bkgregionfile=' + main_dir + 'bkg_region_files/' + list_obs[
                           j] + '_bkg.reg indir=' + main_dir + list_obs[j] + '/out outdir=' + main_dir + list_obs[j] + '/products instrument=FPMA steminputs=nu' + list_obs[
                           j] + ' bkgextract=yes lcfile=NONE bkglcfile=NONE cleanup=yes clobber=yes chatter=5'
                # cmd3 = 'nuproducts srcregionfile=' + main_dir + 'src_region_files/' + src_name[
                #     i] + '_src.reg bkgregionfile=' + main_dir + 'bkg_region_files/' + list_obs[
                #            j] + '_bkg.reg indir=' + main_dir + list_obs[j] + '/out outdir=' + main_dir + list_obs[j] + '/products instrument=FPMB steminputs=nu' + list_obs[
                #            j] + ' bkgextract=yes lcfile=NONE bkglcfile=NONE cleanup=yes clobber=yes chatter=5'

                # print('\ncmd1', cmd1)
                # os.system(cmd1)
                print('\ncmd2', cmd2)
                os.system(cmd2)
                # print('\ncmd3', cmd3)
                # os.system(cmd3)

                sys.exit()
        except Exception as e:
            with open(os.devnull, "w") as f:
                print("Skipping {} because of {}...".format(j, e), file=f)
