import json
import os 
from dotenv import load_dotenv

from dkg import DKG
from dkg.providers import BlockchainProvider, NodeHTTPProvider

load_dotenv()

API_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3MDQ5NzI5NjQsImV4cCI6MTcyMDc1MTc2NCwianRpIjoiNTYyYzVjYzUtZjIxMC00ZTFlLWI0MDYtNzc0NDA5NzhmNWY0In0.xo1Z81-mGsDBQBGADftNXrjCYk6GUxjwQinE3Bdv1IA"
ENVIRONMENT = "devnet"
OT_NODE_ENDPOINT = "https://v6-pegasus-node-19.origin-trail.network:8900"
PRIVATE_KEY = os.getenv("PRIVATE_KEY")

node_provider = NodeHTTPProvider(
    endpoint_uri=OT_NODE_ENDPOINT,
    auth_token=API_TOKEN
)

blockchain_provider = BlockchainProvider(
    ENVIRONMENT,
    blockchain_id="gnosis:10200",
    private_key=PRIVATE_KEY
)

dkg = DKG(node_provider, blockchain_provider)

# Read knowledge assets
with open("./knowledge-assets/tool.json", "r") as file:
    tool_asset = json.load(file)

with open("./knowledge-assets/market.json", "r") as file:
    market_asset = json.load(file)

with open("./knowledge-assets/prediction.json", "r") as file:
    prediction_asset = json.load(file)

public_assertion_id = dkg.assertion.get_public_assertion_id(content)
print("Public Assertion ID", public_assertion_id)

public_assertion_size = dkg.assertion.get_size(content)
print("Public Assertion Size", public_assertion_size)

bid_suggestion = dkg.network.get_bid_suggestion(
    public_assertion_id,
    public_assertion_size,
    2,
)
print("Bid Suggestion: ", bid_suggestion)

current_allowance = dkg.asset.get_current_allowance()
print("Current Allowance: ", current_allowance)

allowance_increase = dkg.asset.increase_allowance(bid_suggestion)
print("Increased Allowance: ", allowance_increase)

print("Creating asset...")
create_asset_result = dkg.asset.create(content, 2)

print(create_asset_result)



