# Stocks Template project

## Create virtual environment and install dependencies

### For Linux & Mac

```bash
python -m virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

### For Windows
```bash
python -m virtualenv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```

If you find some issues regarding the execution policy run the following command in PowerShell as Administrator

```bash
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

For both Windows and Mac, if `python` does not work, use `python3`.

## Project configuration

First, create a file called `.env` in the base path of the project, and paste the following content.

```text
AWS_SHARED_CREDENTIALS_FILE=./aws/credentials
AWS_CONFIG_FILE=./aws/config
AWS_PROFILE=default
```

Then, create a folder called `aws` in the base path of the project, and within that folder, create two files (`config` and `credentials`) with the following content

`config` file:
```text
[default]
region = <paste_your_region>
output = json
```

`credentials` file:
```text
[default]
aws_access_key_id = <AWS_ACCESS_KEY>
aws_secret_access_key = <AWS_SECRET_ACCESS_KEY>
```

## Testing

If you completed all the setup with the correct values and you setup the environment properly, you should be able to execute the following and give a new row created in your DynamoDB table.

```bash
python main.py
```