



# Smart Farming Advisor: Agentic RAG-Based System

## **Project Overview**

The Smart Farming Advisor is an AI-powered system that assists farmers in:

* Recommending optimal crops based on soil and climate data.
* Detecting plant diseases from leaf images.
* Providing expert agricultural guidance via a Retrieval-Augmented Generation (RAG) knowledge base.
* Acting intelligently to choose the appropriate tool for each query.

This project integrates **Machine Learning (ML)**, **Deep Learning (DL)**, and **RAG pipelines** under a single agentic framework for practical farming decision support.

---

## **Folder Structure**

```
smart_farming_agent/
│
├── data/
│   ├── crop_data.csv             # Crop recommendation dataset
│   ├── plant_images/             # PlantVillage subset images
│   └── faq_data.csv              # Farmer FAQ / knowledge base
│
├── models/
│   ├── crop_model.pkl            # Trained ML model
│   └── disease_model.h5          # Trained DL model
│
├── tools/
│   ├── __init__.py
│   ├── crop_predictor.py         # ML crop predictor tool
│   ├── disease_detector.py       # DL disease detection tool
│   └── rag_qa.py                 # RAG + LLM tool
│
├── agent/
│   ├── __init__.py
│   └── agent_pipeline.py         # Agentic pipeline integration
│
├── build_faiss_index.py          # Script to create FAISS vector index
├── main.py                       # Single entry point
├── requirements.txt              # Python dependencies
└── README.md
```

---

## **Setup Instructions**

### **1. Clone the Repository**

```bash
git clone https://github.com/YourUsername/smart_farming_agent.git
cd smart_farming_agent
```

### **2. Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
# Activate
source venv/bin/activate       # Linux/Mac
venv\Scripts\activate          # Windows
```

### **3. Install Dependencies**

```bash
pip install -r requirements.txt
```

### **4. Prepare Data**

* Place crop dataset as `data/crop_data.csv`.
* Place leaf images for disease detection in `data/plant_images/`.
* Place FAQ knowledge base as `data/faq_data.csv`.

### **5. Train or Load Models**

* **Crop Predictor:** Train on your crop dataset or place pre-trained model in `models/crop_model.pkl`.
* **Disease Detector:** Train a CNN/ResNet50 model on `plant_images/` and save as `models/disease_model.h5`.

### **6. Build FAISS Index**

> Run this step **once** to create the semantic search index for RAG.

```bash
python build_faiss_index.py
```

* This creates a `faiss_index/` folder used by the RAG QA tool.

---

## **Usage**

1. Run the main agent:

```bash
python main.py
```

2. Enter queries in the terminal:

* **Crop Recommendation Example:**

```
Which crop should I plant with N=90, P=42, K=43?
```

* **Disease Detection Example:**

```
My tomato leaf has spots. Detect the disease. 
```

* **RAG QA Example:**

```
How can I improve soil fertility for wheat?
```

3. The agent will:

   * Parse your query.
   * Choose the appropriate tool.
   * Return a prediction, disease label, or expert answer.

4. To exit, type:

```
exit
```

---

## **Evaluation**

* Crop Predictor: Accuracy, Precision, Recall, F1-score.
* Disease Detector: Accuracy, loss, inference time.
* RAG QA: Relevance, BLEU, Hit Rate.
* Agent: Tool routing correctness.

---

## **Future Improvements**

* Automatic parsing of numeric soil/weather inputs from free-text queries.
* Expand disease detection to more crops and multi-class diseases.
* GUI integration (web or mobile) for farmer-friendly access.
* Weather forecast-based predictive crop recommendations.

---



