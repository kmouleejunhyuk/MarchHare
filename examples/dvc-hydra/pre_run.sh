cd ~/MarchHare/examples/dvc-hydra
unzip sample_dataset.zip
dvc init --subdir
dvc config core.autostage true
dvc add sample_dataset
unzip conf.zip
dvc add conf
