# 🍳 YouTube Recipe Extractor

A pipeline that converts cooking videos into structured recipes using **captions, visual food detection, and a local LLM**.

---
⚙️ Logic Pipeline
1. Download YouTube video and clean VTT captions.
2. Extract frames and run YOLOv8 to detect ingredients.
3. Split instructions into single-action steps using Regex.
4. Refinement: Use Llama 3.2 to convert all info we collected from frames, captions into logical recipe 
5. Output: Generate structured JSON 
---
🚀 Running Instructions
1.  we already cloned  yolo food ingredient model from  https://github.com/anushkaspatil/Food-Detection.git , and Manually moved 'best.pt' from the cloned folder to your project root
2. 
 ```bash
python -m venv venv
venv\Scripts\activate 
pip install -r .\requirements.txt
venv\Scripts\python.exe -m pip install streamlit webvtt-py
 Download: https://ollama.com/download
ollama pull llama3.2
venv\Scripts\python.exe -m streamlit run app.py
```
3. give url of youtube video you wish to extract recipe from


