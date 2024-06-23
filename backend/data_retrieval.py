import requests
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def fetch_latest_posts(site_url):
    response = requests.get(f"{site_url}/wp-json/wp/v2/posts")
    return response.json()

def generate_embeddings(text):
    return model.encode([text])

def update_vector_database(post_id, embeddings, index):
    post_id_array = np.array([post_id], dtype=np.int64)
    index.add_with_ids(embeddings, post_id_array)

def update_embeddings_on_new_post(site_url, index):
    posts = fetch_latest_posts(site_url)
    for post in posts:
        text = post['content']['rendered']
        embeddings = generate_embeddings(text)
        post_id = post['id']
        update_vector_database(post_id, embeddings, index)

if __name__ == "__main__":
    index = faiss.IndexFlatL2(384)  # Dimension should match your embedding size
    site_url = "https://wptavern.com"  # Example site
    update_embeddings_on_new_post(site_url, index)
