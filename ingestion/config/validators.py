from ingestion.config.yaml_loader import load_yaml

def validate_roles_config(file_path: str) -> list[str]:
    config = load_yaml(file_path)
    roles= config.get("roles")
    if not roles:
        raise ValueError(
            f"Roles configuration is empty: {file_path}"
        )
    if not(isinstance(roles, list) and all(isinstance(role, str) for role in roles)):
        raise ValueError(
            f"Invalid roles configuration format in {file_path}. Expected a list of strings."
        ) 
    return roles

def validate_ingestion_config(file_path: str) -> dict:
    config = load_yaml(file_path)
    if not config:
        raise ValueError(
            f"Ingestion configuration is empty: {file_path}"
        )
    if "results_per_page" not in config:
        raise ValueError(
            f"Missing 'results_per_page' in ingestion configuration: {file_path}"
        )
    if "max_pages" not in config:
        raise ValueError(
            f"Missing 'max_pages' in ingestion configuration: {file_path}"
        )   
    if not isinstance(config["results_per_page"], int):
        raise ValueError(
            "results_per_page must be an integer"
        )
    if not isinstance(config["max_pages"], int):
        raise ValueError(
            "max_pages must be an integer"
        )

    if int(config["results_per_page"]) <= 0:
        raise ValueError(
            f"Invalid results_per_page value: {config['results_per_page']} in {file_path}"
        )
    if int(config["max_pages"]) <= 0:
        raise ValueError(
            f"Invalid max_pages value: {config['max_pages']} in {file_path}"
        )

    return config