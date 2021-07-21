from O365 import Account

file_name = 'foo.txt'

""" Azure """
client_id = '51b8bcee-defd-47a7-9349-ac404e1b1cb9'
client_secret = '2m0XV~47cj5F9uGwO_O.rpOe~S4YN35646'
tenant_id = '15c14e48-7293-4ec2-9d2f-09db64edea9b'
CHUNK_SIZE = 1024 * 1024 * 5

""" Sharepoint """ 
host_name = 'hubsystemsconz.sharepoint.com' 
path_to_site = '/sites/SambaReplacement'

""" Login """
credentials = (client_id, client_secret)
account = Account(credentials, auth_flow_type='credentials', tenant_id=tenant_id)
if account.authenticate():
   print('Authenticated!')

   storage = account.sharepoint()
   # print(storage)

   my_site = storage.get_site(host_name, path_to_site)
   # print(my_site)

   # go to the folder called "Documents"
   my_drive = my_site.get_default_document_library()
   # print(my_drive)

   root_folder = my_drive.get_root_folder()

   # iterate over the first 25 items on the root folder
   print("Documents:")
   for item in root_folder.get_items(limit=25):
      print(item.name)
               
   # upload a file
   print(root_folder.upload_file(file_name), "sent!")