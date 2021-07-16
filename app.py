from jina import Flow
from jina.types.document.generators import from_csv
from jinahub.indexers.simple import SimpleIndexer

with open("data/community_20.csv") as fp:
    docs = list(from_csv(fp, field_resolver={"title": "text"}))

flow = (
    Flow(port_expose=45678, protocol="http")
    .add(
        uses="jinahub+docker://TransformerTorchEncoder",
        name="encoder",
        override_with={
            "pretrained_model_or_path": "sentence-transformers/msmarco-distilbert-base-v3"
        },
    )
    .add(
        uses=SimpleIndexer,
        name="indexer",
        override_with={"index_file_name": "index.json", "dump_path": "workspace"},
    )
)
with flow:
    flow.post(on="/index", inputs=docs)
    flow.block()
