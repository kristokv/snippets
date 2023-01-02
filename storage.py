#%%
from minio import Minio
from config import SETTINGS

# %%
BUCKET_NAME = "seabirds"
BUCKET_PREFIX = "2022/Bergen_Fles"
# %%
# access key and id can be created on minio.seabee.sigma2.no
# and added to the `.env` file
sigma2_client = Minio(
    "storage.seabee.sigma2.no",
    access_key=SETTINGS.ACCESS_ID,
    secret_key=SETTINGS.SECRET_KEY,
)
#%%
# List all objects in seabirds bucket under `2022/Bergen_Fles` path
[
    o.object_name
    for o in sigma2_client.list_objects(
        BUCKET_NAME, prefix=BUCKET_PREFIX, recursive=True
    )
]
# %%
