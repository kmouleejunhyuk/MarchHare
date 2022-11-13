import hydra
from omegaconf import DictConfig, OmegaConf
import logging


log = logging.getLogger(__name__)


@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg: DictConfig) -> None:
    """dummy application for dvc_hydra demo

    Args:
        cfg (DictConfig): hydra configuration
    """

    if cfg.train.dry_run:
      log.info(cfg)
    else:
        log.info('fool!!!!')


if __name__ == "__main__":
    my_app()
