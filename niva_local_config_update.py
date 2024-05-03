#%%
import pathlib
import s3fs

from config import SETTINGS

# %%

client = s3fs.S3FileSystem(
    key=SETTINGS.MINIO_ACCESS_ID,
    secret=SETTINGS.MINIO_SECRET_KEY,
    endpoint_url="https://storage.seabee.sigma2.no",
    config_kwargs={
        "read_timeout": 300,
    },
)

# %%
base_path = pathlib.Path("E:/SEABEE_DATA")

# %%
for year in ["2022", "2023"]:
    for dir in (base_path / year).iterdir():
        print(dir.name)
        conf_path = f"niva-tidy/{year}/{dir.name}/config.seabee.yaml"
        if client.exists(conf_path):
            client.download(conf_path, dir / "config.seabee.yaml")
