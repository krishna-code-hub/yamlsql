import os
import sqlparse
import argparse
import re


def split_sql_file(filename, replacements):
    # Read the file contents
    with open(filename, "r") as f:
        content = f.read()

    # Use sqlparse to split the content into individual queries
    queries = sqlparse.split(content)

    # Write each query to a separate file
    for i, query in enumerate(queries):
        if len(query) > 10 :
            modified_queries = replace_params(query,replacements)
            with open(f"query_{i + 1}.sql", "w") as f:
                f.write(modified_queries)


def replace_params(sql_content, replacements):
    # Replace placeholders with corresponding values
    for key, value in replacements.items():
        # Assuming placeholders in SQL file are in the format ${key}
        pattern = r"\$\{hiveconf:" + key + r"\}"
        sql_content = re.sub(pattern, value, sql_content)

    return sql_content


if __name__ == "__main__":
    # Set up argument parsing
    parser = argparse.ArgumentParser(
        description="Replace SQL parameters with command line arguments."
    )
    parser.add_argument("-f", required=True, help="Path to the SQL file")
    parser.add_argument(
        "-hiveconf",
        action="append",
        help="Key-value pairs in the format key=value to replace in the SQL file",
    )

    args = parser.parse_args()

    filename = args.f

    #filename = "D:\\airflow\\dbtairflow\\dbtairflow\\dbt\\models\\core\\multi_sql.sql"
    #split_sql_file(filename)

    # Convert list of 'key=value' pairs into a dictionary
    replacements = {}
    if args.hiveconf:
        for item in args.hiveconf:
            key, value = item.split("=")
            replacements[key] = value

    # Read SQL file and replace placeholders
    split_sql_file(filename, replacements)

