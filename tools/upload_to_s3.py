


from os import walk


dir = 'recettes/staticfiles/'
import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory 
    tree by walking the tree either top-down or bottom-up. For each 
    directory in the tree rooted at directory top (including top itself), 
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.   
full_file_paths = get_filepaths(dir)

from b2sdk.v2 import B2Api
from b2sdk.v2 import InMemoryAccountInfo
info = InMemoryAccountInfo()
b2_api = B2Api(info)
application_key_id = '00314725e97d32a0000000001'
application_key = 'K00343CN/VirUBDdM3AGZ3quA0TBwDE'
b2_api.authorize_account("production", application_key_id, application_key)
bucket = b2_api.get_bucket_by_name('Elisa-s-Corner')
# print(bucket)
print(full_file_paths)
for file in full_file_paths:
    local_file_path = file
    if os.path.isfile(local_file_path):
        print("willmase")
    print(local_file_path)
    b2_file_name = file.replace(dir,'static/')
    print(b2_file_name)
    file_info = {'how': 'good-file'}

    v = bucket.upload_local_file(
            local_file=local_file_path,
            file_name=b2_file_name,
            file_infos=file_info)
    # print(v)
    # break
