

<p align="center">
  <img height="100" src="https://github.com/qdrant/qdrant/raw/master/docs/logo.svg" alt="Qdrant">
</p>

<p align="center">
    <b>Python Client library for the <a href="https://github.com/qdrant/qdrant">Qdrant</a> vector search engine.</b>
</p>


<p align=center>
    <a href="https://qdrant.github.io/qdrant/redoc/index.html"><img src="https://img.shields.io/badge/Docs-OpenAPI%203.0-success" alt="OpenAPI Docs"></a>
    <a href="https://github.com/qdrant/qdrant_client/blob/master/LICENSE"><img src="https://img.shields.io/badge/License-Apache%202.0-success" alt="Apache 2.0 License"></a>
    <a href="https://qdrant.to/discord"><img src="https://img.shields.io/badge/Discord-Qdrant-5865F2.svg?logo=discord" alt="Discord"></a>
    <a href="https://qdrant.to/roadmap"><img src="https://img.shields.io/badge/Roadmap-2023-bc1439.svg" alt="Roadmap 2023"></a>
</p>

# Python Qdrant Client

Client library and SDK for the [Qdrant](https://github.com/qdrant/qdrant) vector search engine.

Library contains type definitions for all Qdrant API and allows to make both Sync and Async requests.

Client allows calls for all [Qdrant API methods](https://qdrant.github.io/qdrant/redoc/index.html) directly.
It also provides some additional helper methods for frequently required operations, e.g. initial collection uploading.

See [QuickStart](https://qdrant.tech/documentation/quick_start/#create-collection) for more details!

## Installation

```
pip install qdrant-client
```

## Features

- Type hints for all API methods
- Local mode - use same API without running server
- REST and gRPC support
- Minimal dependencies

## Local mode

<p align="center">
  <!--- https://github.com/qdrant/qdrant_client/raw/master -->
  <img height="180" src="docs/images/try-develop-deploy.png" alt="Qdrant">
</p>

Python client allows you to run same code in local mode without running Qdrant server.

Simply initialize client like this:

```python
from qdrant_client import QdrantClient

client = QdrantClient(":memory:")
# or
client = QdrantClient(path="path/to/db")  # Persists changes to disk
```

Local mode is useful for development, prototyping and testing.

- You can use it to run qdrant in your CI/CD pipeline
- Run it in Colab or Jupyter Notebook, no extra dependencies required
- When you need to scale, simply switch to server mode

### How it works?

We just implemented Qdrant API in pure python and extensively covered it with tests, to be sure it works exactly the same as server version.

## Examples

Instance a client
```python
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", port=6333)
# or
client = QdrantClient(url="http://localhost:6333")
```

Create a new collection
```python
from qdrant_client.models import Distance, VectorParams

client.recreate_collection(
    collection_name="my_collection",
    vectors_config=VectorParams(size=100, distance=Distance.COSINE),
)
```

Insert vectors into a collection

```python
import numpy as np
from qdrant_client.models import PointStruct

vectors = np.random.rand(100, 100)
client.upsert(
    collection_name="my_collection",
    points=[
        PointStruct(
            id=idx,
            vector=vector.tolist(),
            payload={"color": "red", "rand_number": idx % 10}
        )
        for idx, vector in enumerate(vectors)
    ]
)
```

Search for similar vectors

```python
query_vector = np.random.rand(100)
hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    limit=5  # Return 5 closest points
)
```

Search for similar vectors with filtering condition

```python
from qdrant_client.http.models import Filter, FieldCondition, Range

hits = client.search(
    collection_name="my_collection",
    query_vector=query_vector,
    query_filter=Filter(
        must=[  # These conditions are required for search results
            FieldCondition(
                key='rand_number',  # Condition based on values of `rand_number` field.
                range=Range(
                    gte=3  # Select only those results where `rand_number` >= 3
                )
            )
        ]
    ),
    limit=5  # Return 5 closest points
)
```

See more examples in our [Documentation](https://qdrant.tech/documentation/)!

### gRPC

To enable (typically, much faster) collection uploading with gRPC, use the following initialization:

```python
from qdrant_client import QdrantClient

client = QdrantClient(host="localhost", grpc_port=6334, prefer_grpc=True)
```


### Development

This project uses git hooks to run code formatters.

Install `pre-commit` with `pip3 install pre-commit` and set up hooks with `pre-commit install`.

> pre-commit requires python>=3.8
