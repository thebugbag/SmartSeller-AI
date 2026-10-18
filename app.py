import requests

print("Welcome to SmartSeller AI!")

product = input("Enter your product name: ")
price = input("Enter your product price in Rs.: ")
feature = input("Enter your product's special feature: ")

prompt = f"""
Write a short, attractive product description for an online shop.

Product: {product}
Price: Rs. {price}
Special feature: {feature}

Rules:
- Write 3 to 4 sentences.
- Mention the product name and exact price.
- Highlight the special feature.
- Use friendly, persuasive language.
- Use ONLY the product details provided above. Never invent materials, packaging, certifications, quality claims, or other features. If a detail is not provided, do not mention it.
- Return only the description.
"""

print("\nGenerating your AI description...")

try:
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:0.5b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()
    description = response.json()["response"]

    print("\n--- YOUR AI PRODUCT DESCRIPTION ---")
    print(description)
    print(f"\nPrice: Rs. {price}")

except requests.exceptions.RequestException:
    print("Could not connect to Ollama. Make sure Ollama is running.")