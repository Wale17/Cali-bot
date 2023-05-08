import supabase


supabase_url = "https://cnkgdkwmdpopbamybgeo.supabase.co"
supabase_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNua2dka3dtZHBvcGJhbXliZ2VvIiwicm9sZSI6ImFub24iLCJpYXQiOjE2ODE3ODc2NjAsImV4cCI6MTk5NzM2MzY2MH0.Ju161N-NJ9xLbnsRPAab3lHFD0rWiBEJEsqeT85FOVc"
table_name = 'Cali bot'
primary_key = "idld"
client = supabase.create_client(supabase_url, supabase_key)


# Insert data into table
def insert_filled_ld(idld, radicado, ldname):
    try:
        # insert_query = f"INSERT INTO {table_name} (Idld, Ldname, Radicado) VALUES ({idld, ldname, radicado})"
        response = client.table(table_name).insert({"idld": idld, "Ldname": ldname, "Radicado number": radicado, }).execute()
        print(response)
    except Exception as e:
        raise e

# Select data from table
def check_DB_for_LD(idld, ):
    try:
        # select_query = f"SELECT {primary_key} FROM {table_name} WHERE {primary_key} = {idld}"
        response = client.table("Cali bot").select("idld").eq("idld", idld).execute()
        print(response.data)
        if not response.data:
            return True
        else:
            return False
    except Exception as e:
        raise e

# Close connection
def close_connection_to_db():
    client.close()