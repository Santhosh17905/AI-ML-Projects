import numpy as np
import struct

with open(
    "dataset/emnist-balanced-train-labels-idx1-ubyte",
    "rb"
) as f:

    magic, size = struct.unpack(">II", f.read(8))

    labels = np.frombuffer(
        f.read(),
        dtype=np.uint8
    )

print("Classes:", np.unique(labels))
print("Total Classes:", len(np.unique(labels)))