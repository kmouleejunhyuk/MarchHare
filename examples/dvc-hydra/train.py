import hydra
from omegaconf import DictConfig, OmegaConf

@hydra.main(version_base=None, config_path="conf", config_name="config")
def my_app(cfg : DictConfig) -> None:
  """dummy application for dvc_hydra demo

  Args:
      cfg (DictConfig): hydra configuration
  """
  if cfg.dry_run:
    print(OmegaConf.to_yaml(cfg))
  else:
    print('fool!!!!')
    

if __name__ == "__main__":
    my_app()
