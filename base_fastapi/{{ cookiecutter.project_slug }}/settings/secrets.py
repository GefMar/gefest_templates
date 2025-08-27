from dynaconf import Dynaconf


config = Dynaconf(
    envvar_prefix="AIP",
    load_dotenv=True,
    environments=True,
    root_path="{{ cookiecutter.project_slug }}/conf",
    settings_files=["config.toml"],
)
