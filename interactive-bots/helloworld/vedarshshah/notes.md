Where I had problems:
    * Installing the zulip_bots package 
        * When the command "pip install zulip_bots" was executed, pip automatically used python 2, which caused multiple errors.
        * I fixed it by using "pip3.6" in the command instead of just "pip", forcing pip to use python 3.