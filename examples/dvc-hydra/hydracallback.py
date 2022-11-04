# hydra_git_callback.py
import logging
from typing import Any
import git  # installed with `pip install gitpython`
from hydra.experimental.callback import Callback
from omegaconf import DictConfig

log = logging.getLogger(__name__)

def get_git_sha():
    repo = git.Repo(search_parent_directories=True)
    sha = repo.head.object.hexsha
    return sha

class MyCallback(Callback):
    def on_run_start(self, config: DictConfig, **kwargs: Any) -> None:
        sha = get_git_sha()
        log.info(f"Git sha: {sha}")

    def on_multirun_start(self, config: DictConfig, **kwargs: Any) -> None:
        sha = get_git_sha()
        log.info(f"Git sha: {sha}")