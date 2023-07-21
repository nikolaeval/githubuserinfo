/*
This file is used to bootstrap development database locally.

Note: ONLY development database;
*/

CREATE USER githubinfo SUPERUSER PASSWORD 'githubinfo';
CREATE DATABASE githubinfo OWNER githubinfo ENCODING 'utf-8';
