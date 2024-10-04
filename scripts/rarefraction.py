import os
import subprocess

def subsample_files(iterations=10, target_reads=200000000, output_folder="original_files_200M"):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # List of files to be subsampled
    files_to_sample = [
        "SRR2726671_1.fastq",
        "SRR2726671_2.fastq",
        "SRR2726672_1.fastq",
        "SRR2726672_2.fastq"
    ]

    for file in files_to_sample:
        for i in range(1, iterations + 1):
            output_file = os.path.join(output_folder, f"subsampled_{file.rsplit('.', 1)[0]}_{i}.fastq")
            cmd = f"seqtk sample -s{i} {file} {target_reads} > {output_file}"
            subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    subsample_files()

