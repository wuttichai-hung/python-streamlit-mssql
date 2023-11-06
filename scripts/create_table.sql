IF OBJECT_ID(N'{SCHEMA}.{TABLE_NAME}', N'U') IS NULL
CREATE TABLE {TABLE_NAME} (
    id int,
    fname text
)