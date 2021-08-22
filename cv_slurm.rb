require_relative "slurm"

class CvSlurm < Slurm

    def sample
        6
    end

    def file_name
        'deep_nnEq_cv_hpc.py'
    end
end