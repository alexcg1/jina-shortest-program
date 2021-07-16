from jina import Flow
from jina.types.document.generators import from_csv
from jinahub.indexers.simple import SimpleIndexer

flow = (
    Flow(port_expose=45678, protocol="http")
    .add(uses="jinahub+docker://TransformerTorchEncoder", pretrained_model_or_path="sentence-transformers/msmarco-distilbert-base-v3")
    .add(
        uses=SimpleIndexer,
        dump_path="workspace",
        override_with={"index_file_name": "index.json"},
    )
)
with flow:
    flow.post(on="/index", inputs=from_csv("data/input.csv"))
    flow.block()
