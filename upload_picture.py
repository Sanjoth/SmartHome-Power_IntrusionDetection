##
#   Author : Sanjoth Shaw
#   Description : Script to upload files to Dropbox via Temboo API
##

# Import correct libraries
import base64
import sys
from temboo.core.session import TembooSession
from temboo.Library.Dropbox.FilesAndMetadata import UploadFile

print str(sys.argv[1])

# Encode image
with open(str(sys.argv[1]), "rb") as image_file:
    encoded_string = base64.b64encode(image_file.read())

# Declare Temboo session and Choreo to upload files
session = TembooSession('sanjoth', 'SmartCam', 'CwaQOIo0vSO3RIjuvNM95gTM7RihPY56')
uploadFileChoreo = UploadFile(session)

# Get an InputSet object for the choreo
uploadFileInputs = uploadFileChoreo.new_input_set()

# Set inputs
uploadFileInputs.set_AppSecret("p98wlhv0n1f3x8v")
uploadFileInputs.set_AccessToken("2mqxfzuwpyiuguwp")
uploadFileInputs.set_FileName(str(sys.argv[1]))
uploadFileInputs.set_AccessTokenSecret("w7xxw5ywxbemubj")
uploadFileInputs.set_AppKey("e3zsgvapvyfv0ec")
uploadFileInputs.set_FileContents(encoded_string)
uploadFileInputs.set_Root("sandbox")

# Execute choreo
uploadFileResults = uploadFileChoreo.execute_with_results(uploadFileInputs)
