import json
import os
from dotenv import load_dotenv

from dkg import DKG
from dkg.providers import BlockchainProvider, NodeHTTPProvider

load_dotenv()

API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDQ5NzI5NjQsImV4cCI6MTcyMDc1MTc2NCwianRpIjoiNTYyYzVjYzUtZjIxMC00ZTFlLWI0MDYtNzc0NDA5NzhmNWY0In0.xo1Z81-mGsDBQBGADftNXrjCYk6GUxjwQinE3Bdv1IA"
ENVIRONMENT = "testnet"
OT_NODE_ENDPOINT = "https://v6-pegasus-node-19.origin-trail.network:8900"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

node_provider = NodeHTTPProvider(endpoint_uri=OT_NODE_ENDPOINT, auth_token=API_TOKEN)

blockchain_provider = BlockchainProvider(
    ENVIRONMENT, blockchain_id="gnosis:10200", private_key=PRIVATE_KEY
)

dkg = DKG(node_provider, blockchain_provider)

print("Node Info: ", dkg.node.info)

content = {
    "@context": "https://schema.org",
    "@id": "0x0094fa304017d5c2b355790e2976f769ea600492",
    "title": "Will the Hisense U8K be considered a top-tier screen for well-lit rooms by 22 August 2023?",
    "@type": "Market",
    "Prediction": {
        "@type": "Prediction",
        "@id": "46575543203365495795461826533331162746381515212880293824967167776593568770457",
        "result": "Yes",
        "tool": {
            "@type": "Tool",
            "name": "prediction-online",
        },
    },
}

create_asset_result = dkg.asset.create(
    {
        "public": content,
    },
    epochs_number=2,
)

print(create_asset_result)
