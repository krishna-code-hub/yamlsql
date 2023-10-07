import os
import yaml
import re


def yaml_from_sql_file():
    # Specify the path to the directory containing your SQL files
    directory_path = "D:\\airflow\\dbtairflow\\dbtairflow\\dbt\\target\\compiled\\rbdatahub\\models\\core\\"

    # Initialize an empty dictionary to store filenames and SQL queries

    sql_files_list = []
    # Iterate over each file in the directory
    for filename in os.listdir(directory_path):
        print(filename)
        if filename.endswith(".sql"):
            # Open the SQL file
            with open(os.path.join(directory_path, filename), "r") as sql_file:
                # Read the SQL query and remove comments
                sql_query = sql_file.read()
                print(sql_query)
                cleaned_sql_query = re.sub(
                    r"/\*[^*]*\*+(?:[^/*][^*]*\*+)*/", "", sql_query
                )

                # Remove empty lines
                cleaned_sql_query = re.sub(
                    r"^\s*$", "", cleaned_sql_query, flags=re.MULTILINE
                )

                # Add the filename and SQL query to the dictionary
                # sql_files_dict[filename] = cleaned_sql_query

                sql_files_dict = {}
                sql_files_dict["filename"] = filename
                sql_files_dict["query"] = cleaned_sql_query
                sql_files_list.append(sql_files_dict)

    # Write the dictionary to a YAML file
    target_filename = directory_path + "combined_sql_files.yaml"
    with open(target_filename, "w") as yaml_file:
        yaml.dump(sql_files_list, yaml_file, default_flow_style=False)


if __name__ == "__main__":
    yaml_from_sql_file()
