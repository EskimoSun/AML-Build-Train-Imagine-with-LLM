# AML-Build-Train-Imagine-with-LLM
This is a shared repository for Columbia University COMS4995W032 Applied Machine Learning course final project.

Set the api_key first:
```sh
export OPENAI_API_KEY="replace-your-api-key-here"
```

Run the following to test cases:
```sh
    source venv/bin/activate
    docker build -t code-sandbox -f sandbox/Dockerfile .
```

```sh
python main.py --mode loop --index 10
python main.py --mode baseline --index 10
```
