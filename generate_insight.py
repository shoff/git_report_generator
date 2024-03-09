import os
import openapi

openapi.api_key = os.environ.get("OPENAI_API_KEY")


# Cache file path

cache_file = 'insights_cache.json'


def generate_insight_hash(commit_logs, analysis_report):

    # Generate a unique hash for the combination of commit_logs and analysis_report

    input_string = commit_logs + analysis_report

    return hashlib.sha256(input_string.encode('utf-8')).hexdigest()


def save_insight_to_cache(hash_key, insight):

    # Load existing cache

    if os.path.exists(cache_file):

        with open(cache_file, 'r') as file:

            cache = json.load(file)

    else:

        cache = {}


    # Update cache

    cache[hash_key] = insight


    # Save cache

    with open(cache_file, 'w') as file:

        json.dump(cache, file)


def get_insight_from_cache(hash_key):

    # Check if cache exists

    if not os.path.exists(cache_file):

        return None


    # Load cache

    with open(cache_file, 'r') as file:

        cache = json.load(file)


    # Return cached insight if exists

    return cache.get(hash_key)


def generate_insight(commit_logs, analysis_report):
    # Generate hash key for the input
    hash_key = generate_insight_hash(commit_logs, analysis_report)
    if cached_insight := get_insight_from_cache(hash_key):
        return cached_insight
    # If insight not in cache, generate new insight
    prompt = f"Let's delve into the insights gleaned from our recent developments. Below, you'll find a concise summary of the pivotal changes captured in our Git commit logs, alongside a comprehensive analysis of our code's current state. These findings not only reflect our progress but also spotlight areas ripe for improvement. Please review: Git Commit Logs: {commit_logs} Code Analysis Report: {analysis_report} Your expertise and feedback are invaluable as we refine our approach and forge ahead. Outline what each committer has committed to the project."

    response = openapi.ChatCompletion.create(
        model="gpt-4-0125-preview",
        messages=[

            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]

    )


    insight = response.choices[0].message['content']


    # Save new insight to cache

    save_insight_to_cache(hash_key, insight)

    return insight


