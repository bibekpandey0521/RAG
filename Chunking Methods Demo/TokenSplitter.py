# Install required packages:
# pip install langchain
# pip install langchain-text-splitters
# pip install tiktoken

from langchain_text_splitters import (
    TokenTextSplitter
)

# input document
sample_text = """
# Introduction to Machine Learning
Machine Learning is a branch of Artificial Intelligence (AI) that enables computers
to learn from data and make predictions or decisions without being explicitly programmed.

## Types of Machine Learning:
## Supervised Learning
Supervised learning uses labeled datasets to train machine learning models.
Applications include email spam detection, house price prediction, and disease diagnosis.



## Unsupervised Learning:
Unsupervised learning works with unlabeled data to discover hidden patterns.
Applications include customer segmentation, anomaly detection, and market analysis.

## Reinforcement Learning:
Reinforcement learning enables an agent to learn through rewards and penalties.
Applications include robotics, self-driving cars, game playing, and autonomous systems.

## Applications of Machine Learning:
1. Healthcare: Disease prediction, medical image analysis, and drug discovery.
2. Finance: Fraud detection, credit scoring, and stock market prediction.
3. Education: Personalized learning and automated grading.
4. E-commerce: Product recommendations and customer behavior analysis.
5. Transportation: Traffic prediction and autonomous vehicles.
6. Agriculture: Crop monitoring, yield prediction, and plant disease detection.
7. Cybersecurity: Malware detection and suspicious activity identification.
Conclusion:
Machine Learning is transforming many industries by automating tasks,
improving decision-making, and discovering useful insights from large datasets.
"""
"""
Basic character text splitting
"""

print("\n3. Token  Text Splitter Example : Perfect for LLM token limit management")

splitter = TokenTextSplitter(
    chunk_size=100,
    chunk_overlap=20
)

chunks = splitter.split_text(sample_text)

for i , chunk in enumerate(chunks,1):
    print(f"\n Chunk {i}:")
    print(chunk)
    print("-" * 50)

