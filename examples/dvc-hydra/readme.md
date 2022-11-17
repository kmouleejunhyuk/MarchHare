usage of examples
# dataset is downloaded and sampled by stanfordcars. 
## Used 30 samples of image to prevent wrong usage.

Log git sha and exp name based on hydra callback & config
This is an example case.

- case 1: you did not commit your changes, and want to run exp(ex: for debug purpose)
    `>>> python train.py expname=dummmy1 log_git=disabled train.dry_run=1`
    ```
    # in outputs/dummmy1-yyyy-mm-dd-hh-MM-ss/train.log
    [2022-11-17 13:55:25,451][__main__][INFO] - git_sha: UNAVAILABLE
    [2022-11-17 13:55:25,451][__main__][INFO] - {'log_git': 'disabled', 'expname': 'dummmy1', 'git_sha': 'UNAVAILABLE', 'train': {'name': 'dummy1', 'text': 'hello. I am dummy 1', 'resize': 64, 'dry_run': 1}}
    ```

- case 2: you already committed your changes, and want to run exp(ex: for main experiment purpose)
    `python train.py expname=dummmy2 log_git=disabled train.dry_run=1`
  ```
  # in outputs/dummmy2-yyyy-mm-dd-hh-MM-ss/train.log
  - [2022-11-17 13:57:59,533][__main__][INFO] - git_sha: b16163b67c2d444f2b85bd30870d72c335c0eacf
  - [2022-11-17 13:57:59,533][__main__][INFO] - {'log_git': 'enabled', 'expname': 'dummmy1', 'git_sha': 'b16163b67c2d444f2b85bd30870d72c335c0eacf', 'train': {'name': 'dummy1', 'text': 'hello. I am dummy 1', 'resize': 64, 'dry_run': 1}}
  ```

- case of modify data and config
  ```
    dvc status
    dvc commit
    git commit -m 'something'
  ```
- further usage cases
  - if storage is S3, maybe it will be easier to share configs and dataset with others(out of cluster)
  - in case of 'cluster only' use, this case study will be closed