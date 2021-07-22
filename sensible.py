from jina import Flow
from jina.types.document.generators import from_csv

# Open our data CSV
with open("data/community_20.csv") as file:
    # Create a DocumentArray from the CSV, choosing "title" as the field to encode and index
    docs = list(from_csv(file, field_resolver={"title": "text"}))

# Create a Flow. This is a pipeline that takes a DocumentArray as input, processes it, and returns a different DocumentArray as output
flow = (
    Flow(port_expose=45678, protocol="http") # Set up REST gateway for searching
    .add(
        uses="jinahub+docker://TransformerTorchEncoder", # Add an encoder. This is the neural net that "understands" your data, downloaded from Jina Hub
        name="encoder",
    )
    .add(
        uses="jinahub+docker://SimpleIndexer", # Add an indexer. This creates a searchable index of the encodings and metadata
        name="indexer",
    )
)

# Start the Flow
with flow:
    flow.post(on="/index", inputs=docs) # Set the Flow to index
    flow.block() # Keep the Flow open, ready for user to search
