import json
from datetime import datetime
import pandas as pd
from vector_store import VectorStore
from timescale_vector.client import uuid_from_time
import numpy as np 

# Initialize VectorStore
vec = VectorStore()

# vec.create_tables() 
# vec.drop_index()     
# vec.create_index()   #(DiskAnnIndex)

# Prepare data for insertion
def prepare_record(row):
    """Prepare a record for insertion into the vector store."""
    # content = row["summarizedText"]

    content = row["Content"]
    embedding = vec.get_embedding(content)
    
    # Ensure embedding is a numpy array (or a list of floats)
    embedding = np.array(embedding).tolist() 
    
    # Serialize metadata as JSON
    metadata = json.dumps({
        "created_at": datetime.now().isoformat(),
        "url":  row["url"],
    })
    
    return pd.Series(
        {
            "id": str(uuid_from_time(datetime.now())), 
            "metadata": metadata,  
            "contents": content,
            "embedding": embedding,  
        }
    )


path = "dataCollection/data/supportTickets/faq.csv"


df = pd.read_csv(path)
records_df = df.apply(prepare_record, axis=1)

print("Finished implementing embeddings ....")
vec.upsert(records_df) 
