# hydra_git_callback.py
import logging
from typing import Any
from git.repo import Repo # installed with `pip install gitpython`
from hydra.experimental.callback import Callback
from omegaconf import DictConfig

log = logging.getLogger(__name__)

def get_git_sha(repo: Repo) -> str:
    """return current git hash string

    Args:
        repo (git.Repo): git Repo object

    Returns:
        sha (str): git hash string
    """
    sha = repo.head.object.hexsha
    return sha

def check_git_sanity(repo: Repo) -> None:
    """assert if git has uncommited changes

    Args:
        repo (git.Repo): git Repo object
    """
    if 'clean' not in repo.git.status():
        log.error(
            "for experiment hash logging, please commit your changes"
        )
        log.error(
            "exiting experiment"
        )
        exit(0)

class MyCallback(Callback):
    """callback for logging git hash

    Args:
        Callback (_type_): hydra callback object
    """
    def on_run_start(self, config: DictConfig, **kwargs: Any) -> None:
        """if config.log_git is True, else log None
            - checks sanity
            - logs git commit hash to hydra log

        Args:
            config (DictConfig): hydra config object
        """
        if config.log_git=='enabled':
            repo = Repo(search_parent_directories=True)
            check_git_sanity(repo)
            log.warning(f"Git sha: {get_git_sha(repo)}")
        else:
            log.warning(f"Git sha: {'UNAVAILABLE'}")

    def on_multirun_start(self, config: DictConfig, **kwargs: Any) -> None:
        """if config.git_logging.log is True, else log None
            - checks sanity
            - logs git commit hash to hydra log

        Args:
            config (DictConfig): hydra config object
        """
        if config.log_git=='enabled':
            repo = Repo(search_parent_directories=True)
            check_git_sanity(repo)
            log.warning(f"Git sha: {get_git_sha(repo)}")
        else:
            log.warning(f"Git sha: {'UNAVAILABLE'}")