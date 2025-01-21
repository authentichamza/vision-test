import argparse
import time
import base64
import os
from openai import OpenAI
from PIL import Image
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_image_with_vision(image_path, prompt, model="gpt-4o", detail="low"):
    """Analyze an image using OpenAI's Vision API and time the request"""
   

    start_time = time.time()
    if not image_path.startswith("http"):
        with open(image_path, "rb") as image_file:
            base64_image = base64.b64encode(image_file.read()).decode('utf-8')
        image_url = f"data:image/png;base64,{base64_image}"
    else:
        image_url = image_path

    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url,
                            "detail": detail,
                        }
                    },
                ],
            }
        ],
    )
    
    processing_time = time.time() - start_time
    return response.choices[0].message.content, processing_time

def main():
    parser = argparse.ArgumentParser(description="Image Analysis with OpenAI Vision")
    parser.add_argument("--detail", required=False, help="Quality of Image Analysis (default: low)")
    parser.add_argument("--prompt", required=True, help="Analysis prompt for the image")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model to use (default: gpt-4o)")
    parser.add_argument("--image", required=True, help="Image Path")
    
    args = parser.parse_args()

    image_path = args.image

    # Analyze with Vision API
    analysis, processing_time = analyze_image_with_vision(image_path, args.prompt, args.model, args.detail)
    
    print(f"\nProcessing Results:")
    print(f"Model: {args.model}")
    print(f"Prompt: {args.prompt}")
    print(f"Processing Time: {processing_time:.2f} seconds")
    print(f"\nAnalysis:\n{analysis}")

if __name__ == "__main__":
    main()