# OpenAI Vision Image Analyzer

A Python CLI tool to analyze images using OpenAI's Vision API (GPT-4o). Supports both local images and URLs.

## Features
- Analyze images from local files or URLs
- Customizable prompts for image analysis
- Processing time measurement
- Adjustable detail level for image processing

## Installation

1. Clone repository:

2. Install dependencies:
```
pip install -r requirements.txt
```
Add your OpenAI API key to .env:

```bash

echo "OPENAI_API_KEY=your-api-key-here" > .env
```
Usage
```bash
python vision_analyzer.py --image <PATH_OR_URL> --prompt "<PROMPT>" [--model MODEL] [--detail DETAIL]
```
3. Arguments:
Argument	Description	Default
--image	Image path or URL	Required
--prompt	Analysis question/instruction	Required
--model	OpenAI model to use	gpt-4o
--detail	Image processing detail (low, high, auto)	low
Examples
Analyze local image:

```bash
python vision_analyzer.py \
    --image "path/to/image.jpg" \
    --prompt "Describe what's happening in this photo" \
    --detail high
```
Analyze image from URL:

```bash
python vision_analyzer.py \
    --image "https://example.com/image.png" \
    --prompt "What colors dominate this image?" \
    --model gpt-4o-mini
```
