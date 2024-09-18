import os
import frontmatter
from datetime import datetime

def add_date_to_md(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                with open(file_path, "r+", encoding="utf-8") as f:
                    post = frontmatter.load(f)
                    if "date" not in post.metadata:
                        creation_time = os.path.getctime(file_path)
                        creation_date = datetime.fromtimestamp(creation_time).strftime("%Y-%m-%d")
                        post.metadata["date"] = creation_date
                        print(file_path, creation_date)
                        f.seek(0)
                        f.write(frontmatter.dumps(post))
                        f.truncate()

if __name__ == "__main__":
    directory = "_posts2"
    add_date_to_md(directory)