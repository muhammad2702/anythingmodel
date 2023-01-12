# In this file, we define download_model
# It runs during container build time to get model weights built into the container

from diffusers import DiffusionPipeline, EulerDiscreteScheduler
import torch

import os

def download_model():
    # do a dry run of loading the huggingface model, which will download weights at build time
    #Set auth token which is required to download stable diffusion model weights
    HF_AUTH_TOKEN = os.getenv("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")


    repo_id = "Linaqruf/anything-v3.0"

    scheduler = EulerDiscreteScheduler.from_pretrained(repo_id, subfolder="scheduler", prediction_type="v_prediction")

    model = DiffusionPipeline.from_pretrained(repo_id, 
        scheduler=scheduler,
        use_auth_token=HF_AUTH_TOKEN
    )



if __name__ == "__main__":
    download_model()
