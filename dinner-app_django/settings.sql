CREATE DATABASE dinnerapp_other;
CREATE USER dinneruser WITH PASSWORD 'dinner';
GRANT ALL PRIVILEGES ON DATABASE dinnerapp_other TO dinneruser;