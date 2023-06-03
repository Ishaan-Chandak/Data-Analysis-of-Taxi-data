@data_exporter
def export_data_to_big_query(data, **kwargs) -> None:
    """
    Template for exporting data to a BigQuery warehouse.
    Specify your configuration settings in 'io_config.yaml'.

    Docs: https://docs.mage.ai/design/data-loading#bigquery
    """
    # We choose the BigQuery transformer since we are using BigQuery through Google Cloud 
    # We made some changes to the io_config.yaml basically linking our account with mage
    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'default'
    
    for key, value in data.items() :
        table_id = 'fast-circle-387906.ishaan_data_project.{}'.format(key)
    

        BigQuery.with_config(ConfigFileLoader(config_path, config_profile)).export(
            DataFrame(value),
            table_id,
            if_exists='replace',  # Specify resolution policy if table name already exists
        )
