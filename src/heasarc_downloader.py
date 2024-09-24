import os
from multiprocessing import Pool
import argparse
import subprocess as subp
from tqdm import tqdm


def singular_download_process(sdp_args):
    """
    :param sdp_args: Tuple containing abs_path (output directory) and download_command.
    :return: None
    """

    abs_path, download_command = sdp_args
    try:
        proc = subp.Popen(download_command, cwd=abs_path, shell=True)
        proc.wait()  # Wait for the process to finish
        if proc.returncode != 0:
            print(f"Command failed with return code {proc.returncode}: {download_command}")
    except Exception as e:
        print(f"An error occurred while running command: {download_command}\nError: {str(e)}")


def heasarc_download_script_formatter(abs_path: str) -> []:
    """

    :param abs_path: Path of download script from HEASARC.
    :return: A list of strings with each string a download command.
    """

    commands = list()
    with open(abs_path, "r") as fp:
        for line in fp:
            if line and line[0] != "#" and line != '\n':
                commands.append(line.strip())

    return commands


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dsp', nargs=1, type=str, help='Download script path.')
    parser.add_argument('--outdir', nargs=1, type=str, help='Output files directory.')
    args = parser.parse_args()

    if args.dsp and args.outdir:
        script_path: str = args.dsp[0]
        out_path: str = args.outdir[0]
        iter_args = list()
        cmds = heasarc_download_script_formatter(script_path)

        for cmd in cmds:
            iter_args.append([out_path, cmd])

        with Pool(maxtasksperchild=1) as download_pool:
            download_pool.imap(singular_download_process, tqdm(iter_args), chunksize=os.cpu_count())
            download_pool.close()
            download_pool.join()
    else:
        parser.parse_args(['-h'])
