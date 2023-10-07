import os
import yaml
import re
import sqlparse


def yaml_from_sql_file():
    # Specify the path to the directory containing your SQL files
    directory_path = "D:\\airflow\\dbtairflow\\dbtairflow\\dbt\\target\\compiled\\rbdatahub\\models\\core\\"

    # Initialize a list to store dictionaries for each SQL file
    sql_files_list = []

    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        if filename.endswith(".sql"):
            # Open the SQL file
            with open(os.path.join(directory_path, filename), "r") as sql_file:
                # Read the SQL query and remove comments
                sql_query = sql_file.read()
                cleaned_sql_query = re.sub(
                    r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", sql_query
                )

                # Remove empty lines
                cleaned_sql_query = "\n".join(
                    [
                        line
                        for line in cleaned_sql_query.split("\n")
                        if line.strip() != ""
                    ]
                )
                print(f" {filename} -  {len(cleaned_sql_query.splitlines())}")

                formatted_sql = sqlparse.format(
                    cleaned_sql_query, reindent=True, keyword_case="upper"
                )
                # Create a dictionary for this SQL file
                sql_file_dict = {"filename": filename, "query": formatted_sql}

                # Add the dictionary to the list
                sql_files_list.append(sql_file_dict)

    # Customize YAML representers to use literal block style for multiline strings
    def str_presenter(dumper, data):
        if len(data.splitlines()) > 1:
            return dumper.represent_scalar("tag:yaml.org,2002:str", data, style="|")
        return dumper.represent_scalar("tag:yaml.org,2002:str", data)

    yaml.add_representer(str, str_presenter)

    target_filename = (
        "C:\\Users\\Krishna\\PycharmProjects\\yamlsql\\output\\"
        + "combined_sql_files1.yaml"
    )
    # Write the list of dictionaries to a YAML file

    outer_dict = {"sql_files": sql_files_list}
    with open(target_filename, "w") as yaml_file:
        yaml.dump(outer_dict, yaml_file, default_flow_style=False)

    # Open the YAML file
    with open(target_filename, "r") as yaml_file:
        # Load all documents from the YAML file
        sql_files_out_list = yaml.safe_load(yaml_file)

    print(sql_files_out_list)

    # Iterate over each SQL file data
    for sql_files_out_dict in sql_files_out_list["sql_files"]:
        # Extract the filename and SQL query
        filename = sql_files_out_dict["filename"]
        sql_query = sql_files_out_dict["query"]

        # Here, you can process each SQL query as you need
        print(f"Filename: {filename}")
        print(f"SQL query:\n{sql_query}\n")


if __name__ == "__main__":
    yaml_from_sql_file()
