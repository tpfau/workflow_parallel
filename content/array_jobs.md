# Using a slurm array job

Slurm array jobs are jobs, that are run multiple times, with the same settings.
a slurm batch script with an array job looks something like:

```slurm
#!/bin/bash
#SBATCH --job-name=my_array_job
#SBATCH --array=2-100:2
#SBATCH --output=output_%A_%a.txt
#SBATCH --error=error_%A_%a.txt

# Your job commands go here
# You can use the environment variable SLURM_ARRAY_TASK_ID to get the current task ID

# Example command: replace with your actual command
your_command --parameter $SLURM_ARRAY_TASK_ID
```

where `--array=2-100:2` creates 50 jobs numbered from 2 to 100 with a step size of 2
(the step size defaults to 1 if omitted). `%A` and `%a` in output and error indicate
the jobID and arrayID of the job respectively. The only difference in these jobs is the
environment variable `SLURM_ARRAY_TASK_ID` which is set to the array id of the job
and can be used to select what to calculate in this job.
