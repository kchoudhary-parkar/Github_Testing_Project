"""
GTP-002: Database Operations Module
This module handles database queries and operations
WARNING: This file intentionally contains SQL injection vulnerabilities for testing
"""

import sqlite3
import pymysql
from app_config import DATABASE_URL, PROD_DB_PASS

class DatabaseManager:
    """Manages database connections and queries"""
    
    def __init__(self):
        # SECURITY ISSUE: Hardcoded credentials in code
        self.conn = sqlite3.connect('app.db')
        self.password = "db_admin_password_123"
    
    def get_user_by_id(self, user_id):
        """
        SECURITY ISSUE: SQL Injection vulnerability
        User input is directly concatenated into SQL query
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM users WHERE id = " + str(user_id)
        cursor.execute(query)
        return cursor.fetchone()
    
    def authenticate_user(self, username, password):
        """
        SECURITY ISSUE: SQL Injection vulnerability
        String formatting with user input creates SQL injection risk
        """
        cursor = self.conn.cursor()
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(query)
        return cursor.fetchone()
    
    def search_products(self, search_term):
        """
        SECURITY ISSUE: SQL Injection via LIKE clause
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM products WHERE name LIKE '%" + search_term + "%'"
        cursor.execute(query)
        return cursor.fetchall()
    
    def delete_user(self, user_id):
        """
        SECURITY ISSUE: SQL Injection in DELETE statement
        """
        cursor = self.conn.cursor()
        query = "DELETE FROM users WHERE id = " + user_id
        cursor.execute(query)
        self.conn.commit()
    
    def update_user_email(self, user_id, new_email):
        """
        SECURITY ISSUE: SQL Injection in UPDATE statement
        """
        cursor = self.conn.cursor()
        sql = "UPDATE users SET email = '%s' WHERE id = %s" % (new_email, user_id)
        cursor.execute(sql)
        self.conn.commit()
    
    def get_orders_by_status(self, status):
        """
        SECURITY ISSUE: SQL Injection with .format()
        """
        cursor = self.conn.cursor()
        query = "SELECT * FROM orders WHERE status = '{}'".format(status)
        cursor.execute(query)
        return cursor.fetchall()
    
    def execute_raw_query(self, table_name, condition):
        """
        SECURITY ISSUE: Direct execution of user-provided SQL
        """
        cursor = self.conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE {condition}"
        cursor.execute(query)
        return cursor.fetchall()

def connect_to_mysql():
    """
    SECURITY ISSUE: Hardcoded MySQL credentials
    """
    connection = pymysql.connect(
        host='192.168.1.100',
        user='mysql_admin',
        password='MyS3cr3tP@ssw0rd!',
        database='production_db',
        charset='utf8mb4'
    )
    return connection

def get_user_data(username):
    """
    SECURITY ISSUE: SQL Injection in function
    """
    conn = connect_to_mysql()
    cursor = conn.cursor()
    # Vulnerable query
    sql = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(sql)
    result = cursor.fetchone()
    conn.close()
    return result

def admin_login(admin_user, admin_pass):
    """
    SECURITY ISSUE: Hardcoded admin credentials for comparison
    """
    # Bad practice: hardcoded admin credentials
    if admin_user == "superadmin" and admin_pass == "SuperAdmin@2024!":
        return True
    return False

# SECURITY ISSUE: Global connection with hardcoded password
global_connection = sqlite3.connect('production.db')
MASTER_PASSWORD = "M@sterDBP@ss2024!"

class QueryBuilder:
    """Builds SQL queries - INSECURELY"""
    
    @staticmethod
    def build_select(table, where_clause):
        """
        SECURITY ISSUE: String concatenation for SQL building
        """
        return f"SELECT * FROM {table} WHERE {where_clause}"
    
    @staticmethod
    def build_insert(table, columns, values):
        """
        SECURITY ISSUE: No input validation or parameterization
        """
        cols = ", ".join(columns)
        vals = ", ".join([f"'{v}'" for v in values])
        return f"INSERT INTO {table} ({cols}) VALUES ({vals})"

print("[DATABASE] Database module loaded with vulnerable query methods")
