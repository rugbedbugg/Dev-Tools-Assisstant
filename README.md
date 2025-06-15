# Dev Tools Assistant

This is a small project I made to help developers discover useful tools based on what they're working on. The idea is to create an AI agent to recommend tools depending on your project type, language, and goals.

## 🛠 What It Does

* Suggests tools you might find useful via web scraping, crawling and LLM reasoning
* Could be helpful if you’re not sure what tools to use, especially when starting something new

Right now it’s pretty simple and still a work in progress!

## 📦 How to Run It

0. Install the `uv` Package Manager

```
pip install uv
```

1. Clone the repo:

```
git clone https://github.com/rugbedbugg/Dev-Tools-Assisstant.git
cd Dev-Tools-Assisstant
```

2. Install the requirements:

```
uv pip install -r pyproject.toml
```

3. Set environment variables:

If you're in linux type the following commands in the root directory of the project
```
touch .env
echo "FIRECRAWL_API_KEY=your-firecrawl-api-key" >> .env
echo "OPENAI_API_KEY=your-openai-api-key" >> .env
```
If you're in Windows just create a file named `.env` with the following content
```
FIRECRAWL_API_KEY=your-firecrawl-api-key
OPENAI_API_KEY=your-openai-api-key
```

4. Run the script:

```
uv run main.py
```


## 🤔 Why I Made This

I often found myself Googling “best tools for X” when starting a new project. So I automate that a bit and this is my attempt to make something helpful, and learn more along the way.

## 🚧 Things I Might Add

* Better formatting for the output
* Agentic Setup and RAG capabilities 
* GUI (also, maybe??)

## 💡 Contributions

If you have ideas or just want to help make this better, feel free to fork it or open a pull request! It's just a fun side project, so anything goes.

