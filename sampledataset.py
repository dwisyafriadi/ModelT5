import random
import json
from datetime import datetime, timedelta

# Sample lists of random questions and answers
questions = [
    "What is the latest update on the project?",
    "How does the new feature improve user experience?",
    "What are the main benefits of the new system?",
    "How can we integrate the new API with our existing setup?",
    "What security measures have been implemented in the update?"
    "What are the key benefits of owning an NFT?",
    "How can NFTs be used in the gaming industry?",
    "What factors affect the value of an NFT?",
    "How do NFTs contribute to the digital art economy?",
    "What is the environmental impact of minting NFTs?",
    "What are the advantages of using a CEX over a DEX?",
    "How does a CEX ensure the security of user funds?",
    "What are the common fees associated with trading on a CEX?",
    "How do CEX platforms handle regulatory compliance?",
    "What features should users look for in a reliable CEX?",
    "What is the primary function of a DAO?",
    "How do members participate in decision-making within a DAO?",
    "What are the benefits of using a DAO for project governance?",
    "How is transparency maintained in a DAO?",
    "What are the challenges faced by DAOs in achieving consensus?"
]

answers = [
    "The latest update includes performance improvements and bug fixes.",
    "The new feature streamlines the workflow, making it easier for users to navigate.",
    "The main benefits include increased efficiency and scalability.",
    "The new API can be integrated by following the updated documentation.",
    "New encryption protocols have been added to enhance security.",
    "NFTs provide ownership of unique digital assets and the ability to trade them on various marketplaces.",
    "In gaming, NFTs can represent unique in-game items, characters, or virtual real estate that players can trade or sell.",
    "The value of an NFT is influenced by its rarity, the creator's reputation, and market demand.",
    "NFTs allow artists to tokenize their work, enabling direct sales to collectors without intermediaries.",
    "The environmental impact of NFTs depends on the blockchain they are minted on, with some being more energy-intensive than others.",
    "CEXs often provide higher liquidity, faster transaction speeds, and more user-friendly interfaces compared to DEXs.",
    "CEXs implement security measures such as multi-signature wallets, cold storage, and regular security audits.",
    "Common fees on a CEX include trading fees, withdrawal fees, and sometimes deposit fees.",
    "CEX platforms comply with regulations by implementing KYC (Know Your Customer) and AML (Anti-Money Laundering) procedures.",
    "Users should look for a CEX with strong security, transparent fees, a wide range of supported assets, and responsive customer support.",
    "A DAO is designed to manage and govern projects, organizations, or communities in a decentralized manner through smart contracts.",
    "Members participate in decision-making by voting on proposals using governance tokens specific to the DAO.",
    "DAOs provide decentralized governance, ensuring that decisions are made collectively by stakeholders rather than a central authority.",
    "Transparency in a DAO is maintained through on-chain voting and the public availability of all proposals and decisions.",
    "Challenges in achieving consensus include low voter turnout, the risk of governance attacks, and the difficulty of reaching agreements in large, diverse communities."
]

# Function to generate a random timestamp within the last year
def random_timestamp():
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    random_date = start_date + (end_date - start_date) * random.random()
    return random_date.strftime("%Y-%m-%d %H:%M:%S")

# Generate a list of dictionaries with random questions and answers
qa_list = []
for _ in range(2):  # Adjust the range for more entries
    qa_list.append({
        "content": f"Question: {random.choice(questions)} Answer: {random.choice(answers)}",
        "meta": {
            "time": random_timestamp()
        }
    })

qa_list

# Define the number of loops
looping = 1000000  # Example: generating 10 random QA pairs

# Generate a list of dictionaries with random questions and answers
qa_list = []
for _ in range(looping):
    qa_list.append({
        "content": f"Question: {random.choice(questions)} Answer: {random.choice(answers)}",
        "meta": {
            "time": random_timestamp()
        }
    })

# Save the output to a JSON file
output_file_path = 'dataset.json'
with open(output_file_path, 'w') as json_file:
    json.dump(qa_list, json_file, indent=4)
success_message = f"Successfully generated random dataset with a total of {looping} entries."
print(success_message)
