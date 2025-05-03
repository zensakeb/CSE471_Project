from users.supabase_client import supabase

def get_all_projects():
    # Fetch all projects
    response = supabase.table('projects').select('*').execute()
    
    if response.error:
        print("Error fetching projects:", response.error)
        return []

    # Return the list of projects
    return response.data
