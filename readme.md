# Grooo Google Vision
Use google cloud vision to detect text in image.
# Getting Started
## Requirement
- Ubuntu 16.04
- Python 3.5
- Google cloud account ([here](https://console.cloud.google.com)).

## Installing
- Install google cloud sdk from pip3
```commandline
pip3 install google-cloud-vision
```

- Create a project with the Google Cloud Console, and enable the Vision API.

- Set up your environment with [Application Default Credentials](https://developers.google.com/identity/protocols/application-default-credentials).
 For example, from the Cloud Console, you might create a service account, download its json credentials file, then set the appropriate environment variable:

```commandline
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/your-project-credentials.json
```
## Running

```commandline
python3 detect_text.py mypath/input_folder
```

# Authors
[Hoàng Anh Tú](https://fb.com/tuhoang.bk) 

[Grooo International](https://grooo.vn/)

